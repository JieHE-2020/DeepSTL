import os
# root path
root_path = os.path.abspath(os.path.dirname(__file__)).split('NLP')[0] + 'NLP'
# data preprocessing
csv_path = root_path + '/data_preprocessing/subword/dataset/corpus_split.csv'
tokenization_dataset_path = [root_path + '/data_preprocessing/subword/dataset/tokenization_dataset.txt']
joint_bpe_tokenizer_path = root_path + '/data_preprocessing/subword/joint_bpe_tokenizer.json'
stl_wordlevel_tokenizer_path = root_path + '/data_preprocessing/subword/stl_wordlevel_tokenizer.json'
eng_wordlevel_tokenizer_path = root_path + '/data_preprocessing/subword/eng_wordlevel_tokenizer.json'
preprocess_info_dict_path = root_path + '/data_preprocessing/subword/preprocess_info_dict'

# transformer
transformer_record_path = root_path + '/transformer/record/'
# attention
attention_record_path = root_path + '/attention/record/'
# seq2seq
seq2seq_record_path = root_path + '/seq2seq/record/'

test_cases_path = root_path + '/test_cases/test_cases.txt'
test_case_eng_path = root_path + '/test_cases/test_case_eng.txt'
test_case_stl_path = root_path + '/test_cases/test_case_stl.txt'