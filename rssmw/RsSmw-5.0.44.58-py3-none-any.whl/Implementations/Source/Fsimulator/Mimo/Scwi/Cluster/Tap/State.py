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

	def set(self, state: bool, cluster=repcap.Cluster.Default, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:TAP<ST>:STATe \n
		Snippet: driver.source.fsimulator.mimo.scwi.cluster.tap.state.set(state = False, cluster = repcap.Cluster.Default, mimoTap = repcap.MimoTap.Default) \n
		Enables/disables the selected cluster. \n
			:param state: 1| ON| 0| OFF
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.bool_to_str(state)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:TAP{mimoTap_cmd_val}:STATe {param}')

	def get(self, cluster=repcap.Cluster.Default, mimoTap=repcap.MimoTap.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:TAP<ST>:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mimo.scwi.cluster.tap.state.get(cluster = repcap.Cluster.Default, mimoTap = repcap.MimoTap.Default) \n
		Enables/disables the selected cluster. \n
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: state: 1| ON| 0| OFF"""
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:TAP{mimoTap_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
