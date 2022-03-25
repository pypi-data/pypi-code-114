"""
Class for the defining relation of a design.

Created on: 25/03/2022
Author: u0133728
"""

# %% Packages
import re
from collections import Counter, defaultdict
from itertools import chain, combinations
from typing import Dict, List


# %% Declaration
# Anonymous function to verify that a letter is lower case
def is_lower_case(w):
    """
    Return True if a word only contains lower case letters

    Parameters
    ----------
    w : str
        Word

    Returns
    -------
    bool

    """
    return ord(w) > 96 & ord(w) < 123


class DefiningRelation:
    """
    This class holds the information about the defining relation of a design.

    Parameters
    ----------
    word_list : List[str]
        The words of the added factors of the design

    Attributes
    ----------
    added_words : List[str]
        List of the p words of the p added factors of the design

    n_added_factors : int
        Number of added factors

    len_def_relation : int
        Total number of words in the defining relation

    defining_relation : Dict[int, List[str]]
        Full defining relation, created from all possible combinations of the words
        of the added factors of the design.
    """

    def __init__(self, word_list: List[str]):
        # Check integrity of the word list
        if any([not all(map(is_lower_case, w)) for w in word_list]):
            raise ValueError("Words must only contain lower case letters")
        # Metrics of the defining relation
        self.added_words = word_list
        self.n_added_factors = len(self.added_words)
        self.len_def_relation = 2**self.n_added_factors - 1

        # Create the full defining relation
        word_dict = defaultdict(list)
        for word in self.added_words:
            word_dict[len(word)].append(word)
        for i in range(2, self.n_added_factors + 1):
            word_combinations = combinations(self.added_words, i)
            for word_comb in word_combinations:
                c = Counter("".join(word_comb))
                new_word = "".join([k for k, v in c.items() if v % 2 != 0])
                word_dict[len(new_word)].append(new_word)
        self.defining_relation = word_dict

    def basic(self) -> List[str]:
        """
        Only return the basic words of the defining relation, i.e., the words
        corresponding to the added factors.

        Returns
        -------
        List[str]

        """
        return self.added_words

    def to_list(self) -> List[str]:
        """
        Return all the words in the defining relation as a list of strings.

        Returns
        -------
        List[str]

        """
        return list(chain(*self.defining_relation.values()))

    def by_factor(self) -> Dict[str, List[str]]:
        """
        Return the defining relation ordered by factors instead of length.

        Returns
        -------
        Dict[str, List[str]]
        """
        word_list = defaultdict(list)
        for word in chain(*self.defining_relation.values()):
            for factor in word:
                word_list[factor].append(word)
        return word_list

    def confounding(self, order: int = 2, max_len: int = 3):
        """
        Create the confouding pattern of all interactions of order 1 to `order`,
        that have a maximum length of `max_len`.

        Parameters
        ----------
        order : int, optional
            Maximum order of interactions for which the confounding pattern is
            generated. Default is 2.
        max_len : int, optional
            Maximum length of interactions that are included in the confouding
            pattern. If set to None, all interactions are included. Default is 3.

        Returns
        -------

        """
        confounding_dict = defaultdict(list)
        # Words too long should not be accounted for in the confouding pattern
        if max_len is None:
            word_subset = self.to_list()
        else:
            word_subset = list(
                chain(
                    *[
                        v
                        for k, v in self.defining_relation.items()
                        if k <= max_len + order
                    ]
                )
            )
        for i in range(1, order + 1):
            for word in word_subset:
                factor_interactions = combinations(word, i)
                for interaction in factor_interactions:
                    key = "".join(interaction)
                    value = word
                    for factor in interaction:
                        value = re.sub(factor, "", value)
                    confounding_dict[key].append(value)
        return dict(confounding_dict)


if __name__ == "__main__":
    pass
