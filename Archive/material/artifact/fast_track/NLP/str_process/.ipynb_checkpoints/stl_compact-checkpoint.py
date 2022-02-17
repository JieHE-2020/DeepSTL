from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
from public import paths
import pickle

letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
               'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
underscore_list = ['_']
letter_underscore_list = letter_list + underscore_list
letter_digit_list = letter_list + digit_list
letter_digit_underscore_list = letter_list + digit_list + underscore_list


# print('-------------------------- Pre-tokenization --------------------------')
pre_tokenizer = pre_tokenizers.Sequence([
    Whitespace(),
    Punctuation(),
    Digits(individual_digits=True)
])
# print('pre-tokenization instantiated')

# print('-------------------------- Tokenization --------------------------')
f = open(paths.preprocess_info_dict_path, 'rb')
preprocess_info_dict = pickle.load(f)
f.close()
tokenizer = preprocess_info_dict['stl_word_tokenizer']

#
# print('-------------------------- Obtain original vocab list --------------------------')
# print('vocab_size:', tokenizer.get_vocab_size())
vocab_list = list(tokenizer.get_vocab().keys())
# print(vocab_list)

# print('-------------------------- Process vocab list --------------------------')
letter_digit_underscore_dot_list = letter_digit_underscore_list + ['.']
letter_digit_underscore_dot_set = set(letter_digit_underscore_dot_list)

vocab_set_no_id_num = set(vocab_list) - letter_digit_underscore_dot_set - {'[UNK]'}
vocab_list_no_id_num = list(vocab_set_no_id_num)
# print(vocab_list_no_id_num)
# print(len(vocab_list_no_id_num))


# print('-------------------------- id and num recognition & raw template generation --------------------------')
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
    for id_str in id_set_no_space:
        char_num_list.append(len(id_str))
    for num_str in num_set_no_space:
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


def delete_stl_id_num_space(stl_formula):
    stl_data_list = [stl_formula]
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
        formula_template = formula_pre_tokenized
        id_list = list(formula_id_num_info_dict['id_set'])
        id_list.sort(key=lambda i: len(i), reverse=True)
        num_list = list(formula_id_num_info_dict['num_set'])
        num_list.sort(key=lambda i: len(i), reverse=True)

        for identifier in id_list:
            formula_template = formula_template.replace(identifier, 'id')
        for num in num_list:
            formula_template = formula_template.replace(num, 'num')

        # delete space for identifiers and numbers
        formula_compact = formula_pre_tokenized
        # delete space, could not use relevant info in formula_id_num_info_dict
        # this is because if two strings have identical length, problem will arise
        id_list_no_space = []
        num_list_no_space = []
        for id in id_list:
            id = id.replace(' ', '')
            id_list_no_space.append(id)
        for num in num_list:
            num = num.replace(' ', '')
            num_list_no_space.append(num)

        for i in range(len(id_list_no_space)):
            formula_compact = formula_compact.replace(id_list[i], id_list_no_space[i])
        for i in range(len(num_list_no_space)):
            formula_compact = formula_compact.replace(num_list[i], num_list_no_space[i])

        # assemble formula info
        formula_info_dict = {
            'formula': formula,
            'formula_word_list': formula_word_list,
            'formula_pre_tokenized': formula_pre_tokenized,
            'formula_id_num_info_dict': formula_id_num_info_dict,
            'formula_template': formula_template,
            'formula_compact': formula_compact
        }
        stl_data_info_list.append(formula_info_dict)
    # print('recognition id and num finished')

    # # for test
    # return stl_data_info_list[0]
    formula_compact = stl_data_info_list[0]['formula_compact']
    formula_compact = formula_compact.replace('= =', '==')
    formula_compact = formula_compact.replace('> =', '>=')
    formula_compact = formula_compact.replace('< =', '<=')
    formula_compact = formula_compact.replace('- >', '->')

    return formula_compact


# stl_formula = 'always ( (rise (_ v N g f U Y W >= 7419)) and (not fall (N g m f W c Z v q == n)) -> (fall (Y C R >= 8547 and Y C R < 9927)) and (not (q v b V D a M M == 4446.7)) )'
# print(stl_formula)
# print(delete_stl_id_num_space(stl_formula))
