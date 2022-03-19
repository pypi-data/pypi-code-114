from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:STATe \n
		Snippet: driver.source.bb.c2K.bstation.state.set(state = False, baseStation = repcap.BaseStation.Default) \n
		The command activates and deactivates the specified base station. \n
			:param state: 1| ON| 0| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.bool_to_str(state)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:STATe {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.c2K.bstation.state.get(baseStation = repcap.BaseStation.Default) \n
		The command activates and deactivates the specified base station. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: state: 1| ON| 0| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
