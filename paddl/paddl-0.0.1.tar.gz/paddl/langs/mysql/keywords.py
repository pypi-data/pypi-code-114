# https://pyparsing-docs.readthedocs.io/en/latest/HowToUsePyparsing.html#hello-world
from pyparsing import Keyword, OneOrMore, Optional, Group

CREATE = Keyword('CREATE')
TEMPORARY = Optional(Keyword('TEMPORARY')('temporary'))
TABLE = Keyword('TABLE')
IF_NOT_EXISTS = Optional(Keyword('IF NOT EXISTS')('if_not_exists'))


# extract to util
def wrap(word, many=False):
    if many:
        word = OneOrMore(word)
    return word


_ = wrap
