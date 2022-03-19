from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aid:
	"""Aid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aid", core, parent)

	def set(self, aid: str, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:AID \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.aid.set(aid = '1', vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the airport ID. \n
			:param aid: string
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.value_to_quoted_str(aid)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:AID {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:AID \n
		Snippet: value: str = driver.source.bb.gbas.vdb.mconfig.aid.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the airport ID. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: aid: string"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:AID?')
		return trim_str_response(response)
