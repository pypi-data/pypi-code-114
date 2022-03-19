from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


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

	def get_destination(self) -> int:
		"""SCPI: [SOURce<HW>]:FSIMulator:COPY:DESTination \n
		Snippet: value: int = driver.source.fsimulator.copy.get_destination() \n
		Selects a group whose settings will be overwritten. \n
			:return: destination: integer Range: 1 to 4 (Standard Delay) / 8 (Fine Delay)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:COPY:DESTination?')
		return Conversions.str_to_int(response)

	def set_destination(self, destination: int) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:COPY:DESTination \n
		Snippet: driver.source.fsimulator.copy.set_destination(destination = 1) \n
		Selects a group whose settings will be overwritten. \n
			:param destination: integer Range: 1 to 4 (Standard Delay) / 8 (Fine Delay)
		"""
		param = Conversions.decimal_value_to_str(destination)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:COPY:DESTination {param}')

	def get_source(self) -> int:
		"""SCPI: [SOURce<HW>]:FSIMulator:COPY:SOURce \n
		Snippet: value: int = driver.source.fsimulator.copy.get_source() \n
		Sets the group whose settings are to be copied. \n
			:return: source: integer Range: 1 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:COPY:SOURce?')
		return Conversions.str_to_int(response)

	def set_source(self, source: int) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:COPY:SOURce \n
		Snippet: driver.source.fsimulator.copy.set_source(source = 1) \n
		Sets the group whose settings are to be copied. \n
			:param source: integer Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(source)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:COPY:SOURce {param}')

	def clone(self) -> 'Copy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Copy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
