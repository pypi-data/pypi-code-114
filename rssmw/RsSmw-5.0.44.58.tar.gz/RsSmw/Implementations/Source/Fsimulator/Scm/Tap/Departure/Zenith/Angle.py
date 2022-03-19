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

	def set(self, zenith_departure: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:DEParture:ZENith:ANGLe \n
		Snippet: driver.source.fsimulator.scm.tap.departure.zenith.angle.set(zenith_departure = 1.0, mimoTap = repcap.MimoTap.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) of the cluster. \n
			:param zenith_departure: float Range: 0 to 359.999
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(zenith_departure)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:DEParture:ZENith:ANGLe {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:DEParture:ZENith:ANGLe \n
		Snippet: value: float = driver.source.fsimulator.scm.tap.departure.zenith.angle.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) of the cluster. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: zenith_departure: No help available"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:DEParture:ZENith:ANGLe?')
		return Conversions.str_to_float(response)
