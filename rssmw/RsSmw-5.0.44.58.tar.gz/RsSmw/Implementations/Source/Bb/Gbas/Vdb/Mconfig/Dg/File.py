from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:DG:FILE \n
		Snippet: value: str = driver.source.bb.gbas.vdb.mconfig.dg.file.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Queries the currently selected GBAS differential file. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: filename: string Filename with file extension (*.rs_gbas)"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:DG:FILE?')
		return trim_str_response(response)
