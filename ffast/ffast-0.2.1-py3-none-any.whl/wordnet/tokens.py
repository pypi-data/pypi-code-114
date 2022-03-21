from typing import List, Generator, Optional
from math import sin,cos

from scipy.stats import gmean, hmean
from scipy.fft import fftn
from numpy import (
    ndarray, concatenate, argmax, array,
    zeros, mean, max, min, sum
)

from ffast.wordnet.token import Token
from ffast.wordnet.utils import (
    WordNet, METAPHONES, VOCABULARY, RANDOM_MATRIX,
    SIZE_WORD_VECTOR, SIZE_SEMANTIC_VECTOR, SIZE_METAPHONES,
)

class Tokens:
    def __init__(self, tokens:List[Token]) -> None:
        self.tokens = tokens
        self.__pointer = -1
        self.ids = list(map(lambda token:token.id,self))
        self.vector = self.__sentence_embedding() if any(tokens) else None

    def __repr__(self) -> str:
        return '\n'.join(map(repr,self.tokens))
    
    def __str__(self) -> str:
        return ' '.join(map(str,self.tokens))

    def __len__(self) -> int:
        return len(self.tokens)

    def __iter__(self) -> "Tokens":
        return self
    
    def __next__(self) -> Token: 
        self.__pointer += 1
        if self.__pointer < len(self):
            return self.tokens[self.__pointer]
        raise StopIteration
    
    def __getitem__(self,index:int) -> Token:
        return self.tokens[index]

    def projection(self) -> Optional[ndarray]:
        if self.vector is None:
            return None
        return RANDOM_MATRIX @ self.vector

    def skip_unknowns(self) -> "Tokens":
        return Tokens(list(filter(lambda token:token.tag != WordNet.UNKNOWN.value,self.tokens)))

    def skip_stopwords(self) -> "Tokens":
        return Tokens(list(filter(lambda token:token.tag != WordNet.STOPWORD.value,self.tokens)))
    
    def nouns(self) -> "Tokens":
        return Tokens(list(filter(lambda token:token.tag == WordNet.POS_NOUN.value, self.tokens)))

    def verbs(self) -> "Tokens":
        return Tokens(list(filter(lambda token:token.tag == WordNet.POS_VERB.value, self.tokens)))

    def entities(self) -> "Tokens":
        return Tokens(list(filter(lambda token:token.tag in (WordNet.POS_VERB.value,WordNet.POS_NOUN.value,WordNet.UNKNOWN.value), self.tokens)))

    def paraphrase(self) -> Generator[str, None, None]:
        for index,token in enumerate(self.tokens):
            for similar_token in token.similar_tokens:
                yield f"{' '.join(map(str,self.tokens[:index]))} {similar_token} {' '.join(map(str,self.tokens[index+1:]))}"
        yield str(self)

    def most_similar(self, others:List["Tokens"]) -> Optional["Tokens"]:
        if self.vector is None:
            return None
        others_with_vectors = filter(lambda other:other.vector is not None,others)
        others_vectors = array(list(map(
            lambda other:other.vector, 
            others_with_vectors
        )))
        index_best = argmax(others_vectors@self.vector)
        return others[index_best]

    def __sentence_embedding(self) -> ndarray:
        sparse_token_vectors = list(map(self.__embed_token,self.tokens))
        position_vectors = list(map(self.__embed_position,range(len(self.tokens))))
        contextual_token_vectors = sum([sparse_token_vectors,position_vectors],axis=0)
        dynamics_of_token_vectors = self.__fourier_transformation(sparse_token_vectors)
        return concatenate([
            self.__power_means(contextual_token_vectors),
            self.__power_means(dynamics_of_token_vectors)
        ])
        
    @staticmethod
    def __power_means(vectors:List[ndarray]) -> ndarray:
        positive_vectors = list(map(abs,vectors))
        return concatenate([
            max(vectors,axis=0),
            min(vectors,axis=0),
            mean(vectors,axis=0),
            gmean(positive_vectors),
            hmean(positive_vectors),
        ])
    
    @staticmethod
    def __fourier_transformation(vectors:List[ndarray]) -> ndarray:
        return abs(fftn(vectors))

    @staticmethod 
    def __embed_position(position:int) -> ndarray:
        position_vector = zeros(SIZE_WORD_VECTOR)
        for index in range(0,SIZE_WORD_VECTOR-1,2):
            angle = position/(1e5 ** ((2*index)/SIZE_WORD_VECTOR))
            position_vector[index]=sin(angle)
            position_vector[index+1]=cos(angle)
        return position_vector

    @staticmethod
    def __embed_token_phonetics(token:Token) -> ndarray:
        embedding = zeros(SIZE_METAPHONES)
        for character in token.phonology:
            metaphone_index = METAPHONES.index(character)
            embedding[metaphone_index] = 1
        return embedding

    @staticmethod
    def __embed_token_semantics(token:Token) -> ndarray:
        embedding = zeros(SIZE_SEMANTIC_VECTOR)
        if token.id > SIZE_SEMANTIC_VECTOR:
            return embedding
        embedding[token.id] = 1
        for name in token.semantics:
            relation_index = VOCABULARY.index(name)
            embedding[relation_index] = 1
        return embedding
        
    @staticmethod
    def __embed_token(token:Token) -> ndarray:
        return concatenate([
            Tokens.__embed_token_phonetics(token),
            Tokens.__embed_token_semantics(token),
        ])    
    