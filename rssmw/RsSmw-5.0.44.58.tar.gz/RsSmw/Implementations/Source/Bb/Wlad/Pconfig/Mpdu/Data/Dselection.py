from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselection:
	"""Dselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselection", core, parent)

	def set(self, filename: str, macPdu=repcap.MacPdu.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:DSELection \n
		Snippet: driver.source.bb.wlad.pconfig.mpdu.data.dselection.set(filename = '1', macPdu = repcap.MacPdu.Default) \n
		Selects the data list for the DLISt data source selection. The lists are stored as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. \n
			:param filename: string
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
		"""
		param = Conversions.value_to_quoted_str(filename)
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:DSELection {param}')

	def get(self, macPdu=repcap.MacPdu.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.wlad.pconfig.mpdu.data.dselection.get(macPdu = repcap.MacPdu.Default) \n
		Selects the data list for the DLISt data source selection. The lists are stored as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. \n
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
			:return: filename: string"""
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:DSELection?')
		return trim_str_response(response)
