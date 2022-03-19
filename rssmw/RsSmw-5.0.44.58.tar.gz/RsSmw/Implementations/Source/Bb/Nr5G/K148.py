from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K148:
	"""K148 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k148", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:K148:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.k148.get_state() \n
		No command help available \n
			:return: opt_state_k_148: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:K148:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, opt_state_k_148: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:K148:STATe \n
		Snippet: driver.source.bb.nr5G.k148.set_state(opt_state_k_148 = False) \n
		No command help available \n
			:param opt_state_k_148: No help available
		"""
		param = Conversions.bool_to_str(opt_state_k_148)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:K148:STATe {param}')
