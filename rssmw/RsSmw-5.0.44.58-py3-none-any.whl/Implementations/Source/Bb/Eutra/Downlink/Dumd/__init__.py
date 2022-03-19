from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dumd:
	"""Dumd commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dumd", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	# noinspection PyTypeChecker
	def get_data(self) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.eutra.downlink.dumd.get_data() \n
		Selects the data source for dummy data. \n
			:return: data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:DUMD:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def set_data(self, data: enums.DataSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:DATA \n
		Snippet: driver.source.bb.eutra.downlink.dumd.set_data(data = enums.DataSourceA.DLISt) \n
		Selects the data source for dummy data. \n
			:param data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DUMD:DATA {param}')

	def get_dselect(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:DSELect \n
		Snippet: value: str = driver.source.bb.eutra.downlink.dumd.get_dselect() \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:return: filename: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:DUMD:DSELect?')
		return trim_str_response(response)

	def set_dselect(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:DSELect \n
		Snippet: driver.source.bb.eutra.downlink.dumd.set_dselect(filename = '1') \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param filename: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DUMD:DSELect {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.ModulationD:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:MODulation \n
		Snippet: value: enums.ModulationD = driver.source.bb.eutra.downlink.dumd.get_modulation() \n
		Selects modulation for dummy data. \n
			:return: modulation: QPSK| QAM16| QAM64 | QAM256 | QAM1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:DUMD:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationD)

	def set_modulation(self, modulation: enums.ModulationD) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:MODulation \n
		Snippet: driver.source.bb.eutra.downlink.dumd.set_modulation(modulation = enums.ModulationD.QAM1024) \n
		Selects modulation for dummy data. \n
			:param modulation: QPSK| QAM16| QAM64 | QAM256 | QAM1024
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationD)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DUMD:MODulation {param}')

	def get_op_sub_frames(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:OPSubframes \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.dumd.get_op_sub_frames() \n
		If the OCNG is used, you can disable (omit) the OCNG transmission in the non-muted PRS subframes. \n
			:return: omit_prs_sf: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:DUMD:OPSubframes?')
		return Conversions.str_to_bool(response)

	def set_op_sub_frames(self, omit_prs_sf: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:OPSubframes \n
		Snippet: driver.source.bb.eutra.downlink.dumd.set_op_sub_frames(omit_prs_sf = False) \n
		If the OCNG is used, you can disable (omit) the OCNG transmission in the non-muted PRS subframes. \n
			:param omit_prs_sf: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(omit_prs_sf)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DUMD:OPSubframes {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:POWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.dumd.get_power() \n
		Sets the power for dummy data. \n
			:return: power: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:DUMD:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DUMD:POWer \n
		Snippet: driver.source.bb.eutra.downlink.dumd.set_power(power = 1.0) \n
		Sets the power for dummy data. \n
			:param power: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DUMD:POWer {param}')

	def clone(self) -> 'Dumd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dumd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
