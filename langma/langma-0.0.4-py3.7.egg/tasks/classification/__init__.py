# *_*coding:utf-8 *_*

from .abc_model import ABCClassificationModel
from .bi_gru_model import BiGRU_Model
from .bi_lstm_model import BiLSTM_Model
from .cnn_attention_model import CNN_Attention_Model
from .cnn_gru_model import CNN_GRU_Model
from .cnn_lstm_model import CNN_LSTM_Model
from .cnn_model import CNN_Model

ALL_MODELS = [
    BiGRU_Model, BiLSTM_Model, CNN_Attention_Model, CNN_GRU_Model,
    CNN_LSTM_Model, CNN_Model
]
