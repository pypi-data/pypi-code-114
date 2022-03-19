from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lockout:
	"""Lockout commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lockout", core, parent)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST<HW>:REMote:LOCKout:[STATe] \n
		Snippet: driver.test.remote.lockout.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST<HwInstance>:REMote:LOCKout:STATe {param}')
