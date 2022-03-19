from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Copy:
	"""Copy commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("copy", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.RegObj:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect:COPY:DESTination \n
		Snippet: value: enums.RegObj = driver.source.regenerator.object.copy.get_destination() \n
		Sets the object whose settings are overwritten. \n
			:return: destination: ALL| 1| 2| 3| 4| 5| 6| 7| 8| 9| 12| 11| 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:OBJect:COPY:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.RegObj)

	def set_destination(self, destination: enums.RegObj) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect:COPY:DESTination \n
		Snippet: driver.source.regenerator.object.copy.set_destination(destination = enums.RegObj._1) \n
		Sets the object whose settings are overwritten. \n
			:param destination: ALL| 1| 2| 3| 4| 5| 6| 7| 8| 9| 12| 11| 10
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.RegObj)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect:COPY:DESTination {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.RegObjOne:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect:COPY:SOURce \n
		Snippet: value: enums.RegObjOne = driver.source.regenerator.object.copy.get_source() \n
		Selects the object whose settings are copied. \n
			:return: source: 1| 2| 3| 4| 5| 6| 7| 8| 9| 11| 12| 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:OBJect:COPY:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.RegObjOne)

	def set_source(self, source: enums.RegObjOne) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect:COPY:SOURce \n
		Snippet: driver.source.regenerator.object.copy.set_source(source = enums.RegObjOne._1) \n
		Selects the object whose settings are copied. \n
			:param source: 1| 2| 3| 4| 5| 6| 7| 8| 9| 11| 12| 10
		"""
		param = Conversions.enum_scalar_to_str(source, enums.RegObjOne)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect:COPY:SOURce {param}')

	def clone(self) -> 'Copy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Copy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
