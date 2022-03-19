from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cphase:
	"""Cphase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cphase", core, parent)

	def set(self, cphase: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:CPHase \n
		Snippet: driver.source.fsimulator.delPy.group.path.cphase.set(cphase = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the start phase rotation. \n
			:param cphase: float Range: 0 to 359.9, Unit: DEG
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(cphase)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CPHase {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:CPHase \n
		Snippet: value: float = driver.source.fsimulator.delPy.group.path.cphase.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the start phase rotation. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: cphase: float Range: 0 to 359.9, Unit: DEG"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CPHase?')
		return Conversions.str_to_float(response)
