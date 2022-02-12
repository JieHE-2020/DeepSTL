"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

from transformer.model.add_norm import AddNorm
from transformer.model.ffn import PositionWiseFFN
import torch
from torch import nn
from d2l import torch as d2l
import math


class DecoderBlock(nn.Module):
    """
    The i-th block in the decoder of Transformer
    5 sources of noise from dropout:
    1. self.attention1 (masked multi-head decoder attention)
    2. self.addnorm1
    3. self.attention2 (masked multi-head encoder-decoder attention)
    4. self.addnorm2
    5. self.addnorm3
    """

    def __init__(self, key_size, query_size, value_size, num_hiddens,
                 norm_shape, ffn_num_input, ffn_num_hiddens, num_heads,
                 dropout, i, **kwargs):
        super(DecoderBlock, self).__init__(**kwargs)
        self.i = i
        self.attention1 = d2l.MultiHeadAttention(key_size, query_size,
                                                 value_size, num_hiddens,
                                                 num_heads, dropout)
        self.addnorm1 = AddNorm(norm_shape, dropout)
        self.attention2 = d2l.MultiHeadAttention(key_size, query_size,
                                                 value_size, num_hiddens,
                                                 num_heads, dropout)
        self.addnorm2 = AddNorm(norm_shape, dropout)
        self.ffn = PositionWiseFFN(ffn_num_input, ffn_num_hiddens,
                                   num_hiddens)
        self.addnorm3 = AddNorm(norm_shape, dropout)

    def forward(self, X, state):
        """
        For training: X represents all the tokens in the whole sequence
        For testing (prediction): X represents the token the decoder outputted in the last step
        """

        enc_outputs, enc_valid_lens, Y_valid_len = state[0], state[1], state[3]
        # During training, all the tokens of any output sequence are processed
        # at the same time, so `state[2][self.i]` is `None` as initialized.
        # When decoding any output sequence token by token during prediction,
        # `state[2][self.i]` contains representations of the decoded output
        #  up to the current time step at the `i`-th block
        if state[2][self.i] is None:
            """
            In training and the first step of testing, this branch will be executed.
            For training, state[2][self.i] is None
            This is because everytime when one batch is starting to process, the program will execute:
            Y_hat, _ = net(X, dec_input, X_valid_len, Y_valid_len)
            Then the forward() function of EncoderDecoder class will be executed, which will lead to the automatic
            execution of: dec_state = self.decoder.init_state(enc_outputs, *args)
            This will initialize state[2][self.i] as None
            For testing (prediction), in the first step, state[2][self.i] is also None, because the decoder state is
            manually initialized
            """
            key_values = X
        else:
            """
            In testing (prediction), starting from the second step, this branch will be executed since
            state[2][self.i] has been filled in the first step.
            Also for each step starting from the second testing step, 
            Y, dec_state = net.decoder(dec_X, dec_state) will be executed.
            This will directly execute forward() function of class TransformerDecoder, which does not
            involve initializing dec_state (namely state), but will update it instead, and the only 
            updated part is state[2]. For example, 
            At (k-1)th step, key_values.shape = (1, k-1, num_hiddens)
            At kth step, X.shape = (1, 1, num_hiddens) -> used as query for self.attention1
            After torch.cat((state[2][self.i], X), axis=1),
            key_values.shape = (1, k, num_hiddens) -> used as key and value for self.attention1
            Finally, state[2][self.i] will be replaced by the newly concatenated key_values
            """
            key_values = torch.cat((state[2][self.i], X), axis=1)
        state[2][self.i] = key_values
        if self.training:
            batch_size, num_steps, _ = X.shape
            # Shape of `dec_valid_lens`: (`batch_size`, `num_steps`), where
            # every row is [1, 2, ..., `num_steps`]
            dec_valid_lens = torch.arange(1, num_steps + 1, device=X.device).repeat(batch_size, 1)
            '''
            The following commented codes consider effective length for padded tokens 
            when computing their attention weights.
            Although this consideration is more accurate, since we have already masked padding tokens
            when computing loss in training, it does not matter whether to consider effective length
            for padded tokens in executing self-attention for the decoder. The loss result is the same
            whether we execute the following commented codes
            '''
            # for i in range(batch_size):
            #     effective_length = int(Y_valid_len[i]) + 1  # consider 'bos'
            #     dec_valid_lens[i][effective_length:] = effective_length
        else:
            '''
            For testing, there is no need to set dec_valid_lens because there is only one query, which is
            the decoded output of the last time step, and it should calculate attention weights on all the
            tokens outputted from the decoder up to the current time step
            '''
            dec_valid_lens = None

        # Self-attention
        # for training, X = key_values
        # -> X2.shape: (batch_size, num_steps, num_hiddens)
        # for testing at kth step, X.shape = (1, 1, num_hiddens), key_values = (1, k, num_hiddens)
        # -> X2.shape: (1, 1, num_hiddens)
        X2 = self.attention1(X, key_values, key_values, dec_valid_lens)
        Y = self.addnorm1(X, X2)
        # Encoder-decoder attention
        # for training,
        # Y.shape: (batch_size, num_steps, num_hiddens), enc_outputs.shape: (batch_size, num_steps, num_hiddens)
        # -> Y2.shape: (batch_size, num_steps, num_hiddens)
        # for testing,
        # Y.shape = (1, 1, num_hiddens), enc_outputs.shape: (1, num_steps, num_hiddens)
        # -> Y2.shape: (1, 1, num_hiddens)
        Y2 = self.attention2(Y, enc_outputs, enc_outputs, enc_valid_lens)
        # Z.shape = Y2.shape
        Z = self.addnorm2(Y, Y2)
        return self.addnorm3(Z, self.ffn(Z)), state


