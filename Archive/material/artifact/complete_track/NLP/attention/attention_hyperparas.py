from d2l import torch as d2l

# model
embed_size = 128
num_hiddens = 128
num_layers = 2
dropout_rate = 0.1

# train & validate
max_epochs = 10
batch_size = 64
warmup_steps = 4000
lr = 0.005
factor = 0.1
device = d2l.try_gpu(0)

# test
# beam search
topk = 1
enlarge_factor = 1
alpha = 0.75
