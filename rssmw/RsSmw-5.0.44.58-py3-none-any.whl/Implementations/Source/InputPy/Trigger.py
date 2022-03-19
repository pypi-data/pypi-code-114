from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SlopeType:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:SLOPe \n
		Snippet: value: enums.SlopeType = driver.source.inputPy.trigger.get_slope() \n
		Sets the polarity of the active slope of an applied instrument trigger. \n
			:return: slope: NEGative| POSitive
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TRIGger:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_slope(self, slope: enums.SlopeType) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:SLOPe \n
		Snippet: driver.source.inputPy.trigger.set_slope(slope = enums.SlopeType.NEGative) \n
		Sets the polarity of the active slope of an applied instrument trigger. \n
			:param slope: NEGative| POSitive
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TRIGger:SLOPe {param}')
