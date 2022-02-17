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

letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
               'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
underscore_list = ['_']
letter_underscore_list = letter_list + underscore_list
letter_digit_list = letter_list + digit_list
letter_digit_underscore_list = letter_list + digit_list + underscore_list

print('-------------------------- Read data set --------------------------')
# df = pd.read_csv('./test_cases/corpus_test.csv')
df = pd.read_csv('./corpus_split.csv')
stl_data_list = list(df['STL'])
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
print(vocab_list)

print('-------------------------- Process vocab list --------------------------')
letter_digit_underscore_dot_list = letter_digit_underscore_list + ['.']
letter_digit_underscore_dot_set = set(letter_digit_underscore_dot_list)

vocab_set_no_id_num = set(vocab_list) - letter_digit_underscore_dot_set - {'[UNK]'}
vocab_list_no_id_num = list(vocab_set_no_id_num)
# vocab_list_no_id_num = ['or', 'once', '(', 'fall', 'rise', '>', 'historically', 'eventually', '<', '-', 'and', '=', 'not', '[', ')', ']', 'until', 'always', 'since', ':']
print(vocab_list_no_id_num)
print(len(vocab_list_no_id_num))

print('-------------------------- id and num recognition & raw template generation --------------------------')


def id_num_recognize(word_list):
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

    # delete repetitive elements for template abstraction
    id_set = set(id_list)
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
    # print('identifier - char num:')
    for id_str in id_set_no_space:
        char_num_list.append(len(id_str))
    #     print(id_str)
    #     print('length:', len(id_str))
    # print('constant - digit num:')
    for num_str in num_list_no_space:
        digit_num_list.append(len(num_str))
        # print(num_str)
        # print('length:', len(num_str))

    id_num_info_dict = {
        'id_list': id_list,
        'num_list': num_list,
        'id_set': id_set,
        'num_set': num_set,
        'id_list_no_space': id_list_no_space,
        'num_list_no_space': num_list_no_space,
        'id_set_no_space': id_set_no_space,
        'num_set_no_space': num_set_no_space,
        'id_number': len(id_set),  # a > 1 and a < 1 (counted as 1 identifier)
        'num_number': len(num_list),
        'char_num_list': char_num_list,
        'digit_num_list': digit_num_list
    }
    # print('identifier number:', id_num_info_dict['id_number'])
    return id_num_info_dict


formula_word_list = []
formula_info_dict = {}
stl_data_info_list = []

# count = 0
for formula in stl_data_list:

    # print('--------------------------')
    # print('formula ' + str(count + 1) + ':')
    # count = count + 1

    # pre-tokenization
    formula_word_list = []
    for item in pre_tokenizer.pre_tokenize_str(formula):
        formula_word_list.append(item[0])
    formula_pre_tokenized = ' '.join(formula_word_list)

    # recognize id and num
    formula_id_num_info_dict = id_num_recognize(formula_word_list)

    # replace id and num
    formula_template = formula_pre_tokenized
    id_list = list(formula_id_num_info_dict['id_set'])
    id_list.sort(key=lambda i: len(i), reverse=True)
    num_list = list(formula_id_num_info_dict['num_set'])
    num_list.sort(key=lambda i: len(i), reverse=True)

    for identifier in id_list:
        identifier = ' ' + identifier + ' '
        formula_template = formula_template.replace(identifier, ' id ')
    for num in num_list:
        formula_template = formula_template.replace(num, 'num')

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


def get_sub_formula_num(word_list):
    keyword_list = ['not', 'rise', 'fall', 'eventually', 'always', 'once', 'historically', 'until', 'since',
                    'and', 'or']

    # algorithmic operator
    num_equal = 0
    num_larger = 0
    num_larger_equal = 0
    num_smaller = 0
    num_smaller_equal = 0
    num_imply = 0
    num_keyword = 0

    for i in range(len(word_list)):
        # algorithmic + imply operator
        if word_list[i] == '=' and word_list[i + 1] == '=':
            num_equal = num_equal + 1
        if word_list[i] == '>' and word_list[i + 1] != '=' and word_list[i - 1] != '-':  # consider ->
            num_larger = num_larger + 1
        if word_list[i] == '>' and word_list[i + 1] == '=':
            num_larger_equal = num_larger_equal + 1
        if word_list[i] == '<' and word_list[i + 1] != '=':
            num_smaller = num_smaller + 1
        if word_list[i] == '<' and word_list[i + 1] == '=':
            num_smaller_equal = num_smaller_equal + 1
        if word_list[i] == '-' and word_list[i + 1] == '>':
            num_imply = num_imply + 1
        # keyword
        if word_list[i] in keyword_list:
            num_keyword = num_keyword + 1

    num_sub_formula = \
        num_equal + num_larger + num_larger_equal + num_smaller + num_smaller_equal + num_imply + num_keyword

    return num_sub_formula


