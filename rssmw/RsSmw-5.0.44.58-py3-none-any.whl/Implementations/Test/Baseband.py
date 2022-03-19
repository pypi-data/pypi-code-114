from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Baseband:
	"""Baseband commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("baseband", core, parent)

	def get_log(self) -> str:
		"""SCPI: TEST:BASeband:LOG \n
		Snippet: value: str = driver.test.baseband.get_log() \n
		Queries the log message reported during the baseband test. This is a password-protected function. Unlock the protection
		level 1 to access it. See method RsSmw.System.Protect.State.set. \n
			:return: test_baseband_log: string
		"""
		response = self._core.io.query_str('TEST:BASeband:LOG?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Test:
		"""SCPI: TEST:BASeband \n
		Snippet: value: enums.Test = driver.test.baseband.get_value() \n
		Queries the result of the baseband selftest. \n
			:return: test_bb_error: 0| 1| RUNning| STOPped
		"""
		response = self._core.io.query_str('TEST:BASeband?')
		return Conversions.str_to_scalar_enum(response, enums.Test)
