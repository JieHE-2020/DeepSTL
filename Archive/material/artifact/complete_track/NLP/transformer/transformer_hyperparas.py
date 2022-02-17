from d2l import torch as d2l

# model
num_hiddens = 128
ffn_num_hiddens = 512
num_layers = 4
num_heads = 8
dropout_rate = 0.1

# train & validate
max_epochs = 40
batch_size = 64
warmup_steps = 4000
factor = 2
device = d2l.try_gpu(0)

# test
# beam search
topk = 1
enlarge_factor = 1
alpha = 0.75
