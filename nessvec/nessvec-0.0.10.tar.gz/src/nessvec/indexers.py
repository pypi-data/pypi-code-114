# indexers.py
import argparse
import logging
from pathlib import Path
import time

import numpy as np
import pandas as pd         # conda install -c conda-forge pandas
import pynndescent as pynn  # conda install -c conda-forge pynndescent
import psutil               # conda install -c anaconda psutil

from .constants import __version__, DATA_DIR, LOGGING_LEVEL
from .files import load_hdf5
from .util import download_if_necessary

COUNTRY_NAME_EXAMPLES = "Australia USA PNG France China Indonesia India Congo Ethiopia".split()
log = logging.getLogger(__name__)

class Index(pynn.NNDescent):

    def __init__(self, data=None, vectors=None, vocab=None, metric='cosine', metric_kwds=None, num_vecs=100_000, metric_kwargs=None, **kwargs):
        """Default distance measure changed from Euclidian to cosine distance

        Inputs:
            data (2D array): table of row vectors to be indexed (each row is typically an embedding)
            vocab (array of str): array of words (str) associated with each vector, self.vocab.index = words, self.vocab.values = rownums

        Outputs:
            index (augmented pynn.NNDescent): adds
        .data
            .vocab
            .get_nearest()
            .reword_sentence() 


        >>> metrics =  (
        ...     "euclidean manhattan chebyshev minkowski canberra braycurtis mahalanobis wminkowski seuclidean cosinecorrelation "
        ...     + "haversine hamming jaccard dice russelrao kulsinski rogerstanimoto sokalmichener sokalsneath yule hellinger wasserstein-1d"
        ...     ).split()
        """
        # data and vectors are synonymous and both are optional
        # data is canonical because that's what NNDescent calls it
        if data is None:
            data = vectors
        if data is None:
            data, vocab = load_hdf5(num_vecs=num_vecs) 
        data = np.array(data)
        if len(data.shape) == 1 and 4096 >= len(data) >= 3:
            data = data.reshape(1, -1)
        if vocab is None:
            vocab = np.arange(len(data))
        self.vocab = pd.Series(vocab, index=getattr(vocab, 'index', vocab))
        metric_kwargs = metric_kwds if metric_kwds is not None else metric_kwargs
        super().__init__(data=data, metric=metric, metric_kwds=metric_kwargs, **kwargs)
        self.data = self._raw_data


    # def update(self, vectors, **kwargs):
    #     """ Appends additional vectors to _raw_data and words to .vocab using NNDescent.update

    #     # pseudocode for the internal NNDescent.update() method
    #     def NNDescent.update(self, X):
    #         ...
    #         X = check_array(X, dtype=np.float32, accept_sparse="csr", order="C")
    #         ...
    #         self._raw_data = np.vstack([self._raw_data[original_order, :], X])
    #         ...
    #         nn_descent(self._raw_data)
    #     """
    #     super().update(data=vectors, **kwargs)

    def get_nearest(self, word, k=None, num_neighbors=10):
        if k is None:
            k = num_neighbors
        if k is None:
            k = 10
        if isinstance(word, str):
            return self.query_series(
                self.data[self.vocab[word]], k=k)
            # qresults = self.query(
            #     self.data[self.vocab[word]], k=num_neighbors)
        if isinstance(word, int):
            return self.query_series(
                self.data[word], k=k)
            # qresults = self.query(
            #     self.data[word], k=num_neighbors)
        return self.query_series(word, k=k)
        #     qresults = self.query(word, k=num_neighbors)
        # words = self.vocab.iloc[qresults[0][0]]
        # distances = qresults[1][0]
        # return pd.Series(distances, index=words.index)


    def query_series(self, *args, **kwargs):
        qresults = self.query(*args, **kwargs)
        words = self.vocab.iloc[qresults[0][0]]
        distances = qresults[1][0]
        return pd.Series(distances, index=words.index)


    def expand_examples(self, examples=COUNTRY_NAME_EXAMPLES, num_neighbors=10, depth=1):
        """ Given list/set of words find similar word vectors, and recurse for `depth` iterations

        >>> index = Index()
        >>> index.expand_examples('Australia', num_neighbors=3, depth=2)
        """
        if isinstance(examples, str):
            examples = [examples]
        new_examples = set(examples)
        for d in range(depth):
            query_words = list(new_examples)
            for word in query_words:
                new_examples = new_examples.union(self.get_nearest(
                    word,
                    num_neighbors=num_neighbors + 1,
                ).index.values[1:])
                print(word, new_examples)
        return new_examples


    def reword_sentence(self, sent, max_dist=0.2):
        # FIXME: regular for loop instead of list comprehension
        return " ".join(
            [
                self.get_nearest(tok).index.values[1]
                if self.get_nearest(tok).iloc[1] < max_dist
                else tok
                for tok in sent.split()
            ]
        )

    def query_word(self, word, k=10):
        return self.query(self.data[self.vocab[word]], k=k)

    def query(self, query_data, *args, **kwargs):
        return super().query(np.array(query_data).reshape((-1, self.dim)), *args, **kwargs)


