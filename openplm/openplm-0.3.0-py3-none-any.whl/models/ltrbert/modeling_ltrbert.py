"""
LTR-BERT

@author: weijie liu
@ref:
    1. Learning-to-rank with BERT in TF-RANKING
    2. https://github.com/tensorflow/ranking/blob/master/tensorflow_ranking/python/losses_impl.py

"""
from dataclasses import dataclass
from typing import Optional, Tuple, List

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.distributed as dist

import transformers
from transformers.models.roberta.modeling_roberta import RobertaPreTrainedModel, RobertaModel
from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertModel
from transformers.file_utils import ModelOutput


@dataclass
class RankOutput(ModelOutput):

    loss: Optional[torch.FloatTensor] = None
    logits: torch.FloatTensor = None
    scores: torch.FloatTensor = None
    hidden_states: Optional[Tuple[torch.FloatTensor]] = None
    attentions: Optional[Tuple[torch.FloatTensor]] = None


class RankLoss(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self,
                logits,
                labels,
                temperature=None,
                margin=None
    ):
        raise NotImplementedError()


class PointwiseCrossEntropyLoss(RankLoss):

    def __init__(self):
        super().__init__()
        self.loss = nn.BCELoss()

    def forward(self,
                logits,
                labels,
                temperature=None,
                margin=None
    ):
        """
        logits: Tensor, (batch_size, list_size), after sigmoid
        labels: Tensor, (batch_size, list_size), 0 or 1
        """
        logits = logits.view((-1, ))
        labels = labels.view((-1, ))
        loss = self.loss(logits, labels)
        return loss


class PairwiseLoss(RankLoss):

    def forward(self,
                logits,
                labels,
                temperature=1.0,
                margin=0
    ):
        """
        logits: Tensor, (batch_size, list_size), after sigmoid
        labels: Tensor, (batch_size, list_size), 0 or 1
        """
        logits = logits / temperature
        pairwise_labels, pairwise_logits = self._pairwise_comparison(labels, logits)
        pairwise_weights = pairwise_labels
        pairwise_logits = pairwise_logits + margin
        pairwise_loss = self._pairwise_loss(pairwise_logits)
        loss = torch.sum(pairwise_loss * pairwise_weights) / torch.sum(pairwise_weights)
        return loss

    def _pairwise_comparison(self, labels, logits):
        """
        Args:
            labels: A `Tensor` with shape [batch_size, list_size].
            logits: A `Tensor` with shape [batch_size, list_size].
        Returns:
            A tuple of (pairwise_labels, pairwise_logits) with each having the shape
            [batch_size, list_size, list_size].
                                /
                                | 1   if l_i > l_j for valid l_i and l_j.
            * `pairwise_labels` = |
                                | 0   otherwise
                                \
            * `pairwise_logits` = pairwise_logits_op(s_i, s_j)
        """
        batch_size = labels.size(0)
        list_size = labels.size(1)

        labels_extend = labels.unsqueeze(1).repeat(1, list_size, 1)  # batch_size x list_size x list_size
        pairwise_labels = (labels_extend.transpose(1, 2) > labels_extend).type(torch.float32)

        logits_extend = logits.unsqueeze(1).repeat(1, list_size, 1)
        pairwise_logits = logits_extend.transpose(1, 2) - logits_extend

        return pairwise_labels, pairwise_logits


class PairwiseLogisticLoss(PairwiseLoss):

    def _pairwise_loss(self, pairwise_logits):
        # The following is the same as log(1 + exp(-pairwise_logits)).
        return torch.relu(-pairwise_logits) + torch.log1p(torch.exp(-torch.abs(pairwise_logits)))


class PairwiseHingeLoss(PairwiseLoss):

    def _pairwise_loss(self, pairwise_logits):
        return torch.relu(1 - pairwise_logits)


class BertForRank(BertPreTrainedModel):

    def __init__(self,
                 config
    ):
        super().__init__(config)
        self.config = config

        self.bert = BertModel(config)
        self.ranker = nn.Linear(config.hidden_size, 1)

        self.support_loss_types = {
            'point-wise/CrossEntropy': PointwiseCrossEntropyLoss(),
            'pair-wise/Logistic': PairwiseLogisticLoss(),
            'pair-wise/Hinge': PairwiseHingeLoss(),
            'list-wise/None': None
        }

        try:
            self.init_weights()
        except:
            self.post_init()

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
        loss_type='point-wise/CrossEntropy',
        loss_temperature=1.0,
        loss_margin=0,
    ):
        """
        input_ids: Tensor, batch_size x list_size x seq_length
        labels   : Tensor, batch_size x list_size
        """
        assert len(input_ids.size()) == 3, "input_ids must be in size of (batch_size, list_size, seq_length)."
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        batch_size = input_ids.size(0)
        list_size = input_ids.size(1)
        seq_length = input_ids.size(2)

        assert loss_type in self.support_loss_types.keys(), f"loss_type must be in {self.support_loss_types.keys()}."
        if loss_type.startswith('pair-wise') or loss_type.startswith('list-wise'):
            assert list_size >= 2, "For pair/list-wise loss, the list_size must greater than 2."

        # Flatten input for encoding
        input_ids = input_ids.view((-1, input_ids.size(-1))) # (batch_size * list_size, seq_length)
        attention_mask = attention_mask.view((-1, attention_mask.size(-1)))
        if token_type_ids is not None:
            token_type_ids = token_type_ids.view((-1, token_type_ids.size(-1)))

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        pooler_output = outputs.pooler_output  # (batch_size * list_size, hidden_size)
        logits = self.ranker(pooler_output)  # (batch_size * list_size, )
        logits = logits.view((batch_size, list_size))  # (batch_size, list_size)
        rank_score = torch.sigmoid(logits)

        loss = None
        if labels is not None:
            loss = self.support_loss_types[loss_type](
                rank_score,
                labels,
                temperature=loss_temperature,
                margin=loss_margin
            )

        return RankOutput(
            loss=loss,
            scores=rank_score,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions
        )




