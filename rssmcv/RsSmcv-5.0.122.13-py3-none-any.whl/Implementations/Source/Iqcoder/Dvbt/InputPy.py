from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.CodingInputSignalInputAsi:
		"""SCPI: [SOURce]:[IQCoder]:DVBT:INPut:LOW \n
		Snippet: value: enums.CodingInputSignalInputAsi = driver.source.iqcoder.dvbt.inputPy.get_low() \n
		No command help available \n
			:return: ipart_nput_lp: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBT:INPut:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputAsi)

	def set_low(self, ipart_nput_lp: enums.CodingInputSignalInputAsi) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBT:INPut:LOW \n
		Snippet: driver.source.iqcoder.dvbt.inputPy.set_low(ipart_nput_lp = enums.CodingInputSignalInputAsi.ASI1) \n
		No command help available \n
			:param ipart_nput_lp: No help available
		"""
		param = Conversions.enum_scalar_to_str(ipart_nput_lp, enums.CodingInputSignalInputAsi)
		self._core.io.write(f'SOURce:IQCoder:DVBT:INPut:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.CodingInputSignalInputAsi:
		"""SCPI: [SOURce]:[IQCoder]:DVBT:INPut:[HIGH] \n
		Snippet: value: enums.CodingInputSignalInputAsi = driver.source.iqcoder.dvbt.inputPy.get_high() \n
		No command help available \n
			:return: ipart_nput: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBT:INPut:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputAsi)

	def set_high(self, ipart_nput: enums.CodingInputSignalInputAsi) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBT:INPut:[HIGH] \n
		Snippet: driver.source.iqcoder.dvbt.inputPy.set_high(ipart_nput = enums.CodingInputSignalInputAsi.ASI1) \n
		No command help available \n
			:param ipart_nput: No help available
		"""
		param = Conversions.enum_scalar_to_str(ipart_nput, enums.CodingInputSignalInputAsi)
		self._core.io.write(f'SOURce:IQCoder:DVBT:INPut:HIGH {param}')
