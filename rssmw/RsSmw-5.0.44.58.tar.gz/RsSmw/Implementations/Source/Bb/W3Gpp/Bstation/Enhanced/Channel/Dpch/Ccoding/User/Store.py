from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, filename: str, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:USER:STORe \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.user.store.set(filename = '1', channelNull = repcap.ChannelNull.Default) \n
		The command saves the current settings for channel coding as user channel coding in the specified file. The files are
		stored with the fixed file extensions *.3g_ccod_dl in a directory of the user's choice. The directory in which the file
		is stored is defined with the command method RsSmw.MassMemory.currentDirectory. To store the files in this directory, you
		only have to give the file name, without the path and the file extension. \n
			:param filename: string
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(filename)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:USER:STORe {param}')
