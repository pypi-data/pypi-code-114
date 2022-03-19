from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def set(self, gain: float, cluster=repcap.Cluster.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:GAIN \n
		Snippet: driver.source.fsimulator.mimo.scwi.cluster.gain.set(gain = 1.0, cluster = repcap.Cluster.Default) \n
		Sets the relative gain (in dB) of the selected cluster. \n
			:param gain: float Range: -50 to 0
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
		"""
		param = Conversions.decimal_value_to_str(gain)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:GAIN {param}')

	def get(self, cluster=repcap.Cluster.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:GAIN \n
		Snippet: value: float = driver.source.fsimulator.mimo.scwi.cluster.gain.get(cluster = repcap.Cluster.Default) \n
		Sets the relative gain (in dB) of the selected cluster. \n
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:return: gain: float Range: -50 to 0"""
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:GAIN?')
		return Conversions.str_to_float(response)
