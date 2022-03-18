# coding=utf-8
"""Tokenization classes for BertSum."""


import collections
import os
import unicodedata
import copy
from typing import TYPE_CHECKING, Any, Dict, List, NamedTuple, Optional, Sequence, Tuple, Union

from transformers.tokenization_utils_base import (
    TextInput,
    PreTokenizedInput,
    PaddingStrategy,
    TruncationStrategy,
    TensorType,
    BatchEncoding
)
from transformers.models.bert.tokenization_bert import BertTokenizer
from transformers.utils import logging


class BertSumTokenizer(BertTokenizer):

    def __init__(
        self,
        vocab_file,
        do_lower_case=False,
        do_basic_tokenize=True,
        never_split=None,
        unk_token="[UNK]",
        sep_token="[SEP]",
        pad_token="[PAD]",
        cls_token="[CLS]",
        mask_token="[MASK]",
        tokenize_chinese_chars=True,
        strip_accents=None,
        **kwargs
    ):

        super().__init__(
            vocab_file=vocab_file,
            do_lower_case=do_lower_case,
            do_basic_tokenize=do_basic_tokenize,
            never_split=never_split,
            unk_token=unk_token,
            sep_token=sep_token,
            pad_token=pad_token,
            cls_token=cls_token,
            mask_token=mask_token,
            tokenize_chinese_chars=tokenize_chinese_chars,
            strip_accents=strip_accents,
            **kwargs
        )

    def __call__(
        self,
        text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]],
        text_pair: Optional[Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]]] = None,
        add_special_tokens: bool = True,
        padding: Union[bool, str, PaddingStrategy] = False,
        truncation: Union[bool, str, TruncationStrategy] = False,
        max_length: Optional[int] = None,
        stride: int = 0,
        is_split_into_words: bool = False,
        pad_to_multiple_of: Optional[int] = None,
        return_tensors: Optional[Union[str, TensorType]] = 'pt',
        return_token_type_ids: Optional[bool] = None,
        return_attention_mask: Optional[bool] = None,
        return_overflowing_tokens: bool = False,
        return_special_tokens_mask: bool = True,
        return_offsets_mapping: bool = False,
        return_length: bool = False,
        verbose: bool = True,
        **kwargs
    ) -> BatchEncoding:

        text = copy.deepcopy(text)
        assert return_tensors == 'pt', ValueError('return_tensors must be pt')
        assert return_special_tokens_mask, ValueError('return_special_tokens_mask must be True')

        if text_pair is not None:
            raise ValueError("BertSumTokenizer only support one text input.")

        if not isinstance(text, list):
            text = [text]

        for i in range(len(text)):
            text[i] = text[i].replace('\n', ' {} '.format(self.sep_token))

        outputs =  super().__call__(
            text,
            text_pair,
            add_special_tokens,
            padding,
            truncation,
            max_length,
            stride,
            is_split_into_words,
            pad_to_multiple_of,
            return_tensors,
            return_token_type_ids,
            return_attention_mask,
            return_overflowing_tokens,
            return_special_tokens_mask,
            return_offsets_mapping,
            return_length,
            verbose,
            **kwargs
        )

        if 'special_tokens_mask' in outputs:
            outputs['special_tokens_mask'] *= outputs['attention_mask']  # keep only the [CLS] token.

        outputs['input_ids'] = outputs['input_ids'][:, :max_length]
        outputs['token_type_ids'] = outputs['token_type_ids'][:, :max_length]
        outputs['special_tokens_mask'] = outputs['special_tokens_mask'][:, :max_length]
        outputs['attention_mask'] = outputs['attention_mask'][:, :max_length]

        return outputs

    def _tokenize(self, text, **kwargs):
        """
        Converts a string in a sequence of tokens (string), using the tokenizer. Split in words for word-based
        vocabulary or sub-words for sub-word-based vocabularies (BPE/SentencePieces/WordPieces).
        Do NOT take care of added tokens.
        """
        split_tokens = []
        if self.do_basic_tokenize:
            for token in self.basic_tokenizer.tokenize(text, never_split=self.all_special_tokens):

                # If the token is part of the never_split set
                if token in self.basic_tokenizer.never_split:
                    split_tokens.append(token)
                else:
                    split_tokens += self.wordpiece_tokenizer.tokenize(token)
        else:
            split_tokens = self.wordpiece_tokenizer.tokenize(text)
        return split_tokens

    def build_inputs_with_special_tokens(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        """
        Build model inputs from a sequence for sequence classification tasks by concatenating and
        adding special tokens. A BERTSUM sequence has the following format:
        - single sequence: ``[CLS] A [SEP] [CLS] B [SEP] [CLS] C [SEP]``
        Args:
            token_ids_0 (:obj:`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (:obj:`List[int]`, `optional`):
                Must be None.
        Returns:
            :obj:`List[int]`: List of `input IDs <../glossary.html#input-ids>`__ with the appropriate special tokens.
        """
        new_token_ids = []
        for i, tid in enumerate(token_ids_0):
            if tid == self.sep_token_id:
                new_token_ids.append(tid)
                new_token_ids.append(self.cls_token_id)
            elif i == len(token_ids_0) - 1 and tid != self.sep_token_id:
                new_token_ids.append(self.sep_token_id)
                new_token_ids.append(self.cls_token_id)
            else:
                new_token_ids.append(tid)

        new_token_ids = [self.cls_token_id] + new_token_ids[:-1]
        return new_token_ids

    def get_special_tokens_mask(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None, already_has_special_tokens: bool = False
    ) -> List[int]:
        """
        Get the [CLS] token position.
        Args:
            token_ids_0 (:obj:`List[int]`):
                List of IDs.
            token_ids_1 (:obj:`List[int]`, `optional`):
                Must be None.
            already_has_special_tokens (:obj:`bool`, `optional`, defaults to :obj:`False`):
                Whether or not the token list is already formatted with special tokens for the model.
        Returns:
            :obj:`List[int]`: A list of integers in the range [0, 1]: 1 for a [CLS] token, 0 for a other token.
        """

        special_token_mask = []
        for i, tid in enumerate(token_ids_0):
            if tid == self.sep_token_id:
                special_token_mask.append(0)
                special_token_mask.append(1)
            elif i == len(token_ids_0) - 1 and tid != self.sep_token_id:
                special_token_mask.append(0)
                special_token_mask.append(1)
            else:
                special_token_mask.append(0)
        special_token_mask = [1] + special_token_mask[:-1]
        return special_token_mask

    def create_token_type_ids_from_sequences(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A BERT sequence
        pair mask has the following format:
        ::
            0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
            | first sequence    | second sequence |  third qequence |
        If :obj:`token_ids_1` is :obj:`None`, this method only returns the first portion of the mask (0s).
        Args:
            token_ids_0 (:obj:`List[int]`):
                List of IDs.
            token_ids_1 (:obj:`List[int]`, `optional`):
                Must be None.
        Returns:
            :obj:`List[int]`: List of `token type IDs <../glossary.html#token-type-ids>`_ according to the given
            sequence(s).
        """
        token_type_ids = []
        token_id = 0
        for i, tid in enumerate(token_ids_0):
            if tid == self.sep_token_id:
                token_type_ids.append(token_id)
                token_id = (token_id + 1) % 2
                token_type_ids.append(token_id)
            elif i == len(token_ids_0) - 1 and tid != self.sep_token_id:
                token_type_ids.append(token_id)
                token_type_ids.append(token_id)
            else:
                token_type_ids.append(token_id)
        token_type_ids = [0] + token_type_ids[:-1]
        return token_type_ids

