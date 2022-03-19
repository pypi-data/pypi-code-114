from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Res:
	"""Res commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("res", core, parent)

	# noinspection PyTypeChecker
	def get_color(self) -> enums.Colour:
		"""SCPI: TEST:RES:COLor \n
		Snippet: value: enums.Colour = driver.test.res.get_color() \n
		No command help available \n
			:return: color: No help available
		"""
		response = self._core.io.query_str('TEST:RES:COLor?')
		return Conversions.str_to_scalar_enum(response, enums.Colour)

	def set_color(self, color: enums.Colour) -> None:
		"""SCPI: TEST:RES:COLor \n
		Snippet: driver.test.res.set_color(color = enums.Colour.GREen) \n
		No command help available \n
			:param color: No help available
		"""
		param = Conversions.enum_scalar_to_str(color, enums.Colour)
		self._core.io.write(f'TEST:RES:COLor {param}')

	def get_text(self) -> str:
		"""SCPI: TEST:RES:TEXT \n
		Snippet: value: str = driver.test.res.get_text() \n
		No command help available \n
			:return: text: No help available
		"""
		response = self._core.io.query_str('TEST:RES:TEXT?')
		return trim_str_response(response)

	def set_text(self, text: str) -> None:
		"""SCPI: TEST:RES:TEXT \n
		Snippet: driver.test.res.set_text(text = '1') \n
		No command help available \n
			:param text: No help available
		"""
		param = Conversions.value_to_quoted_str(text)
		self._core.io.write(f'TEST:RES:TEXT {param}')

	def get_wind(self) -> bool:
		"""SCPI: TEST:RES:WIND \n
		Snippet: value: bool = driver.test.res.get_wind() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('TEST:RES:WIND?')
		return Conversions.str_to_bool(response)

	def set_wind(self, state: bool) -> None:
		"""SCPI: TEST:RES:WIND \n
		Snippet: driver.test.res.set_wind(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST:RES:WIND {param}')
