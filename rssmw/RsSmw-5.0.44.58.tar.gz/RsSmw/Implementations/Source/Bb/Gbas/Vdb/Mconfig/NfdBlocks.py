from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NfdBlocks:
	"""NfdBlocks commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nfdBlocks", core, parent)

	def set(self, nfdb: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:NFDBlocks \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.nfdBlocks.set(nfdb = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > SCAT-I' header information. Sets the number of FAS data blocks. \n
			:param nfdb: integer Range: 1 to 5
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(nfdb)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:NFDBlocks {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:NFDBlocks \n
		Snippet: value: int = driver.source.bb.gbas.vdb.mconfig.nfdBlocks.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > SCAT-I' header information. Sets the number of FAS data blocks. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: nfdb: integer Range: 1 to 5"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:NFDBlocks?')
		return Conversions.str_to_int(response)
