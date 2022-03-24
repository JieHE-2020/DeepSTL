import pandas as pd
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
import pickle


def pre_tokenize(formula):
    pre_tokenizer = pre_tokenizers.Sequence([
        Whitespace(),
        Punctuation(),
        Digits(individual_digits=True)
    ])
    word_list = []
    for item in pre_tokenizer.pre_tokenize_str(formula):
        word_list.append(item[0])
    pretokenized_formula = ' '.join(word_list)

    return word_list, pretokenized_formula


# algorithmic operator
num_equal = 0
num_larger = 0
num_larger_equal = 0
num_smaller = 0
num_smaller_equal = 0

# rise, fall, negate operator
num_single_rise = 0
num_single_fall = 0
num_rise = 0
num_fall = 0
num_not = 0
num_not_rise = 0
num_not_fall = 0

# temporal operator
num_eventually = 0
num_always = 0
num_once = 0
num_historically = 0
num_until = 0
num_since = 0

# and, or, imply operator#
num_and = 0
num_or = 0
num_imply = 0

df = pd.read_csv('./corpus_split.csv')
stl_data_list = list(df['STL'])
print('read data set finished')
count = 0
for formula in stl_data_list:
    if count % 10000 == 0:
        print(count)
    word_list, pretokenized_formula = pre_tokenize(formula)
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

        # rise, fall, negate operator
        if word_list[i] == 'rise' and word_list[i - 1] != 'not':
            num_single_rise = num_single_rise + 1
        if word_list[i] == 'fall' and word_list[i - 1] != 'not':
            num_single_fall = num_single_fall + 1
        if word_list[i] == 'not':
            num_not = num_not + 1
        if word_list[i] == 'not' and word_list[i + 1] == 'rise':
            num_not_rise = num_not_rise + 1
        if word_list[i] == 'not' and word_list[i + 1] == 'fall':
            num_not_fall = num_not_fall + 1

        # temporal operator
        if word_list[i] == 'eventually':
            num_eventually = num_eventually + 1
        if word_list[i] == 'always':
            num_always = num_always + 1
        if word_list[i] == 'once':
            num_once = num_once + 1
        if word_list[i] == 'historically':
            num_historically = num_historically + 1
        if word_list[i] == 'until':
            num_until = num_until + 1
        if word_list[i] == 'since':
            num_since = num_since + 1

        # and, or operator
        if word_list[i] == 'and':
            num_and = num_and + 1
        if word_list[i] == 'or':
            num_or = num_or + 1

    count = count + 1

# num_always = num_always - len(stl_data_list)  # do not consider 'always' in the beginning
num_rise = num_single_rise + num_not_rise
num_fall = num_single_fall + num_not_fall

# algorithmic operator
print()
print('num_equal:', num_equal)
print('num_larger:', num_larger)
print('num_larger_equal:', num_larger_equal)
print('num_smaller:', num_smaller)
print('num_smaller_equal:', num_smaller_equal)
print()

# rise, fall, negate operator
print('num_rise:', num_rise)
print('num_fall:', num_fall)
print('num_not:', num_not)
print()

# temporal operator
print('num_eventually:', num_eventually)
print('num_always:', num_always)
print('num_once:', num_once)
print('num_historically:', num_historically)
print('num_until:', num_until)
print('num_since:', num_since)
print()

# and, or, imply operator
print('num_and:', num_and)
print('num_or:', num_or)
print('num_imply:', num_imply)
