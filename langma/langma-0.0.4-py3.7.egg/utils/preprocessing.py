# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function

import math
from datetime import timedelta, datetime
import pandas as pd
import numpy as np
import jieba
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer, \
    OneHotEncoder
import pickle
from tqdm import tqdm
import warnings
from gensim.models.word2vec import LineSentence, Word2Vec
from langma.utils.logutil import logger

from langma.utils.file_utils import save_dict

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: "{:.2f}".format(x))


def get_max_len(data: pd.Series, up=False):
    """获得合适的最大长度值
    >>> MAX_LEN = get_max_len(df['content'])

    :param data: 待统计的数据
    :return: 最大长度值
    """

    max_lens = data.apply(lambda x: x.count(' ') + 1)
    if up:
        # 向上取整
        return math.ceil(np.mean(max_lens) + 2 * np.std(max_lens))
    else:
        # 向下取整
        return int(np.mean(max_lens) + 2 * np.std(max_lens))


def load_stopwords(file):
    """加载停用词"""
    return {line.strip() for line in open(file, encoding='utf-8').readlines()}


def remove_punctuation(sentence, only_chinese=False):
    '''删除特殊符号

Usage:
    >>> df['clean_title'] = df['title'].apply(remove_punctuation)

    :param sentence:
    :param only_chinese:
    :return:
    '''
    sentence = str(sentence)
    if sentence.strip() == '':
        return ''
    # 删除特殊符号
    sentence = re.sub(
        r'[\s+\-\!\/\[\]\{\}_,.$%^*(+\"\')]+|[:：+——()?【】“”！，。？、~@#￥%……&*（）]+|评|你好|您好',
        ' ', sentence)
    if only_chinese:
        # 删除汉字以外的所有符号
        rule = re.compile(u"[^\u4E00-\u9FA5]")
    else:
        # 删除除字母,数字，汉字以外的所有符号
        rule = re.compile(u"[^a-zA-Z0-9\u4E00-\u9FA5]")
    line = rule.sub('', sentence)
    return line


def sentence_preprocess(sentence, stopwords, only_chinese=False):
    # 删除特殊字符
    sentence = remove_punctuation(sentence, only_chinese=only_chinese)

    # 切词，默认精确模式，全模式cut参数cut_all=True
    words = jieba.cut(sentence, cut_all=False)

    # 去停用词
    words = [w for w in words if w not in stopwords]
    return words


def tokenizer_words(wds_series: pd.Series, num_words=50000):
    tokenizer = Tokenizer(num_words=num_words,
                          filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~',
                          lower=True,
                          oov_token="<UNK>")
    token_wds = wds_series.values
    tokenizer.fit_on_texts(token_wds)
    word_index = tokenizer.word_index
    logger.info('共有 %s 个不相同的词语.' % len(word_index))
    sequences = tokenizer.texts_to_sequences(token_wds)
    return tokenizer, sequences


def padding_sequencies(tokend_sequences,
                       maxlen=180,
                       padding='post',
                       truncating='post'):
    # 填充sequence,让sequence的各个列的长度统一
    paded_sequences = sequence.pad_sequences(tokend_sequences,
                                             maxlen=maxlen,
                                             padding=padding,
                                             truncating=truncating)
    return paded_sequences


def create_data(text: pd.Series,
                label: pd.Series,
                num_words=50000,
                maxlen=128,
                file_x="",
                file_y="",
                tokenizer_pickle=""):
    '''

    :param text: df.content
    :param label: df.label
    :param num_words:
    :param maxlen:
    :return:
    '''
    # 对于label处理
    # le, y = multi_label_encoder(label)
    # le, y = label_encoder(label)
    le, y = onehot_encoder(label)

    # 对文本处理
    tokenizer, x = tokenizer_words(text, num_words=num_words)
    x = padding_sequencies(x, maxlen=maxlen)

    # 保存数据
    np.save(file_x, x)
    np.save(file_y, y)
    logger.info('已创建并保存x,y至：\n {} \n {}'.format(file_x, file_y))

    # 同时还要保存tokenizer和 multi_label_binarizer
    # 否则训练结束后无法还原把数字还原成文本
    tb = {'tokenizer': tokenizer, 'binarizer': le}
    with open(tokenizer_pickle, 'wb') as f:
        pickle.dump(tb, f)
    logger.info('已创建并保存tokenizer和binarizer至：\n {}'.format(tokenizer_pickle))
    return x, y


def load_processed_data(file_x="", file_y=""):
    x = np.load(file=file_x)
    y = np.load(file=file_y)
    return x, y


def label_statistics(label: pd.Series):
    '''统计标签的数量'''
    label_value_counts = label.value_counts()
    lbs = {'label': label_value_counts.index, 'count': label_value_counts}
    return pd.DataFrame(data=lbs).reset_index(drop=True)


def label_weights(labels: pd.Series) -> dict:
    """Statistics label proportion"""
    total = labels.count()
    value_counts = labels.value_counts()
    value_counts = dict(value_counts)
    for key, value in value_counts.items():
        value_counts[key] = round(value / total, 2)
    return value_counts


def tf_keras_label_encoder(label: pd.Series, num_class=3):
    from tensorflow.keras.utils import to_categorical
    return to_categorical(label.values, num_class)