def template_refine(raw_template):
    relation_list = ['id = = num', 'id = = id', 'id > = num', 'id > num', 'id < = num', 'id < num']
    for string in relation_list:
        if string in raw_template:
            raw_template = raw_template.replace(string, 'phi')

    return raw_template


template_list = []
sub_formula_num_list = []
overall_id_num_list = []
overall_id_char_num_list = []
overall_num_digit_num_list = []

count = 0
for i in range(len(stl_data_info_list)):
    if count % 10000 == 0:
        print(count)

    # template
    raw_template = stl_data_info_list[i]['formula_template']
    template = template_refine(raw_template)
    stl_data_info_list[i]['refined_formula_template'] = template
    template_list.append(template)

    # sub-formula
    # template_string = stl_data_info_list[i]['formula_template']
    template_word_list = stl_data_info_list[i]['formula_template'].split(' ')
    sub_formula_num_list.append(get_sub_formula_num(template_word_list))

    # statistical info of id and num
    overall_id_num_list.append(stl_data_info_list[i]['formula_id_num_info_dict']['id_number'])
    overall_id_char_num_list = \
        overall_id_char_num_list + stl_data_info_list[i]['formula_id_num_info_dict']['char_num_list']
    overall_num_digit_num_list = \
        overall_num_digit_num_list + stl_data_info_list[i]['formula_id_num_info_dict']['digit_num_list']

    count = count + 1

template_set = set(template_list)
# for i in list(template_set):
#     print(i)

print('-------------------------- operator existence analysis --------------------------')
operator_dict = {
    'equal': 0,
    'larger': 0,
    'largerEqual': 0,
    'smaller': 0,
    'smallerEqual': 0,
    'not': 0,
    'rise': 0,
    'fall': 0,
    'eventually': 0,
    'always': 0,
    'once': 0,
    'historically': 0,
    'until': 0,
    'since': 0,
    'and': 0,
    'or': 0,
    'imply': 0
}

count = 0
for i in range(len(stl_data_info_list)):
    if count % 10000 == 0:
        print(count)

    if '= =' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['equal'] = operator_dict['equal'] + 1
    if 'id > num' in stl_data_info_list[i]['formula_template']:
        operator_dict['larger'] = operator_dict['larger'] + 1
    if '> =' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['largerEqual'] = operator_dict['largerEqual'] + 1
    if 'id < num' in stl_data_info_list[i]['formula_template']:
        operator_dict['smaller'] = operator_dict['smaller'] + 1
    if '< =' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['smallerEqual'] = operator_dict['smallerEqual'] + 1
    if 'not' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['not'] = operator_dict['not'] + 1
    if 'rise' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['rise'] = operator_dict['rise'] + 1
    if 'fall' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['fall'] = operator_dict['fall'] + 1
    if 'eventually' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['eventually'] = operator_dict['eventually'] + 1
    if 'always' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['always'] = operator_dict['always'] + 1
    if 'once' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['once'] = operator_dict['once'] + 1
    if 'historically' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['historically'] = operator_dict['historically'] + 1
    if 'until' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['until'] = operator_dict['until'] + 1
    if 'since' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['since'] = operator_dict['since'] + 1
    if 'and' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['and'] = operator_dict['and'] + 1
    if 'or' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['or'] = operator_dict['or'] + 1
    if '- >' in stl_data_info_list[i]['formula_pre_tokenized']:
        operator_dict['imply'] = operator_dict['imply'] + 1

    count = count + 1

# print(operator_dict)
sentence_num_list = list(operator_dict.values())

print('-------------------------- Table 1 Info --------------------------')
print('formula number:', len(stl_data_info_list))
print('template number:', len(template_set))
print('min # sub formula per formula:', min(sub_formula_num_list))
print('max # sub formula per formula:', max(sub_formula_num_list))
print('avg # sub formula per formula:', np.mean(sub_formula_num_list))
print('median # sub formula per formula:', np.median(sub_formula_num_list))

print('-------------------------- Table 2 Info --------------------------')
print('avg # operator per formula:', np.mean(sub_formula_num_list))
print('median # operator per formula:', np.median(sub_formula_num_list))
print('max # operator per formula:', max(sub_formula_num_list))
print('avg # formula per operator:', np.mean(sentence_num_list))
print('median # formula per operator:', np.median(sentence_num_list))
print('max # formula per operator:', max(sentence_num_list))

print('-------------------------- Table 3 Info --------------------------')
print('avg # of identifiers per formula:', np.mean(overall_id_num_list))
# print('max # of identifiers per formula:', max(overall_id_num_list))
print('min # of chars per identifier:', min(overall_id_char_num_list))
print('avg # of chars per identifier:', np.mean(overall_id_char_num_list))
print('median # of chars per identifier:', np.median(overall_id_char_num_list))
print('min # of digits per constant:', min(overall_num_digit_num_list))
# print('max # of digits per constant:', max(overall_num_digit_num_list))
print('avg # of digits per constant:', np.mean(overall_num_digit_num_list))
print('median # of digits per constant:', np.median(overall_num_digit_num_list))

# for item in template_set:
#     print(item)
