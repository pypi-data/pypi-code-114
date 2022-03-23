class AssignError(Exception):
	""" AssignError will be raised when an invalid datatype is assigned to an attribute. """

	def __init__(self, message, parameter=None, required=None, invalid=None):
		self.parameter = parameter
		self.required = required
		self.invalid = invalid

		super().__init__(message)