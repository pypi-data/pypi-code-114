from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def get(self, band=repcap.Band.Default) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:BAND<CH>:LOWer \n
		Snippet: value: float = driver.source.efrontend.frequency.band.lower.get(band = repcap.Band.Default) \n
		Queries the lower/upper limit of the corresponding frequency band. \n
			:param band: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Band')
			:return: fe_freq_band_low: float"""
		band_cmd_val = self._cmd_group.get_repcap_cmd_value(band, repcap.Band)
		response = self._core.io.query_str(f'SOURce<HwInstance>:EFRontend:FREQuency:BAND{band_cmd_val}:LOWer?')
		return Conversions.str_to_float(response)
