from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DATA:DSELect \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.data.dselect.set(dselect = '1', baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the data list for the DLISt data source selection. The lists are stored as files with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined
		with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give
		the file name, without the path and the file extension. \n
			:param dselect: string
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DATA:DSELect {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.bstation.channel.data.dselect.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the data list for the DLISt data source selection. The lists are stored as files with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined
		with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give
		the file name, without the path and the file extension. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: dselect: string"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DATA:DSELect?')
		return trim_str_response(response)
