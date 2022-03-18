# coding: utf-8
"""
A ROUGE metric implementation, supporting both English and Chinese.

@ref: https://github.com/pltrdy/rouge
      https://github.com/google-research/google-research/rouge
      https://aclanthology.org/W04-1013.pdf
"""
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import itertools
import six
import io
import os
import re
import collections

import six
from six.moves import map
from six.moves import range

from copy import deepcopy

import nltk
from nltk.stem import porter


class Ngrams(object):
    """
        Ngrams datastructure based on `set` or `list`
        depending in `exclusive`
    """

    def __init__(self, ngrams={}, exclusive=True):
        if exclusive:
            self._ngrams = set(ngrams)
        else:
            self._ngrams = list(ngrams)
        self.exclusive = exclusive

    def add(self, o):
        if self.exclusive:
            self._ngrams.add(o)
        else:
            self._ngrams.append(o)

    def __len__(self):
        return len(self._ngrams)

    def intersection(self, o):
        if self.exclusive:
            inter_set = self._ngrams.intersection(o._ngrams)
            return Ngrams(inter_set, exclusive=True)
        else:
            other_list = deepcopy(o._ngrams)
            inter_list = []

            for e in self._ngrams:
                try:
                    i = other_list.index(e)
                except ValueError:
                    continue
                other_list.pop(i)
                inter_list.append(e)
            return Ngrams(inter_list, exclusive=False)

    def union(self, *ngrams):
        if self.exclusive:
            union_set = self._ngrams
            for o in ngrams:
                union_set = union_set.union(o._ngrams)
            return Ngrams(union_set, exclusive=True)
        else:
            union_list = deepcopy(self._ngrams)
            for o in ngrams:
                union_list.extend(o._ngrams)
            return Ngrams(union_list, exclusive=False)


def _get_ngrams(n, text, exclusive=True):
    """Calcualtes n-grams.
    Args:
      n: which n-grams to calculate
      text: An array of tokens
    Returns:
      A set of n-grams
    """
    ngram_set = Ngrams(exclusive=exclusive)
    text_length = len(text)
    max_index_ngram_start = text_length - n
    for i in range(max_index_ngram_start + 1):
        ngram_set.add(tuple(text[i:i + n]))
    return ngram_set


def _split_into_words(sentences):
    """Splits multiple sentences into words and flattens the result"""
    return list(itertools.chain(*[_.split(" ") for _ in sentences]))


def _get_word_ngrams(n, sentences, exclusive=True):
    """Calculates word n-grams for multiple sentences.
    """
    assert len(sentences) > 0
    assert n > 0

    words = _split_into_words(sentences)
    return _get_ngrams(n, words, exclusive=exclusive)


def multi_rouge_n(sequences,
                  scores_ids,
                  n=2,
                  exclusive=True
    ):
    """
    Efficient way to compute highly repetitive scoring
    i.e. sequences are involved multiple time
    Args:
        sequences(list[str]): list of sequences (either hyp or ref)
        scores_ids(list[tuple(int)]): list of pairs (hyp_id, ref_id)
            ie. scores[i] = rouge_n(scores_ids[i][0],
                                    scores_ids[i][1])
    Returns:
        scores: list of length `len(scores_ids)` containing rouge `n`
                scores as a dict with 'f', 'r', 'p'
    Raises:
        KeyError: if there's a value of i in scores_ids that is not in
                  [0, len(sequences)[
    """
    ngrams = [_get_word_ngrams(n, sequence, exclusive=exclusive)
              for sequence in sequences]
    counts = [len(ngram) for ngram in ngrams]

    scores = []
    for hyp_id, ref_id in scores_ids:
        evaluated_ngrams = ngrams[hyp_id]
        evaluated_count = counts[hyp_id]

        reference_ngrams = ngrams[ref_id]
        reference_count = counts[ref_id]

        overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
        overlapping_count = len(overlapping_ngrams)

        scores += [f_r_p_rouge_n(evaluated_count,
                                 reference_count, overlapping_count)]
    return scores


