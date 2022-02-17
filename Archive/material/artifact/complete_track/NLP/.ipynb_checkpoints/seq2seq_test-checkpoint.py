from seq2seq.model.seq2seq_encoder import Seq2SeqEncoder
from seq2seq.model.seq2seq_decoder import Seq2SeqDecoder
from seq2seq import seq2seq_hyperparas
from seq2seq.test.seq2seq_predict_beam import seq2seq_predict_beam
from seq2seq.test.predict_greedy import predict_greedy
from str_process import stl_template_extractor
from str_process import string_accuracy
from str_process import bleu
from str_process import eng_split
from str_process import stl_compact
from public import paths
import torch
from d2l import torch as d2l
import pickle
import time


# IMPORTANT SETTINGS
# predictor - 'greedy' (greedy search)
#           - 'beam'   (beam search)
predictor = 'beam'
# the folder name where data is stored
seed_list = [100]
# mode - 'inner_test'
#      - 'extrapolate'
#      - 'output_results'
mode_list = ['extrapolate']

# seq2seq paras
embed_size = seq2seq_hyperparas.embed_size
num_hiddens = seq2seq_hyperparas.num_hiddens
num_layers = seq2seq_hyperparas.num_layers
dropout = seq2seq_hyperparas.dropout_rate

# dataset & tokenizer & vocabulary
f = open(paths.preprocess_info_dict_path, 'rb')
preprocess_info_dict = pickle.load(f)
f.close()
src_vocab = preprocess_info_dict['eng_tokenizer']
tgt_vocab = preprocess_info_dict['stl_tokenizer']
len_src_vocab = src_vocab.get_vocab_size()
len_tgt_vocab = tgt_vocab.get_vocab_size()
num_steps = preprocess_info_dict['max_length']

# device
device = seq2seq_hyperparas.device

# define model
encoder = Seq2SeqEncoder(len_src_vocab, embed_size, num_hiddens, num_layers, dropout)
decoder = Seq2SeqDecoder(len_tgt_vocab, embed_size, num_hiddens*2, num_layers, dropout)
net = d2l.EncoderDecoder(encoder, decoder)


def multi_acc_compute(net, preprocess_info_dict, src_vocab, tgt_vocab, num_steps, device, seed):
    test_eng_list = preprocess_info_dict['test_eng_list']
    test_stl_list = preprocess_info_dict['test_stl_list']
    print('number of test cases:', len(test_eng_list))
    print()
    metric = d2l.Accumulator(4)
    for i in range(len(test_eng_list)):
        src_sentence = test_eng_list[i]
        reference = test_stl_list[i]
        reference_id_list = tgt_vocab.encode(reference).ids
        if predictor == 'greedy':
            pred_id_list, pred, attention_weight = \
                predict_greedy(net, src_sentence, src_vocab, tgt_vocab, num_steps, device)
        else:
            pred_id_list, pred, criterion, attention_weight = \
                seq2seq_predict_beam(net, src_sentence, src_vocab, tgt_vocab, num_steps, device)
        # metric 1: string accuracy
        str_acc = string_accuracy.str_acc_compute(reference_id_list, pred_id_list, tgt_vocab)

        # metric 2: template accuracy
        refer_template = stl_template_extractor.template_extract([test_stl_list[i]])
        refer_template_id_list = tgt_vocab.encode(refer_template).ids
        pred_template = stl_template_extractor.template_extract([pred])
        pred_template_id_list = tgt_vocab.encode(pred_template).ids
        template_acc = string_accuracy.str_acc_compute(refer_template_id_list, pred_template_id_list, tgt_vocab)

        # metric 3: bleu
        n_gram = 4
        bleu_score = bleu.bleu_compute(reference, pred, tgt_vocab, n_gram)

        metric.add(str_acc, template_acc, bleu_score, 1)
        if (i + 1) % 100 == 0:
            print('Test Case ' + str(i + 1) + ':')
            print('Reference:')
            print(reference)
            print('Reference template:')
            print(refer_template)
            print('Prediction:')
            print(pred)
            print(stl_compact.delete_stl_id_num_space(pred))
            print('Prediction template:')
            print(pred_template)
            print('Average accuracies of first ' + str(i + 1) + ' test cases:')
            print('avg string acc:', metric[0] / metric[3])
            print('avg template acc:', metric[1] / metric[3])
            print('avg bleu score:', metric[2] / metric[3])
            print()

    acc_dict = {
        'avg_string_acc': metric[0] / metric[3],
        'avg_template_acc': metric[1] / metric[3],
        'avg_bleu_score': metric[2] / metric[3],
    }

    info_dict = torch.load(paths.seq2seq_record_path + str(seed) + '/info_dict')
    info_dict['inner_test_acc'] = acc_dict
    torch.save(info_dict, paths.seq2seq_record_path + str(seed) + '/info_dict')

    return metric


