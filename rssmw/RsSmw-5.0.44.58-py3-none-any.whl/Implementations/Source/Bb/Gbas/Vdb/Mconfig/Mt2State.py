from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mt2State:
	"""Mt2State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mt2State", core, parent)

	def set(self, mt_2_state: bool, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:MT2State \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.mt2State.set(mt_2_state = False, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Enables the message type 2 configuration. \n
			:param mt_2_state: 0| 1| OFF| ON
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.bool_to_str(mt_2_state)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:MT2State {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:MT2State \n
		Snippet: value: bool = driver.source.bb.gbas.vdb.mconfig.mt2State.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Enables the message type 2 configuration. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: mt_2_state: 0| 1| OFF| ON"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:MT2State?')
		return Conversions.str_to_bool(response)
