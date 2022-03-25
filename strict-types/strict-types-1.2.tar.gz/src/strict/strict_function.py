from .strict_class import StrictClass

class StrictFunction(StrictClass):
	""" StrictFunction is used to compare the keyword arguments datatypes with the desired datatypes and run a function
	with those arguments. """

	def __init__(self, func, **kwargs):
		""" Initialize object attributes.

		:param func: the function this object should execute
		:param kwargs: everything that must be validated and stored inside the object before calling the function """

		# Validate every keyword.
		super().__init__(**kwargs)

		# Run the function with the keywords and stores the output of the function.
		self.__function = lambda: func(**kwargs)

	def __call__(self):
		return self.__function()