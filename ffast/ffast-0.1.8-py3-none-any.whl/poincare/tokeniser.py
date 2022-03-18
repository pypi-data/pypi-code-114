from typing import List, Generator

from nltk.util import ngrams
from numpy import zeros

from ffast.poincare.token import Token
from ffast.poincare.tokens import Tokens
from ffast.poincare.utils import Poincare, PREPROCESSOR, VOCABULARY, VECTORS

class Tokeniser:
    @staticmethod
    def encode(text:str) -> Tokens:
        return Tokens(Tokeniser._tokenise(text))
    
    @staticmethod
    def decode(ids:List[int]) -> Tokens:
        return Tokens(list(Tokeniser._convert_ids_to_tokens(ids)))

    @staticmethod
    def _tokenise(text:str) -> List[Token]:
        words = text.split()
        number_of_words = len(words)
        tokens = [None]*number_of_words
        for ngram_size in range(number_of_words+1,0,-1):
            for index_start,ngram in enumerate(ngrams(words,ngram_size)):
                index_end = index_start + ngram_size
                if any(tokens[index_start:index_end]):
                    continue 
                raw_token = ' '.join(words[index_start:index_end])
                normalised_token = PREPROCESSOR.normalise(text=' '.join(ngram))
                if normalised_token in VOCABULARY:
                    id = VOCABULARY.index(normalised_token)
                    vector = VECTORS[id]
                elif raw_token in VOCABULARY:
                    id = VOCABULARY.index(raw_token)
                    vector = VECTORS[id]
                else:
                    id = Poincare.SIZE_VOCABULARY.value+1
                    vector = zeros(Poincare.SIZE_VECTOR.value)
                    normalised_token = Poincare.UNKNOWN.value
                if id <= Poincare.SIZE_VOCABULARY.value or ngram_size==1:
                    tokens[index_start:index_end] = [Poincare.SKIP.value]*ngram_size
                    tokens[index_start] = Token(
                        raw_token=raw_token,
                        normalised_token=normalised_token,
                        vector = vector,
                        id = id
                    )
        return list(filter(lambda token:isinstance(token,Token),tokens))

    @staticmethod
    def _convert_ids_to_tokens(ids:List[int]) -> Generator[Token,None,None]:
        for id in ids:
            if id < Poincare.SIZE_VOCABULARY.value:
                token = VOCABULARY[id]
                vector = VECTORS[id]
            else:
                token = Poincare.UNKNOWN.value
                vector= zeros(Poincare.SIZE_VECTOR.value)
            yield Token(
                raw_token=token,
                normalised_token=token,
                vector = vector,
                id = id
            )