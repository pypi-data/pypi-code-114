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
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:COFFset \n
		Snippet: value: int = driver.source.bb.c2K.copy.get_coffset() \n
		The command sets the offset for the Walsh code in the destination base station. The minimum value is 0 (Walsh codes are
		identical) , the maximum value is 255. This command is only available in the downlink (SOUR:BB:C2K:LINK FORW/DOWN) . \n
			:return: coffset: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:COPY:COFFset?')
		return Conversions.str_to_int(response)

	def set_coffset(self, coffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:COFFset \n
		Snippet: driver.source.bb.c2K.copy.set_coffset(coffset = 1) \n
		The command sets the offset for the Walsh code in the destination base station. The minimum value is 0 (Walsh codes are
		identical) , the maximum value is 255. This command is only available in the downlink (SOUR:BB:C2K:LINK FORW/DOWN) . \n
			:param coffset: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(coffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:COPY:COFFset {param}')

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:DESTination \n
		Snippet: value: enums.NumberA = driver.source.bb.c2K.copy.get_destination() \n
		The command selects the station to which data is to be copied. Whether the data is copied to a base station or a mobile
		station depends on which transmission direction is selected (command C2K:LINK UP | DOWN) . \n
			:return: destination: 1| 2| 3| 4 Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:COPY:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_destination(self, destination: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:DESTination \n
		Snippet: driver.source.bb.c2K.copy.set_destination(destination = enums.NumberA._1) \n
		The command selects the station to which data is to be copied. Whether the data is copied to a base station or a mobile
		station depends on which transmission direction is selected (command C2K:LINK UP | DOWN) . \n
			:param destination: 1| 2| 3| 4 Range: 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:COPY:DESTination {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:SOURce \n
		Snippet: value: enums.NumberA = driver.source.bb.c2K.copy.get_source() \n
		The command selects the station that has data to be copied. Whether the station copied is a base or mobile station
		depends on which transmission direction is selected (command C2K:LINK UP | DOWN) . \n
			:return: source: 1| 2| 3| 4 Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:COPY:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_source(self, source: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:COPY:SOURce \n
		Snippet: driver.source.bb.c2K.copy.set_source(source = enums.NumberA._1) \n
		The command selects the station that has data to be copied. Whether the station copied is a base or mobile station
		depends on which transmission direction is selected (command C2K:LINK UP | DOWN) . \n
			:param source: 1| 2| 3| 4 Range: 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(source, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:COPY:SOURce {param}')

	def clone(self) -> 'Copy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Copy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
