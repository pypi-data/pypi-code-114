# *_*coding:utf-8 *_*

import os
from typing import Dict, Any

from langma.embeddings.transformer_embedding import TransformerEmbedding


class BertEmbedding(TransformerEmbedding):
    """
    BertEmbedding is a simple wrapped class of TransformerEmbedding.
    If you need load other kind of transformer based language model, please use the TransformerEmbedding.
    """
    def to_dict(self) -> Dict[str, Any]:
        info_dic = super(BertEmbedding, self).to_dict()
        info_dic['config']['model_folder'] = self.model_folder
        return info_dic

    def __init__(self, model_folder: str,
                 vocab_name='vocab.txt', config_name='bert_config.json',
                 **kwargs: Any):
        """

        Args:
            model_folder: path of checkpoint folder.
            kwargs: additional params
        """
        self.model_folder = model_folder
        vocab_path = os.path.join(self.model_folder, vocab_name)
        config_path = os.path.join(self.model_folder, config_name)
        checkpoint_path = os.path.join(self.model_folder, 'bert_model.ckpt')
        kwargs['vocab_path'] = vocab_path
        kwargs['config_path'] = config_path
        kwargs['checkpoint_path'] = checkpoint_path
        kwargs['model_type'] = 'bert'
        super(BertEmbedding, self).__init__(**kwargs)


if __name__ == "__main__":
    pass
