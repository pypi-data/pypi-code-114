from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_pep(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:CALibrated:POWer:PEP \n
		Snippet: value: float = driver.source.rfAlignment.calibrated.power.get_pep() \n
		Queries the PEP for that the calibration data is valid. \n
			:return: pep: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CALibrated:POWer:PEP?')
		return Conversions.str_to_float(response)
