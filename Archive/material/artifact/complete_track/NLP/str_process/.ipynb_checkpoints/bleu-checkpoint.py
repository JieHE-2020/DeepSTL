"""
The codes in this file refer to the following online tutorial of deep learning:
https://d2l.ai/
We added some comments or made several modifications to fit the needs of the paper.
"""

import math
import collections


def bleu_compute(label_seq, pred_seq, tokenizer, k):
    label_tokens, pred_tokens = tokenizer.encode(label_seq).tokens, tokenizer.encode(pred_seq).tokens
    # print('pred_tokens:', pred_tokens)
    # print('label_tokens:', label_tokens)
    len_pred, len_label = len(pred_tokens), len(label_tokens)
    # print('len_pred:', len_pred)
    # print('len_label:', len_label)
    score = math.exp(min(0, 1-len_label/len_pred))
    # print('penalty score:', score)
    # print()

    for n in range(1, k + 1):  # process from 1-gram to k-gram
        # process n gram
        num_matches, label_subs = 0, collections.defaultdict(int)
        # print(num_matches, label_subs)
        for i in range(len_label - n + 1):
            # get n-gram of lebelled sentence
            # number of n-grams = len_label - n + 1 (i=0,1,...,len_label - n)
            # print(''.join(label_tokens[i:i + n]))
            label_subs[''.join(label_tokens[i:i + n])] += 1
        # print(label_subs)

        for i in range(len_pred - n + 1):
            # match n-gram in pred against n-gram in label
            # number of n-grams = len_pred - n + 1 (i=0,1,...,len_pred - n)
            if label_subs[''.join(pred_tokens[i:i + n])] > 0:
                num_matches += 1
                # the maximum matched number for a specific n-gram in pred is
                # the occurrence times of such n-garm in label
                label_subs[''.join(pred_tokens[i:i + n])] -= 1
        score *= math.pow(num_matches / (len_pred - n + 1), math.pow(0.5, n))
    return score