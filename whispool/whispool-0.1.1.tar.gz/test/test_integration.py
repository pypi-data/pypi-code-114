from whispool import Whispool
import os
import numpy as np
import json
from pathlib import Path

with open("test/vocab.json", "r") as f:
    all_words = json.loads(f.read())


def gen_words():
    """
    Generate a list of words randomly
    """

    return list(np.random.choice(all_words, 10))


def gen_info():
    """
    Generate a list of id/ genre/ category/ label
    """

    return list(str(np.random.randint(1, 100)) for _ in range(3))


def gen_data(n):
    """
    Generate test data in n rows
    """

    words, info = [], []
    for i in range(n):
        words.append(gen_words())
        info.append(gen_info())
    return words, info


sentence, info = gen_data(300)


def test_whispool_pipeline():
    os.system(f"rm -rf test_data")
    whisper_multi = Whispool(
        directory=Path("test_data"), threads=2, capacity=200)
    print(f"🛢 input batch 1")
    whisper_multi.consume(sentence, info)
    print(f"🛢 input batch 2")
    whisper_multi.consume(sentence, info)
    print(f"🛢 input batch 3")
    whisper_multi.consume(sentence, info)
    print(f"🛠 start collecting")
    df = whisper_multi.final_stats(["1", None, None], 1)
    columns = list(df.columns)
    assert len(df) > 0
    assert "word" in columns
    assert "ratio" in columns
    assert "match_count" in columns
    assert (df["total_occur"] < 1).sum() == 0
    os.system(f"rm -rf test_data")
