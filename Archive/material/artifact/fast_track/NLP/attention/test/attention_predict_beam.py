import torch
from d2l import torch as d2l
from attention import attention_hyperparas
import heapq
import math
import copy


class Candidate:
    def __init__(self, tgt_vocab):

        self.tgt_vocab = tgt_vocab
        self.seq_list = []
        self.prob_list = []
        self.end_flag = 0
        self.seq_len = 0
        self.log_sum = 0
        self.criterion = 0
        self.dec_state = []
        self.last_element_tensor = None

    def dec_state_process(self, dec_state):
        self.dec_state.append(dec_state[0].clone().to(attention_hyperparas.device))
        self.dec_state.append(dec_state[1].clone().to(attention_hyperparas.device))
        self.dec_state.append(dec_state[2].clone().to(attention_hyperparas.device))

    def update(self):
        self.last_element_tensor = torch.tensor([[self.seq_list[-1]]], device=attention_hyperparas.device)
        if self.seq_list[-1] == self.tgt_vocab.encode('<eos>').ids[0]:
            self.end_flag = True
        else:
            self.end_flag = False
        self.seq_len = len(self.seq_list)
        self.log_sum = self.log_sum + math.log(self.prob_list[-1])
        self.criterion = self.log_sum / (self.seq_len ** attention_hyperparas.alpha)


def attention_predict_beam(net, src_sentence, src_vocab, tgt_vocab, num_steps, device, save_attention_weights=False):
    net.eval()
    src_tokens = src_vocab.encode(src_sentence).ids + src_vocab.encode('<eos>').ids
    enc_valid_len = torch.tensor([len(src_tokens)], device=device)
    src_tokens = d2l.truncate_pad(src_tokens, num_steps, src_vocab.encode('<pad>').ids[0])

    # prepare 2 lists
    output_id_list, attention_weight_seq = [], []

    # initialize encoder
    enc_X = torch.unsqueeze(torch.tensor(src_tokens, dtype=torch.long, device=device), dim=0)
    enc_outputs = net.encoder(enc_X, enc_valid_len)
    # initialize decoder
    dec_state = net.decoder.init_state(enc_outputs, enc_valid_len)
    dec_X = torch.unsqueeze(torch.tensor(tgt_vocab.encode('<bos>').ids, dtype=torch.long, device=device),
                            dim=0)

    step = 0
    selected_list = []
    complete_sent_list = []
    softmax = torch.nn.Softmax(dim=2)
    while step < num_steps and len(complete_sent_list) < attention_hyperparas.topk:
        """
        seq2seq+attention:
        During initialization at first step, the source of dec_state ([enc_outputs, hidden_state, enc_valid_lens]) is 
        from the encoder. However, after initialization, the 'enc_outputs' and 'enc_valid_lens' parts in dec_state will
        not change since they are from the encoder. The only changing part at each decoding step is 'hidden state'. 
        """
        # print('step:', step)
        if step == 0:
            temp_candidate_list = []
            Y, dec_state = net.decoder(dec_X, dec_state)
            Y1 = softmax(Y).squeeze(1)
            Y1 = Y1[0].cpu().detach().numpy().tolist()

            topk_value_list = heapq.nlargest(attention_hyperparas.enlarge_factor * attention_hyperparas.topk, Y1)
            topk_index_list = list(map(Y1.index, topk_value_list))
            # print(topk_value_list)
            # print(topk_index_list)

            for i in range(len(topk_index_list)):
                candidate = Candidate(tgt_vocab)
                candidate.prob_list.append(topk_value_list[i])
                candidate.seq_list.append(topk_index_list[i])
                candidate.dec_state_process(dec_state)
                candidate.update()
                temp_candidate_list.append(candidate)
            # now temp_candidate_list has enlarge_factor*topk candidates

        else:  # step >= 1
            temp_candidate_list = []
            for candidate in selected_list:
                Y, dec_state = net.decoder(candidate.last_element_tensor, candidate.dec_state)
                Y1 = softmax(Y).squeeze(1)
                Y1 = Y1[0].cpu().detach().numpy().tolist()
                topk_value_list = \
                    heapq.nlargest(attention_hyperparas.enlarge_factor * attention_hyperparas.topk, Y1)
                topk_index_list = list(map(Y1.index, topk_value_list))
                # print(topk_value_list)
                # print(topk_index_list)

                for i in range(len(topk_index_list)):
                    candidate_successor = Candidate(tgt_vocab)

                    candidate_successor.seq_list = copy.deepcopy(candidate.seq_list)
                    candidate_successor.prob_list = copy.deepcopy(candidate.prob_list)
                    candidate_successor.end_flag = copy.deepcopy(candidate.end_flag)
                    candidate_successor.seq_len = copy.deepcopy(candidate.seq_len)
                    candidate_successor.log_sum = copy.deepcopy(candidate.log_sum)
                    candidate_successor.criterion = copy.deepcopy(candidate.criterion)

                    candidate_successor.prob_list.append(topk_value_list[i])
                    candidate_successor.seq_list.append(topk_index_list[i])
                    candidate_successor.dec_state_process(dec_state)
                    candidate_successor.update()

                    temp_candidate_list.append(candidate_successor)
        # now temp_candidate_list has len(selected_list)*enlarge_factor*topk (topk*enlarge_factor*topk) candidates
        temp_candidate_list.sort(key=lambda obj: obj.criterion, reverse=True)

        selected_list = []
        for j in range(len(temp_candidate_list)):
            candidate = temp_candidate_list.pop(0)
            if candidate.end_flag:
                complete_sent_list.append(candidate)
            else:
                selected_list.append(candidate)
            if len(complete_sent_list) == attention_hyperparas.topk or \
                    len(selected_list) == attention_hyperparas.topk:
                break
        step = step + 1

    if len(complete_sent_list) > 0:
        complete_sent_list.sort(key=lambda obj: obj.criterion, reverse=True)
        winner = complete_sent_list.pop(0)
        output_id_list = winner.seq_list[:-1]
    else:
        selected_list.sort(key=lambda obj: obj.criterion, reverse=True)
        winner = selected_list.pop(0)
        output_id_list = winner.seq_list

    criterion = winner.criterion
    tgt_vocab.decode(output_id_list)
    return output_id_list, tgt_vocab.decode(output_id_list), criterion, attention_weight_seq
