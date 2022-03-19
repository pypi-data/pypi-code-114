from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hardware:
	"""Hardware commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hardware", core, parent)

	def get_state(self) -> bool:
		"""SCPI: TEST:FADer:HARDware:STATe \n
		Snippet: value: bool = driver.test.fader.hardware.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('TEST:FADer:HARDware:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST:FADer:HARDware:STATe \n
		Snippet: driver.test.fader.hardware.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST:FADer:HARDware:STATe {param}')
