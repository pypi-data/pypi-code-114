# constants.py
from collections.abc import Mapping
from collections import OrderedDict
import datetime
# from decimal import Decimal
import logging
import numpy as np
import pandas as pd
from pathlib import Path
from pytz import timezone
import string

log = logging.getLogger(__name__)
__version__ = '0.0.9rc'
log.debug(f'Running {__name__} version {__version__} ...')
LOGLEVEL = logging.ERROR

data_dir_names_ = ['.nlpia2-data', 'nessvec-data']
DATA_DIR = Path('~').expanduser().resolve().absolute() / data_dir_names_[0]

for dir_name in data_dir_names_:
    DATA_DIR = DATA_DIR.parent / dir_name
    if DATA_DIR.is_dir():
        break

# the last of the data_dir possibilities is the default
if not DATA_DIR.is_dir():
    DATA_DIR.mkdir()
log.debug(f'Storing vectors, models, and benchmark datasets in DATA_DIR={DATA_DIR}')


ANALOGY_URLS = [
    # SAT(acronym for Scholastic Aptitude Test), 5 610 questions divided into 374 semantic classes.
    'https://gitlab.com/tangibleai/word-vector-benchmarks/-/raw/main/word-analogy/monolingual/en/sat.csv',

    # SemEval-2017 Task 2 (Measuring Degrees of Relational Similarity)
    # 10014 questions in 10 classes, 79 subclasses .
    'https://gitlab.com/tangibleai/word-vector-benchmarks/-/raw/main/word-analogy/monolingual/en/semeval.csv',

    # JAIR (Journal of AI Research)
    # 430 questions in 20 semantic classes. Contains words & collocations (e.g. solar system).
    'https://gitlab.com/tangibleai/word-vector-benchmarks/-/raw/main/word-analogy/monolingual/en/jair.csv',

    # MSR(acronym for Microsoft Research Syntactic Analogies), 8000 questions divided into 16 morphological classes.
    'https://gitlab.com/tangibleai/word-vector-benchmarks/-/raw/main/word-analogy/monolingual/en/msr.csv',

    # Semantic-Syntactic Word Relationship Dataset (Google)
    # 19544 questions in 2 classes: morphological (10675) and semantic (8869) relationships) & 10 subclasses
    'https://gitlab.com/tangibleai/word-vector-benchmarks/-/raw/main/word-analogy/monolingual/en/google-analogies.csv',
]


ANALOGY_FILEPATHS = [
    # SAT(acronym for Scholastic Aptitude Test), 5 610 questions divided into 374 semantic classes.
    'en-word-analogy-sat.csv',

    # SemEval-2017 Task 2 (Measuring Degrees of Relational Similarity)
    # 10014 questions in 10 classes, 79 subclasses .
    'en-word-analogy-semeval.csv',

    # JAIR (Journal of AI Research)
    # 430 questions in 20 semantic classes. Contains words & collocations (e.g. solar system).
    'en-word-analogy-jair.csv',

    # MSR(acronym for Microsoft Research Syntactic Analogies), 8000 questions divided into 16 morphological classes.
    'en-word-analogy-msr.csv',

    # Semantic-Syntactic Word Relationship Dataset (Google)
    # 19544 questions in 2 classes: morphological (10675) and semantic (8869) relationships) & 10 subclasses
    'en-word-analogy-google.csv',
]


LARGE_FILES = dict(
    ("-".join(fn.split(".")[0].split("-")[-2:]), dict(url=u, filename=fn))
    for (u, fn) in zip(ANALOGY_URLS, ANALOGY_FILEPATHS)
)


#########################################################
# qary.constants

LOGGING_FORMAT = '%(asctime)s.%(msecs)d %(levelname)-4s %(filename)s:%(lineno)d %(message)s'
LOGGING_DATEFMT = '%Y-%m-%d:%H:%M:%S'
LOGGING_LEVEL = logging.ERROR
logging.basicConfig(
    format=LOGGING_FORMAT,
    datefmt=LOGGING_DATEFMT,
    level=LOGGING_LEVEL)
# root_logger = logging.getLogger()
log = logging.getLogger(__name__)

# TZ constants
DEFAULT_TZ = timezone('UTC')

MAX_LEN_FILEPATH = 1023  # on OSX `open(fn)` raises OSError('Filename too long') if len(fn)>=1024

#####################################################################################
# pugnlp.constants

tld_iana = pd.read_csv(Path(DATA_DIR) / 'constants' / 'tlds-from-iana.csv', encoding='utf8')
tld_iana = OrderedDict(sorted(zip((tld.strip().lstrip('.') for tld in tld_iana.domain),
                                  [(sponsor.strip(), -1) for sponsor in tld_iana.sponsor]),
                              key=lambda x: len(x[0]),
                              reverse=True))
