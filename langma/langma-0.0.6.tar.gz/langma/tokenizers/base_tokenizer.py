# *_*coding:utf-8 *_*
from typing import List


class Tokenizer:
    """
    Abstract base class for all implemented tokenizer.
    """
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into token sequence
        Args:
            text: target text sample

        Returns:
            List of tokens in this sample
        """
        return text.split(' ')
