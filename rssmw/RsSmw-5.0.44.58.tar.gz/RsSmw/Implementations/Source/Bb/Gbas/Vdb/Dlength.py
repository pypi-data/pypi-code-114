from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlength:
	"""Dlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlength", core, parent)

	def set(self, data_len: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:DLENgth \n
		Snippet: driver.source.bb.gbas.vdb.dlength.set(data_len = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the application data length. \n
			:param data_len: integer Range: 1 to 65495
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(data_len)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:DLENgth {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:DLENgth \n
		Snippet: value: int = driver.source.bb.gbas.vdb.dlength.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the application data length. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: data_len: integer Range: 1 to 65495"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:DLENgth?')
		return Conversions.str_to_int(response)
