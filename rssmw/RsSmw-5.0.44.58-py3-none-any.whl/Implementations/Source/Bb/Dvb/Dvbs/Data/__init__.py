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
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.dvb.dvbs.data.get_dselection() \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: fselection: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, fselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:DSELection \n
		Snippet: driver.source.bb.dvb.dvbs.data.set_dselection(fselection = '1') \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param fselection: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(fselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:DATA:DSELection {param}')

	def get_gselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:GSELection \n
		Snippet: value: str = driver.source.bb.dvb.dvbs.data.get_gselection() \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: fselection: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:DATA:GSELection?')
		return trim_str_response(response)

	def set_gselection(self, fselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:GSELection \n
		Snippet: driver.source.bb.dvb.dvbs.data.set_gselection(fselection = '1') \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param fselection: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(fselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:DATA:GSELection {param}')

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:LENGth \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.data.get_length() \n
		Sets the data length. \n
			:return: dlength: integer Range: 1 to 65536, Unit: Bytes
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:DATA:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, dlength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:LENGth \n
		Snippet: driver.source.bb.dvb.dvbs.data.set_length(dlength = 1) \n
		Sets the data length. \n
			:param dlength: integer Range: 1 to 65536, Unit: Bytes
		"""
		param = Conversions.decimal_value_to_str(dlength)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:DATA:LENGth {param}')

	def get_tselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:TSELection \n
		Snippet: value: str = driver.source.bb.dvb.dvbs.data.get_tselection() \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: fselection: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:DATA:TSELection?')
		return trim_str_response(response)

	def set_tselection(self, fselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA:TSELection \n
		Snippet: driver.source.bb.dvb.dvbs.data.set_tselection(fselection = '1') \n
		Selects an existing data list, transport file (TS) or GSE file from the default or from the specific directory.
			INTRO_CMD_HELP: Selects the clock source: \n
			- TS files are files with extension *.gts, *.ts, or *.trp.
			- GSE files are files with extension *.gse
			- Data lists are files with extension *.dm_iqd
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param fselection: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(fselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:DATA:TSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DvbDataSource:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA \n
		Snippet: value: enums.DvbDataSource = driver.source.bb.dvb.dvbs.data.get_value() \n
		Selects the data source. \n
			:return: data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| TFILe| GFILe PATTern To set the bit pattern, use the command [:SOURcehw]:BB:DVB:DVBS|DVBX:DATA:PATTern. DLISt|TFILe|GFILe To select the data list, TS file or the GSE file, use the command [:SOURcehw]:BB:DVB:DVBS|DVBX:DATA:DSELection|TSELection|GSELection.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DvbDataSource)

	def set_value(self, data: enums.DvbDataSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:DATA \n
		Snippet: driver.source.bb.dvb.dvbs.data.set_value(data = enums.DvbDataSource.DLISt) \n
		Selects the data source. \n
			:param data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| TFILe| GFILe PATTern To set the bit pattern, use the command [:SOURcehw]:BB:DVB:DVBS|DVBX:DATA:PATTern. DLISt|TFILe|GFILe To select the data list, TS file or the GSE file, use the command [:SOURcehw]:BB:DVB:DVBS|DVBX:DATA:DSELection|TSELection|GSELection.
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DvbDataSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
