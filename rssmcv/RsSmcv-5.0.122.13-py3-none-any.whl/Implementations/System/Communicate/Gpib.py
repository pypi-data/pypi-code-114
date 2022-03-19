from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gpib:
	"""Gpib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gpib", core, parent)

	# noinspection PyTypeChecker
	def get_lterminator(self) -> enums.IecTermMode:
		"""SCPI: SYSTem:COMMunicate:GPIB:LTERminator \n
		Snippet: value: enums.IecTermMode = driver.system.communicate.gpib.get_lterminator() \n
		No command help available \n
			:return: lterminator: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:GPIB:LTERminator?')
		return Conversions.str_to_scalar_enum(response, enums.IecTermMode)

	def set_lterminator(self, lterminator: enums.IecTermMode) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB:LTERminator \n
		Snippet: driver.system.communicate.gpib.set_lterminator(lterminator = enums.IecTermMode.EOI) \n
		No command help available \n
			:param lterminator: No help available
		"""
		param = Conversions.enum_scalar_to_str(lterminator, enums.IecTermMode)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:LTERminator {param}')
