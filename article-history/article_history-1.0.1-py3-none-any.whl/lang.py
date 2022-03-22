import collections

from gensim import corpora, models, similarities

STOPLIST = set('for a of the and to in but'.split())


def _article_analysis(articles):
    """The Natural Language Processing analysis on the
    articles, returns a dictionary bag-of-words vector"""
    """Creates an additional set of stop words, final
    check to make sure some words do not get through"""
    # Lowercase each document, split it by white
    # space and filter out stopwords
    texts = [
        [word for word in article.lower().split()
         if word not in STOPLIST]
        for article in articles
    ]

    # Counts word frequencies
    frequency = collections.Counter()
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Only keeps words that appear more than once
    tokens = [
        [token for token in text if frequency[token] > 1]
        for text in texts
    ]
    return tokens


def process_article(original_article, related_articles):
    articles = [original_article] + related_articles
    tokens = _article_analysis(articles)
    dictionary = corpora.Dictionary(tokens)
    bow_corpus = _keywords_into_vectors(tokens)
    sims = _training_the_model(original_article, bow_corpus, dictionary)
    return sims


def _keywords_into_vectors(processed_article):
    dictionary = corpora.Dictionary(processed_article)
    bow_corpus = [dictionary.doc2bow(text) for text in processed_article]
    return bow_corpus


def _training_the_model(original_article, bow_corpus, dictionary):
    lsi = models.LsiModel(bow_corpus, id2word=dictionary, num_topics=2)
    vec_bow = dictionary.doc2bow(original_article.lower().split())
    vec_lsi = lsi[vec_bow]

    index = similarities.SparseMatrixSimilarity(lsi[bow_corpus],
            num_best=10, num_features=len(dictionary))
    sims = index[vec_lsi]  # perform a similarity query against the corpus

    related_article_similarities = sims[1:]

    ret = [
        (idx - 1, sim) for (idx, sim) in related_article_similarities
    ]
    return ret
