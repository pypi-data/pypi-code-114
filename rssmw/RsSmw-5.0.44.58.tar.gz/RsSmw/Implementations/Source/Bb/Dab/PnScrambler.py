from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnScrambler:
	"""PnScrambler commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnScrambler", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DAB:PNSCrambler:[STATe] \n
		Snippet: value: bool = driver.source.bb.dab.pnScrambler.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:PNSCrambler:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:PNSCrambler:[STATe] \n
		Snippet: driver.source.bb.dab.pnScrambler.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:PNSCrambler:STATe {param}')
