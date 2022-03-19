from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CidGroup:
	"""CidGroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cidGroup", core, parent)

	def get(self, carrier=repcap.Carrier.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:CIDGroup \n
		Snippet: value: int = driver.source.bb.eutra.downlink.carrier.niot.cidGroup.get(carrier = repcap.Carrier.Default) \n
		Queries the physical cell identity group. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: cell_id_gr: integer Range: 0 to 111"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:CIDGroup?')
		return Conversions.str_to_int(response)
