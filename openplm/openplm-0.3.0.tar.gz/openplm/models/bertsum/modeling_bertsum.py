"""PyTorch BertSum model. """
import math
import os
import warnings
from dataclasses import dataclass
from typing import Optional, Tuple

import torch
import torch.utils.checkpoint
from torch import nn
from torch.nn import BCEWithLogitsLoss, CrossEntropyLoss, MSELoss
from packaging import version

from transformers.models.bert.modeling_bert import (
    BertPreTrainedModel,
    BertModel,
    TokenClassifierOutput
)
from ..modeling_outputs import ExtractiveSummaryOutput
from .configuration_bertsum import BertSumConfig


def gelu(x):
    return 0.5 * x * (1 + torch.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))


class PositionwiseFeedForward(nn.Module):

    def __init__(
        self,
        hidden_size,
        feedforward_size,
        dropout=0.1
    ):
        super().__init__()
        self.w1 = nn.Linear(hidden_size, feedforward_size)
        self.w2 = nn.Linear(feedforward_size, hidden_size)
        self.layer_norm = nn.LayerNorm(hidden_size, eps=1e-6)
        self.active_func = gelu
        self.dropout_1 = nn.Dropout(dropout)
        self.dropout_2 = nn.Dropout(dropout)

    def forward(
        self,
        input_hidden_states  # batch_size x sents_num x hidden_size
    ):
        output_hidden_states = self.dropout_1(self.active_func(self.w1(self.layer_norm(hidde_states))))
        output_hidden_states = self.dropout_2(self.w2(output_hidden_states))
        return output_hidden_states + input_hidden_states


class MultiHeadedAttention(nn.Module):

    def __init__(
        self,
        head_num,
        hidden_size,
        dropout=0.1,
        use_final_linear=True
    ):
        super().__init__()
        assert hidden_size % head_num == 0, ValueError("hidden_size must be a multiple of head_num.")
        self.hidden_size = hidden_size
        self.size_per_head = hidden_size // head_num
        self.head_num = head_num

        self.K = nn.Linear(hidden_size, hidden_size)
        self.Q = nn.Linear(hidden_size, hidden_size)
        self.V = nn.Linear(hidden_size, hidden_size)

        self.softmax = nn.Softmax(dim=-1)
        self.dropout = nn.Dropout(dropout)

        self.use_final_linear = use_final_linear
        if use_final_linear:
            self.final_linear = nn.Linear(hidden_size, hidden_size)

    def forward(self, key, query, value, mask):
        batch_size = key.size(0)
        key_len = key.size(1)
        query_len = query.size(1)

        def shape(x):
            """  projection """
            return x.view(batch_size, -1, self.head_num, self.size_per_head) \
                .transpose(1, 2)

        def unshape(x):
            """  compute context """
            return x.transpose(1, 2).contiguous() \
                .view(batch_size, -1, self.head_num * self.size_per_head)

        key = self.K(key)
        query = self.Q(query)
        value = self.V(value)

        key = shape(key)
        value = shape(value)
        query = shape(query)

        query = query / math.sqrt(self.size_per_head)
        scores = torch.matmul(query, key.transpose(2, 3))

        if mask is not None:
            mask = mask.unsqueeze(1).expand_as(scores)
            scores = scores.masked_fill(mask, -1e18)

        attn = self.softmax(scores)
        drop_attn = self.dropout(attn)
        output = unshape(torch.matmul(drop_attn, value))

        if self.use_final_linear:
            output = self.final_linear(output)
        return output


