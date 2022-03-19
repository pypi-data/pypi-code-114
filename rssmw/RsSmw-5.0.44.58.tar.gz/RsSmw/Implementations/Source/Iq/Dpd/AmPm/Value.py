from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def get(self, xvalue: float, xunit: enums.Unknown) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMPM:VALue \n
		Snippet: value: float = driver.source.iq.dpd.amPm.value.get(xvalue = 1.0, xunit = enums.Unknown.DBM) \n
		Queries the delta phase value of the generated RF signal for a selected <XValue>. \n
			:param xvalue: float Value on the x-axis. Value range depends on the selected PEPinMin and PEPinMax values. Range: -100 to 100
			:param xunit: DBM| V
			:return: delta_phase: float Range: -180 to 180"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.Float), ArgSingle('xunit', xunit, DataType.Enum, enums.Unknown))
		response = self._core.io.query_str(f'SOURce<HwInstance>:IQ:DPD:AMPM:VALue? {param}'.rstrip())
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMPM:VALue:LEVel \n
		Snippet: value: float = driver.source.iq.dpd.amPm.value.get_level() \n
		Queries the delta phase value for the current root mean square (RMS) power level of the generated RF signal. \n
			:return: delta_phase: float Range: -180 to 180
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:AMPM:VALue:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:AMPM:VALue:PEP \n
		Snippet: value: float = driver.source.iq.dpd.amPm.value.get_pep() \n
		Queries the delta phase value for the current peak envelope power (PEP) level of the generated RF signal. \n
			:return: delta_phase: float Range: -180 to 180
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:AMPM:VALue:PEP?')
		return Conversions.str_to_float(response)
