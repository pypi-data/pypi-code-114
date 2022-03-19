from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CHANnel<CH>:DPDCh:DATA:DSELect \n
		Snippet: driver.source.bb.w3Gpp.mstation.channel.dpdch.data.dselect.set(dselect = '1', mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		The command selects the data list for the DLISt data source selection. The files are stored with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name, without the path and the file extension. \n
			:param dselect: data list name
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:DPDCh:DATA:DSELect {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CHANnel<CH>:DPDCh:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.mstation.channel.dpdch.data.dselect.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		The command selects the data list for the DLISt data source selection. The files are stored with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name, without the path and the file extension. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: dselect: data list name"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:DPDCh:DATA:DSELect?')
		return trim_str_response(response)
