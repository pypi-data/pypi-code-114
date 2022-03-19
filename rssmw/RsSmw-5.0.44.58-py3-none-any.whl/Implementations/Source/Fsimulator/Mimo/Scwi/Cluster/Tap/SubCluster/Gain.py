from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def get(self, cluster=repcap.Cluster.Default, mimoTap=repcap.MimoTap.Default, subCluster=repcap.SubCluster.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:TAP<ST>:SUBCluster<DI>:GAIN \n
		Snippet: value: float = driver.source.fsimulator.mimo.scwi.cluster.tap.subCluster.gain.get(cluster = repcap.Cluster.Default, mimoTap = repcap.MimoTap.Default, subCluster = repcap.SubCluster.Default) \n
		Queries the resulting relative gain of an enabled sub-cluster. \n
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param subCluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubCluster')
			:return: gain: float Range: -50 to 0"""
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		subCluster_cmd_val = self._cmd_group.get_repcap_cmd_value(subCluster, repcap.SubCluster)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:TAP{mimoTap_cmd_val}:SUBCluster{subCluster_cmd_val}:GAIN?')
		return Conversions.str_to_float(response)
