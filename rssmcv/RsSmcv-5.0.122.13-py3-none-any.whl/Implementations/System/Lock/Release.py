from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Release:
	"""Release commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("release", core, parent)

	def set_all(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:LOCK:RELease:ALL \n
		Snippet: driver.system.lock.release.set_all(pseudo_string = '1') \n
		Revokes the exclusive access to the instrument. \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:LOCK:RELease:ALL {param}')

	def set_value(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:LOCK:RELease \n
		Snippet: driver.system.lock.release.set_value(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:LOCK:RELease {param}')
