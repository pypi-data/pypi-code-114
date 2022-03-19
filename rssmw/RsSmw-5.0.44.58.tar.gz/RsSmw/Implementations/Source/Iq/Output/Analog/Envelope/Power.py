from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:POWer:OFFSet \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.power.get_offset() \n
		Queries the current power offset, that is the sum of enabled 'RF Level > Offset' and 'User Correction'. \n
			:return: power_offset: float Range: -200 to 200
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:POWer:OFFSet?')
		return Conversions.str_to_float(response)
