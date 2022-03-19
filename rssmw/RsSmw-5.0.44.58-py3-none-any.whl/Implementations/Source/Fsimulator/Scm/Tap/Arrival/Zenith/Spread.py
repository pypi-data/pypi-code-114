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

	def set(self, arr_zen_spr: float, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:ARRival:ZENith:SPRead \n
		Snippet: driver.source.fsimulator.scm.tap.arrival.zenith.spread.set(arr_zen_spr = 1.0, mimoTap = repcap.MimoTap.Default) \n
		Sets the ZoA (zenith of arrival) spread of the cluster. \n
			:param arr_zen_spr: float Range: 0 to 75
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.decimal_value_to_str(arr_zen_spr)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:ARRival:ZENith:SPRead {param}')

	def get(self, mimoTap=repcap.MimoTap.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:ARRival:ZENith:SPRead \n
		Snippet: value: float = driver.source.fsimulator.scm.tap.arrival.zenith.spread.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the ZoA (zenith of arrival) spread of the cluster. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: arr_zen_spr: float Range: 0 to 75"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:ARRival:ZENith:SPRead?')
		return Conversions.str_to_float(response)
