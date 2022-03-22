from torch import nn

from .mmoe import MMoE
from .bottom import TPlusT, TxT


class MultiTaskTPlustT(nn.Module):
    def __init__(self, ctx_nums, seq_num, expert_num, expert_hidden_sizes,
                 task_num, task_hidden_sizes, task_last_activations,
                 ctx_cross_size=100, seq_cross_size=200, is_candidate_mode=True,
                 context_transformer_kwargs=None, sequence_transformer_kwargs=None):
        super().__init__()
        self.is_candidate_mode = is_candidate_mode
        self.shared_bottom = TPlusT(
            ctx_nums=ctx_nums,
            seq_num=seq_num,
            ctx_cross_size=ctx_cross_size,
            seq_cross_size=seq_cross_size,
            is_candidate_mode=is_candidate_mode,
            context_transformer_kwargs=context_transformer_kwargs,
            sequence_transformer_kwargs=sequence_transformer_kwargs,
        )
        mmoe_input_size = ctx_cross_size + seq_cross_size + self.shared_bottom.sequence_transformer.seq_embed_size
        self.mmoe = MMoE(
            input_size=mmoe_input_size,
            expert_num=expert_num,
            expert_hidden_sizes=expert_hidden_sizes,
            task_num=task_num,
            task_hidden_sizes=task_hidden_sizes,
            task_last_activations=task_last_activations,
        )

    def forward(self, ctx_in, seq_in, vl_in, candidate_in, seq_history=None):
        bottom_features = self.shared_bottom(ctx_in, seq_in, vl_in, candidate_in, seq_history)
        outs = self.mmoe(bottom_features)
        return outs


class MultiTaskTxT(nn.Module):
    def __init__(self, ctx_nums, seq_num, expert_num, expert_hidden_sizes,
                 task_num, task_hidden_sizes, task_last_activations,
                 cross_size=200, is_candidate_mode=True,
                 context_transformer_kwargs=None, sequence_transformer_kwargs=None):
        super().__init__()
        self.is_candidate_mode = is_candidate_mode
        self.shared_bottom = TxT(
            ctx_nums=ctx_nums,
            seq_num=seq_num,
            cross_size=cross_size,
            is_candidate_mode=is_candidate_mode,
            context_transformer_kwargs=context_transformer_kwargs,
            sequence_transformer_kwargs=sequence_transformer_kwargs,
        )
        mmoe_input_size = cross_size + self.shared_bottom.sequence_transformer.seq_embed_size
        self.mmoe = MMoE(
            input_size=mmoe_input_size,
            expert_num=expert_num,
            expert_hidden_sizes=expert_hidden_sizes,
            task_num=task_num,
            task_hidden_sizes=task_hidden_sizes,
            task_last_activations=task_last_activations,
        )

    def forward(self, ctx_in, seq_in, vl_in, candidate_in, seq_history=None):
        bottom_features = self.shared_bottom(ctx_in, seq_in, vl_in, candidate_in, seq_history)
        outs = self.mmoe(bottom_features)
        return outs
