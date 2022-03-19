from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qhs:
	"""Qhs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhs", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:QHS:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.qhs.get_state() \n
		No command help available \n
			:return: qhs_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:QHS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qhs_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:QHS:STATe \n
		Snippet: driver.source.bb.btooth.qhs.set_state(qhs_state = False) \n
		No command help available \n
			:param qhs_state: No help available
		"""
		param = Conversions.bool_to_str(qhs_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:QHS:STATe {param}')