class TransformerBlock(nn.Module):

    def __init__(
        self,
        hidden_size,
        head_num,
        feedforward_size,
        dropout
    ):
        super().__init__()
        self.self_attn = MultiHeadedAttention(head_num, hidden_size, dropout=dropout)
        self.feedforward = PositionwiseFeedForward(hidden_size, feedforward_size, dropout=dropout)
        self.layer_norm = nn.LayerNorm(hidden_size, eps=1e-6)
        self.dropout = nn.Dropout(dropout)

    def forward(self, iter, hidden_states, mask):
        if iter != 0:
            hidden_states_norm = self.layer_norm(hidden_states)
        else:
            hidden_states_norm = hidden_states

        mask = mask.unsqueeze(1)
        output = self.self_attn(hidden_states_norm, hidden_states_norm, hidden_states_norm, mask=mask)
        output = self.dropout(output) + hidden_states
        return output


class PositionalEncoding(nn.Module):

    def __init__(self, dropout, dim, max_len=5000):
        pe = torch.zeros(max_len, dim)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp((torch.arange(0, dim, 2, dtype=torch.float) * -(math.log(10000.0) / dim)))
        pe[:, 0::2] = torch.sin(position.float() * div_term)
        pe[:, 1::2] = torch.cos(position.float() * div_term)
        pe = pe.unsqueeze(0)
        super(PositionalEncoding, self).__init__()
        self.register_buffer('pe', pe)
        self.dropout = nn.Dropout(p=dropout)
        self.dim = dim

    def forward(self, emb, step=None):
        emb = emb * math.sqrt(self.dim)
        if (step):
            emb = emb + self.pe[:, step][:, None, :]

        else:
            emb = emb + self.pe[:, :emb.size(1)]
        emb = self.dropout(emb)
        return emb

    def get_emb(self, emb):
        return self.pe[:, :emb.size(1)]


