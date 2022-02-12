import copy
import re
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


# print('-------------------------- Tokenization --------------------------')
f = open(paths.preprocess_info_dict_path, 'rb')
preprocess_info_dict = pickle.load(f)
f.close()
tokenizer = preprocess_info_dict['eng_word_tokenizer']

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
vocab_set_final = vocab_set_no_id_num - {'(', ')', '[', ']', '{', '}', ',', '\'', ':'}
vocab_list_final = list(vocab_set_final)
# print(vocab_list_final)
# print(len(vocab_list_final))
# print('---------------------------------------------------------------------------------')


def split_identifier(string):
    output_sentence = copy.deepcopy(string)
    word_set = set(re.findall('[A-Za-z_][\w]*', output_sentence))
    # print(word_set)
    include_identifier_list = list(word_set - vocab_set_final)
    include_identifier_list.sort(key=lambda i: len(i), reverse=True)
    # print(include_identifier_list)

    for string in include_identifier_list:
        str_list = list(string)
        new_str = ' '.join(str_list)
        # print(new_str)
        output_sentence = output_sentence.replace(string, new_str)

    return output_sentence


# eng_string = 'Whenever Op_Cmd is set to Running and Spd_Tgt is in [0, 1000] for at least 20 time units then in response PWM should enter the range of [1, 12] at sometime within 200 time units.'
# eng_string_split = split_identifier(eng_string)
# print(eng_string)
# print(eng_string_split)
