from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:SUBPath:STATe \n
		Snippet: driver.source.fsimulator.scm.tap.subPath.state.set(state = False, mimoTap = repcap.MimoTap.Default) \n
		If enabled, random start phases are selected. \n
			:param state: 1| ON| 0| OFF
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.bool_to_str(state)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:SUBPath:STATe {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:SUBPath:STATe \n
		Snippet: value: bool = driver.source.fsimulator.scm.tap.subPath.state.get(mimoTap = repcap.MimoTap.Default) \n
		If enabled, random start phases are selected. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: state: 1| ON| 0| OFF"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:SUBPath:STATe?')
		return Conversions.str_to_bool(response)
