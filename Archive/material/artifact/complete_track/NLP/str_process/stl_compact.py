from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
from public import paths
import pickle
import copy

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
def id_num_recognize(word_list, formula_pre_tokenized):
    # print(word_list)
    total_len = len(word_list)
    key_word_list = []
    for i in range(len(word_list)):
        if word_list[i] in vocab_list_no_id_num:
            key_word_list.append({
                'type': 'key',
                'fragment': [word_list[i]],
                'word_list_index': [i, i]
            })
    # print(key_word_list)

    non_key_word_list = []
    for j in range(len(key_word_list)):
        if j == 0:  # the first element in key_word_list
            if key_word_list[j]['word_list_index'][0] > 0:
                left = 0
                right = key_word_list[j]['word_list_index'][0]
                non_key_word_list.append({
                    'type': 'non-key',
                    'fragment': word_list[left:right],
                    'word_list_index': [left, right - 1]
                })
        elif 0 < j < len(key_word_list) - 1:  # not the first element nor the last element in key_word_list
            left = key_word_list[j]['word_list_index'][0]
            right = key_word_list[j+1]['word_list_index'][0]
            if right - left > 1:
                non_key_word_list.append({
                    'type': 'non-key',
                    'fragment': word_list[left + 1:right],
                    'word_list_index': [left + 1, right - 1]
                })
        else:  # the last element in key_word_list
            if key_word_list[j]['word_list_index'][0] < len(word_list) - 1:  # there are still non key words afterwards
                left = key_word_list[j]['word_list_index'][0]
                right = len(word_list) - 1
                non_key_word_list.append({
                    'type': 'non-key',
                    'fragment': word_list[left + 1:],
                    'word_list_index': [left + 1, right]
                })
    # print(non_key_word_list)

    refined_word_list = key_word_list + non_key_word_list
    refined_word_list.sort(key=lambda obj: obj['word_list_index'][1])

    id_list = []
    num_list = []
    for item in refined_word_list:
        if item['type'] == 'non-key':
            # start analysis
            fragment_analysis_list = []
            template_list = []
            symbol_list = copy.deepcopy(item['fragment'])
            # print(symbol_list)
            while len(symbol_list) > 0:
                if len(symbol_list) > 1:
                    # check the identity of the first element of symbol_list
                    if symbol_list[0] in letter_underscore_list:
                        match_type = 'identifier'
                        new_id_list = [symbol_list[0]]
                    elif (symbol_list[0] in digit_list) or (symbol_list[0] == '0' and symbol_list[1] == '.'):
                    # elif (symbol_list[0] in digit_list and symbol_list[0] != '0') or \
                    #         (symbol_list[0] == '0' and symbol_list[1] == '.'):
                        match_type = 'number'
                        new_num_list = [symbol_list[0]]
                    else:
                        match_type = 'others'

                    if match_type == 'identifier':
                        right = i = 1
                        for i in range(1, len(symbol_list)):
                            if symbol_list[i] in letter_digit_underscore_list:
                                right = i + 1
                            else:
                                right = i
                                break
                        new_id_list = new_id_list + symbol_list[1:right]
                        fragment_analysis_list.append([new_id_list, 'i d'])
                        template_list.append('i d')
                        id_list.append(' '.join(new_id_list))
                        del symbol_list[0:right]
                    elif match_type == 'number':
                        right = i = 1
                        for i in range(1, len(symbol_list)):
                            if symbol_list[i] in digit_list:
                                right = i + 1
                            elif symbol_list[i] == '.' and i < len(symbol_list) - 1:
                                if '.' not in symbol_list[0:i] and symbol_list[i+1] in digit_list:
                                    right = i + 1
                                else:
                                    right = i
                                    break
                            else:
                                right = i
                                break
                        new_num_list = new_num_list + symbol_list[1:right]
                        fragment_analysis_list.append([new_num_list, 'n u m'])
                        template_list.append('n u m')
                        num_list.append(' '.join(new_num_list))
                        del symbol_list[0:right]
                    else:
                        fragment_analysis_list.append([[symbol_list[0]], symbol_list[0]])
                        template_list.append(symbol_list[0])
                        del symbol_list[0:1]

                else:
                    if symbol_list[0] in letter_underscore_list:
                        match_type = 'identifier'
                        fragment_analysis_list.append([[symbol_list[0]], 'i d'])
                        template_list.append('i d')
                        id_list.append(' '.join(symbol_list[0]))
                    elif symbol_list[0] in digit_list:
                        match_type = 'number'
                        fragment_analysis_list.append([[symbol_list[0]], 'n u m'])
                        template_list.append('n u m')
                        num_list.append(' '.join(symbol_list[0]))
                    else:
                        match_type = 'others'
                        fragment_analysis_list.append([[symbol_list[0]], symbol_list[0]])
                        template_list.append(symbol_list[0])
                    del symbol_list[0:1]
            # print('fragment_analysis_list:', fragment_analysis_list)
            # print('template_list:', template_list)
            # print()
            item['fragment_analysis'] = fragment_analysis_list
            item['template'] = template_list
    # print('refined_word_list:', refined_word_list)

    word_list_new_1 = []
    for item in refined_word_list:
        word_list_new_1 = word_list_new_1 + item['fragment']
    str_get_back = ' '.join(word_list_new_1)
    if formula_pre_tokenized != str_get_back:
        print('false')

    word_list_new_2 = []
    for item in refined_word_list:
        if item['type'] == 'key':
            word_list_new_2 = word_list_new_2 + item['fragment']
        else:
            word_list_new_2 = word_list_new_2 + item['template']
    template_get_back = ' '.join(word_list_new_2)
    # print(formula_pre_tokenized)
    # print(template_get_back)

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
        'id_number': len(id_set),  # a > 1 and a < 1 (counted as 1 identifier)
        'num_number': len(num_list),
        'char_num_list': char_num_list,
        'digit_num_list': digit_num_list,
        'formula_template': template_get_back
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
        formula_id_num_info_dict = id_num_recognize(formula_word_list, formula_pre_tokenized)

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


# stl_formula = 'always ( (rise (_ v N g f U Y W >= 7 4 1 9)) and (not fall (N g m f W c Z v q == n)) -> (fall (Y C R >= 8547 and Y C R < 9927)) and (not (q v b V D a M M == 4446.7)) )'
# print(stl_formula)
# print(delete_stl_id_num_space(stl_formula))
