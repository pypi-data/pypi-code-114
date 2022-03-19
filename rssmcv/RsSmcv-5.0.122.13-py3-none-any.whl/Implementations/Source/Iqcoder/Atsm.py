from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atsm:
	"""Atsm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atsm", core, parent)

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.CodingInputSignalInputSfe:
		"""SCPI: [SOURce]:[IQCoder]:ATSM:INPut \n
		Snippet: value: enums.CodingInputSignalInputSfe = driver.source.iqcoder.atsm.get_input_py() \n
		No command help available \n
			:return: atscmh_input: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:ATSM:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputSfe)

	def set_input_py(self, atscmh_input: enums.CodingInputSignalInputSfe) -> None:
		"""SCPI: [SOURce]:[IQCoder]:ATSM:INPut \n
		Snippet: driver.source.iqcoder.atsm.set_input_py(atscmh_input = enums.CodingInputSignalInputSfe.ASI1) \n
		No command help available \n
			:param atscmh_input: No help available
		"""
		param = Conversions.enum_scalar_to_str(atscmh_input, enums.CodingInputSignalInputSfe)
		self._core.io.write(f'SOURce:IQCoder:ATSM:INPut {param}')
