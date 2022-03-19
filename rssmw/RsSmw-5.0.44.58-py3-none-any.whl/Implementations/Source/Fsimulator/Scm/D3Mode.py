from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class D3Mode:
	"""D3Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("d3Mode", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:D3Mode:STATe \n
		Snippet: value: bool = driver.source.fsimulator.scm.d3Mode.get_state() \n
		Enables the 3D geometry-based channel model. \n
			:return: three_dmode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:D3Mode:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, three_dmode: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:D3Mode:STATe \n
		Snippet: driver.source.fsimulator.scm.d3Mode.set_state(three_dmode = False) \n
		Enables the 3D geometry-based channel model. \n
			:param three_dmode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(three_dmode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:D3Mode:STATe {param}')
