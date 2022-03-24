import pandas as pd
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
import pickle
import numpy as np


letter_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
               'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
underscore_list = ['_']
letter_underscore_list = letter_list + underscore_list
letter_digit_list = letter_list + digit_list
letter_digit_underscore_list = letter_list + digit_list + underscore_list


print('-------------------------- Read data set --------------------------')
df = pd.read_csv('./corpus_split.csv')
eng_data_list = list(df['English'])
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
tokenizer.train_from_iterator(eng_data_list, trainer)
tokenizer.save("./eng_wordlevel_tokenizer.json", pretty=True)
tokenizer = Tokenizer.from_file("./eng_wordlevel_tokenizer.json")
print('tokenization finished')

print('-------------------------- Obtain original vocab list --------------------------')
print('vocab_size:', tokenizer.get_vocab_size())
vocab_list = list(tokenizer.get_vocab().keys())
print('vocab_size:', vocab_list)

input_sentence = 'As soon as G U q doesn\'t get set to J 1 z A and the state of signal Y is q w p M h g L then in response there should be a certain time point within the next 583.17 time units, at which the t U j J X signal is between [5, 6] finally.'
print('input sentence:', input_sentence)
output = tokenizer.encode(input_sentence)
print('tokens:', output.tokens)
print('token ids:', output.ids)
line = tokenizer.decode(output.ids, skip_special_tokens=False)
print('input sentence after tokenization:', line)
# test pre-tokenization
sentence_word_list = []
for item in pre_tokenizer.pre_tokenize_str(input_sentence):
    sentence_word_list.append(item[0])
sentence_pre_tokenized = ' '.join(sentence_word_list)
print('sentence_pre_tokenized:', sentence_pre_tokenized)


print('-------------------------- Process vocab list --------------------------')
letter_digit_underscore_dot_list = letter_digit_underscore_list + ['.']
letter_digit_underscore_dot_set = set(letter_digit_underscore_dot_list)

vocab_set_no_id_num = set(vocab_list) - letter_digit_underscore_dot_set - {'[UNK]'}
vocab_list_no_id_num = list(vocab_set_no_id_num)
print('vocab_list_no_id_num:', vocab_list_no_id_num)
print(len(vocab_list_no_id_num))
vocab_set_final = vocab_set_no_id_num - {'(', ')', '[', ']', '{', '}', ',', '\'', ':'}
vocab_list_final = list(vocab_set_final)
print('vocab_list_final:', vocab_list_final)
print(len(vocab_list_final))

distinct_vocab_set = set()
for word in vocab_list_final:
    distinct_vocab_set.add(word.lower())

# 1. do not distinguish capital or lower-case letter,
# 2. different formats of the same word are considered different words
distinct_vocab_list = list(distinct_vocab_set)
print('distinct_vocab_list:', distinct_vocab_list)
print(len(distinct_vocab_list))


print('-------------------------- compute word per sentence --------------------------')
sentence_info_dict = {}
eng_data_info_list = []
sentence_effective_word_num_list = []

count = 0
for sentence in eng_data_list:
    if count % 10000 == 0:
        print(count)

    sentence_effective_word_num = 0
    # option 1: use pre-tokenization
    sentence_word_list = []
    for item in pre_tokenizer.pre_tokenize_str(sentence):
        sentence_word_list.append(item[0])
    sentence_pre_tokenized = ' '.join(sentence_word_list)

    # # option 2: use wordlevel tokenizer (equivalent to option 1 in test)
    # output = tokenizer.encode(sentence)
    # sentence_word_list = output.tokens
    # sentence_pre_tokenized = tokenizer.decode(output.ids, skip_special_tokens=False)

    for token in sentence_word_list:
        if token in vocab_list_final:
            sentence_effective_word_num = sentence_effective_word_num + 1
    sentence_effective_word_num_list.append(sentence_effective_word_num)

    sentence_info_dict = {
        'sentence': sentence,
        'sentence_word_list': sentence_word_list,
        'sentence_pre_tokenized': sentence_pre_tokenized,
        'sentence_effective_word_num': sentence_effective_word_num
    }

    eng_data_info_list.append(sentence_info_dict)
    count = count + 1

print('-------------------------- compute sentence per word --------------------------')
num_sentence_per_word_list = []
count = 0

for word in vocab_list_final:
    if count % 10 == 0:
        print(count)
    sentence_num = 0
    for i in range(len(eng_data_info_list)):
        if word in eng_data_info_list[i]['sentence_pre_tokenized']:
            sentence_num = sentence_num + 1
    num_sentence_per_word_list.append(sentence_num)
    count = count + 1


print('-------------------------- Table 4 Info --------------------------')
print('# of sentences:', len(eng_data_list))
print('# of words:', len(distinct_vocab_list))
print('avg # of words per sentence:', np.mean(sentence_effective_word_num_list))
print('median # of words per sentence:', np.median(sentence_effective_word_num_list))
print('avg # of sentence per word:', np.mean(num_sentence_per_word_list))
print('median # sentence per word:', np.median(num_sentence_per_word_list))

