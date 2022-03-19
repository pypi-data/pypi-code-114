from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psetup:
	"""Psetup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psetup", core, parent)

	def set(self, psetup: bool, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:PSETup \n
		Snippet: driver.source.bb.c2K.bstation.pdChannel.psetup.set(psetup = False, baseStation = repcap.BaseStation.Default) \n
		Selects for F-PDCH if all subpackets are generated using the same settings or if the settings of subchannel 1 are valid
		for all sub channels. However, the value of 'Number of Bits per Encoder Packet' is a quality of the complete encoder
		packet, therefore it is always set for all sub packet channels via the entry for sub channel 1. \n
			:param psetup: 1| ON| 0| OFF ON Packet parameters can be changed only for sub packet 1, all sub packets are generated with these settings. OFF Packet parameters can be set individually for each sub packet.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.bool_to_str(psetup)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:PSETup {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:PSETup \n
		Snippet: value: bool = driver.source.bb.c2K.bstation.pdChannel.psetup.get(baseStation = repcap.BaseStation.Default) \n
		Selects for F-PDCH if all subpackets are generated using the same settings or if the settings of subchannel 1 are valid
		for all sub channels. However, the value of 'Number of Bits per Encoder Packet' is a quality of the complete encoder
		packet, therefore it is always set for all sub packet channels via the entry for sub channel 1. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: psetup: 1| ON| 0| OFF ON Packet parameters can be changed only for sub packet 1, all sub packets are generated with these settings. OFF Packet parameters can be set individually for each sub packet."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:PSETup?')
		return Conversions.str_to_bool(response)
