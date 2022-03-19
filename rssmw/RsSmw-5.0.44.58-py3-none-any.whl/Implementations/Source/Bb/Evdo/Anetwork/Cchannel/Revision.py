from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Revision:
	"""Revision commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("revision", core, parent)

	def get_maximum(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:REVision:MAXimum \n
		Snippet: value: int = driver.source.bb.evdo.anetwork.cchannel.revision.get_maximum() \n
		Sets the value of the maximum revision field within the control channel message. \n
			:return: maximum: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:REVision:MAXimum?')
		return Conversions.str_to_int(response)

	def set_maximum(self, maximum: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:REVision:MAXimum \n
		Snippet: driver.source.bb.evdo.anetwork.cchannel.revision.set_maximum(maximum = 1) \n
		Sets the value of the maximum revision field within the control channel message. \n
			:param maximum: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(maximum)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:REVision:MAXimum {param}')

	def get_minimum(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:REVision:MINimum \n
		Snippet: value: int = driver.source.bb.evdo.anetwork.cchannel.revision.get_minimum() \n
		Sets the value of the minimum revision field within the control channel message. \n
			:return: minimum: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:REVision:MINimum?')
		return Conversions.str_to_int(response)

	def set_minimum(self, minimum: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:REVision:MINimum \n
		Snippet: driver.source.bb.evdo.anetwork.cchannel.revision.set_minimum(minimum = 1) \n
		Sets the value of the minimum revision field within the control channel message. \n
			:param minimum: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(minimum)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:REVision:MINimum {param}')
