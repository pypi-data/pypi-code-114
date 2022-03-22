import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from abc import ABC
from sklearn import metrics
from dataclasses import dataclass
from typing import Union, Any, Optional
from SnowML.evaluation.evaluation_utils import find_best_threshold


@dataclass
class BaseEvaluator(ABC):
    model: Any
    X_train: Union[pd.Series, np.ndarray]
    X_test: Union[pd.Series, np.ndarray]
    y_train: Union[pd.Series, np.ndarray]
    y_test: Union[pd.Series, np.ndarray]


@dataclass
class ThresholdEvaluator(BaseEvaluator):
    th: Optional[float] = 0.5

    def get_probabilities(self, label_index: int=None, batch_size: int=8):
        """
        Calcualte probabilities for all labels or a single label at 'return_index' in self.X_test
        using 'self.model.predict_proba' .
        :param label_index: The label index to return probabilities for.
        :return: numpy array or n-array for given label(s).
        """


        if type(self.model).__name__ == "Sequential": # If model is a keras sequential model
            return self.model.predict(self.X_test, batch_size=batch_size, verbose=0)

        if label_index is not None:
            return self.model.predict_proba(self.X_test)[:, label_index]

        return self.model.predict_proba(self.X_test)

    def get_predictions(self, by_proba=True, positive_label=1, use_best=True):
        """
        Calculate predictions for instance's test set.
        :param by_proba: when true, predictions will be calculated
        from `self.probabilities` and a threshold. probabilities are calculated from `model.predict_proba' or needed
        to be provided to self.probabilities.
        :param positive_label: The positive label to calculate prediction for.
        Suitable only for binary classification.
        :param use_best: if true, using best threshold (found be
        find_best_threshold) for predictions. Using instance's thereshold otherwise. :return:
        """

        if by_proba:
            self.probabilities = self.get_probabilities(positive_label)

            if use_best:
                fpr, tpr, thresholds = metrics.roc_curve(self.y_test, self.probabilities)
                self.best_threshold = find_best_threshold(fpr, tpr, thresholds)
                self.th = self.best_threshold

            self.predictions = (self.probabilities > self.th).astype(int)
        else:
            self.predictions = self.model.predict(self.X_test)

        return self.predictions

    def _confusion_matrix(self, labels: list):
        """
        Inner function to compute confusion matrix using sklearn's implementation.
        """
        self.cm = pd.DataFrame(metrics.confusion_matrix(self.y_test, self.predictions, labels=labels))

    def _classification_report(self, **kwargs):
        """
        Inner function to compute classification report using sklearn's implementation.
        classification report is saved as dictionary to instance 'cm' and as text to instance 'cr_text'.
        """
        self.cr = metrics.classification_report(self.y_test,
                                                self.predictions,
                                                **kwargs,
                                                output_dict=True)

        self.cr_text = metrics.classification_report(self.y_test,
                                                     self.predictions,
                                                     **kwargs,
                                                     output_dict=False)

    def _classification_metrics(self):
        """
        Inner function to compute individual metrics.
        """

        self.metrics = dict()

        self.metrics['FPR'] = self.cm.iloc[0, 1] / self.cm.sum(axis=1)[0]
        self.metrics['AUC'] = metrics.roc_auc_score(self.y_test, self.probabilities)
        self.metrics['Accuracy'] = metrics.accuracy_score(self.y_test, self.predictions)
        self.metrics['Used Threshold'] = self.th

    def summary_report(self, labels: list) -> str:
        """
        Summarize classification as text report.

        ****************************************************
        Confusion Matrix=
           0  1
        0  6  2
        1  2  0
        Classification Report=
                      precision    recall  f1-score   support

                   0      0.750     0.750     0.750         8
                   1      0.000     0.000     0.000         2

            accuracy                          0.600        10
           macro avg      0.375     0.375     0.375        10
        weighted avg      0.600     0.600     0.600        10

        FPR: 0.25
        AUC: 0.5625
        Accuracy: 0.6
        Used Threshold: 0.63
        ****************************************************
        :param labels: labels to be passed to sklearn functions.
        :return: text report
        """

        self._confusion_matrix(labels)
        self._classification_report(digits=3,
                                    target_names=[str(l) for l in labels])
        self._classification_metrics()

        report = []
        divider = '****************************************************'

        report.append(divider)

        report.append('Confusion Matrix=')
        report.append(self.cm.to_string())

        report.append('Classification Report=')
        report.append(self.cr_text)

        for key, value in self.metrics.items():
            report.append(''.join([key, ': ', str(round(value, 4))]))

        report.append(divider)

        return '\n'.join(report)

    def plot_roc_auc(self):
        label = "{} AUC={:.2f}"

        # Plot test ROC
        plt.figure()
        fpr, tpr, thresholds = metrics.roc_curve(self.y_test, self.probabilities)
        plt.plot(fpr, tpr, label=label.format('test',
                                              metrics.auc(fpr, tpr)
                                              )
                 )

        # Plot train
        probabilities = self.model.predict_proba(self.X_train)[:, 1]
        fpr, tpr, thresholds = metrics.roc_curve(self.y_train, probabilities)
        plt.plot(fpr, tpr, label=label.format('train',
                                              metrics.auc(fpr, tpr)
                                              )
                 )

        plt.plot([0, 1], [0, 1], 'r--', label='random guess')
        plt.title("ROC", fontsize=18)
        plt.legend()
        plt.show()

        rcl_per_disp = metrics.plot_precision_recall_curve(self.model, self.X_test, self.y_test)
        plt.show()

        roc_disp = metrics.plot_roc_curve(self.model, self.X_test, self.y_test)
        plt.cla()
        plt.clf()
        plt.close()
