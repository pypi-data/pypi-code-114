""" utils/text_tools.py

テキスト処理のユーティリティ
"""
import re
import unicodedata

from django.core.validators import validate_email

from janome.tokenizer import Tokenizer

DEFAULT_TOKENIZER = Tokenizer()


def shortnate(string, length):
    """ 文字列が既定の長さ以上だった場合に規定の長さまでで残りを省略とする """
    return string if len(string) <= length else string[:length - 4] + '...'


def get_words(text, customdict=None):
    """ 与えられたテキストを形態素解析して、含まれる名詞のリストを返す """

    def _filter(s):
        """ 名詞だけにフィルタリングする """
        reg = re.compile(r'名詞')
        ignore_reg = re.compile(r'非自立')
        if (reg.search(s.part_of_speech) and
                not ignore_reg.search(s.part_of_speech)):
            return True

    if customdict:
        t = Tokenizer(customdict)
    else:
        t = DEFAULT_TOKENIZER

    __word = ''
    __results = []
    __text = re.sub(r'[()!?.,]+', ' ', unicodedata.normalize('NFKC', text))
    for s in t.tokenize(__text):
        if _filter(s):
            __word += s.surface
        elif __word:
            __results.append(__word)
            __word = ''
    if __word:
        __results.append(__word)
    return __results


def mask_email(email):
    """ メールアドレスをマスクする """
    # メールアドレス形式かチェックして、合わなかったらそのまま返す。
    try:
        validate_email(email)
    except:
        return email

    local, domain = email.split('@')
    if len(local) > 2:
        local = local[:1] + '*'*(len(local)-2)
    data = {
        'local': local,
        'domain': domain
    }
    return '{local}@{domain}'.format(**data)
