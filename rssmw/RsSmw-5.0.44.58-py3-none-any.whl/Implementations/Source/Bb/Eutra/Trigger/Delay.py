from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	# noinspection PyTypeChecker
	def get_unit(self) -> enums.TrigDelUnit:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:DELay:UNIT \n
		Snippet: value: enums.TrigDelUnit = driver.source.bb.eutra.trigger.delay.get_unit() \n
		Sets the units in that the trigger delay is expressed. \n
			:return: del_unit: SAMPle| TIME
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:DELay:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.TrigDelUnit)

	def set_unit(self, del_unit: enums.TrigDelUnit) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:DELay:UNIT \n
		Snippet: driver.source.bb.eutra.trigger.delay.set_unit(del_unit = enums.TrigDelUnit.SAMPle) \n
		Sets the units in that the trigger delay is expressed. \n
			:param del_unit: SAMPle| TIME
		"""
		param = Conversions.enum_scalar_to_str(del_unit, enums.TrigDelUnit)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:DELay:UNIT {param}')
