from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:DG:CCGP:STATe \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.dg.ccgp.state.set(state = False, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		No command help available \n
			:param state: No help available
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.bool_to_str(state)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:DG:CCGP:STATe {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:DG:CCGP:STATe \n
		Snippet: value: bool = driver.source.bb.gbas.vdb.mconfig.dg.ccgp.state.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		No command help available \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: state: No help available"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:DG:CCGP:STATe?')
		return Conversions.str_to_bool(response)
