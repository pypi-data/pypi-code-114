from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Valsf:
	"""Valsf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("valsf", core, parent)

	def set(self, valid: bool, carrier=repcap.Carrier.Default, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:SF<ST0>:VALSf \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.sf.valsf.set(valid = False, carrier = repcap.Carrier.Default, subframeNull = repcap.SubframeNull.Default) \n
		Sets the valid subframes. \n
			:param valid: 1| ON| 0| OFF 1 Valid subframe 0 Not valid subframe
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sf')
		"""
		param = Conversions.bool_to_str(valid)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:SF{subframeNull_cmd_val}:VALSf {param}')

	def get(self, carrier=repcap.Carrier.Default, subframeNull=repcap.SubframeNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:SF<ST0>:VALSf \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.carrier.niot.sf.valsf.get(carrier = repcap.Carrier.Default, subframeNull = repcap.SubframeNull.Default) \n
		Sets the valid subframes. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sf')
			:return: valid: 1| ON| 0| OFF 1 Valid subframe 0 Not valid subframe"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:SF{subframeNull_cmd_val}:VALSf?')
		return Conversions.str_to_bool(response)