# FIXME: move "augmentation of Index" from Index to here.
def IndexedWordVectors(Index):


    def __init__(self, vectors, vocab=None, metric='cosine', metric_kwds=None, metric_kwargs=None, **kwargs):
        """Default distance measure changed from Euclidian to cosine distance

        >>> metrics =  (
        ...     "euclidean manhattan chebyshev minkowski canberra braycurtis mahalanobis wminkowski seuclidean cosinecorrelation "
        ...     + "haversine hamming jaccard dice russelrao kulsinski rogerstanimoto sokalmichener sokalsneath yule hellinger wasserstein-1d"
        ...     ).split()
        """
        vectors = np.array(vectors)
        if len(vectors.shape) == 1 and 4096 >= len(vectors) >= 3:
            vectors = vectors.reshape(1, -1)
        self.vocab = vocab or np.arange(len(vectors))
        self.vocab = pd.Series(vocab)
        metric_kwargs = metric_kwds if metric_kwds is not None else metric_kwargs
        super().__init__(data=data, metric=metric, metric_kwds=metric_kwargs, **kwargs)


    # def __init__(self, vocab, vectors=None, normalizer=glove_normalize):
    #     self.normalizer = normalizer
    #     if vectors is None:
    #         self.load()
    #     elif isinstance(vectors, dict):
    #         self.df = pd.DataFrame(vectors)
    #     else:
    #         self.df = pd.DataFrame(vectors, index=(index or range(len(vectors))))


    def get(self, key, default=None):
        if key in self.df.columns:
            return self.df[key]
        return default

    def __getitem__(self, key):
        try:
            return self.df[key]
        except KeyError:
            print(f"Unable to find '{key}' in {self.df.shape} DataFrame of vectors")
        normalized_key = self.normalizer(str(key))
        try:
            return self.df[normalized_key]
        except KeyError:
            print(f"Unable to find '{normalized_key}' in {self.df.shape} DataFrame of vectors")
        raise(KeyError(f"Unable to find any of {set([key, normalized_key])} in self.df.shape DataFrame of vectors"))


# class IndexedVectors:
#     def __init__(self, vectors=None, index=None, normalizer=glove_normalize):
#         self.normalizer = normalizer
#         if vectors is None:
#             self.load()
#         elif isinstance(vectors, dict):
#             self.df = pd.DataFrame(vectors)
#         else:
#             self.df = pd.DataFrame(vectors, index=(index or range(len(vectors))))

#     def load(self, dim=50, size=6):
#         self.df = pd.DataFrame(load_glove(dim=dim, size=size))
#         return self

#     def get(self, key, default=None):
#         if key in self.df.columns:
#             return self.df[key]
#         return default

#     def __getitem__(self, key):
#         try:
#             return self.df[key]
#         except KeyError:
#             print(f"Unable to find '{key}' in {self.df.shape} DataFrame of vectors")
#         normalized_key = self.normalizer(str(key))
#         try:
#             return self.df[normalized_key]
#         except KeyError:
#             print(f"Unable to find '{normalized_key}' in {self.df.shape} DataFrame of vectors")
#         raise(KeyError(f"Unable to find any of {set([key, normalized_key])} in self.df.shape DataFrame of vectors"))

#     def keys(self):
#         return self.df.columns.values

#     def values(self):
#         return self.df.T.values

#     def iteritems(self):
#         return self.df.T.iterrows()

#     def iterrows(self):
#         return self.df.T.iterrows()


