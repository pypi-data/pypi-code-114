from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Double:
	"""Double commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("double", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DOUBle:DELay \n
		Snippet: value: float = driver.source.bb.general.pulm.double.get_delay() \n
		Sets the double pulse delay in microseconds. \n
			:return: pulm_dbl_del: float Range: 50E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:DOUBle:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, pulm_dbl_del: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DOUBle:DELay \n
		Snippet: driver.source.bb.general.pulm.double.set_delay(pulm_dbl_del = 1.0) \n
		Sets the double pulse delay in microseconds. \n
			:param pulm_dbl_del: float Range: 50E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(pulm_dbl_del)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:DOUBle:DELay {param}')

	def get_width(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DOUBle:WIDTh \n
		Snippet: value: float = driver.source.bb.general.pulm.double.get_width() \n
		Defines the double pulse width in microseconds. \n
			:return: pulm_dbl_width: float Range: 50E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:DOUBle:WIDTh?')
		return Conversions.str_to_float(response)

	def set_width(self, pulm_dbl_width: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DOUBle:WIDTh \n
		Snippet: driver.source.bb.general.pulm.double.set_width(pulm_dbl_width = 1.0) \n
		Defines the double pulse width in microseconds. \n
			:param pulm_dbl_width: float Range: 50E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(pulm_dbl_width)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:DOUBle:WIDTh {param}')
