from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spread:
	"""Spread commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spread", core, parent)

	def set(self, dep_zen_spread: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:DEParture:ZENith:SPRead \n
		Snippet: driver.source.fsimulator.scm.tap.departure.zenith.spread.set(dep_zen_spread = 1.0, mimoTap = repcap.MimoTap.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) spread (AS) of the cluster. \n
			:param dep_zen_spread: float Range: 1 to 75
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(dep_zen_spread)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:DEParture:ZENith:SPRead {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:DEParture:ZENith:SPRead \n
		Snippet: value: float = driver.source.fsimulator.scm.tap.departure.zenith.spread.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the AoA (angle of arrival) / AoD (angle of departure) spread (AS) of the cluster. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: dep_zen_spread: No help available"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:DEParture:ZENith:SPRead?')
		return Conversions.str_to_float(response)
