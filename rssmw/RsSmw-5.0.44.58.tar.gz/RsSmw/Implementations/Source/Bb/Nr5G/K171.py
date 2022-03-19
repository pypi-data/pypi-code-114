from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K171:
	"""K171 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k171", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:K171:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.k171.get_state() \n
		No command help available \n
			:return: opt_state_k_171: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:K171:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, opt_state_k_171: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:K171:STATe \n
		Snippet: driver.source.bb.nr5G.k171.set_state(opt_state_k_171 = False) \n
		No command help available \n
			:param opt_state_k_171: No help available
		"""
		param = Conversions.bool_to_str(opt_state_k_171)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:K171:STATe {param}')
