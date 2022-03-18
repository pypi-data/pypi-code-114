from __future__ import annotations
from typing import Sequence
import tempfile
from functools import partial

try:
    import jieba_fast as jieba
except ImportError:
    import jieba
import tensorflow as tf
import tensorflow_text as tftext

from sknlp.vocab import Vocab


class Tokenizer:
    def __init__(self, vocab: Vocab) -> None:
        self.vocab = vocab

    def tokenize(self, text: str | Sequence[str]) -> list[list[str]] | list[str]:
        raise NotImplementedError()


class JiebaTokenizer(Tokenizer):
    def __init__(self, vocab: Vocab) -> None:
        super().__init__(vocab)
        with tempfile.NamedTemporaryFile("w+") as f:
            for token in vocab.sorted_tokens:
                f.write(f"{token} {vocab._token_frequency.get(token, 1)}\n")
            f.flush()
            tokenizer = jieba.Tokenizer(dictionary=f.name)
            tokenizer.initialize()
            self.tokenizer = partial(tokenizer.lcut, HMM=False)

    def tokenize(self, text: str | Sequence[str]) -> list[list[str]] | list[str]:
        if isinstance(text, str):
            return self.tokenizer(text)
        return [self.tokenize(t) for t in text]


class CharTokenizer(Tokenizer):
    def tokenize(self, text: str | Sequence[str]) -> list[list[str]] | list[str]:
        if isinstance(text, str):
            return list(text)
        return [self.tokenize(t) for t in text]


class BertTokenizer(Tokenizer):
    def __init__(self, vocab: Vocab) -> None:
        super().__init__(vocab)
        self.tokenizer = tftext.BertTokenizer(
            tf.lookup.StaticVocabularyTable(
                tf.lookup.KeyValueTensorInitializer(
                    self.vocab.sorted_tokens,
                    list(range(len(self.vocab))),
                    key_dtype=tf.string,
                    value_dtype=tf.int64,
                ),
                1,
            ),
            token_out_type=tf.string,
            unknown_token=None,
        )

    def tokenize(
        self, text: str | Sequence[str] | tf.Tensor | Sequence[tf.Tensor]
    ) -> list[str] | list[list[str]] | tf.Tensor:
        is_flat = False
        if isinstance(text, (str, tf.Tensor)):
            is_flat = True
            text = [text]

        text_tensor = tf.stack(text, 0)
        ragged_tokens = self.tokenizer.tokenize(text_tensor).merge_dims(-2, -1)
        is_tensor = isinstance(text[0], tf.Tensor)
        if is_tensor:
            return ragged_tokens.to_tensor(self.vocab.pad)
        tokens_list = ragged_tokens.to_list()
        tokens_list = [
            [token.decode("UTF-8") for token in tokens] for tokens in tokens_list
        ]
        if is_flat:
            return tokens_list[0]
        else:
            return tokens_list


def get_tokenizer(name: str, vocab: Vocab) -> Tokenizer:
    if name == "jieba" or name == "word":
        return JiebaTokenizer(vocab)
    elif name == "list" or name == "char":
        return CharTokenizer(vocab)
    elif name == "bert" or name is None:
        return BertTokenizer(vocab)
    else:
        raise ValueError("unknown segmenter %s" % name)