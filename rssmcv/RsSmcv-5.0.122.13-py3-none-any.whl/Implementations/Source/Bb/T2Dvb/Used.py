from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Used:
	"""Used commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("used", core, parent)

	def get_bandwidth(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:USED:[BANDwidth] \n
		Snippet: value: int = driver.source.bb.t2Dvb.used.get_bandwidth() \n
		Queries the used channel bandwidth. The used bandwidth depends on the channel bandwidth, the FFT size and the carrier
		mode as described in Table 'Dependencies of the used bandwidth'. \n
			:return: used_bw: integer Range: 0.0 to 9999999.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:USED:BANDwidth?')
		return Conversions.str_to_int(response)
