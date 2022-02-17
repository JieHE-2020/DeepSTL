import pandas as pd
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
import numpy as np
import pickle
import copy
import collections

letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
               'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
underscore_list = ['_']
letter_underscore_list = letter_list + underscore_list
letter_digit_list = letter_list + digit_list
letter_digit_underscore_list = letter_list + digit_list + underscore_list

print('-------------------------- Read data set --------------------------')
df = pd.read_csv('./dataset/reference_dataset.csv', quotechar="'")
stl_data_list = list(df['STL'])
#print(stl_data_list)
print('read data set finished')

print('-------------------------- Pre-tokenization --------------------------')
tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
trainer = WordLevelTrainer(vocab_size=1000, special_tokens=["[UNK]"])
pre_tokenizer = pre_tokenizers.Sequence([
    Whitespace(),
    Punctuation(),
    Digits(individual_digits=True)
])
tokenizer.pre_tokenizer = pre_tokenizer
print('pre-tokenization instantiated')

print('-------------------------- Tokenization --------------------------')
tokenizer.train_from_iterator(stl_data_list, trainer)
tokenizer.save("./stl_wordlevel_tokenizer.json", pretty=True)
tokenizer = Tokenizer.from_file("./stl_wordlevel_tokenizer.json")
print('tokenization finished')

print('-------------------------- Obtain original vocab list --------------------------')
print('vocab_size:', tokenizer.get_vocab_size())
vocab_list = list(tokenizer.get_vocab().keys())
#print(vocab_list)

print('-------------------------- Process vocab list --------------------------')
letter_digit_underscore_dot_list = letter_digit_underscore_list + ['.']
letter_digit_underscore_dot_set = set(letter_digit_underscore_dot_list)

vocab_set_no_id_num = set(vocab_list) - letter_digit_underscore_dot_set - {'[UNK]'}
vocab_list_no_id_num = list(vocab_set_no_id_num)
algorithmic_symbol_list = ['ABS', 'VECSUM', 'DERIVATIVE', 'DIFF', ',']
special_signal_pattern_list = ['SPIKE']
quantity_keyword_list = ['EPSILON', 'INF']
vocab_list_no_id_num \
    = vocab_list_no_id_num + algorithmic_symbol_list + special_signal_pattern_list + quantity_keyword_list
#print(vocab_list_no_id_num)
#print(len(vocab_list_no_id_num))

print('-------------------------- id and num recognition & raw template generation --------------------------')


def id_num_recognize(word_list):
    # print(word_list)
    digit_dot_list = digit_list + ['.']
    id_list = []
    num_list = []
    new_id_str = ''
    new_num_str = ''
    start_id = True
    start_num = True
    id_lock = 0
    num_lock = 0

    for i in range(len(word_list)):
        if word_list[i] in vocab_list_no_id_num:
            if i == 0:
                pass
            elif word_list[i - 1] in vocab_list_no_id_num:
                pass
            else:  # word_list[i-1] not in vocab_list_no_id_num
                if not start_id:
                    id_list.append(new_id_str)
                    new_id_str = ''
                    id_lock = 0
                    start_id = True
                if not start_num:
                    num_list.append(new_num_str)
                    new_num_str = ''
                    num_lock = 0
                    start_num = True
        else:
            if num_lock == 0:
                if start_id:
                    # start of id
                    if word_list[i] in letter_underscore_list:
                        new_id_str = word_list[i]
                        id_lock = 1
                        start_id = False
                else:
                    # in the processing of id
                    if word_list[i] in letter_digit_underscore_list:
                        new_id_str = new_id_str + ' ' + word_list[i]

            if id_lock == 0:
                if not (word_list[i] == '0' and word_list[i - 1] == '[' and word_list[i + 1] == ':'):
                    if start_num:
                        # start of num
                        if word_list[i] in digit_list:
                            new_num_str = word_list[i]
                            num_lock = 1
                            start_num = False
                    else:
                        # in the processing of num
                        if word_list[i] in digit_dot_list:
                            new_num_str = new_num_str + ' ' + word_list[i]

    # in case an expression ends with an identifier or a number (e.g., a single id := phi)
    if new_id_str != '':
        id_list.append(new_id_str)
    if new_num_str != '':
        num_list.append(new_num_str)

    # delete repetitive elements for template abstraction
    id_set = set(id_list)
    # print(id_set)
    num_set = set(num_list)

    # delete space
    id_list_no_space = []
    num_list_no_space = []
    for id in id_list:
        id = id.replace(' ', '')
        id_list_no_space.append(id)
    for num in num_list:
        num = num.replace(' ', '')
        num_list_no_space.append(num)

    id_set_no_space = set(id_list_no_space)
    num_set_no_space = set(num_list_no_space)

    # get char number and digit number of every id and constant
    char_num_list = []
    digit_num_list = []
    for id_str in id_set_no_space:
        char_num_list.append(len(id_str))
    for num_str in num_list_no_space:
        digit_num_list.append(len(num_str))

    id_num_info_dict = {
        'id_list': id_list,
        'num_list': num_list,
        'id_set': id_set,
        'num_set': num_set,
        'id_list_no_space': id_list_no_space,
        'num_list_no_space': num_list_no_space,
        'id_set_no_space': id_set_no_space,
        'num_set_no_space': num_set_no_space,
        'id_number': len(id_set),
        'num_number': len(num_list),
        'char_num_list': char_num_list,
        'digit_num_list': digit_num_list
    }

    return id_num_info_dict


