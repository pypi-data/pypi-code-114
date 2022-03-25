from .exceptions import AssignError

class StrictClass:
	""" StrictClass is used to compare the keyword arguments datatypes with the desired datatypes. """

	def __init__(self, **kwargs) -> None:
		""" Initialize object attributes.

		:param kwargs: everything that must be validated and/or stored inside the object """

		# Check if there is any annotation.
		if '__annotations__' in dir(self):

			# Check each annotation key and the desired datatype with the input parameters.
			for key in self.__annotations__:

				# Check if every annotation key was passed in the parameters.
				if key in kwargs:

					# Has the annotation more than one expression? ...
					if '__args__' in dir(self.__annotations__[key]):

						# Does the keyword object's datatype match any of the annotation expression datatypes? So raise exception if not.
						if not type(kwargs[key]) in self.__annotations__[key].__args__:
							raise AssignError(
								'Trying to assign an invalid datatype to the parameter "%s". Datatype must be %s, and not %s.'
								% (key, " or ".join([str(t) for t in self.__annotations__[key].__args__]), type(kwargs[key])),
								parameter=key, required=self.__annotations__[key].__args__, invalid=type(kwargs[key])
							)

					# Does it only has one expression? So raise exception if the datatypes don't match.
					elif not type(kwargs[key]) is self.__annotations__[key]:
						raise AssignError(
							'Trying to assign an invalid datatype to the parameter "%s". Datatype must be %s, and not %s.'
							% (key, self.__annotations__[key], type(kwargs[key])),
							parameter=key, required=(self.__annotations__[key],), invalid=type(kwargs[key])
						)

				# Raise exception if any annotations parameter isn't available.
				else:
					raise AssignError('A missing keyword ("%s") must be passed.' % key, parameter=key)

		# After the annotations validations, store every keyword inside the object.
		for keyword in kwargs:
			self.__dict__[keyword] = kwargs[keyword]

	def __getitem__(self, name):
		return self.__dict__[name]

	def __iter__(self):
		return iter(self.__dict__)