# probability classifier is a classifier that can use any linear and non linear classifier
# together with a linear regression
# the classifier is trained on the data first, then the regression model is trained on the probability
# then the classifier is built on top of the probability that the regression model predicts


from sklearn.ensemble import RandomForestClassifier as SklearnRandomForestClassifier
from sklearn.linear_model import LinearRegression as SklearnLinearRegression
from pyspark.ml.classification import RandomForestClassifier as SparkRandomForestClassifier
from pyspark.ml.regression import LinearRegression as SparkLinearRegression
from pandas import DataFrame as PandasDF
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from ..evaluation._get_confusion_matrix_df import convert_confusion_matrix_to_df
from ..evaluation._evaluate_mutliclass_classification import _evaluate_multiclass_classification


class ProbabilityClassifier:
	def __init__(self, classifier, regressor, threshold=0.5):
		"""
		a classifier based on any other kind of classifier and a regressor that predicts probability
		:type classifier: SklearnRandomForestClassifier or SparkRandomForestClassifier
		:type regressor: SklearnLinearRegression or SparkLinearRegression
		:type threshold: float
		"""

		self._classifier = classifier
		self._regressor = regressor
		self._threshold = threshold

		self._classes = None
		self._x_columns = None
		self._y_dtype = None
		self._coefficients = None
		self._confusion_matrix = None

	def fit(self, X, y):
		self._x_columns = X.columns
		self._classifier.fit(X, y)
		self._y_dtype = y.dtype
		probabilities = self._classifier.predict_proba(X)
		self._regressor.fit(X, probabilities)

	def _predict_probabilities(self, X):
		return self._regressor.predict(X[self._x_columns])

	@property
	def classes(self):
		"""
		:rtype: list[str]
		"""
		if self._classes is None:
			self._classes = list(self._classifier.classes_)
		return self._classes

	@property
	def coefficients(self):
		"""
		:rtype: dict[str, float]
		"""
		if self._coefficients is None:
			result = {}
			for i, prediction_class in enumerate(self.classes):
				coef_values = list(self._regressor.coef_[i])
				if len(coef_values) != len(self._x_columns):
					raise RuntimeError(f'There are {len(self._x_columns)} features but {len(coef_values)} coefficients!')
				intercept = self._regressor.intercept_[i]
				internal_dictionary = {col: value for col, value in zip(self._x_columns, coef_values)}
				internal_dictionary['intercept'] = intercept
				result[prediction_class] = internal_dictionary
			self._coefficients = result
		return self._coefficients

	def predict_probabilities(
			self, X, append=False, infer_prediction=False,
			prediction_column='prediction', suffix='_prediction_probability'
	):
		probabilities_array = self._predict_probabilities(X=X)
		result = PandasDF(probabilities_array, columns=[f'{col}{suffix}' for col in self.classes])
		if infer_prediction:
			predictions = self._convert_probabilities_array_to_prediction(probabilities_array=probabilities_array)
			result[prediction_column] = predictions

		if append:
			result = pd.concat([X, result], axis=1)
		return result

	predict_proba = predict_probabilities

	def _convert_probabilities_array_to_prediction(self, probabilities_array):
		the_classes = self.classes.copy()

		def get_index_of_max(row):
			return np.array(the_classes[max(range(row.size), key=row.__getitem__)], dtype=self._y_dtype)

		return np.apply_along_axis(get_index_of_max, axis=1, arr=probabilities_array)

	def predict(self, X):
		probabilities_array = self._predict_probabilities(X=X)
		return self._convert_probabilities_array_to_prediction(probabilities_array=probabilities_array)


	def get_confusion_matrix(self, X, y, actual_prefix='actual_', prediction_prefix='predicted_'):
		predictions = self.predict(X=X)
		self._confusion_matrix = confusion_matrix(y, predictions, labels=self.classes)
		return convert_confusion_matrix_to_df(
			confusion_matrix=self._confusion_matrix, classes=self.classes,
			actual_prefix=actual_prefix, prediction_prefix=prediction_prefix
		)

	def evaluate(self, X=None, y=None):
		if X is not None and y is not None:
			predictions = self.predict(X=X)
			self._confusion_matrix = confusion_matrix(y, predictions, labels=self.classes)
		elif X is None and y is not None:
			raise ValueError('y should be provided if X is provided!')
		elif X is not None and y is None:
			raise ValueError('X should be provided if y is provided!')
		elif self._confusion_matrix is None:
			raise RuntimeError('confusion matrix should exist when X and y are not provided!')

		return _evaluate_multiclass_classification(confusion_matrix=self._confusion_matrix, classes=self.classes)
