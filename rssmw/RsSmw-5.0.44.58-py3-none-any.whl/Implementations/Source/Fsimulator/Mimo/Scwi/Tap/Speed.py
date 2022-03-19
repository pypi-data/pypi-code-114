from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speed:
	"""Speed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speed", core, parent)

	def set(self, speed: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:TAP<ST>:SPEed \n
		Snippet: driver.source.fsimulator.mimo.scwi.tap.speed.set(speed = 1.0, mimoTap = repcap.MimoTap.Default) \n
		Sets the speed of the mobile station. \n
			:param speed: float Range: 0 to 27778
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(speed)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:TAP{mimoTap_cmd_val}:SPEed {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:TAP<ST>:SPEed \n
		Snippet: value: float = driver.source.fsimulator.mimo.scwi.tap.speed.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the speed of the mobile station. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: speed: float Range: 0 to 27778"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:TAP{mimoTap_cmd_val}:SPEed?')
		return Conversions.str_to_float(response)
