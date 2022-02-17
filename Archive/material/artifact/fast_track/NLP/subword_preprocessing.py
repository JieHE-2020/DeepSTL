import random
import numpy as np

# IMPORTANT SETTINGS
seed = 100
np.random.seed(seed)
random.seed(seed)


from public import hyperparameters
from public import paths
from data_preprocessing.subword.tokenizer import BPEtokenizer
from data_preprocessing.subword.tokenizer import eng_wordlevel_tokenizer
from data_preprocessing.subword.tokenizer import stl_wordlevel_tokenizer
import pandas as pd
import pickle
import math


class SubwordDataPreprocess:
    def __init__(self):
        self.eng_data_list, self.stl_data_list, \
        self.train_dev_eng_list, self.train_dev_stl_list, self.test_eng_list, self.test_stl_list = self.get_data_list()
        self.eng_tokenizer, self.stl_tokenizer = self.get_subword_tokenizer()
        self.eng_word_tokenizer, self.stl_word_tokenizer = self.get_wordlevel_tokenizer()
        self.max_length = self.find_max_length()
        self.write_file()

    @staticmethod
    def get_data_list():
        print('read data set')
        df = pd.read_csv(paths.csv_path)
        eng_data_original_list = list(df['English'])
        stl_data_original_list = list(df['STL'])

        num_examples = len(eng_data_original_list)
        indices = list(range(num_examples))
        random.shuffle(indices)

        eng_data_list = [eng_data_original_list[index] for index in indices]
        stl_data_list = [stl_data_original_list[index] for index in indices]

        with open(paths.tokenization_dataset_path[0], 'a') as f:
            for i in range(len(eng_data_list)):
                f.write(eng_data_list[i] + '\n')
                f.write(stl_data_list[i] + '\n')

        print('data list generation done')
        test_set_num = math.floor(len(eng_data_list) * hyperparameters.test_ratio)
        test_eng_list = eng_data_list[:test_set_num]
        test_stl_list = stl_data_list[:test_set_num]
        train_dev_eng_list = eng_data_list[test_set_num:]
        train_dev_stl_list = stl_data_list[test_set_num:]

        return eng_data_list, stl_data_list, train_dev_eng_list, train_dev_stl_list, test_eng_list, test_stl_list

    @staticmethod
    def get_subword_tokenizer():
        eng_tokenizer, stl_tokenizer = BPEtokenizer.process_BPE_tokenization()
        return eng_tokenizer, stl_tokenizer

    @staticmethod
    def get_wordlevel_tokenizer():
        eng_word_tokenizer = eng_wordlevel_tokenizer.eng_wordlevel_tokenization()
        stl_word_tokenizer = stl_wordlevel_tokenizer.stl_wordlevel_tokenization()
        return eng_word_tokenizer, stl_word_tokenizer

    def find_max_length(self):
        print('start tokenizing')
        eng2id_list = []
        stl2id_list = []
        eng_max_length = 0
        stl_max_length = 0

        for eng, stl in zip(self.eng_data_list, self.stl_data_list):
            eng2id_list.append(self.eng_tokenizer.encode(eng).ids)
            eng_id_len = len(eng2id_list[-1])
            if eng_id_len > eng_max_length:
                eng_max_length = eng_id_len

            stl2id_list.append(self.stl_tokenizer.encode(stl).ids)
            stl_id_len = len(stl2id_list[-1])
            if stl_id_len > stl_max_length:
                stl_max_length = stl_id_len

        max_length = max(eng_max_length, stl_max_length) + 2  # consider <bos>, <eos>

        return max_length

    def write_file(self):
        preprocess_info_dict = dict()
        preprocess_info_dict['train_dev_eng_list'] = self.train_dev_eng_list
        preprocess_info_dict['train_dev_stl_list'] = self.train_dev_stl_list
        preprocess_info_dict['test_eng_list'] = self.test_eng_list
        preprocess_info_dict['test_stl_list'] = self.test_stl_list
        preprocess_info_dict['eng_tokenizer'] = self.eng_tokenizer
        preprocess_info_dict['stl_tokenizer'] = self.stl_tokenizer
        preprocess_info_dict['eng_word_tokenizer'] = self.eng_word_tokenizer
        preprocess_info_dict['stl_word_tokenizer'] = self.stl_word_tokenizer
        preprocess_info_dict['max_length'] = self.max_length

        f = open(paths.preprocess_info_dict_path, 'wb')
        pickle.dump(preprocess_info_dict, f)
        f.close()

        return preprocess_info_dict


data = SubwordDataPreprocess()
# print(data.train_dev_eng_list[0])
# print(data.train_dev_stl_list[0])
# print(data.train_dev_eng_list[-1])
# print(data.train_dev_stl_list[-1])
