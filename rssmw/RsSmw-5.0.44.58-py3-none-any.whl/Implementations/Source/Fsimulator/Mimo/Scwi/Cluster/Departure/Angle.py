from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)

	def set(self, angle: float, cluster=repcap.Cluster.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:DEParture:ANGLe \n
		Snippet: driver.source.fsimulator.mimo.scwi.cluster.departure.angle.set(angle = 1.0, cluster = repcap.Cluster.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) of the selected cluster. \n
			:param angle: float Range: 0 to 359.999
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
		"""
		param = Conversions.decimal_value_to_str(angle)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:DEParture:ANGLe {param}')

	def get(self, cluster=repcap.Cluster.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SCWI:CLUSter<CH>:DEParture:ANGLe \n
		Snippet: value: float = driver.source.fsimulator.mimo.scwi.cluster.departure.angle.get(cluster = repcap.Cluster.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) of the selected cluster. \n
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:return: angle: float Range: 0 to 359.999"""
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:SCWI:CLUSter{cluster_cmd_val}:DEParture:ANGLe?')
		return Conversions.str_to_float(response)
