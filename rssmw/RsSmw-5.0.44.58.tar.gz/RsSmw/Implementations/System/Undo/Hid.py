from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hid:
	"""Hid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hid", core, parent)

	def set_select(self, select: int) -> None:
		"""SCPI: SYSTem:UNDO:HID:SELect \n
		Snippet: driver.system.undo.hid.set_select(select = 1) \n
		No command help available \n
			:param select: No help available
		"""
		param = Conversions.decimal_value_to_str(select)
		self._core.io.write(f'SYSTem:UNDO:HID:SELect {param}')
