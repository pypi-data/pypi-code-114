"""Process w4wtr english to chinese."""
from typing import List, Union

# from pathlib import Path
# import msgpack
import nltk
from nltk.corpus import stopwords
from simplemma import lemmatize, load_data

# nltk.download("stopwords")
# do this
# python -m nltk.downloader stopwords
# or

try:
    stopwords_ = set(stopwords.words("english"))
except Exception: # download when use the first time
    nltk.download("stopwords")
    stopwords_ = set(stopwords.words("english"))

langdata = load_data("en")


# fmt: off
def process_en(
        text: Union[str, List[str]],
        remove_en_stopwords: bool = True,
        lemma: bool = True,
        # remove_zh_stopwords: bool = True,
        dedup: bool = True,
) -> List[List[str]]:
    #  fmt: on
    """Process w4wtr english to chinese.

    Args:
        text: english text to process_en
        remove_en_stopwords: remove stopwords
        lemma: lemmatize english ussing simplemma.text_lemmatize
        dedup: remove duplicate chinese chars

    Returns:
        w4w split text

    """
    if isinstance(text, str):
        res = [text]
    else:
        res = text.copy()

    def remove_(elm):
        if isinstance(elm, str):
            elm = elm.split()
        return [word for word in elm if word.lower() not in stopwords_]

    # remove_en_stopwords
    res = [*map(str.split, res)]
    if remove_en_stopwords:
        res = [*map(remove_, res)]

    # simplemma.lemmatize or str.lower
    if lemma:
        res = [[*map(lambda x: lemmatize(x, langdata), line)] for line in res]
    else:
        res = [[*map(str.lower, line)] for line in res]

    # dedup
    if dedup:
        res = [list(set(line)) for line in res]

    return res
