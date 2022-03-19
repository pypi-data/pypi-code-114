from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dot:
	"""Dot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dot", core, parent)

	def set(self, dot_angle: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:TAP<ST>:DOT \n
		Snippet: driver.source.fsimulator.mimo.scwi.tap.dot.set(dot_angle = 1.0, mimoTap = repcap.MimoTap.Default) \n
		Sets the direction of travel of the mobile station. \n
			:param dot_angle: float Range: 0 to 359.9
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(dot_angle)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:TAP{mimoTap_cmd_val}:DOT {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:TAP<ST>:DOT \n
		Snippet: value: float = driver.source.fsimulator.mimo.scwi.tap.dot.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the direction of travel of the mobile station. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: dot_angle: float Range: 0 to 359.9"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:TAP{mimoTap_cmd_val}:DOT?')
		return Conversions.str_to_float(response)
