from .losses import AUCMLoss
from .losses import APLoss
from .losses import CompositionalLoss
from .losses import CrossEntropyLoss
from .losses import FocalLoss
from .losses import AUCM_MultiLabel

# Experiments
from .losses import AUCMLoss_V1, AUCMLoss_V2


# alias name
AUCLoss = AUCMLoss
SOAPLoss = APLoss
CompositionalAUCLoss = CompositionalLoss
