from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:KRONecker:CORRelation:TX:[AB]:PHASe \n
		Snippet: driver.source.fsimulator.mimo.tap.kronecker.correlation.tx.ab.phase.set(phase = 1.0, mimoTap = repcap.MimoTap.Default) \n
		No command help available \n
			:param phase: No help available
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(phase)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:KRONecker:CORRelation:TX:AB:PHASe {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:KRONecker:CORRelation:TX:[AB]:PHASe \n
		Snippet: value: float = driver.source.fsimulator.mimo.tap.kronecker.correlation.tx.ab.phase.get(mimoTap = repcap.MimoTap.Default) \n
		No command help available \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: phase: No help available"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:KRONecker:CORRelation:TX:AB:PHASe?')
		return Conversions.str_to_float(response)
