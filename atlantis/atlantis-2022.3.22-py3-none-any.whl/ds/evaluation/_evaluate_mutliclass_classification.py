from sklearn.metrics import confusion_matrix
import numpy as np
from pandas import DataFrame


def _evaluate_multiclass_classification(confusion_matrix, classes):
	metrics = {}
	metrics['false_positives'] = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)
	metrics['false_negatives'] = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
	metrics['true_positives'] = np.diag(confusion_matrix)
	metrics['true_negatives'] = confusion_matrix.sum() - (
				metrics['false_positives'] + metrics['false_negatives'] + metrics['true_positives'])
	FP = metrics['false_positives'].astype(float)
	FN = metrics['false_negatives'].astype(float)
	TP = metrics['true_positives'].astype(float)
	TN = metrics['true_negatives'].astype(float)

	# Precision or positive predictive value
	metrics['precision'] = TP / (TP + FP)
	# Sensitivity, hit rate, recall, or true positive rate

	metrics['recall'] = TP / (TP + FN)
	# Specificity or true negative rate

	metrics['specificity'] = TN / (TN + FP)

	# Negative predictive value
	metrics['negative_predictive_value'] = TN / (TN + FN)

	# Fall out or false positive rate
	metrics['false_positive_rate'] = FP / (FP + TN)

	# False negative rate
	metrics['false_negative_rate'] = FN / (TP + FN)

	# False discovery rate
	metrics['false_discovery_rate'] = FP / (TP + FP)

	# Overall accuracy for each class
	metrics['accuracy'] = (TP + TN) / (TP + FP + FN + TN)

	return DataFrame({'class': classes, **metrics})


def evaluate_multiclass_classification(actual, predicted, classes):
	cnf_matrix = confusion_matrix(actual, predicted, labels=classes)
	return _evaluate_multiclass_classification(confusion_matrix=cnf_matrix, classes=classes)
