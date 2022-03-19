from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:[LP]:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.dvb.dvbh.lp.data.get_dselection() \n
		Selects an existing TS file from the default directory or from the specific directory. TS files are files with extension
		*.gts, *.ts, or *.trp. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file
		handling in the default and in a specific directory. \n
			:return: dselection: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:LP:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:[LP]:DATA:DSELection \n
		Snippet: driver.source.bb.dvb.dvbh.lp.data.set_dselection(dselection = '1') \n
		Selects an existing TS file from the default directory or from the specific directory. TS files are files with extension
		*.gts, *.ts, or *.trp. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file
		handling in the default and in a specific directory. \n
			:param dselection: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:LP:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DvbDataSour:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:[LP]:DATA \n
		Snippet: value: enums.DvbDataSour = driver.source.bb.dvb.dvbh.lp.data.get_value() \n
		Selects the data source to be used. \n
			:return: data: PAC0| PAC1| PN15| PN23| DLISt ZERO Internal 0 is used. ONE Internal 1 is used. PN15/23 Internally generated PRBS data as per CCITT with period lengths between (29-1 and 223-1) . DLISt Internal data from a TS file is used.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:LP:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DvbDataSour)

	def set_value(self, data: enums.DvbDataSour) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:[LP]:DATA \n
		Snippet: driver.source.bb.dvb.dvbh.lp.data.set_value(data = enums.DvbDataSour.DLISt) \n
		Selects the data source to be used. \n
			:param data: PAC0| PAC1| PN15| PN23| DLISt ZERO Internal 0 is used. ONE Internal 1 is used. PN15/23 Internally generated PRBS data as per CCITT with period lengths between (29-1 and 223-1) . DLISt Internal data from a TS file is used.
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DvbDataSour)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:LP:DATA {param}')
