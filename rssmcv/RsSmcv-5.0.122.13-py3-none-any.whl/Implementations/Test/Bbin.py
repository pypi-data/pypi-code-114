from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bbin:
	"""Bbin commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbin", core, parent)

	def get_rb_error(self) -> bool:
		"""SCPI: TEST<HW>:BBIN:RBERror \n
		Snippet: value: bool = driver.test.bbin.get_rb_error() \n
		No command help available \n
			:return: rb_error: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:BBIN:RBERror?')
		return Conversions.str_to_bool(response)

	def get_value(self) -> bool:
		"""SCPI: TEST:BBIN \n
		Snippet: value: bool = driver.test.bbin.get_value() \n
		No command help available \n
			:return: bbin: No help available
		"""
		response = self._core.io.query_str('TEST:BBIN?')
		return Conversions.str_to_bool(response)
