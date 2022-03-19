from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfall:
	"""Sfall commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfall", core, parent)

	def set(self, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:SFALl \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.sfall.set(carrier = repcap.Carrier.Default) \n
		Sets all SFs to valid. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:SFALl')

	def set_with_opc(self, carrier=repcap.Carrier.Default, opc_timeout_ms: int = -1) -> None:
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:SFALl \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.sfall.set_with_opc(carrier = repcap.Carrier.Default) \n
		Sets all SFs to valid. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:SFALl', opc_timeout_ms)