formula_word_list = []
formula_info_dict = {}
stl_data_info_list = []

for formula in stl_data_list:
    # pre-tokenization
    formula_word_list = []
    for item in pre_tokenizer.pre_tokenize_str(formula):
        formula_word_list.append(item[0])
    formula_pre_tokenized = ' '.join(formula_word_list)

    # recognize id and num
    formula_id_num_info_dict = id_num_recognize(formula_word_list)

    # replace id and num
    formula_template = copy.deepcopy(formula_pre_tokenized)
    if ': =' in formula_template:  # in case of definition of substitution
        formula_template = ' ' + formula_template + ' '
    id_list = list(formula_id_num_info_dict['id_set'])
    id_list.sort(key=lambda i: len(i), reverse=True)
    num_list = list(formula_id_num_info_dict['num_set'])
    num_list.sort(key=lambda i: len(i), reverse=True)
    # process id
    for identifier in id_list:
        identifier = ' ' + identifier + ' '
        formula_template = formula_template.replace(identifier, ' id ')
    formula_template = formula_template.strip()  # recovery
    # process num
    for num in num_list:
        if num != '0':
            formula_template = formula_template.replace(num, 'num')
    # in case of temporal shift starting with 0
    if '0' in num_list:
        ft_word_list = formula_template.split(' ')
        for i in range(len(ft_word_list)):
            if ft_word_list[i] == '0':
                if ft_word_list[i - 1] == '[' and ft_word_list[i + 1] == ':':
                    pass
                else:
                    ft_word_list[i] = 'num'
        formula_template = ' '.join(ft_word_list)

    # assemble formula info
    formula_info_dict = {
        'formula': formula,
        'formula_word_list': formula_word_list,
        'formula_pre_tokenized': formula_pre_tokenized,
        'formula_id_num_info_dict': formula_id_num_info_dict,
        'formula_template': formula_template
    }
    stl_data_info_list.append(formula_info_dict)
print('recognition id and num finished')

print('-------------------------- STL formula analysis --------------------------')


