from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.wlad.pconfig.data.get_dselection() \n
		Selects a data list, for the DLIST data source selection. The lists are stored as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name without the path and the file extension. \n
			:return: dselection: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:DSELection \n
		Snippet: driver.source.bb.wlad.pconfig.data.set_dselection(dselection = '1') \n
		Selects a data list, for the DLIST data source selection. The lists are stored as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name without the path and the file extension. \n
			:param dselection: string
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:DSELection {param}')

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:LENGth \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.data.get_length() \n
		Sets the size of the data field in bytes. The data length is related to the number of data symbols that is set with
		BB:WLAD:PCON:DATA:SYMB. Whenever the data length changes, the number of data symbols is updated and vice versa. \n
			:return: length: integer Range: 1 to 262107
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:LENGth \n
		Snippet: driver.source.bb.wlad.pconfig.data.set_length(length = 1) \n
		Sets the size of the data field in bytes. The data length is related to the number of data symbols that is set with
		BB:WLAD:PCON:DATA:SYMB. Whenever the data length changes, the number of data symbols is updated and vice versa. \n
			:param length: integer Range: 1 to 262107
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:LENGth {param}')

	def get_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:RATE \n
		Snippet: value: float = driver.source.bb.wlad.pconfig.data.get_rate() \n
		Queries the PPDU data rate. \n
			:return: rate: float Range: 0 to LONG_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:RATE?')
		return Conversions.str_to_float(response)

	def get_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:SYMBols \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.data.get_symbols() \n
		No command help available \n
			:return: symbols: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:SYMBols?')
		return Conversions.str_to_int(response)

	def set_symbols(self, symbols: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA:SYMBols \n
		Snippet: driver.source.bb.wlad.pconfig.data.set_symbols(symbols = 1) \n
		No command help available \n
			:param symbols: No help available
		"""
		param = Conversions.decimal_value_to_str(symbols)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:DATA:SYMBols {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.WlannDataSource:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA \n
		Snippet: value: enums.WlannDataSource = driver.source.bb.wlad.pconfig.data.get_value() \n
		Sets the data source. \n
			:return: data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| AMPDU
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.WlannDataSource)

	def set_value(self, data: enums.WlannDataSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:DATA \n
		Snippet: driver.source.bb.wlad.pconfig.data.set_value(data = enums.WlannDataSource.AMPDU) \n
		Sets the data source. \n
			:param data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| AMPDU
		"""
		param = Conversions.enum_scalar_to_str(data, enums.WlannDataSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
