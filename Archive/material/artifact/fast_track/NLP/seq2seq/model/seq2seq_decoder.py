"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

import torch
from torch import nn
from d2l import torch as d2l


class Seq2SeqDecoder(d2l.Decoder):
    """
    decoder is unidirectional
    decoder's num_hiddens = encoder's num_hiddens * D
    D = 1 for unidirectional encoder
    D = 2 for bidirectional encoder
    """

    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers,
                 dropout=0, **kwargs):
        super(Seq2SeqDecoder, self).__init__(**kwargs)
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.rnn = nn.GRU(embed_size + num_hiddens, num_hiddens, num_layers,
                          dropout=dropout)
        self.dense = nn.Linear(num_hiddens, vocab_size)

    def init_state(self, enc_outputs, *args):
        return enc_outputs[1]  # state

    def forward(self, X, state):
        """
        For training: X represents all the tokens in the whole sequence
        For testing (prediction): X represents the token the decoder outputted in the last step
        """

        # X.shape before embedding: (batch_size, num_steps)
        # X.shape after embedding and permutation: (num_steps, batch_size, embed_size)
        X = self.embedding(X).permute(1, 0, 2)
        # print('X.shape:', X.shape)

        # broadcasting for 'context' through copying the last element of 'state' for 'num_steps' times,
        # so dimension 0 of 'context' equals to 'num_steps', the same as 'X'
        context = state[-1].repeat(X.shape[0], 1, 1)  # context.shape: (num_steps, batch_size, num_hiddens)

        # print('state[-1].shape:', state[-1].shape)
        # print('state[-1]:\n', state[-1])
        # print('context.shape:', context.shape)
        # print('context:\n', context)

        # concatenate 'X' and 'context' in dimension 2, namely the last dimension
        # X_and_context.shape: (num_steps, batch_size, embed_size+num_hiddens)
        X_and_context = torch.cat((X, context), 2)
        # print('X_and_context.shape:', X_and_context.shape)

        # the initial hidden states of each layer of the decoder come from
        # corresponding hidden states of each layer of the encoder in the last time step
        output, state = self.rnn(X_and_context, state)  # output.shape: (num_steps, batch_size, num_hiddens)

        output = self.dense(output).permute(1, 0, 2)
        # print(output)

        # output.shape: (batch_size, num_steps, vocab_size)
        # state.shape: (num_layers, batch_size, num_hiddens)
        return output, state
