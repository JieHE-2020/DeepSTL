import torch
import random
import numpy as np

# IMPORTANT SETTINGS
train_from_start = True
seed = 100
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.enabled = False

from attention.model.attention_encoder import AttentionEncoder
from attention.model.attention_decoder import Seq2SeqAttentionDecoder
from attention.train_validate.attention_train_dev_data_iterator import AttentionTrainDevDataIterator
from attention.train_validate.attention_trainer_validator import AttentionTrainerValidator
from attention import attention_hyperparas
from public import paths
from torch import nn
from d2l import torch as d2l
import pickle

# attention paras
embed_size = attention_hyperparas.embed_size
num_hiddens = attention_hyperparas.num_hiddens
num_layers = attention_hyperparas.num_layers
dropout = attention_hyperparas.dropout_rate

# dataset & tokenizer & vocabulary
f = open(paths.preprocess_info_dict_path, 'rb')
preprocess_info_dict = pickle.load(f)
f.close()
src_vocab = preprocess_info_dict['eng_tokenizer']
tgt_vocab = preprocess_info_dict['stl_tokenizer']
len_src_vocab = src_vocab.get_vocab_size()
len_tgt_vocab = tgt_vocab.get_vocab_size()

# train procedure
max_epochs = attention_hyperparas.max_epochs
device = attention_hyperparas.device

# define model
encoder = AttentionEncoder(len_src_vocab, embed_size, num_hiddens, num_layers, dropout)
decoder = Seq2SeqAttentionDecoder(len_tgt_vocab, embed_size, num_hiddens*2, num_layers, dropout)
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
        torch.save(checkpoint_dict, paths.attention_record_path + str(seed) + '/checkpoint_dict')
        # initialize data iterator and write to file
        data_iterator = AttentionTrainDevDataIterator(seed)
    else:  # update max_epochs if it gets changed
        checkpoint_dict = torch.load(paths.attention_record_path + str(seed) + '/checkpoint_dict')
        checkpoint_dict['max_epochs'] = max_epochs
        torch.save(checkpoint_dict, paths.attention_record_path + str(seed) + '/checkpoint_dict')

    trainer_validator = AttentionTrainerValidator(seed)
