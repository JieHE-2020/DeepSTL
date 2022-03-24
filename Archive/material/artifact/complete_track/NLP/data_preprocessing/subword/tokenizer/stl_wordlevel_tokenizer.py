from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Punctuation
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits
from public import hyperparameters
from public import paths
import pandas as pd


def stl_wordlevel_tokenization():
    df = pd.read_csv(paths.csv_path)
    stl_data_list = list(df['STL'])

    tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
    trainer = WordLevelTrainer(vocab_size=hyperparameters.stl_wordlevel_vocab_size, special_tokens=["[UNK]"])
    pre_tokenizer = pre_tokenizers.Sequence([
        Whitespace(),
        Punctuation(),
        Digits(individual_digits=True)
    ])
    tokenizer.pre_tokenizer = pre_tokenizer

    tokenizer.train_from_iterator(stl_data_list, trainer)
    tokenizer.save(paths.stl_wordlevel_tokenizer_path, pretty=True)
    tokenizer = Tokenizer.from_file(paths.stl_wordlevel_tokenizer_path)

    return tokenizer