# def get_sub_formula_num(word_list):
#     keyword_list = ['not', 'rise', 'fall', 'eventually', 'always', 'once', 'historically', 'until', 'since',
#                     'and', 'or']
#
#     # algorithmic operator
#     num_equal = 0
#     num_larger = 0
#     num_larger_equal = 0
#     num_smaller = 0
#     num_smaller_equal = 0
#     num_imply = 0
#     num_keyword = 0
#
#     for i in range(len(word_list)):
#         # algorithmic + imply operator
#         if word_list[i] == '=' and word_list[i + 1] == '=':
#             num_equal = num_equal + 1
#         if word_list[i] == '>' and word_list[i + 1] != '=' and word_list[i - 1] != '-':  # consider ->
#             num_larger = num_larger + 1
#         if word_list[i] == '>' and word_list[i + 1] == '=':
#             num_larger_equal = num_larger_equal + 1
#         if word_list[i] == '<' and word_list[i + 1] != '=':
#             num_smaller = num_smaller + 1
#         if word_list[i] == '<' and word_list[i + 1] == '=':
#             num_smaller_equal = num_smaller_equal + 1
#         if word_list[i] == '-' and word_list[i + 1] == '>':
#             num_imply = num_imply + 1
#         # keyword
#         if word_list[i] in keyword_list:
#             num_keyword = num_keyword + 1
#
#     num_sub_formula = \
#         num_equal + num_larger + num_larger_equal + num_smaller + num_smaller_equal + num_imply + num_keyword
#
#     return num_sub_formula


def template_refine(raw_template):
    left_symbol_list = ['id', 'ABS ( id )', 'VECSUM ( id )', 'DERIVATIVE ( id )',
                        'DIFF ( id , id )', 'ABS ( DIFF ( id , id ) )']
    operator_list = [' = = num', ' = = - num', ' = = id',
                     ' > = num', ' > = - num', ' > = id',
                     ' > num', ' > - num', ' > id',
                     ' < = num', ' < = - num', ' < = id',
                     ' < num', ' < - num', ' < id']

    relation_list = []
    for left_symbol in left_symbol_list:
        for operator in operator_list:
            relation = left_symbol + operator
            relation_list.append(relation)

    # in case of range
    range_min_list = []
    for i in [' > ', ' > = ']:
        for j in ['- num', 'num', 'id']:
            range_min_list.append('id' + i + j)
    range_max_list = []

    # algorithmic operation
    for i in [' < ', ' < = ']:
        for j in ['- num', 'num', 'id']:
            range_max_list.append('id' + i + j)
    range_list = []

    for i in range_min_list:
        for j in range_max_list:
            range_list.append(i + ' and ' + j)

    for string in range_list:
        if string in raw_template:
            raw_template = raw_template.replace(string, 'range')

    for string in relation_list:
        if string in raw_template:
            raw_template = raw_template.replace(string, 'phi')

    return raw_template


template_list = []
sub_formula_num_list = []
# overall_id_num_list = []
# overall_id_char_num_list = []
# overall_num_digit_num_list = []

count = 0
for i in range(len(stl_data_info_list)):
    # if count % 10000 == 0:
    #     print(count)

    # template
    raw_template = stl_data_info_list[i]['formula_template']
    template = template_refine(raw_template)
    stl_data_info_list[i]['refined_formula_template'] = template
    template_list.append(template)

    # # sub-formula
    # # template_string = stl_data_info_list[i]['formula_template']
    # template_word_list = stl_data_info_list[i]['formula_template'].split(' ')
    # sub_formula_num_list.append(get_sub_formula_num(template_word_list))
    #
    # # statistical info of id and num
    # overall_id_num_list.append(stl_data_info_list[i]['formula_id_num_info_dict']['id_number'])
    # overall_id_char_num_list = \
    #     overall_id_char_num_list + stl_data_info_list[i]['formula_id_num_info_dict']['char_num_list']
    # overall_num_digit_num_list = \
    #     overall_num_digit_num_list + stl_data_info_list[i]['formula_id_num_info_dict']['digit_num_list']

    count = count + 1

template_set = set(template_list)

print('1. Template analysis:')
count = 2
for item in stl_data_info_list:
    print('index in .csv file:', count)
    print(item['formula_template'])
    print(item['refined_formula_template'])
    count = count + 1
    print()

counter = collections.Counter(template_list)
# print(counter.items())
template_freqs = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print('2. Template frequency (sorted):')
print(template_freqs)


sum = 0
for i in range(len(template_freqs)):
    sum = sum + template_freqs[i][1]
print('\n3. Total number of formulas:')
print(sum)

print('\n4. Print template frequency:')
for item in template_freqs:
    print(item)