def multi_label_encoder(label: pd.Series):
    '''多标签编码

    :param label:
    :return:
    '''

    # https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html?highlight=labelencoder#sklearn.preprocessing.LabelEncoder
    mlb = MultiLabelBinarizer()
    result = mlb.fit_transform(label)
    logger.info(list(mlb.classes_))
    return mlb, result


def onehot_encoder(label: pd.Series):
    '''onehot 编码

    :param label:
    :return:
    '''

    # https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html?highlight=onehot#sklearn.preprocessing.OneHotEncoder
    oht = OneHotEncoder()
    result = oht.fit_transform(label.values.reshape(-1, 1))
    logger.info(list(oht.categories_))
    return oht, result


def label_encoder(label: pd.Series):
    '''
>>> from sklearn.preprocessing import LabelEncoder
>>> from collections import Counter
>>> import pandas as pd

>>> test_list = ['05db9164', '68fd1e64', '05db9164', '8cf07265', '05db9164',
             '68fd1e64', '5bfa8ab5', '5a9ed9b0', '05db9164', '9a89b36c',
             '68fd1e64', '8cf07265', '05db9164', '68fd1e64', '5a9ed9b0',
             '68fd1e64', '5a9ed9b0', '05db9164', '05db9164', '2d4ea12b']

# 初始化
>>> lbe = LabelEncoder()
# 先fit转换为set, 然后在transform。
>>> lbe_res = lbe.fit_transform(test_list)
# 如何看标签个数及顺序？[注：这里标签顺序 不是根据词频]
>>> print(lbe.classes_)
    ['05db9164' '2d4ea12b' '5a9ed9b0' '5bfa8ab5' '68fd1e64' '8cf07265' '9a89b36c']
# 如何看编码结果？
>>> print(lbe_res)
    [0 4 0 5 0 4 3 2 0 6 4 5 0 4 2 4 2 0 0 1]
# 如何看某个编码对应的原始值？
>>> print(lbe.inverse_transform([5, 2, 1]))
    ['8cf07265', '5a9ed9b0', '2d4ea12b']
    :param label:
    :return:
    '''
    # https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html?highlight=labelencoder#sklearn.preprocessing.LabelEncoder
    le = LabelEncoder()
    result = le.fit_transform(label)
    logger.info(list(le.classes_))
    return le, result


def save_tokenizer(tokenizer, tokenizer_pickle=""):
    '''keep tokenizer'''
    with open(tokenizer_pickle, 'wb') as f:
        pickle.dump(tokenizer, f)
    logger.info('已创建并保存tokenizer和binarizer至：\n {}'.format(tokenizer_pickle))


def load_tokenizer(tokenizer_pickle=""):
    '''
    tokenizer = load_tokenizer()
    tokenizer.word_index
    :return:
    '''
    with open(tokenizer_pickle, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer


def load_tokenizer_binarizer(tokenizer_pickle=""):
    '''
    tokenizer, mlb = load_tokenizer_binarizer()
    tokenizer.word_index
    :return:
    '''
    with open(tokenizer_pickle, 'rb') as f:
        tb = pickle.load(f)
    return tb['tokenizer'], tb['binarizer']


def train_word2vec(seg_path,
                   train_x_pad_path,
                   train_y_pad_path,
                   test_x_pad_path,
                   embedding_file,
                   vocab_file,
                   reverse_vocab_file,
                   model_file,
                   embedding_dim=300,
                   train_epochs=3):
    logger.info('start build w2v model')
    wv_model = Word2Vec(LineSentence(seg_path),
                        size=embedding_dim,
                        sg=1,
                        workers=8,
                        iter=train_epochs,
                        window=5,
                        min_count=5)
    vocab = wv_model.wv.vocab

    # 词向量再次训练
    logger.info('start retrain w2v model')
    wv_model.build_vocab(LineSentence(train_x_pad_path), update=True)
    wv_model.train(LineSentence(train_x_pad_path),
                   epochs=1,
                   total_examples=wv_model.corpus_count)

    logger.info('1/3')
    wv_model.build_vocab(LineSentence(train_y_pad_path), update=True)
    wv_model.train(LineSentence(train_y_pad_path),
                   epochs=1,
                   total_examples=wv_model.corpus_count)

    logger.info('2/3')
    wv_model.build_vocab(LineSentence(test_x_pad_path), update=True)
    wv_model.train(LineSentence(test_x_pad_path),
                   epochs=1,
                   total_examples=wv_model.corpus_count)

    # 保存词向量模型
    wv_model.save(model_file)
    logger.info('finish retrain w2v model')
    logger.info('final w2v_model has vocabulary of ', len(wv_model.wv.vocab))

    # 12. 更新vocab
    vocab = {word: index for index, word in enumerate(wv_model.wv.index2word)}
    reverse_vocab = {
        index: word
        for index, word in enumerate(wv_model.wv.index2word)
    }

    # 保存字典
    save_dict(vocab_file, vocab)
    save_dict(reverse_vocab_file, reverse_vocab)

    # 13. 保存词向量矩阵
    embedding_matrix = wv_model.wv.vectors
    np.save(embedding_file, embedding_matrix)
