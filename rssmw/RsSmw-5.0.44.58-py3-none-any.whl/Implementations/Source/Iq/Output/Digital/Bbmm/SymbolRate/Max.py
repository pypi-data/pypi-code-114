from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get(self, iqConnector=repcap.IqConnector.Default) -> int:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:SRATe:MAX \n
		Snippet: value: int = driver.source.iq.output.digital.bbmm.symbolRate.max.get(iqConnector = repcap.IqConnector.Default) \n
		Queries the maximum supported sample rate. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: dig_iqhs_in_sr_max: integer Range: 1050E6 to 1250E6"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:SRATe:MAX?')
		return Conversions.str_to_int(response)