# top 20 in Google searches per day
# sorted by longest first so .com matches before .om (Oman)
tld_popular = OrderedDict(sorted([
    ('com', ('Commercial', 4860000000)),
    ('org', ('Noncommercial', 1950000000)),
    ('edu', ('US accredited postsecondary institutions', 1550000000)),
    ('gov', ('United States Government', 1060000000)),
    ('uk', ('United Kingdom', 473000000)),  # noqa
    ('net', ('Network services', 206000000)),
    ('ca', ('Canada', 165000000)),  # noqa
    ('de', ('Germany', 145000000)),  # noqa
    ('jp', ('Japan', 139000000)),  # noqa
    ('fr', ('France', 96700000)),  # noqa
    ('au', ('Australia', 91000000)),  # noqa
    ('us', ('United States', 68300000)),  # noqa
    ('ru', ('Russian Federation', 67900000)),  # noqa
    ('ch', ('Switzerland', 62100000)),  # noqa
    ('it', ('Italy', 55200000)),  # noqa
    ('nl', ('Netherlands', 45700000)),  # noqa
    ('se', ('Sweden', 39000000)),  # noqa
    ('no', ('Norway', 32300000)),  # noqa
    ('es', ('Spain', 31000000)),  # noqa
    ('mil', ('US Military', 28400000)),
    ], key=lambda x: len(x[0]), reverse=True))

uri_schemes_iana = sorted(pd.read_csv(Path(DATA_DIR) / 'constants' / 'uri-schemes.xhtml.csv',
                                      index_col=0).index.values,
                          key=lambda x: len(str(x)), reverse=True)
uri_schemes_popular = ['chrome-extension', 'example', 'content', 'bitcoin',
                       'telnet', 'mailto',
                       'https', 'gtalk',
                       'http', 'smtp', 'feed',
                       'udp', 'ftp', 'ssh', 'git', 'apt', 'svn', 'cvs']

# these may not all be the sames isinstance types, depending on the env
FLOAT_TYPES = tuple([t for t in set(np.sctypeDict.values()) if t.__name__.startswith('float')] + [float])
FLOAT_DTYPES = tuple(set(np.dtype(typ) for typ in FLOAT_TYPES))
INT_TYPES = tuple([t for t in set(np.sctypeDict.values()) if t.__name__.startswith('int')] + [int])
INT_DTYPES = tuple(set(np.dtype(typ) for typ in INT_TYPES))
NUMERIC_TYPES = tuple(set(list(FLOAT_TYPES) + list(INT_TYPES)))
NUMERIC_DTYPES = tuple(set(np.dtype(typ) for typ in NUMERIC_TYPES))

DATETIME_TYPES = [t for t in set(np.typeDict.values()) if t.__name__.startswith('datetime')]
DATETIME_TYPES.extend([datetime.datetime, pd.Timestamp])
DATETIME_TYPES = tuple(DATETIME_TYPES)

DATE_TYPES = (datetime.datetime, datetime.date)

# matrices can be column or row vectors if they have a single col/row
VECTOR_TYPES = (list, tuple, np.matrix, np.ndarray)
MAPPING_TYPES = (Mapping, pd.Series, pd.DataFrame)

# These are the valid dates for all 3 datetime types in python (and the underelying integer nanoseconds)
INT_MAX = INT64_MAX = 2 ** 63 - 1
INT_MIN = INT64_MIN = - 2 ** 63
UINT_MAX = UINT64_MAX = - 2 ** 64 - 1

INT32_MAX = 2 ** 31 - 1
INT32_MIN = - 2 ** 31
UINT32_MAX = - 2 ** 32 - 1

INT16_MAX = 2 ** 15 - 1
INT16_MIN = - 2 ** 15
UINT16_MAX = - 2 ** 16 - 1

# Pandas timestamps can handle nanoseconds? but python datetimestamps cannot.
MAX_TIMESTAMP = pd.Timestamp('2262-04-11 23:47:16.854775', tz='utc')
MIN_TIMESTAMP = pd.Timestamp(datetime.datetime(1677, 9, 22, 0, 12, 44), tz='utc')
ZERO_TIMESTAMP = pd.Timestamp('1970-01-01 00:00:00', tz='utc')

# to_pydatetime() rounds to microseconds, ignoring 807 nanoseconds available in other MAX TIMESTAMPs
MIN_DATETIME = MIN_TIMESTAMP.to_pydatetime()
MAX_DATETIME = MAX_TIMESTAMP.to_pydatetime()
MIN_DATETIME64 = MIN_TIMESTAMP.to_datetime64()
MAX_DATETIME64 = MAX_TIMESTAMP.to_datetime64()
INF = np.inf
NAN = np.nan
NAT = pd.NaT


# str constants
MAX_CHR = MAX_CHAR = chr(127)
APOSTROPHE_CHARS = "'`’"
# Monkey patch so import from constants if you want this:
string.unprintable = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0e\x0f' \
    '\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x7f'
ASCII_UNPRINTABLE_CHRS = string.unprintable  # ''.join(chr(i) for i in range(128) if chr(i) not in string.printable)

NULL_VALUES = set(['0', 'None', 'null', "'", ""] + ['0.' + z for z in ['0' * i for i in range(10)]])
# if datetime's are 'repr'ed before being checked for null values sometime 1899-12-30 will come up
NULL_REPR_VALUES = set(['datetime.datetime(1899, 12, 30)'])
# to allow NULL checks to strip off hour/min/sec from string repr when checking for equality
MAX_NULL_REPR_LEN = max(len(s) for s in NULL_REPR_VALUES)

PERCENT_SYMBOLS = ('percent', 'pct', 'pcnt', 'pt', r'%')
FINANCIAL_WHITESPACE = ('Flat', 'flat', ' ', ',', '"', "'", '\t', '\n', '\r', '$')
FINANCIAL_MAPPING = (('k', '000'), ('M', '000000'))

# qary.constants
#########################################################
