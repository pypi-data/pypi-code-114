from sklearn.metrics import confusion_matrix
from numpy import ndarray
from pandas import DataFrame


def convert_confusion_matrix_to_df(confusion_matrix, classes, actual_prefix='actual_', prediction_prefix='predicted_'):
	"""
	gets a confusion matrix created by sklearn which is an array and turns it into a nice dataframe
	:type confusion_matrix: ndarray
	:type classes: iterable
	:rtype: DataFrame
	"""

	return DataFrame(
		confusion_matrix,
		index=[f'{actual_prefix}{x}' for x in classes],
		columns=[f'{prediction_prefix}{x}' for x in classes]
	)


def get_confusion_matrix_df(actual, predicted, classes, actual_prefix='actual_', prediction_prefix='predicted_'):
	"""
	produces a nice confusion matrix in the form of a dataframe
	:type actual: array
	:type predicted: array
	:type classes: iterable
	:rtype: DataFrame
	"""
	confusion_matrix_array = confusion_matrix(actual, predicted, labels=classes)
	return convert_confusion_matrix_to_df(
		confusion_matrix=confusion_matrix_array,
		classes=classes, actual_prefix=actual_prefix, prediction_prefix=prediction_prefix
	)
