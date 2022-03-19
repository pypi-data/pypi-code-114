from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isdbt:
	"""Isdbt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isdbt", core, parent)

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.CodingInputSignalInputAsi:
		"""SCPI: [SOURce]:[IQCoder]:ISDBt:INPut \n
		Snippet: value: enums.CodingInputSignalInputAsi = driver.source.iqcoder.isdbt.get_input_py() \n
		No command help available \n
			:return: ipart_nput: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:ISDBt:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputAsi)

	def set_input_py(self, ipart_nput: enums.CodingInputSignalInputAsi) -> None:
		"""SCPI: [SOURce]:[IQCoder]:ISDBt:INPut \n
		Snippet: driver.source.iqcoder.isdbt.set_input_py(ipart_nput = enums.CodingInputSignalInputAsi.ASI1) \n
		No command help available \n
			:param ipart_nput: No help available
		"""
		param = Conversions.enum_scalar_to_str(ipart_nput, enums.CodingInputSignalInputAsi)
		self._core.io.write(f'SOURce:IQCoder:ISDBt:INPut {param}')
