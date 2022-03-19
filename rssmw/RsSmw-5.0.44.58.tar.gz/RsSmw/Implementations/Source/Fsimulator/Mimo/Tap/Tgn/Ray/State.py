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

	def set(self, ray_state: bool, mimoTap=repcap.MimoTap.Default, ray=repcap.Ray.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:TGN:RAY<ST>:STATe \n
		Snippet: driver.source.fsimulator.mimo.tap.tgn.ray.state.set(ray_state = False, mimoTap = repcap.MimoTap.Default, ray = repcap.Ray.Default) \n
		Enables/disables the selected ray. \n
			:param ray_state: 1| ON| 0| OFF
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param ray: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ray')
		"""
		param = Conversions.bool_to_str(ray_state)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		ray_cmd_val = self._cmd_group.get_repcap_cmd_value(ray, repcap.Ray)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:TGN:RAY{ray_cmd_val}:STATe {param}')

	def get(self, mimoTap=repcap.MimoTap.Default, ray=repcap.Ray.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:TGN:RAY<ST>:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mimo.tap.tgn.ray.state.get(mimoTap = repcap.MimoTap.Default, ray = repcap.Ray.Default) \n
		Enables/disables the selected ray. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param ray: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ray')
			:return: ray_state: 1| ON| 0| OFF"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		ray_cmd_val = self._cmd_group.get_repcap_cmd_value(ray, repcap.Ray)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:TGN:RAY{ray_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
