from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
from public import hyperparameters
from public import paths


def process_BPE_tokenization():
    tokenizer = Tokenizer(BPE(unk_token='<unk>'))
    # real vocab_size might be smaller than hyperparameters.joint_target_vocab_size
    trainer = BpeTrainer(vocab_size=hyperparameters.joint_target_vocab_size,
                         special_tokens=['<unk>', '<pad>', '<bos>', '<eos>'])
    pre_tokenizer = pre_tokenizers.Sequence([
        Whitespace(),
        Punctuation(),
        Digits(individual_digits=True)
    ])
    tokenizer.pre_tokenizer = pre_tokenizer
    tokenizer.train(paths.tokenization_dataset_path, trainer)
    tokenizer.save(paths.joint_bpe_tokenizer_path, pretty=True)
    joint_tokenizer = Tokenizer.from_file(paths.joint_bpe_tokenizer_path)
    # joint_tokenizer = tokenizer
    eng_tokenizer = tokenizer
    stl_tokenizer = tokenizer

    return eng_tokenizer, stl_tokenizer
