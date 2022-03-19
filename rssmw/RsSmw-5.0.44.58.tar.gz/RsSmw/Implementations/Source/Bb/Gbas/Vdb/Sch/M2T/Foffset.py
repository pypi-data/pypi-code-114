from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, offset: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:M2T:FOFFset \n
		Snippet: driver.source.bb.gbas.vdb.sch.m2T.foffset.set(offset = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the offset frame related to the first frame. \n
			:param offset: integer Range: 0 to 19
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(offset)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:M2T:FOFFset {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:M2T:FOFFset \n
		Snippet: value: int = driver.source.bb.gbas.vdb.sch.m2T.foffset.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the offset frame related to the first frame. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: offset: integer Range: 0 to 19"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:M2T:FOFFset?')
		return Conversions.str_to_int(response)
