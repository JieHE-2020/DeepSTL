from public import paths
import pickle
import torch


def str_acc_compute(reference_id_list, pred_id_list, tgt_vocab):
    if len(pred_id_list) < len(reference_id_list):
        pred_id_list = pad(pred_id_list, len(reference_id_list), tgt_vocab.encode('<pad>').ids)
        total_num = len(reference_id_list)
    elif len(pred_id_list) > len(reference_id_list):
        reference_id_list = pad(reference_id_list, len(pred_id_list), tgt_vocab.encode('<pad>').ids)
        total_num = len(pred_id_list)
    else:
        total_num = len(reference_id_list)
    # print(reference_id_list)
    # print(pred_id_list)
    pred_id_tensor = torch.tensor(pred_id_list)
    reference_id_tensor = torch.tensor(reference_id_list)
    correct_num = correct_num_compute(pred_id_tensor, reference_id_tensor)
    acc = correct_num / total_num

    return acc


def pad(padded_id_list, longer_len, pad_token):
    """Truncate or pad sequences."""
    # pad_token is a list
    return padded_id_list + pad_token * (longer_len - len(padded_id_list))  # Pad


def correct_num_compute(y_hat, y):
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


# f = open(paths.preprocess_info_dict_path, 'rb')
# preprocess_info_dict = pickle.load(f)
# f.close()
# tgt_vocab = preprocess_info_dict['stl_tokenizer']
#
#
# reference_id_list = [0, 2, 4, 5, 7]
# pred_id_list = [1, 1, 4]
#
# acc = str_acc_compute(pred_id_list, reference_id_list, tgt_vocab)
# print(acc)
