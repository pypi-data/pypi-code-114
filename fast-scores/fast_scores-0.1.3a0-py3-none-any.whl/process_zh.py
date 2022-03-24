"""Normalize chinese text and insert spaces beteen chars."""
from typing import List, Union

import re

# from logzero import logger

# from fast_scores.insert_spaces import insert_spaces
# from fast_scores.split_chinese import split_chinese


# fmt: off
def process_zh(
        text: Union[str, List[str]],
        remove_nonchinese: bool = False,
        dedup: bool = False,
        # remove_stopwords: bool = False,  ?na
) -> List[str]:
    # fmt: on
    """Normalize chinese text and insert spaces beteen chars.

    Args
        text: chinese to process
        remove_nonchinese: remove or not
        dedup: deduplicate or not

    Returns
        processed text
    """
    if isinstance(text, str):
        text = [text]

    res = text.copy()

    if remove_nonchinese:
        patt = re.compile(r"[^一-龟]")
        res = map(lambda x: re.sub(patt, "", x), res)

    # insert spaces and split
    # res = [insert_spaces(elm) for elm in res]
    # res = [split_chinese(elm) for elm in res]

    if dedup:
        # res = [list(set(elm)) for elm in res]
        res = ["".join(set(elm)) for elm in res]
    else:
        res = [*res]

    return res
