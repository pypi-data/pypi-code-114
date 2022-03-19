from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tappend:
	"""Tappend commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tappend", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:DESTination:FILE:TAPPend:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.logging.destination.file.tappend.get_state() \n
		Adds a timestamp to the filename. \n
			:return: append: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:DESTination:FILE:TAPPend:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, append: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:DESTination:FILE:TAPPend:[STATe] \n
		Snippet: driver.source.bb.gnss.logging.destination.file.tappend.set_state(append = False) \n
		Adds a timestamp to the filename. \n
			:param append: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(append)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:DESTination:FILE:TAPPend:STATe {param}')
