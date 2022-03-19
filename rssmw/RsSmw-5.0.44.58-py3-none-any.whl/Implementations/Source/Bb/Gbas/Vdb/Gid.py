from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gid:
	"""Gid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gid", core, parent)

	def set(self, gid: str, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:GID \n
		Snippet: driver.source.bb.gbas.vdb.gid.set(gid = '1', vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the GBAS ID. \n
			:param gid: string A four-character (24-bit) alphanumeric field that identifies the ground station broadcasting the message. Permitted are capital letter, numbers and 'space'.
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.value_to_quoted_str(gid)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:GID {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:GID \n
		Snippet: value: str = driver.source.bb.gbas.vdb.gid.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the GBAS ID. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: gid: string A four-character (24-bit) alphanumeric field that identifies the ground station broadcasting the message. Permitted are capital letter, numbers and 'space'."""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:GID?')
		return trim_str_response(response)
