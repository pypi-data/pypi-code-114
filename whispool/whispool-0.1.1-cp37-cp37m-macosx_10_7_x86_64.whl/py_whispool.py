from whispool.whispool import (
    WhispoolMulti,
    WordStats,
    StatsMap,
)

from typing import (
    List, Dict, Any
)
from pathlib import Path
import pandas as pd


def obj_dict(word_stats: WordStats) -> Dict[str, Any]:
    """
    Transform a ```WordStats``` object into a dict
    """
    return dict(
        word=word_stats.word,
        total_occur=word_stats.total_occur,
        match_count=word_stats.match_count,
        ratio=word_stats.ratio,
    )


def parse_results_to_df(statsmap: StatsMap) -> pd.DataFrame:
    """
    Read results into a pandas dataframe
    """

    df = pd.DataFrame(
        list(
            obj_dict(word_stats)
            for _, word_stats in statsmap.stats.items())
    )
    return df.sort_values(by='ratio', ascending=False)


class Whispool:
    """
    Whispool Python Class
    """

    def __init__(self, directory: Path, threads: int, capacity: int = int(1e5)):
        """
        Create a Whispool instance

        directory: Path, the directory to store the data
        threads: int, number of cpu core to use
        capacity: int, num of sentences to save in 1 cache file, default 10,000
        """

        self.directory = str(directory)
        self.threads = threads
        self.capacity = capacity
        self.whispool_multi = WhispoolMulti(
            self.directory, self.threads, self.capacity)

    def consume(self, sentence: List[List[str]], info: List[List[str]]) -> None:
        """
        sentence:List[List[str]], a list of list of string tokens
        info:List[List[str]], a list of id,
            category or label or genre, all in the same length

        sentence = [
            ['This', 'is', 'a', 'sentence'],
            ['This', 'is', 'another', 'sentence'],
            ['This', 'is', 'a', 'third', 'sentence'],
        ]
        info = list([
            ['id1', 'category1', 'label1', 'genre1'],
            ['id2', 'category1', 'label1', 'genre2'],
            ['id3', 'category2', 'label2', 'genre3'],
        ])

        self.consume(sentence, info)
        """

        self.whispool_multi.consume(list(sentence), list(info))

    def final_stats(self, columns: List[str], top_n: int = 5) -> pd.DataFrame:
        """
        columns:List[str], a list of info string you want to get feature on,
            if no filter on a field, just put in None
        top_n:int, mininum total_occur for a word to be included
        """
        statsmap = self.whispool_multi.final_stats(list(columns), top_n)
        return parse_results_to_df(statsmap)
