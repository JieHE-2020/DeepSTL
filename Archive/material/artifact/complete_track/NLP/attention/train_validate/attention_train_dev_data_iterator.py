from public import hyperparameters
from public import paths
from attention import attention_hyperparas
import torch
from d2l import torch as d2l
import pickle
import math


class AttentionTrainDevDataIterator:
    def __init__(self, seed):
        preprocess_info_dict = self.read_file()
        self.train_dev_eng_list = preprocess_info_dict['train_dev_eng_list']
        self.train_dev_stl_list = preprocess_info_dict['train_dev_stl_list']
        self.eng_tokenizer = preprocess_info_dict['eng_tokenizer']
        self.stl_tokenizer = preprocess_info_dict['stl_tokenizer']
        self.max_length = preprocess_info_dict['max_length']
        self.train_eng_list, self.train_stl_list, self.dev_eng_list, self.dev_stl_list = self.train_dev_split()
        train_eng2id_list, train_stl2id_list = self.tokenize(self.train_eng_list, self.train_stl_list)
        dev_eng2id_list, dev_stl2id_list = self.tokenize(self.dev_eng_list, self.dev_stl_list)

        train_eng_array, train_eng_valid_len = self.build_array_nmt(train_eng2id_list, self.eng_tokenizer)
        train_stl_array, train_stl_valid_len = self.build_array_nmt(train_stl2id_list, self.stl_tokenizer)
        self.train_data_arrays = (train_eng_array, train_eng_valid_len, train_stl_array, train_stl_valid_len)

        dev_eng_array, dev_eng_valid_len = self.build_array_nmt(dev_eng2id_list, self.eng_tokenizer)
        dev_stl_array, dev_stl_valid_len = self.build_array_nmt(dev_stl2id_list, self.stl_tokenizer)
        self.dev_data_arrays = (dev_eng_array, dev_eng_valid_len, dev_stl_array, dev_stl_valid_len)

        self.train_data_iter = d2l.load_array(self.train_data_arrays, attention_hyperparas.batch_size)
        self.dev_data_iter = d2l.load_array(self.dev_data_arrays, attention_hyperparas.batch_size)
        self.write_file(seed)

    @staticmethod
    def read_file():
        f = open(paths.preprocess_info_dict_path, 'rb')
        preprocess_info_dict = pickle.load(f)
        f.close()

        return preprocess_info_dict

    def write_file(self, seed):
        data_iter_dict = {'train': self.train_data_iter, 'dev': self.dev_data_iter}
        f = open(paths.attention_record_path + str(seed) + '/data_iter_dict', 'wb')
        pickle.dump(data_iter_dict, f)
        f.close()

    def train_dev_split(self):
        dev_set_num = math.floor(len(self.train_dev_eng_list) * hyperparameters.dev_ratio)
        dev_eng_list = self.train_dev_eng_list[:dev_set_num]
        dev_stl_list = self.train_dev_stl_list[:dev_set_num]
        train_eng_list = self.train_dev_eng_list[dev_set_num:]
        train_stl_list = self.train_dev_stl_list[dev_set_num:]

        return train_eng_list, train_stl_list, dev_eng_list, dev_stl_list

    def tokenize(self, eng_data_list, stl_data_list):
        eng2id_list = []
        stl2id_list = []

        for eng, stl in zip(eng_data_list, stl_data_list):
            eng2id_list.append(self.eng_tokenizer.encode(eng).ids)
            stl2id_list.append(self.stl_tokenizer.encode(stl).ids)

        return eng2id_list, stl2id_list

    @staticmethod
    def truncate_pad(line, num_steps, pad_token):
        """Truncate or pad sequences."""
        # pad_token is a list
        if len(line) > num_steps:
            return line[:num_steps]  # Truncate
        return line + pad_token * (num_steps - len(line))  # Pad

    def build_array_nmt(self, id_list, tokenizer):
        # add token id of <eos>
        id_list = [l + tokenizer.encode('<eos>').ids for l in id_list]
        # pad or truncate
        array = \
            torch.tensor([self.truncate_pad(l, self.max_length, tokenizer.encode('<pad>').ids) for l in id_list])
        valid_len = (array != tokenizer.encode('<pad>').ids[0]).type(torch.int32).sum(1)

        return array, valid_len


# seed = 100
# data = AttentionTrainDevDataIterator(seed)
# for X, X_valid_len, Y, Y_valid_len in data.train_data_iter:
#     print('X:', X.type(torch.int32))
#     print('valid lengths for X:', X_valid_len)
#     print('X_valid_len.shape:', X_valid_len.shape)
#     print('Y:', Y.type(torch.int32))
#     print('valid lengths for Y:', Y_valid_len)
#     #print(X.shape)
#     break
# print()
#
# print('first load:')
# f = open(paths.attention_record_path + str(seed) + '/data_iter_dict', 'rb')
# data_iter_dict = pickle.load(f)
# f.close()
# train_data_iter = data_iter_dict['train']
# state = torch.get_rng_state()
# # print(state)
# for i in range(2):
#     for X, X_valid_len, Y, Y_valid_len in train_data_iter:
#         print('X:', X.type(torch.int32))
#         # print('valid lengths for X:', X_valid_len)
#         # print('X_valid_len.shape:', X_valid_len.shape)
#         # print('Y:', Y.type(torch.int32))
#         # print('Y[0].size:', Y[0].size(0))
#         # print('valid lengths for Y:', Y_valid_len)
#         #print(X.shape)
#         break
# print()
# print('second load:')
# torch.set_rng_state(state)
# f = open(paths.attention_record_path + str(seed) + '/data_iter_dict', 'rb')
# data_iter_dict = pickle.load(f)
# f.close()
# train_data_iter = data_iter_dict['train']
# for i in range(2):
#     for X, X_valid_len, Y, Y_valid_len in train_data_iter:
#         print('X:', X.type(torch.int32))
#         # print('valid lengths for X:', X_valid_len)
#         # print('X_valid_len.shape:', X_valid_len.shape)
#         # print('Y:', Y.type(torch.int32))
#         # print('Y[0].size:', Y[0].size(0))
#         # print('valid lengths for Y:', Y_valid_len)
#         #print(X.shape)
#         break
