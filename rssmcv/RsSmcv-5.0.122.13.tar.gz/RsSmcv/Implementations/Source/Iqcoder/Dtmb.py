from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtmb:
	"""Dtmb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtmb", core, parent)

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.CodingInputSignalInputAsi:
		"""SCPI: [SOURce]:[IQCoder]:DTMB:INPut \n
		Snippet: value: enums.CodingInputSignalInputAsi = driver.source.iqcoder.dtmb.get_input_py() \n
		No command help available \n
			:return: dtmb_source: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DTMB:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputAsi)

	def set_input_py(self, dtmb_source: enums.CodingInputSignalInputAsi) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DTMB:INPut \n
		Snippet: driver.source.iqcoder.dtmb.set_input_py(dtmb_source = enums.CodingInputSignalInputAsi.ASI1) \n
		No command help available \n
			:param dtmb_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(dtmb_source, enums.CodingInputSignalInputAsi)
		self._core.io.write(f'SOURce:IQCoder:DTMB:INPut {param}')
