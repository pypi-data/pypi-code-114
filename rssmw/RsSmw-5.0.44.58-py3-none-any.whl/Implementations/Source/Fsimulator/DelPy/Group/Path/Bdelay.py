from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bdelay:
	"""Bdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bdelay", core, parent)

	def set(self, bdelay: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:BDELay \n
		Snippet: driver.source.fsimulator.delPy.group.path.bdelay.set(bdelay = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the basic group delay. \n
			:param bdelay: float Range: depends on the installed options* *) See 'Major differences between R&S SMW-B14 and R&S SMW-B15'.
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(bdelay)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:BDELay {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:BDELay \n
		Snippet: value: float = driver.source.fsimulator.delPy.group.path.bdelay.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the basic group delay. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: bdelay: float Range: depends on the installed options* *) See 'Major differences between R&S SMW-B14 and R&S SMW-B15'."""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:BDELay?')
		return Conversions.str_to_float(response)
