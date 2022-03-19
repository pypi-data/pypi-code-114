from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DqSpreading:
	"""DqSpreading commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dqSpreading", core, parent)

	def set(self, dq_spreading: bool, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DQSPreading \n
		Snippet: driver.source.bb.evdo.terminal.dqSpreading.set(dq_spreading = False, terminal = repcap.Terminal.Default) \n
		Disables the quadrature spreading (complex multiply) with PN sequences and long code. \n
			:param dq_spreading: 1| ON| 0| OFF
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.bool_to_str(dq_spreading)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DQSPreading {param}')

	def get(self, terminal=repcap.Terminal.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DQSPreading \n
		Snippet: value: bool = driver.source.bb.evdo.terminal.dqSpreading.get(terminal = repcap.Terminal.Default) \n
		Disables the quadrature spreading (complex multiply) with PN sequences and long code. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: dq_spreading: 1| ON| 0| OFF"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DQSPreading?')
		return Conversions.str_to_bool(response)