def load_analogies(filepath='google', num_analogies=None, vocab=None):
    # Load an analogy dataset
    filepath = download_if_necessary('analogy-google')
    # TODO: test filepath is None because of download_if_necessary magic causing bug
    return pd.read_csv(filepath, index_col=0, nrows=num_analogies)

    np.random.seed(451)
    df_6_analogies = df_analogies.sample(6)
    log.info(df_6_analogies)
    for i, row in df_6_analogies.iterrows():
        log.info(f'"{row.word1.title()}" is to "{row.word2}" as "{row.word3}" is to "{row.target}"')
    return df_analogies

    # # "Sink" is to "plumber" as "meat" is to "butcher"
    # # "Plug" is to "insert" as "clamp" is to "grip"
    # # "Noisy" is to "uproar" as "tanned" is to "leather"
    # # "Ceremony" is to "sermon" as "agenda" is to "advertisement"
    # # "Tale" is to "story" as "week" is to "year"
    # #   ^ SEEMS INCORRECT TO ME
    # # "Antiseptic" is to "germs" as "illness" is to "fever"

    # # TODO: search the analogies for NLP/language/linguistics/story/text/writing/computer-related analogies
    # #       subject = vocab['NLP'] + vocab['language'] + vocab['English'] + vocab['computer'] + vocab['AI']
    # df_analogy.sample(6)
    # # ...

    # index.query(np.array([vecs[vocab['king']]]))[0][0]
    # # np.ndarray([2407, 7697, 6406, 1067, 9517, 7610, 600459, 5409, 854338, 5094])

    # vocab.iloc[index.query(np.array([vecs[vocab['king']] - vecs[vocab['man']] + vecs[vocab['woman']]]))[0][0]]
    # # king               2407
    # # queen              6406
    # # kings              7697
    # # monarch            9517
    # # princess          11491
    # # king-            600459
    # # King               1067
    # # prince             7610
    # # queen-consort    623878
    # # queendom         836526
    # # dtype: int64

    # neighbors = index.query(np.array([vecs[vocab['king']] - vecs[vocab['man']] + vecs[vocab['woman']]]))
    # neighbors = pd.DataFrame(
    #     zip(
    #         neighbors[0][0],
    #         neighbors[1][0],
    #         vocab.iloc[neighbors[0][0]].index.values
    #     ),
    #     columns='word_id distance word'.split())


def time_and_memory(resources_t0=0):
    resources = {}
    resources.update(dict(psutil.virtual_memory()._asdict()))
    resources.update({'wall_time': time.time()})
    return pd.Series(resources) - resources_t0


def index_vectors(vecs, resources={}):
    # keep track of the time and memory used for each big task
    resources = pd.DataFrame() if resources is None else resources

    resources_start = time_and_memory()
    index = Index(vecs)
    index.prepare()
    resources['pynndescent_index'] = time_and_memory(resources_start)

    # resources_start = time_and_memory()
    # index.query(vecs[vocab['king']].reshape((-1, index.dim)))
    # resources['pynn_query'] = time_and_memory(resources_start)

    return index, resources


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Load word embeddings (GloVe, FastText, Word2Vec) and index them for approximate nearest neighbor search."
    )

    parser.add_argument(
        "--version", action="version",
        version=f"{parser.prog} version {__version__}"
    )

    parser.add_argument(
        "-v", "--verbose", action='count', default=0,
        help='Increase the verbosity (may be repeated, e.g. -vvv',
    )

    parser.add_argument(
        "-n", "--num_vecs", type=int, default=50000,
        help="Number of vectors to index (default=50000)",
    )

    parser.add_argument(
        '-d', '--data_dir', type=Path, default=DATA_DIR,
        help="Location to cache datasets and models (vectors, benchmarks, SpaCy language models)",
    )

    return parser


def main(args=None, num_vecs=100_000, verbosity=0):
    # level = ERRORis50 - verbosity * 10 => verbosity = (ERRORis50 - level) / 10
    log.setLevel(logging.ERROR - verbosity * 10)
    resources = pd.DataFrame()
    resources['start'] = time_and_memory()
    log.info('\n' + str(resources['start'].round(2)))

    # Load the 1Mx300 FastText vectors trained on Wikipedia
    vecs, vocab = load_hdf5(num_vecs=num_vecs)
    resources['load_hdf5'] = time_and_memory(resources['start'])
    log.info('\n' + str(resources['load_hdf5'].round(2)))

    index, resources = index_vectors(vecs, resources=resources)
    resources[f'index_{num_vecs}_vecs'] = time_and_memory(resources['load_hdf5'])
    log.info('\n' + str(resources[f'index_{num_vecs}_vecs'].round(2)))

    df_analogies = load_analogies()

    log.info(f'Loaded {len(df_analogies)} analogies.')
    results = dict(resources=resources, index=index, vecs=vecs, vocab=vocab, num_vecs=num_vecs)
    globals().update(results)
    return results


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()
    LOGGING_LEVEL = logging.ERROR - args.verbose * 10  # noqa
    logging.getLogger().setLevel(LOGGING_LEVEL)
    # logging.basicConfig(level=LOG_LEVEL)
    log.info('\n' + str(vars(args)))

    # level = ERRORis50 - verbosity * 10 => verbosity = (ERRORis50 - level) / 10
    results = main(num_vecs=args.num_vecs, verbosity=(logging.ERROR - log.getLevel()) / 10)
    

