from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transaction:
	"""Transaction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transaction", core, parent)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:DEXChange:TRANsaction:STATe \n
		Snippet: value: bool = driver.system.dexchange.transaction.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SYSTem:DEXChange:TRANsaction:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SYSTem:DEXChange:TRANsaction:STATe \n
		Snippet: driver.system.dexchange.transaction.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:DEXChange:TRANsaction:STATe {param}')
