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

	def set(self, dselect: str, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:DATA:DSELect \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.data.dselect.set(dselect = '1', mobileStation = repcap.MobileStation.Default) \n
		The command selects the data list for the DLISt data source. The files are stored with the fixed file extensions *.dm_iqd
		in a directory of the user's choice. The directory applicable to the commands is defined with the command method RsSmw.
		MassMemory.currentDirectory. To access the files in this directory, you only have to give the file name, without the path
		and the file extension. \n
			:param dselect: string
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:DATA:DSELect {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.mstation.pcpch.data.dselect.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the data list for the DLISt data source. The files are stored with the fixed file extensions *.dm_iqd
		in a directory of the user's choice. The directory applicable to the commands is defined with the command method RsSmw.
		MassMemory.currentDirectory. To access the files in this directory, you only have to give the file name, without the path
		and the file extension. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: dselect: string"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:DATA:DSELect?')
		return trim_str_response(response)
