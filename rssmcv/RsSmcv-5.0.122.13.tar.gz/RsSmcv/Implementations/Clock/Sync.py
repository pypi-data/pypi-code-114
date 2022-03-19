from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	def get_state(self) -> bool:
		"""SCPI: CLOCk:SYNC:[STATe] \n
		Snippet: value: bool = driver.clock.sync.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CLOCk:SYNC:STATe?')
		return Conversions.str_to_bool(response)
