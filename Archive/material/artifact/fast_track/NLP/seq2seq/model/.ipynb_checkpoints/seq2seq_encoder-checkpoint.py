"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

from torch import nn
from d2l import torch as d2l


class Seq2SeqEncoder(d2l.Encoder):
    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers,
                 dropout=0, **kwargs):
        super(Seq2SeqEncoder, self).__init__(**kwargs)
        self.num_layers = num_layers
        # embedding layer
        self.embedding = nn.Embedding(vocab_size, embed_size)
        # use bidirectional RNN
        self.rnn = nn.GRU(embed_size, num_hiddens, num_layers, bidirectional=True,
                          dropout=dropout)

    def concatenate_hiddens(self, state):
        # initial -> state.shape: (num_layers*2, batch_size, num_hiddens)
        # state.shape: (num_layers, 2, batch_size, num_hiddens)
        state = state.reshape(self.num_layers, 2, state.shape[1], state.shape[2])
        # state.shape: (num_layers, batch_size, 2, num_hiddens)
        state = state.permute(0, 2, 1, 3)
        # state.shape: (num_layers, batch_size, num_hiddens*2)
        state = state.reshape(state.shape[0], state.shape[1], -1)

        return state

    def forward(self, X, *args):
        # X.shape before embedding: (batch_size, num_steps)
        X = self.embedding(X)  # X.shape after embedding: (batch_size, num_steps, embed_size)
        # print(X)
        # by default in pytorch dimension 0 of the input to RNN corresponds to num_steps
        X = X.permute(1, 0, 2)  # (num_steps, batch_size, embed_size)
        # print(X)

        # output.shape: (num_steps, batch_size, num_hiddens*2)
        # state.shape: (num_layers*2, batch_size, num_hiddens)
        output, state = self.rnn(X)
        # print(output)
        # print(state)

        # change state shape
        state = self.concatenate_hiddens(state)

        # output.shape: (num_steps, batch_size, num_hiddens*2)
        # state.shape: (num_layers, batch_size, num_hiddens*2)
        return output, state