def rouge_n(evaluated_sentences,
            reference_sentences,
            n=2,
            exclusive=True
    ):
    """
    Computes ROUGE-N of two text collections of sentences.
    Sourece: http://research.microsoft.com/en-us/um/people/cyl/download/
    papers/rouge-working-note-v1.3.1.pdf
    Args:
      evaluated_sentences: The sentences that have been picked by the
                           summarizer
      reference_sentences: The sentences from the referene set
      n: Size of ngram.  Defaults to 2.
    Returns:
      A tuple (f1, precision, recall) for ROUGE-N
    Raises:
      ValueError: raises exception if a param has len <= 0
    """
    if len(evaluated_sentences) <= 0:
        raise ValueError("Hypothesis is empty.")
    if len(reference_sentences) <= 0:
        raise ValueError("Reference is empty.")

    evaluated_ngrams = _get_word_ngrams(
        n, evaluated_sentences, exclusive=exclusive)
    reference_ngrams = _get_word_ngrams(
        n, reference_sentences, exclusive=exclusive)
    reference_count = len(reference_ngrams)
    evaluated_count = len(evaluated_ngrams)

    # Gets the overlapping ngrams between evaluated and reference
    overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
    overlapping_count = len(overlapping_ngrams)

    return f_r_p_rouge_n(evaluated_count, reference_count, overlapping_count)


def f_r_p_rouge_n(evaluated_count, reference_count, overlapping_count):
    # Handle edge case. This isn't mathematically correct, but it's good enough
    if evaluated_count == 0:
        precision = 0.0
    else:
        precision = overlapping_count / evaluated_count

    if reference_count == 0:
        recall = 0.0
    else:
        recall = overlapping_count / reference_count

    f1_score = 2.0 * ((precision * recall) / (precision + recall + 1e-8))

    return {"f": f1_score, "p": precision, "r": recall}


def _union_lcs(ref, c_list):
    """Find union LCS between a ref sentence and list of candidate sentences.
    Args:
        ref: list of tokens
        c_list: list of list of indices for LCS into reference summary
    Returns:
        List of tokens in ref representing union LCS.
    """
    lcs_list = [lcs_ind(ref, c) for c in c_list]
    return [ref[i] for i in _find_union(lcs_list)]


def _find_union(lcs_list):
    """Finds union LCS given a list of LCS."""
    return sorted(list(set().union(*lcs_list)))


def lcs_ind(ref, can):
    """Returns one of the longest lcs."""
    t = _lcs_table(ref, can)
    return _backtrack_norec(t, ref, can)


