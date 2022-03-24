import enum


class Algorithms(enum.Enum):
    ADABOOST = "ADABOOST"
    BGG = "BGG"
    CATBOOST = "CATBOOST"
    DECISION_TREE = "DECISION_TREE"
    EXTRA_TREE = "EXTRA_TREE"
    GBM = "GBM"
    KNN = "KNN"
    LINEAR_SVM = "LINEAR_SVM"
    LR = "LR"
    LGBM = "LGBM"
    NB = "NB"
    NN = "NN"
    POLY_SVM = "POLY_SVM"
    RANDOM_FOREST = "RANDOM_FOREST"
    SVM = "SVM"
    XGBOOST = "XGBOOST"


class Metrics(enum.Enum):
    ACC = "ACC"
    AUC = "AUC"
    BALANCED_ACC = "BALANCED_ACC"
    F1 = "F1"
    MAE = "MAE"
    MSE = "MSE"
    PRECISION = "PRECISION"
    RECALL = "RECALL"
    RMSE = "RMSE"
    ROC_AUC = "ROC_AUC"
