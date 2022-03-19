from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: float, mimoTap=repcap.MimoTap.Default, gainVector=repcap.GainVector.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor<ST>:PHASe \n
		Snippet: driver.source.fsimulator.mimo.tap.gvector.phase.set(phase = 1.0, mimoTap = repcap.MimoTap.Default, gainVector = repcap.GainVector.Default) \n
		Sets the phase shift of the selected path. \n
			:param phase: float Range: 0 to 360
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param gainVector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gvector')
		"""
		param = Conversions.decimal_value_to_str(phase)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		gainVector_cmd_val = self._cmd_group.get_repcap_cmd_value(gainVector, repcap.GainVector)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor{gainVector_cmd_val}:PHASe {param}')

	def get(self, mimoTap=repcap.MimoTap.Default, gainVector=repcap.GainVector.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor<ST>:PHASe \n
		Snippet: value: float = driver.source.fsimulator.mimo.tap.gvector.phase.get(mimoTap = repcap.MimoTap.Default, gainVector = repcap.GainVector.Default) \n
		Sets the phase shift of the selected path. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param gainVector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gvector')
			:return: phase: float Range: 0 to 360"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		gainVector_cmd_val = self._cmd_group.get_repcap_cmd_value(gainVector, repcap.GainVector)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor{gainVector_cmd_val}:PHASe?')
		return Conversions.str_to_float(response)
