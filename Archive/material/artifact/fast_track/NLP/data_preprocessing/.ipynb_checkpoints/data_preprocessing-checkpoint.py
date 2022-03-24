import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
import shutil
import pickle
import os
from public import hyperparameters
from public import paths
from data.tokenizer import tokenizer


class DataPreprocess:
    def __init__(self, train_from_start):
        self.csv_path = paths.csv_path
        self.train_val_sample_list_path = paths.train_val_sample_list_path
        self.eng_train_list_path = paths.eng_train_list_path
        self.eng_val_list_path = paths.eng_val_list_path
        self.stl_train_list_path = paths.stl_train_list_path
        self.stl_val_list_path = paths.stl_val_list_path
        self.joint_tokenizer_path = paths.joint_tokenizer_path
        self.max_length_info_path = paths.max_length_info_path
        self.max_length_eng_path = paths.max_length_eng_path
        self.max_length_stl_path = paths.max_length_stl_path
        self.max_length_path = paths.max_length_path
        # start preprocess
        self.eng_train_list, self.eng_val_list, self.stl_train_list, self.stl_val_list = \
            self.get_data_list(train_from_start)
        self.train_examples, self.val_examples = self.get_data_tensor()
        self.eng_tokenizer, self.stl_tokenizer = self.tokenize(train_from_start)
        self.max_length_eng, self.max_length_stl, self.max_length = self.find_max_length(train_from_start)

        # for x, y in self.train_examples.take(1):
        #     print(x.shape)
        #     print(y.shape)
        #     print(x)
        #     print(y)

        self.train_dataset = self.train_examples.map(self.tf_encode_to_subword)
        self.train_dataset = self.train_dataset.filter(self.filter_by_max_length)
        # train_dataset has two dimensions, one for eng, the other for stl
        self.train_dataset = self.train_dataset.shuffle(hyperparameters.buffer_size).\
            padded_batch(hyperparameters.batch_size, padded_shapes=([-1], [-1]))

        self.validate_dataset = self.val_examples.map(self.tf_encode_to_subword)
        # valid_dataset has two dimensions, one for eng, the other for stl
        self.validate_dataset = self.validate_dataset.filter(
            self.filter_by_max_length).\
            padded_batch(hyperparameters.batch_size, padded_shapes=([-1], [-1]))
        print('train and validation dataset prepared')

    def get_data_list(self, train_from_start):
        print('read data set')
        if train_from_start:
            df = pd.read_csv(self.csv_path)
            eng_data_list = list(df['English'])
            stl_data_list = list(df['STL'])

            eng_train_list, eng_val_list, stl_train_list, stl_val_list = \
                train_test_split(eng_data_list, stl_data_list, test_size=hyperparameters.test_ratio)

            if os.path.exists(self.train_val_sample_list_path):
                shutil.rmtree(self.train_val_sample_list_path)

            if not os.path.exists(self.train_val_sample_list_path):
                os.mkdir(self.train_val_sample_list_path)

            f = open(self.eng_train_list_path, 'wb')
            pickle.dump(eng_train_list, f)
            f.close()

            f = open(self.eng_val_list_path, 'wb')
            pickle.dump(eng_val_list, f)
            f.close()

            f = open(self.stl_train_list_path, 'wb')
            pickle.dump(stl_train_list, f)
            f.close()

            f = open(self.stl_val_list_path, 'wb')
            pickle.dump(stl_val_list, f)
            f.close()

        else:
            f = open(self.eng_train_list_path, 'rb')
            eng_train_list = pickle.load(f)
            f.close()

            f = open(self.eng_val_list_path, 'rb')
            eng_val_list = pickle.load(f)
            f.close()

            f = open(self.stl_train_list_path, 'rb')
            stl_train_list = pickle.load(f)
            f.close()

            f = open(self.stl_val_list_path, 'rb')
            stl_val_list = pickle.load(f)
            f.close()

        print('train and validation data list split done')
        return eng_train_list, eng_val_list, stl_train_list, stl_val_list

    def get_data_tensor(self):
        train_examples = \
            tf.data.Dataset.from_tensor_slices((self.eng_train_list, self.stl_train_list))
        val_examples = \
            tf.data.Dataset.from_tensor_slices((self.eng_val_list, self.stl_val_list))
        print('tensor transformation done')
        return train_examples, val_examples

    @staticmethod
    def tokenize(train_from_start):
        print('start tokenization')
        eng_tokenizer, stl_tokenizer = tokenizer.process_tokenization(train_from_start)
        print('tokenization done')
        return eng_tokenizer, stl_tokenizer

    def find_max_length(self, train_from_start):
        print('start searching for max length')
        # # option 1: word level
        # if train_from_start or not train_from_start:
        #     max_length_eng = max(len(t) for t in self.eng_train_list)
        #     max_length_stl = max(len(t) for t in self.stl_train_list)
        #     max_length = max(max_length_eng, max_length_stl)

        # option 2: sub-word level
        if train_from_start:
            eng_sample_len_list = []
            stl_sample_len_list = []

            for eng, stl in self.train_examples:
                # print(eng.numpy().decode('UTF-8'))
                # print(type(eng.numpy()))
                # print(type(eng.numpy().decode('UTF-8')))
                # print(type(str(eng.numpy().decode('UTF-8'))))
                eng_tokenized_output = self.eng_tokenizer.encode(eng.numpy().decode('UTF-8'))
                eng_sample_len_list.append(len(eng_tokenized_output.tokens))

                stl_tokenized_output = self.stl_tokenizer.encode(stl.numpy().decode('UTF-8'))
                stl_sample_len_list.append(len(stl_tokenized_output.tokens))

            max_length_eng = max(eng_sample_len_list)
            max_length_stl = max(stl_sample_len_list)
            max_length = max(max_length_eng, max_length_stl)

            if os.path.exists(self.max_length_info_path):
                shutil.rmtree(self.max_length_info_path)

            if not os.path.exists(self.max_length_info_path):
                os.mkdir(self.max_length_info_path)

            f = open(self.max_length_eng_path, 'wb')
            pickle.dump(max_length_eng, f)
            f.close()

            f = open(self.max_length_stl_path, 'wb')
            pickle.dump(max_length_stl, f)
            f.close()

            f = open(self.max_length_path, 'wb')
            pickle.dump(max_length, f)
            f.close()

        else:
            f = open(self.max_length_eng_path, 'rb')
            max_length_eng = pickle.load(f)
            f.close()

            f = open(self.max_length_stl_path, 'rb')
            max_length_stl = pickle.load(f)
            f.close()

            f = open(self.max_length_path, 'rb')
            max_length = pickle.load(f)
            f.close()

        # print(max_length_eng)
        # print(max_length_stl)
        # print(max_length)
        print('max length found')
        return max_length_eng, max_length_stl, max_length

    def tf_encode_to_subword(self, eng_sentence, stl_sentence):
        return tf.py_function(self.encode_to_subword,
                              [eng_sentence, stl_sentence],
                              [tf.int64, tf.int64])

    def encode_to_subword(self, eng_sentence, stl_sentence):
        eng_sequence = [self.eng_tokenizer.get_vocab_size()] + \
                       self.eng_tokenizer.encode(eng_sentence.numpy().decode('UTF-8')).ids + \
                       [self.eng_tokenizer.get_vocab_size() + 1]
        stl_sequence = [self.stl_tokenizer.get_vocab_size()] + \
                        self.stl_tokenizer.encode(stl_sentence.numpy().decode('UTF-8')).ids + \
                       [self.stl_tokenizer.get_vocab_size() + 1]
        return eng_sequence, stl_sequence

    def filter_by_max_length(self, eng, stl):
        # # option 1
        return tf.logical_and(tf.size(eng) <= self.max_length_eng,
                              tf.size(stl) <= self.max_length_stl)


# data = DataPreprocess(True)
# for x, y in data.train_dataset.take(1):
#     print(x.shape)
#     print(y.shape)
# print(data.max_length)
