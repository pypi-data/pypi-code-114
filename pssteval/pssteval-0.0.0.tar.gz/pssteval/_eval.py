import csv
import dataclasses
import json
import multiprocessing
import sys
from dataclasses import dataclass
from functools import lru_cache
from typing import Tuple, Iterable, TypeVar, Type

import phonologic
import psstdata
from phonologic import PhonologicalFeatureSystem, ErrorAnalysisDict
from psstdata import PSSTData, PSSTUtteranceCollection
from tqdm import tqdm

from pssteval import logger
from pssteval._metrics import ErrorSummary

psstdata.load = lru_cache(psstdata.load)  # Cuts down on repeat logging

TRow = TypeVar("TRow")


@dataclass(frozen=True)
class AsrOutputRow:
    utterance_id: str
    asr_transcript: str


@dataclass(frozen=True)
class CorrectnessOutputRow:
    utterance_id: str
    prediction: bool


def load_asr_output(filename) -> Tuple[AsrOutputRow, ...]:
    return tuple(read_tsv(filename, AsrOutputRow))


def load_correctness_output(filename) -> Tuple[CorrectnessOutputRow, ...]:
    return tuple(
        dataclasses.replace(row, prediction=json.loads(row.prediction.lower()))  # Cast string to boolean
        for row in read_tsv(filename, CorrectnessOutputRow)
    )


def read_tsv(tsv_file: str, t: Type) -> Iterable:
    field_names = set(f.name for f in dataclasses.fields(t))
    with open(tsv_file) as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        columns = next(reader)
        rows = (
            dict((key, value) for key, value in zip(columns, row) if key in field_names)
            for row in reader
        )
        return [t(**row) for row in rows ]


def detect_split(utterance_ids: Iterable[str], data: PSSTData):
    utterance_ids = set(utterance_ids)
    for split in ("train", "valid", "test"):
        split_data = getattr(data, split)
        if utterance_ids == set(split_data.utterance_ids()):
            logger.info(f"Evaluating against `{split}` data.")
            return split, split_data
    split_data = PSSTUtteranceCollection((*data.train, *data.valid, *data.test))
    if utterance_ids & set(split_data.utterance_ids()) == utterance_ids:
        logger.warning(f"Utterance IDs don't match any of train/test/valid splits.")
        return "unknown", split_data
    else:
        raise KeyError(f"Unknown utterance ids: {utterance_ids - set(split_data.utterance_ids())}")


def evaluate_asr(filename, n_jobs=None, log_level="INFO") -> ErrorAnalysisDict:
    logger.setLevel(log_level)
    n_jobs = n_jobs or multiprocessing.cpu_count() - 1
    data = psstdata.load()
    asr_output = {
        row.utterance_id: row
        for row in load_asr_output(filename)
    }
    split, split_data = detect_split(set(asr_output.keys()), data)

    decoded_triples = [
        (utterance_id, asr_output[utterance_id].asr_transcript, split_data[utterance_id].transcript)
        for utterance_id in asr_output
    ]

    system = phonologic.load("hayes-arpabet")
    analyzer = ParallelAnalyzer(system)
    analysis = analyzer.analyze_parallel(decoded_triples, n_jobs)
    logger.info(f"ASR metrics for split `{split}`    FER: {100*analysis.fer:.1f}%    PER: {100*analysis.per:.1f}%")
    return analysis


def evaluate_correctness(filename, log_level="INFO") -> ErrorAnalysisDict:
    logger.setLevel(log_level)
    data = psstdata.load()
    correctness_output = {
        row.utterance_id: row
        for row in load_correctness_output(filename)
    }
    split, split_data = detect_split(set(correctness_output.keys()), data)

    utterance_ids, y_true, y_pred = zip(*(
        (utterance_id, row.prediction, split_data[utterance_id].correctness)
        for utterance_id, row in correctness_output.items()
    ))

    summary = ErrorSummary.build(y_true, y_pred)

    print(summary)


class ParallelAnalyzer:
    def __init__(self, system: PhonologicalFeatureSystem):
        self.system = system

    def __call__(self, args):
        utterance_id, actual, expected = args
        analysis_phon = self.system.analyze_phoneme_errors(expected, actual)
        analysis_feat = self.system.analyze_feature_errors(expected, actual)
        return utterance_id, {
            "features": analysis_feat,
            "phonemes": analysis_phon,
        }

    def analyze_parallel(self, data, n_jobs) -> ErrorAnalysisDict:
        if n_jobs == 1:
            jobs = (self(job) for job in data)
        else:
            jobs = multiprocessing.Pool(n_jobs).imap_unordered(self, data)
        results = dict(sorted(tqdm(jobs, total=len(data), file=sys.stderr)))
        total_feature_length = sum(a["features"].expected_length for a in results.values())
        fer = sum(a["features"].distance for a in results.values()) / total_feature_length
        total_phoneme_length = sum(a["phonemes"].expected_length for a in results.values())
        per = sum(a["phonemes"].distance for a in results.values()) / total_phoneme_length
        return ErrorAnalysisDict(fer=fer, per=per, items=results)
