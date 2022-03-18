# coding: utf-8
from dataclasses import dataclass
from typing import Optional, Tuple, List

import torch

from transformers.file_utils import ModelOutput


@dataclass
class ExtractiveSummaryOutput(ModelOutput):
    """
    Base class for outputs of Extractive summary models.
    """

    loss: Optional[torch.FloatTensor] = None
    cls_mask: torch.IntTensor = None
    logits: torch.FloatTensor = None
    hidden_states: Optional[Tuple[torch.FloatTensor]] = None
    attentions: Optional[Tuple[torch.FloatTensor]] = None


@dataclass
class SimCSEOutput(ModelOutput):
    """
    Base class for outputs of Extractive summary models.
    """

    loss: Optional[torch.FloatTensor] = None
    cl_loss: Optional[torch.FloatTensor] = None
    mlm_loss: Optional[torch.FloatTensor] = None
    logits: torch.FloatTensor = None
    hidden_states: Optional[Tuple[torch.FloatTensor]] = None
    attentions: Optional[Tuple[torch.FloatTensor]] = None
