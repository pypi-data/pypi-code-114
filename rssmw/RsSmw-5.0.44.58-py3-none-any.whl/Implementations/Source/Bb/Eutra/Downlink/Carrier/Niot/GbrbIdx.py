from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GbrbIdx:
	"""GbrbIdx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gbrbIdx", core, parent)

	def set(self, rb_index_gb: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:GBRBidx \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.gbrbIdx.set(rb_index_gb = 1, carrier = repcap.Carrier.Default) \n
		In guardband opration, sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param rb_index_gb: integer
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(rb_index_gb)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:GBRBidx {param}')

	def get(self, carrier=repcap.Carrier.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:GBRBidx \n
		Snippet: value: int = driver.source.bb.eutra.downlink.carrier.niot.gbrbIdx.get(carrier = repcap.Carrier.Default) \n
		In guardband opration, sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: rb_index_gb: integer"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:GBRBidx?')
		return Conversions.str_to_int(response)