class ExrTransformer(nn.Module):

    def __init__(
        self,
        hidden_size,
        feedforward_size,
        head_num,
        dropout,
        num_inter_layers
    ):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_inter_layers = num_inter_layers
        self.pos_emb = PositionalEncoding(dropout, hidden_size)
        self.transformers = nn.ModuleList([TransformerBlock(hidden_size, head_num, feedforward_size, dropout) for _ in range(num_inter_layers)])
        self.dropout = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(hidden_size, eps=1e-6)
        self.wo = nn.Linear(hidden_size, 1, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(
        self,
        hidden_states,  # batch_size x sents_num x hidden_size
        mask_cls
    ):
        batch_size, sents_num = hidden_states.size(0), hidden_states.size(1)
        pos_emb = self.pos_emb.pe[:, :sents_num]

        hidden_states = hidden_states * mask_cls[:, :, None].float()
        hidden_states = hidden_states + pos_emb

        for i in range(self.num_inter_layers):
            hidden_states = self.transformers[i](i, hidden_states, torch.logical_not(mask_cls))

        hidden_states = self.layer_norm(hidden_states)
        sent_scores = self.sigmoid(self.wo(hidden_states))
        sent_scores = sent_scores.squeeze(-1) * mask_cls.float()
        return sent_scores


class Classifier(nn.Module):

    def __init__(
        self,
        hidden_size
    ):
        super(Classifier, self).__init__()
        self.linear1 = nn.Linear(hidden_size, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(
        self,
        hidden_states,  # batch_size x sents_num x hidden_size
        mask_cls
    ):
        h = self.linear1(hidden_states).squeeze(-1)
        sent_scores = self.sigmoid(h) * mask_cls.float()
        return sent_scores


class BertSum(BertPreTrainedModel):

    config_class = BertSumConfig
    _keys_to_ignore_on_load_unexpected = [r"pooler"]

    def __init__(self, config):
        super().__init__(config)


class BertSumForExt(BertSum):

    def __init__(self, config):
        super().__init__(config)

        self.bert = BertModel(config, add_pooling_layer=False)
        self.dropout = nn.Dropout(config.ext_dropout)

        if config.ext_layer_type == 'classifier':
            self.ext_layer = Classifier(config.hidden_size)
        elif config.ext_layer_type == 'transformer':
            self.ext_layer = ExrTransformer(config.hidden_size, config.ext_feedforward_size, config.ext_heads, config.ext_dropout, config.ext_layers)
        else:
            raise ValueError(f"Unknown ext_layer_type = {config.ext_layer_type}")

        try:
            self.post_init()  # transformers <= 4.9.2
        except:
            self.init_weights()

        self.loss = nn.BCELoss()
        self.loss.ignore_idx = -100

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        special_tokens_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        batch_size = len(input_ids)
        device = input_ids.device

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
        sequence_output = outputs[0]

        # Obtain the [CLS] position idx and mask through special_tokens_mask
        cls_pos, cls_mask = self._get_cls_position(special_tokens_mask, device)
        max_sents_num = cls_mask.size()[1]

        sequence_output = self.dropout(sequence_output)  # batch_size x seq_length x hidden_size
        sequence_output = sequence_output[torch.arange(batch_size).unsqueeze(1), cls_pos, :]  # batch_size x max_sents_num x hidden_size
        logits = self.ext_layer(sequence_output, cls_mask)  # batch_size x max_sents_num

        # calculate loss
        if labels is not None:
            labels_pt = self._pad_list_to_tensor(labels, device=device, pad_id=self.loss.ignore_idx)  # batch_size x max_sents_num
            labels_pt = labels_pt[:, :max_sents_num]
            # assert torch.all(cls_mask.eq(labels_pt != self.loss.ignore_idx)), "The number of sentences is not equal to the number of labels."
            active_labels = labels_pt[torch.nonzero(cls_mask, as_tuple=True)].to(dtype=torch.float, device=device)
            active_logits = logits[torch.nonzero(cls_mask, as_tuple=True)]
            loss_value = self.loss(active_logits, active_labels)
        else:
            loss_value = None

        if not return_dict:
            raise ValueError("return_dict must be False.")

        return ExtractiveSummaryOutput(
            loss=loss_value,
            cls_mask=cls_mask,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

    def _get_cls_position(self, cls_tokens_mask, device):
        batch_size = cls_tokens_mask.size()[0]
        cls_pos_tmp = torch.nonzero(cls_tokens_mask == 1, as_tuple=False)
        cls_pos = [[] for _ in range(batch_size)]
        for p in cls_pos_tmp:
            cls_pos[p[0]].append(p[1])
        cls_pos = self._pad_list_to_tensor(cls_pos, device, pad_id=-1)  # batch_size x max_sents_num
        cls_mask = cls_pos != -1
        return cls_pos, cls_mask

    def _pad_list_to_tensor(self, data, device, pad_id=-100):
        # data is a list of list, e.g., [[0,1,0],[0,1]]
        if isinstance(data, torch.Tensor):
            return data
        width = max([len(s) for s in data])
        hight = len(data)
        data_pad = [d + [pad_id] * (width - len(d)) for d in data]
        data_pad = torch.tensor(data_pad, device=device)
        return data_pad

    def change_max_position(self, tgt_max_pos: int):
        src_max_pos = self.bert.config.max_position_embeddings
        hidden_size = self.bert.config.hidden_size
        ext_pos_embeddings = nn.Embedding(tgt_max_pos, hidden_size)
        if tgt_max_pos > src_max_pos:
            ext_pos_embeddings.weight.data[:src_max_pos] = self.bert.embeddings.position_embeddings.weight.data
            ext_pos_embeddings.weight.data[src_max_pos:] = self.bert.embeddings.position_embeddings.weight.data[-1][None,:].repeat(tgt_max_pos - src_max_pos, 1)
        else:
            ext_pos_embeddings.weight.data =  self.bert.embeddings.position_embeddings.weight.data[:tgt_max_pos]
        self.bert.embeddings.position_embeddings = ext_pos_embeddings
        self.config.max_position_embeddings = tgt_max_pos
        self.bert.config.max_position_embeddings = tgt_max_pos
        self.bert.embeddings.position_ids = torch.arange(tgt_max_pos).expand((1, -1))
        return None


