from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Magnitude:
	"""Magnitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	def set(self, magnitude: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:KRONecker:CORRelation:TX:BH:MAGNitude \n
		Snippet: driver.source.fsimulator.mimo.tap.kronecker.correlation.tx.bh.magnitude.set(magnitude = 1.0, mimoTap = repcap.MimoTap.Default) \n
		No command help available \n
			:param magnitude: No help available
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(magnitude)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:KRONecker:CORRelation:TX:BH:MAGNitude {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:KRONecker:CORRelation:TX:BH:MAGNitude \n
		Snippet: value: float = driver.source.fsimulator.mimo.tap.kronecker.correlation.tx.bh.magnitude.get(mimoTap = repcap.MimoTap.Default) \n
		No command help available \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: magnitude: No help available"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:KRONecker:CORRelation:TX:BH:MAGNitude?')
		return Conversions.str_to_float(response)