def _lcs_table(ref, can):
    """Create 2-d LCS score table."""
    rows = len(ref)
    cols = len(can)
    lcs_table = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if ref[i - 1] == can[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
    return lcs_table


def _backtrack_norec(t, ref, can):
    """Read out LCS."""
    i = len(ref)
    j = len(can)
    lcs = []
    while i > 0 and j > 0:
        if ref[i - 1] == can[j - 1]:
            lcs.insert(0, i-1)
            i -= 1
            j -= 1
        elif t[i][j - 1] > t[i - 1][j]:
            j -= 1
        else:
            i -= 1
    return lcs


def _summary_level_lcs(ref_sent, can_sent):
    """ROUGE: Summary-level LCS, section 3.2 in ROUGE paper.
    Args:
        ref_sent: list of tokenized reference sentences
        can_sent: list of tokenized candidate sentences
    Returns:
        summary level ROUGE score
    """
    if not ref_sent or not can_sent:
        return 0, 0, 0

    m = sum(map(len, ref_sent))
    n = sum(map(len, can_sent))
    if not n or not m:
        return 0, 0, 0

    # get token counts to prevent double counting
    token_cnts_r = collections.Counter()
    token_cnts_c = collections.Counter()
    for s in ref_sent: # s is a list of tokens
        token_cnts_r.update(s)
    for s in can_sent:
        token_cnts_c.update(s)

    hits = 0
    for r in ref_sent:
        lcs = _union_lcs(r, can_sent)
        for t in lcs:
            if token_cnts_c[t] > 0 and token_cnts_r[t] > 0:
                hits += 1
                token_cnts_c[t] -= 1
                token_cnts_r[t] -= 1

    recall = hits / m
    precision = hits / n

    f1 = (2 * recall * precision) / (recall + precision + 1e-10)

    return recall, precision, f1



def rouge_l_summary_level(evaluated_sentences,
                          reference_sentences,
                          exclusive=True,
                          **_
    ):
    """
    Computes ROUGE-L (summary level) of two text collections of sentences.
    http://research.microsoft.com/en-us/um/people/cyl/download/papers/rouge-working-note-v1.3.1.pdf
    Calculated according to:
    R_lcs = SUM(1, u)[LCS<union>(r_i,C)]/m
    P_lcs = SUM(1, u)[LCS<union>(r_i,C)]/n
    F_lcs = (2*R_lcs*P_lcs) / (R_lcs * P_lcs)
    where:
    SUM(i,u) = SUM from i through u
    u = number of sentences in reference summary
    C = Candidate summary made up of v sentences
    m = number of words in reference summary
    n = number of words in candidate summary
    Args:
      evaluated_sentences: The sentences that have been picked by the
                           summarizer
      reference_sentence: One of the sentences in the reference summaries
    Returns:
      A float: F_lcs
    Raises:
      ValueError: raises exception if a param has len <= 0
    """
    target_tokens_list = [s.split(' ') for s in reference_sentences if len(s) > 0]
    prediction_tokens_list = [s.split(' ') for s in evaluated_sentences if len(s) > 0]
    r, p, f1 = _summary_level_lcs(target_tokens_list, prediction_tokens_list)

    return {"f": f1, "p": p, "r": r}


# Pre-compile regexes that are use often
NON_ALPHANUM_PATTERN = r"[^a-z0-9\u4e00-\u9fa5]+"
NON_ALPHANUM_RE = re.compile(NON_ALPHANUM_PATTERN)
SPACES_PATTERN = r"\s+"
SPACES_RE = re.compile(SPACES_PATTERN)
VALID_TOKEN_PATTERN = r"^[a-z0-9\u4e00-\u9fa5]+$"
VALID_TOKEN_RE = re.compile(VALID_TOKEN_PATTERN)


def cn_split(text):
    seq = ''
    before_is_chinese = False
    for w in text:
        if u'\u4e00' <= w <= u'\u9f5a':  # is Chinese word
            seq = seq + ' ' + w
            before_is_chinese = True
        else:
            if before_is_chinese:
                seq = seq + ' ' + w
            else:
                seq = seq + w
            before_is_chinese = False
    seq = seq.strip()
    tokens = seq.split(' ')
    return tokens


def tokenize(text, stemmer, lang='en'):
    """Tokenize input text into a list of tokens.
    This approach aims to replicate the approach taken by Chin-Yew Lin in
    the original ROUGE implementation.
    Args:
        text: A text blob to tokenize.
        stemmer: An optional stemmer.
    Returns:
        A list of string tokens extracted from input text.
    """

    # Convert everything to lowercase.
    text = text.lower()
    # Replace any non-alpha-numeric characters with spaces.
    text = NON_ALPHANUM_RE.sub(" ", six.ensure_str(text))

    if lang == 'en':
        tokens = SPACES_RE.split(text)
    elif lang in ['zh', 'cn']:
        tokens = cn_split(text)

    if stemmer:
        # Only stem words more than 3 characters long.
        tokens = [six.ensure_str(stemmer.stem(x)) if len(x) > 3 else x for x in tokens]

    # One final check to drop any empty or invalid tokens.
    tokens = [x for x in tokens if VALID_TOKEN_RE.match(x)]

    return tokens


class Rouge(object):

    DEFAULT_METRICS = ["rouge-1", "rouge-2", "rouge-l"]
    AVAILABLE_METRICS = {
        "rouge-1": lambda hyp, ref, **k: rouge_n(hyp, ref, 1, **k),
        "rouge-2": lambda hyp, ref, **k: rouge_n(hyp, ref, 2, **k),
        "rouge-l": lambda hyp, ref, **k: rouge_l_summary_level(hyp, ref, **k),
    }
    DEFAULT_STATS = ["r", "p", "f"]
    AVAILABLE_STATS = ["r", "p", "f"]
    CN_SENTENCE_SPLIT_RE = r"(？|\?\s*|。|\.\s*|！|\!\s*|；|\;\s*|\…\…)"

    def __init__(
        self,
        metrics=None,
        stats=None,
        stemmer=True,
        lang='en',
        exclusive = False
    ):
        self.exclusive = exclusive  # use set or list for n-gram
        self.stemmer = porter.PorterStemmer() if stemmer else None
        self.lang = lang
        self.sentence_split_tag = '\n'

        assert self.lang in ['en', 'cn', 'zh'], ValueError("Unknow lang '%s'" % self.lang)

        if metrics is not None:
            self.metrics = [m.lower() for m in metrics]

            for m in self.metrics:
                if m not in Rouge.AVAILABLE_METRICS:
                    raise ValueError("Unknown metric '%s'" % m)
        else:
            self.metrics = Rouge.DEFAULT_METRICS

        if stats is not None:
            self.stats = [s.lower() for s in stats]

            for s in self.stats:
                if s not in Rouge.AVAILABLE_STATS:
                    raise ValueError("Unknown stat '%s'" % s)
        else:
            self.stats = Rouge.DEFAULT_STATS

    def get_scores(self, hyps, refs, avg=False, ignore_empty=False):
        if isinstance(hyps, six.string_types):
            hyps, refs = [hyps], [refs]

        if ignore_empty:
            assert avg is True, ValueError("ignore_empty only support the avg mode")
            # Filter out hyps of 0 length
            hyps_and_refs = zip(hyps, refs)
            hyps_and_refs = [_ for _ in hyps_and_refs
                             if len(_[0]) > 0
                             and len(_[1]) > 0]
            if len(hyps_and_refs) > 0:
                hyps, refs = zip(*hyps_and_refs)
            else:
                return self._zero_scores()

        assert(isinstance(hyps, type(refs)))
        assert(len(hyps) == len(refs))

        if not avg:
            return self._get_scores(hyps, refs)
        return self._get_avg_scores(hyps, refs)

    def _zero_scores(self):
        sen_score = {}
        for m in self.metrics:
            sen_score[m] = {s: 0.0 for s in self.stats}
        return sen_score

    def _get_scores(self, hyps, refs):

        scores = []
        for hyp, ref in zip(hyps, refs):
            sen_score = {}

            hyp = hyp.lower().replace('\\n', self.sentence_split_tag).replace('\\', '')
            ref = ref.lower().replace('\\n', self.sentence_split_tag).replace('\\', '')

            if self.lang in ['cn', 'zh']:
                hyp = re.sub(self.CN_SENTENCE_SPLIT_RE, '。' + self.sentence_split_tag, hyp)
                ref = re.sub(self.CN_SENTENCE_SPLIT_RE, '。' + self.sentence_split_tag, ref)
            if self.lang in ['en']:
                hyp = self.sentence_split_tag.join(nltk.sent_tokenize(hyp.strip()))
                ref = self.sentence_split_tag.join(nltk.sent_tokenize(ref.strip()))

            hyp = [" ".join(tokenize(_, self.stemmer, self.lang)) for _ in hyp.split(self.sentence_split_tag) if len(_) > 0]
            ref = [" ".join(tokenize(_, self.stemmer, self.lang)) for _ in ref.split(self.sentence_split_tag) if len(_) > 0]

            for m in self.metrics:
                fn = Rouge.AVAILABLE_METRICS[m]
                try:
                    sc = fn(hyp, ref, exclusive=self.exclusive)
                    sen_score[m] = {s: sc[s] for s in self.stats}
                except ValueError as err:
                    sen_score[m] = {s: 0.0 for s in self.stats}

            scores.append(sen_score)
        return scores

    def _get_avg_scores(self, hyps, refs):
        scores = self._get_scores(hyps, refs)
        avg_scores = {}
        for met in self.metrics:
            tmp_dict = {}
            for st in self.stats:
                tmp_dict[st] = 0.0
            avg_scores[met] = tmp_dict
        num = len(scores)
        for s in scores:
            for met in self.metrics:
                for st in self.stats:
                    avg_scores[met][st] += s[met][st] / num
        return avg_scores


