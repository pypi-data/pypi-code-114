from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vh:
	"""Vh commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vh", core, parent)

	def set(self, phase_vh: float, mimoTap=repcap.MimoTap.Default, subPath=repcap.SubPath.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:SUBPath<DI>:PHASe:VH \n
		Snippet: driver.source.fsimulator.scm.tap.subPath.phase.vh.set(phase_vh = 1.0, mimoTap = repcap.MimoTap.Default, subPath = repcap.SubPath.Default) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param phase_vh: No help available
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param subPath: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPath')
		"""
		param = Conversions.decimal_value_to_str(phase_vh)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		subPath_cmd_val = self._cmd_group.get_repcap_cmd_value(subPath, repcap.SubPath)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:SUBPath{subPath_cmd_val}:PHASe:VH {param}')

	def get(self, mimoTap=repcap.MimoTap.Default, subPath=repcap.SubPath.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:TAP<ST>:SUBPath<DI>:PHASe:VH \n
		Snippet: value: float = driver.source.fsimulator.scm.tap.subPath.phase.vh.get(mimoTap = repcap.MimoTap.Default, subPath = repcap.SubPath.Default) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param subPath: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPath')
			:return: phase_vh: No help available"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		subPath_cmd_val = self._cmd_group.get_repcap_cmd_value(subPath, repcap.SubPath)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:SCM:TAP{mimoTap_cmd_val}:SUBPath{subPath_cmd_val}:PHASe:VH?')
		return Conversions.str_to_float(response)
