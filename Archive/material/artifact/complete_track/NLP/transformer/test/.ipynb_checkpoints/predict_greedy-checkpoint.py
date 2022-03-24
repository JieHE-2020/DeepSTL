"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

import torch
from d2l import torch as d2l


def predict_greedy(net, src_sentence, src_vocab, tgt_vocab, num_steps, device, save_attention_weights=False):
    net.eval()
    src_tokens = src_vocab.encode(src_sentence).ids + src_vocab.encode('<eos>').ids
    # print(src_tokens)
    enc_valid_len = torch.tensor([len(src_tokens)], device=device)
    # print(enc_valid_len)
    src_tokens = d2l.truncate_pad(src_tokens, num_steps, src_vocab.encode('<pad>').ids[0])
    # print(src_tokens)
    # print(len(src_tokens))

    # prepare 2 lists
    output_id_list, attention_weight_seq = [], []

    # initialize encoder
    enc_X = torch.unsqueeze(torch.tensor(src_tokens, dtype=torch.long, device=device), dim=0)
    # print(enc_X)
    enc_outputs = net.encoder(enc_X, enc_valid_len)
    # initialize decoder
    dec_state = net.decoder.init_state(enc_outputs, enc_valid_len)
    dec_X = torch.unsqueeze(torch.tensor(tgt_vocab.encode('<bos>').ids, dtype=torch.long, device=device), dim=0)
    # print(dec_X)

    for _ in range(num_steps):
        """
        -- seq2seq:
        During initialization at first step, the source of 'context' is from encoder's hidden state at last time step, 
        but at the second step and afterwards, the source of 'context' is no longer from the encoder, instead it comes
        from the decoder's hidden state in the previous step.
        -- seq2seq+attention:
        During initialization at first step, the source of dec_state ([enc_outputs, hidden_state, enc_valid_lens]) is 
        from the encoder. However, after initialization, the 'enc_outputs' and 'enc_valid_lens' parts in dec_state will
        not change since they are from the encoder. The only changing part at each decoding step is 'hidden state'. 
        -- transformer:
        After initialization, enc_outputs, enc_valid_lens, and Y_valid_lens from
        dec_state (state = [enc_outputs, enc_valid_lens, [None] * self.num_layers, Y_valid_len])
        is fixed. Each decoding step only updates state[2].
        """
        Y, dec_state = net.decoder(dec_X, dec_state)
        # print(Y.shape)
        # print(Y)

        # We use the token with the highest prediction likelihood as the input
        # of the decoder at the next time step
        dec_X = Y.argmax(dim=2)
        # print(dec_X)
        pred = dec_X.squeeze(dim=0).type(torch.int32).item()  # int
        # print(pred)

         # Save attention weights
        if save_attention_weights:
            attention_weight_seq.append(net.decoder.attention_weights)

        # Once the end-of-sequence token is predicted, the generation of the
        # output sequence is complete
        if pred == tgt_vocab.encode('<eos>').ids[0]:
            break
        output_id_list.append(pred)
    # print(output_id_list)

    tgt_vocab.decode(output_id_list)
    return output_id_list, tgt_vocab.decode(output_id_list), attention_weight_seq