from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, diff_gnss_state: bool, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:DG:STATe \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.dg.state.set(diff_gnss_state = False, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Enables the use of differential GNSS data. \n
			:param diff_gnss_state: 0| 1| OFF| ON
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.bool_to_str(diff_gnss_state)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:DG:STATe {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:DG:STATe \n
		Snippet: value: bool = driver.source.bb.gbas.vdb.mconfig.dg.state.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Enables the use of differential GNSS data. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: diff_gnss_state: 0| 1| OFF| ON"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:DG:STATe?')
		return Conversions.str_to_bool(response)
