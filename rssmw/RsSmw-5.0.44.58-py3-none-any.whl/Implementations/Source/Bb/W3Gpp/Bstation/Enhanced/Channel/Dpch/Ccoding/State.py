from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:STATe \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.state.set(state = False, channelNull = repcap.ChannelNull.Default) \n
		The command activates or deactivates channel coding for the selected enhanced DPCH. When channel coding is activated and
		a channel coding type conforming to the standard is selected, (BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:TYPE) the slot format,
		(BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:SFOR) and thus the symbol rate, (BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:SRAT) the bits per frame,
		(BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:BPFR) , the pilot length (BB:W3GP:BST1:CHAN:DPCC:PLEN) and the TFCI state
		(BB:W3GP:BST1:CHAN:DPCC:TFCI STAT) are set to the associated values. \n
			:param state: ON| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(state)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.state.get(channelNull = repcap.ChannelNull.Default) \n
		The command activates or deactivates channel coding for the selected enhanced DPCH. When channel coding is activated and
		a channel coding type conforming to the standard is selected, (BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:TYPE) the slot format,
		(BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:SFOR) and thus the symbol rate, (BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:SRAT) the bits per frame,
		(BB:W3GP:BST:ENH:CHAN:DPCH:CCOD:BPFR) , the pilot length (BB:W3GP:BST1:CHAN:DPCC:PLEN) and the TFCI state
		(BB:W3GP:BST1:CHAN:DPCC:TFCI STAT) are set to the associated values. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: state: ON| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:STATe?')
		return Conversions.str_to_bool(response)
