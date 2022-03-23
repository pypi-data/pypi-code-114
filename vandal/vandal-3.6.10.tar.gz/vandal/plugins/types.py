from typing import Dict, List, Union

vandalType = 'Input / Output Type.'

# simple types.
NumberVector: vandalType = List[float] # one-dimensional vector of integers or floats.
StringVector: vandalType = List[str] # one-dimensional vector of strings.
StringDictionary: vandalType = Dict[str, str] # one-dimensional 'str' : 'str' dictionary vector.
DictionaryVector: vandalType = Dict[str, NumberVector] # one-dimensional 'str' : 'NumberVector' dictionary.

#complex types.
NumberVectorType: vandalType = Union[NumberVector, DictionaryVector] # only number-supported list/vector of values.
NumberArrayType: vandalType = Union[List[NumberVector], List[DictionaryVector]] # array of numerical values only.
AnyArrayType: vandalType = Union[List[NumberVector], List[StringVector], List[StringDictionary], List[DictionaryVector]] # any =>2 dimensional type.
AnyVectorType: vandalType = Union[NumberVector, StringVector, StringDictionary, DictionaryVector] # any one-dimensional type.