class TransformerDecoder(d2l.AttentionDecoder):
    """
    Transformer decoder
    sources of noise from dropout:
    1 + 5*num_layers
    the first one source of noise is from positional encoding
    """
    def __init__(self, vocab_size, key_size, query_size, value_size,
                 num_hiddens, norm_shape, ffn_num_input, ffn_num_hiddens,
                 num_heads, num_layers, dropout, **kwargs):
        super(TransformerDecoder, self).__init__(**kwargs)
        self.num_hiddens = num_hiddens
        self.num_layers = num_layers
        self.embedding = nn.Embedding(vocab_size, num_hiddens)  # use num_hiddens as embed_size
        self.pos_encoding = d2l.PositionalEncoding(num_hiddens, dropout)
        self.blks = nn.Sequential()
        for i in range(num_layers):
            self.blks.add_module(
                "block" + str(i),
                DecoderBlock(key_size, query_size, value_size, num_hiddens,
                             norm_shape, ffn_num_input, ffn_num_hiddens,
                             num_heads, dropout, i))
        self.dense = nn.Linear(num_hiddens, vocab_size)

    def init_state(self, enc_outputs, enc_valid_lens, Y_valid_len=None, *args):
        return [enc_outputs, enc_valid_lens, [None] * self.num_layers, Y_valid_len]

    def forward(self, X, state):
        """
        For training: X represents all the tokens in the whole sequence
        For testing (prediction): X represents the token the decoder outputted in the last step
        """
        X = self.pos_encoding(self.embedding(X) * math.sqrt(self.num_hiddens))
        # the first list stores decoder self-attention wights of each layer
        # the second list stores encoder-decoder attention wights of each layer
        self._attention_weights = [[None] * len(self.blks) for _ in range(2)]
        for i, blk in enumerate(self.blks):
            X, state = blk(X, state)
            # Decoder self-attention weights
            self._attention_weights[0][
                i] = blk.attention1.attention.attention_weights
            # Encoder-decoder attention weights
            self._attention_weights[1][
                i] = blk.attention2.attention.attention_weights
        # transform the last dimension to the size of vocab_size
        return self.dense(X), state

    @property
    def attention_weights(self):
        return self._attention_weights
