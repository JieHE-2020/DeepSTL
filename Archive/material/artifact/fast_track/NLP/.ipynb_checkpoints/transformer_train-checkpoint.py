import torch
import random
import numpy as np

# IMPORTANT SETTINGS
train_from_start = True
seed = 500
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic = True

from transformer.model.transformer_encoder import TransformerEncoder
from transformer.model.transformer_decoder import TransformerDecoder
from transformer.train_validate.transformer_train_dev_data_iterator import TransformerTrainDevDataIterator
from transformer.train_validate.transformer_trainer_validator import TransformerTrainerValidator
from transformer import transformer_hyperparas
from public import paths
from torch import nn
from d2l import torch as d2l
import pickle

# transformer paras
key_size = query_size = value_size = num_hiddens = transformer_hyperparas.num_hiddens
norm_shape = [num_hiddens]
ffn_num_input, ffn_num_hiddens = transformer_hyperparas.num_hiddens, transformer_hyperparas.ffn_num_hiddens
num_layers, num_heads = transformer_hyperparas.num_layers, transformer_hyperparas.num_heads
dropout = transformer_hyperparas.dropout_rate

# dataset & tokenizer & vocabulary
f = open(paths.preprocess_info_dict_path, 'rb')
preprocess_info_dict = pickle.load(f)
f.close()
src_vocab = preprocess_info_dict['eng_tokenizer']
tgt_vocab = preprocess_info_dict['stl_tokenizer']
len_src_vocab = src_vocab.get_vocab_size()
len_tgt_vocab = tgt_vocab.get_vocab_size()

# train procedure
max_epochs = transformer_hyperparas.max_epochs
device = transformer_hyperparas.device

# define model
encoder = TransformerEncoder(len_src_vocab, key_size, query_size, value_size,
                             num_hiddens, norm_shape, ffn_num_input,
                             ffn_num_hiddens, num_heads, num_layers, dropout)
decoder = TransformerDecoder(len_tgt_vocab, key_size, query_size, value_size,
                             num_hiddens, norm_shape, ffn_num_input,
                             ffn_num_hiddens, num_heads, num_layers, dropout)
net = d2l.EncoderDecoder(encoder, decoder)


# initialization if train from start
def xavier_init_weights(m):
    if type(m) == nn.Linear:
        nn.init.xavier_uniform_(m.weight)
    if type(m) == nn.GRU:
        for param in m._flat_weights_names:
            if "weight" in param:
                nn.init.xavier_uniform_(m._parameters[param])


if __name__ == '__main__':
    if train_from_start:
        # initialize checkpoint dict
        # will add keys 'python_random_state', 'numpy_random_state', 'torch_random_state'
        # after finishing one epoch
        checkpoint_dict = {
            'net_model': net,
            'net_state_dict': {},
            'optimizer_state_dict': {},
            'max_epochs': max_epochs,
            'epochs_finished': 0,
            'step': 1,
            'device': device,
            'train_loss_list': [],
            'train_acc_list': [],
            'validate_loss_list': [],
            'validate_acc_list': []
        }
        # initialize net params
        net.apply(xavier_init_weights)
        checkpoint_dict['net_state_dict'] = net.state_dict()
        # write checkpoint dict to file
        torch.save(checkpoint_dict, paths.transformer_record_path + str(seed) + '/checkpoint_dict')
        # initialize data iterator and write to file
        data_iterator = TransformerTrainDevDataIterator(seed)
    else:  # update max_epochs if it gets changed
        checkpoint_dict = torch.load(paths.transformer_record_path + str(seed) + '/checkpoint_dict')
        checkpoint_dict['max_epochs'] = max_epochs
        torch.save(checkpoint_dict, paths.transformer_record_path + str(seed) + '/checkpoint_dict')

    trainer_validator = TransformerTrainerValidator(seed)
