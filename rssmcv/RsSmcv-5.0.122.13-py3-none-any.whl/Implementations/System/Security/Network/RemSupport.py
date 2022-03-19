from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RemSupport:
	"""RemSupport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remSupport", core, parent)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:SECurity:NETWork:REMSupport:[STATe] \n
		Snippet: value: bool = driver.system.security.network.remSupport.get_state() \n
		No command help available \n
			:return: net_rem_support: No help available
		"""
		response = self._core.io.query_str('SYSTem:SECurity:NETWork:REMSupport:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, net_rem_support: bool) -> None:
		"""SCPI: SYSTem:SECurity:NETWork:REMSupport:[STATe] \n
		Snippet: driver.system.security.network.remSupport.set_state(net_rem_support = False) \n
		No command help available \n
			:param net_rem_support: No help available
		"""
		param = Conversions.bool_to_str(net_rem_support)
		self._core.io.write(f'SYSTem:SECurity:NETWork:REMSupport:STATe {param}')
