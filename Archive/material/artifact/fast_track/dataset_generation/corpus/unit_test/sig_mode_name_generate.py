import random
from public import parameters
import global_variables_id

# max_sig_string_length = 20
# max_string_length_inside_parentheses = 5
# max_mode_name_length = 20
# alpha = 0.98


letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
underscore_list = ['_']
letter_underscore_list = letter_list + underscore_list
letter_digit_list = letter_list + digit_list
letter_digit_underscore_list = letter_list + digit_list + underscore_list

p_letter = \
    len(letter_list) ** parameters.alpha / \
    (len(letter_list) ** parameters.alpha + len(digit_list) ** parameters.alpha + (len(underscore_list)+1) ** parameters.alpha)
p_digit = \
    len(digit_list) ** parameters.alpha / \
    (len(letter_list) ** parameters.alpha + len(digit_list) ** parameters.alpha + (len(underscore_list)+1) ** parameters.alpha)
p_underscore = \
    (len(underscore_list)+1) ** parameters.alpha / \
    (len(letter_list) ** parameters.alpha + len(digit_list) ** parameters.alpha + (len(underscore_list)+1) ** parameters.alpha)


def random_symbol_select():
    point = random.uniform(0, 1)
    if point <= p_letter:
        symbol = random.choice(letter_list)
    elif p_letter < point <= p_letter + p_digit:
        symbol = random.choice(digit_list)
    else:
        symbol = underscore_list[0]

    return symbol


def random_identifier_generate():
    # for unit testing
    id_str_length = random.randint(1, parameters.max_identifier_length)
    id_str_first_symbol = random.choice(letter_underscore_list)

    if id_str_length == 1:
        id_str = id_str_first_symbol
    else:
        id_str_second_part = ''
        for i in range(id_str_length - 1):
            id_str_second_part = id_str_second_part + random_symbol_select()
        id_str = id_str_first_symbol + id_str_second_part

    id_str_list = list(id_str)
    new_id_str = ' '.join(id_str_list)
    # id_string = 'i d : ' + new_id_str
    id_string = new_id_str

    # # for execution of the whole program, not for unit testing
    # index = global_variables_id.get_value('ID_COUNTER')
    # index = index + 1
    # global_variables_id.set_value('ID_COUNTER', index)
    # id_string = 'id' + str(index)

    return id_string


def random_identifier_substitute():
    id_str_length = random.randint(1, parameters.max_identifier_length)
    id_str_first_symbol = random.choice(letter_underscore_list)

    if id_str_length == 1:
        id_str = id_str_first_symbol
    else:
        id_str_second_part = ''
        for i in range(id_str_length - 1):
            id_str_second_part = id_str_second_part + random_symbol_select()
        id_str = id_str_first_symbol + id_str_second_part

    # if split:
    #     id_str_list = list(id_str)
    #     new_id_str = ' '.join(id_str_list)
    #     id_string = new_id_str
    # else:
    id_string = id_str

    return id_string


# print("p_letter(%):", p_letter * 100)
# print("p_digit(%):", p_digit * 100)
# print("p_underscore(%):", p_underscore * 100)
#
# for i in range(100):
#     print(random_identifier_substitute())
