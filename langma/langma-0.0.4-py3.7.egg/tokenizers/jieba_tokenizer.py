# *_*coding:utf-8 *_*
from typing import List, Any

from langma.tokenizers.base_tokenizer import Tokenizer


class JiebaTokenizer(Tokenizer):
    """
    Jieba tokenizer
    """
    def __init__(self) -> None:
        try:
            import jieba
            self._jieba = jieba
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Jieba module not found, please install use `pip install jieba`"
            )

    def tokenize(self, text: str, **kwargs: Any) -> List[str]:
        """
        Tokenize text into token sequence
        Args:
            text: target text sample

        Returns:
            List of tokens in this sample
        """

        return list(self._jieba.cut(text, **kwargs))
