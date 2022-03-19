from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Copy:
	"""Copy commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

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

	def get_coffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:COFFset \n
		Snippet: value: int = driver.source.bb.w3Gpp.copy.get_coffset() \n
		Sets the offset for the channelization code in the destination base station. \n
			:return: coffset: integer Range: 0 to 511
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:COPY:COFFset?')
		return Conversions.str_to_int(response)

	def set_coffset(self, coffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:COFFset \n
		Snippet: driver.source.bb.w3Gpp.copy.set_coffset(coffset = 1) \n
		Sets the offset for the channelization code in the destination base station. \n
			:param coffset: integer Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(coffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:COPY:COFFset {param}')

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:DESTination \n
		Snippet: value: enums.NumberA = driver.source.bb.w3Gpp.copy.get_destination() \n
		The command selects the station to which data is to be copied. Whether the data is copied to a base station or a user
		equipment depends on which transmission direction is selected (command W3GPp:LINK UP | DOWN) . \n
			:return: destination: 1| 2| 3| 4 Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:COPY:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_destination(self, destination: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:DESTination \n
		Snippet: driver.source.bb.w3Gpp.copy.set_destination(destination = enums.NumberA._1) \n
		The command selects the station to which data is to be copied. Whether the data is copied to a base station or a user
		equipment depends on which transmission direction is selected (command W3GPp:LINK UP | DOWN) . \n
			:param destination: 1| 2| 3| 4 Range: 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:COPY:DESTination {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:SOURce \n
		Snippet: value: enums.NumberA = driver.source.bb.w3Gpp.copy.get_source() \n
		The command selects the station that has data to be copied. Whether the station copied is a base or user equipment
		depends on which transmission direction is selected (command W3GPp:LINK UP | DOWN) . \n
			:return: source: 1| 2| 3| 4 Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:COPY:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_source(self, source: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:COPY:SOURce \n
		Snippet: driver.source.bb.w3Gpp.copy.set_source(source = enums.NumberA._1) \n
		The command selects the station that has data to be copied. Whether the station copied is a base or user equipment
		depends on which transmission direction is selected (command W3GPp:LINK UP | DOWN) . \n
			:param source: 1| 2| 3| 4 Range: 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(source, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:COPY:SOURce {param}')

	def clone(self) -> 'Copy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Copy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
