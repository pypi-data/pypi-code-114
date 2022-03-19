from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfreq:
	"""Dfreq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfreq", core, parent)

	def set(self, delta_freq: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:DFReq \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.dfreq.set(delta_freq = 1.0, carrier = repcap.Carrier.Default) \n
		Sets the frequency offset between the NB-IoT carrier and the LTE center frequency. \n
			:param delta_freq: float Range: -10000000 to 10000000, Unit: MHz
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(delta_freq)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:DFReq {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:DFReq \n
		Snippet: value: float = driver.source.bb.eutra.downlink.carrier.niot.dfreq.get(carrier = repcap.Carrier.Default) \n
		Sets the frequency offset between the NB-IoT carrier and the LTE center frequency. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: delta_freq: float Range: -10000000 to 10000000, Unit: MHz"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:DFReq?')
		return Conversions.str_to_float(response)
