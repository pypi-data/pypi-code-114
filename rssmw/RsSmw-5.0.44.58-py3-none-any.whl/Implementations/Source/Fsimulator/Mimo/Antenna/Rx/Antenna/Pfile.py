from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pfile:
	"""Pfile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pfile", core, parent)

	def set(self, rx_pattern: str, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:ANTenna<DI>:PFILe \n
		Snippet: driver.source.fsimulator.mimo.antenna.rx.antenna.pfile.set(rx_pattern = '1', index = repcap.Index.Default) \n
		Selects the antenna pattern file (*.ant_pat) per antenna. Querry the existing files with the command
		[:SOURce]:FSIMulator:MIMO:ANTenna:PATTern:CATalog:USER?. \n
			:param rx_pattern: No help available
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.value_to_quoted_str(rx_pattern)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce:FSIMulator:MIMO:ANTenna:RX:ANTenna{index_cmd_val}:PFILe {param}')

	def get(self, index=repcap.Index.Default) -> str:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:ANTenna<DI>:PFILe \n
		Snippet: value: str = driver.source.fsimulator.mimo.antenna.rx.antenna.pfile.get(index = repcap.Index.Default) \n
		Selects the antenna pattern file (*.ant_pat) per antenna. Querry the existing files with the command
		[:SOURce]:FSIMulator:MIMO:ANTenna:PATTern:CATalog:USER?. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: rx_pattern: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce:FSIMulator:MIMO:ANTenna:RX:ANTenna{index_cmd_val}:PFILe?')
		return trim_str_response(response)