def output_test_cases(net, src_vocab, tgt_vocab, num_steps, device):
    txt = open(paths.test_cases_path)
    lines_read = txt.readlines()
    case_index = 1
    for line in lines_read:
        specification = line.replace('\n', '')
        print('Test Case ' + str(case_index) + ':')
        print(specification)
        src_sentence = eng_split.split_identifier(specification)
        if predictor == 'greedy':
            pred_id_list, pred, attention_weight = \
                predict_greedy(net, src_sentence, src_vocab, tgt_vocab, num_steps, device)
        else:
            pred_id_list, pred, criterion, attention_weight = \
                seq2seq_predict_beam(net, src_sentence, src_vocab, tgt_vocab, num_steps, device)
        result = stl_compact.delete_stl_id_num_space(pred)
        print(result)
        if predictor == 'beam':
            print('Criterion:', criterion)
        case_index = case_index + 1
        print()


def extrapolate_acc_compute(net, preprocess_info_dict, src_vocab, tgt_vocab, num_steps, device, seed):
    test_eng_list = preprocess_info_dict['test_eng_list']
    test_stl_list = preprocess_info_dict['test_stl_list']
    print('number of test cases:', len(test_eng_list))
    print()
    metric = d2l.Accumulator(4)
    for i in range(len(test_eng_list)):
        src_sentence = test_eng_list[i]
        src_sentence_split = eng_split.split_identifier(src_sentence)
        reference = test_stl_list[i]
        reference_id_list = tgt_vocab.encode(reference).ids
        if predictor == 'greedy':
            pred_id_list, pred, attention_weight = \
                predict_greedy(net, src_sentence_split, src_vocab, tgt_vocab, num_steps, device)
        else:
            pred_id_list, pred, criterion, attention_weight = \
                seq2seq_predict_beam(net, src_sentence_split, src_vocab, tgt_vocab, num_steps, device)
        # metric 1: string accuracy
        str_acc = string_accuracy.str_acc_compute(reference_id_list, pred_id_list, tgt_vocab)

        # metric 2: template accuracy
        refer_template = stl_template_extractor.template_extract([test_stl_list[i]])
        refer_template_id_list = tgt_vocab.encode(refer_template).ids
        pred_template = stl_template_extractor.template_extract([pred])
        pred_template_id_list = tgt_vocab.encode(pred_template).ids
        template_acc = string_accuracy.str_acc_compute(refer_template_id_list, pred_template_id_list, tgt_vocab)

        # metric 3: bleu
        n_gram = 4
        bleu_score = bleu.bleu_compute(reference, pred, tgt_vocab, n_gram)

        metric.add(str_acc, template_acc, bleu_score, 1)

        print('Test Case ' + str(i + 1) + ':')
        print('English Requirement:')
        print(src_sentence)
        print('Reference:')
        print(reference)
        print('Reference template:')
        print(refer_template)
        print('Prediction:')
        print(pred)
        print(stl_compact.delete_stl_id_num_space(pred))
        print('Prediction template:')
        print(pred_template)
        if predictor == 'beam':
            print('Criterion:', criterion)
        print()

    acc_dict = {
        'avg_string_acc': metric[0] / metric[3],
        'avg_template_acc': metric[1] / metric[3],
        'avg_bleu_score': metric[2] / metric[3],
    }

    info_dict = torch.load(paths.seq2seq_record_path + str(seed) + '/info_dict')
    info_dict['extrapolate_test_acc'] = acc_dict
    torch.save(info_dict, paths.seq2seq_record_path + str(seed) + '/info_dict')

    return metric


if __name__ == '__main__':
    for seed in seed_list:
        print('seed:', seed)
        # gpu is used
        if device != torch.device('cpu'):
            net.load_state_dict(torch.load(paths.seq2seq_record_path + str(seed) + '/net_state_dict'))
            net.to(device)
        else:  # cpu is used
            net.load_state_dict(torch.load(paths.seq2seq_record_path + str(seed) + '/net_state_dict',
                                           map_location=torch.device('cpu')))

        for mode in mode_list:
            if mode == 'inner_test':
                tic = time.time()
                metric = multi_acc_compute(net, preprocess_info_dict, src_vocab, tgt_vocab, num_steps, device, seed)
                print('avg string acc:', metric[0] / metric[3])
                print('avg template acc:', metric[1] / metric[3])
                print('avg bleu score:', metric[2] / metric[3])
                toc = time.time()
                print('Time:' + str((toc - tic)) + 's')
                print()
            elif mode == 'output_results':
                output_test_cases(net, src_vocab, tgt_vocab, num_steps, device)
                print()
            else:
                # this is for give quantitative metrics for extrapolation
                eng_list = []
                stl_list = []
                txt_eng = open(paths.test_case_eng_path)
                lines_read = txt_eng.readlines()
                for line in lines_read:
                    specification = line.replace('\n', '')
                    eng_list.append(specification)
                txt_eng.close()

                txt_stl = open(paths.test_case_stl_path)
                lines_read = txt_stl.readlines()
                for line in lines_read:
                    formula = line.replace('\n', '')
                    stl_list.append(formula)
                txt_stl.close()

                test_dict = {
                    'test_eng_list': eng_list,
                    'test_stl_list': stl_list
                }

                metric = extrapolate_acc_compute(net, test_dict, src_vocab, tgt_vocab, num_steps, device, seed)
                print('avg string acc:', metric[0] / metric[3])
                print('avg template acc:', metric[1] / metric[3])
                print('avg bleu score:', metric[2] / metric[3])
                print()
