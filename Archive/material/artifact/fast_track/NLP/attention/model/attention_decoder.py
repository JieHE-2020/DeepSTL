"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

import torch
from torch import nn
from d2l import torch as d2l


class AttentionDecoder(d2l.Decoder):
    """The base attention-based decoder interface."""

    def __init__(self, **kwargs):
        super(AttentionDecoder, self).__init__(**kwargs)

    @property
    def attention_weights(self):
        raise NotImplementedError


class Seq2SeqAttentionDecoder(AttentionDecoder):
    """
    decoder is unidirectional
    decoder's num_hiddens = encoder's num_hiddens * D
    D = 1 for unidirectional encoder
    D = 2 for bidirectional encoder
    """

    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers,
                 dropout=0, **kwargs):
        super(Seq2SeqAttentionDecoder, self).__init__(**kwargs)
        self.attention = d2l.AdditiveAttention(num_hiddens, num_hiddens, num_hiddens, dropout)
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.rnn = nn.GRU(embed_size + num_hiddens, num_hiddens, num_layers, dropout=dropout)
        self.dense = nn.Linear(num_hiddens, vocab_size)

    def init_state(self, enc_outputs, enc_valid_lens, *args):
        # shape of outputs: (num_steps, batch_size, num_hiddens)
        outputs, hidden_state = enc_outputs
        # reshape 'outputs' as outputs.permute(1, 0, 2): (batch_size, num_steps, num_hiddens),
        # then use reshaped 'outputs' as keys and values
        # hidden_state.shape: (num_layers, batch_size, num_hiddens)
        # enc_valid_lens.shape: (batch_size,)
        return (outputs.permute(1, 0, 2), hidden_state, enc_valid_lens)

    def forward(self, X, state):
        """
        For training: X represents all the tokens in the whole sequence
        For testing (prediction): X represents the token the decoder outputted in the last step
        """

        # enc_outputs.shape: (batch_size, num_steps, num_hiddens) -> keys and values
        # hidden_state.shape: (num_layers, batch_size, num_hiddens)
        # enc_valid_lens.shape: (batch_size,)
        enc_outputs, hidden_state, enc_valid_lens = state  # step 0
        # X.shape before embedding: (batch_size, num_steps)
        X = self.embedding(X).permute(1, 0, 2)  # step 0
        # X.shape after embedding and permutation: (num_steps, batch_size, embed_size)

        outputs, self._attention_weights = [], []
        for x in X:
            # query.shape: (batch_size, 1, num_hiddens)
            query = torch.unsqueeze(hidden_state[-1], dim=1)  # step 1
            # context.shape: (batch_size, 1, num_hiddens)
            context = self.attention(query, enc_outputs, enc_outputs, enc_valid_lens)  # step 2

            # Concatenate 'context' and 'x' on the feature dimension (dimension 2)
            # context.shape: (batch_size, 1, num_hiddens)
            # x.shape: (batch_size, embed_size)
            # (torch.unsqueeze(x, dim=1)).shape: (batch_size, 1, embed_size)
            # print('context.shape:', context.shape)
            # print('x.shape:', x.shape)
            # print('torch.unsqueeze(x, dim=1).shape:', torch.unsqueeze(x, dim=1).shape)
            x = torch.cat((context, torch.unsqueeze(x, dim=1)), dim=-1)  # step 3
            # x.shape (after concat): (batch_size, 1, num_hiddens+embed_size)

            # print('x.shape (after concat):', x.shape)
            # print()

            # reshape x as (1, batch_size, num_hiddens+embed_size)
            x = x.permute(1, 0, 2)  # step 4
            # out.shape: (1, batch_size, num_hiddens)
            # hidden_state.shape: (num_layers, batch_size, num_hiddens) -> used as new queries in the next iteration
            out, hidden_state = self.rnn(x, hidden_state)  # step 5
            outputs.append(out)
            self._attention_weights.append(self.attention.attention_weights)

        # torch.cat(outputs, dim=0).shape: (num_steps, batch_size, num_hiddens)
        # print('torch.cat(outputs, dim=0).shape:', torch.cat(outputs, dim=0).shape)
        # after fully-connected layer transformation, shape of outputs: (num_steps, batch_size, vocab_size)
        outputs = self.dense(torch.cat(outputs, dim=0))

        # shape of outputs after permutation: (batch_size, num_steps, vocab_size)
        # hidden_state is the hidden state of the decoder at the last time step
        return outputs.permute(1, 0, 2), [enc_outputs, hidden_state, enc_valid_lens]

    @property
    def attention_weights(self):
        return self._attention_weights
