from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apf2:
	"""Apf2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apf2", core, parent)

	def set(self, apf_2: List[str], testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:APF2 \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.apf2.set(apf_2 = ['raw1', 'raw2', 'raw3'], testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Sets the value for the information element Field 2 of the Access-Assign PDU. \n
			:param apf_2: 8 bits
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.list_to_csv_str(apf_2)
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:APF2 {param}')

	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:APF2 \n
		Snippet: value: List[str] = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.apf2.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Sets the value for the information element Field 2 of the Access-Assign PDU. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: apf_2: 8 bits"""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:APF2?')
		return Conversions.str_to_str_list(response)
