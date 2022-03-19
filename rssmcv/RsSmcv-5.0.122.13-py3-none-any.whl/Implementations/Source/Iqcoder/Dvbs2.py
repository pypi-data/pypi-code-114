from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbs2:
	"""Dvbs2 commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbs2", core, parent)

	# noinspection PyTypeChecker
	def get_constel(self) -> enums.Dvbs2CodingConstelSfe:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:CONStel \n
		Snippet: value: enums.Dvbs2CodingConstelSfe = driver.source.iqcoder.dvbs2.get_constel() \n
		No command help available \n
			:return: constel_sfe: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBS2:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2CodingConstelSfe)

	def set_constel(self, constel_sfe: enums.Dvbs2CodingConstelSfe) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:CONStel \n
		Snippet: driver.source.iqcoder.dvbs2.set_constel(constel_sfe = enums.Dvbs2CodingConstelSfe.A16) \n
		No command help available \n
			:param constel_sfe: No help available
		"""
		param = Conversions.enum_scalar_to_str(constel_sfe, enums.Dvbs2CodingConstelSfe)
		self._core.io.write(f'SOURce:IQCoder:DVBS2:CONStel {param}')

	# noinspection PyTypeChecker
	def get_fec_frame(self) -> enums.BicmFecFrame:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:FECFrame \n
		Snippet: value: enums.BicmFecFrame = driver.source.iqcoder.dvbs2.get_fec_frame() \n
		No command help available \n
			:return: fec_frame_sfe: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBS2:FECFrame?')
		return Conversions.str_to_scalar_enum(response, enums.BicmFecFrame)

	def set_fec_frame(self, fec_frame_sfe: enums.BicmFecFrame) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:FECFrame \n
		Snippet: driver.source.iqcoder.dvbs2.set_fec_frame(fec_frame_sfe = enums.BicmFecFrame.NORMal) \n
		No command help available \n
			:param fec_frame_sfe: No help available
		"""
		param = Conversions.enum_scalar_to_str(fec_frame_sfe, enums.BicmFecFrame)
		self._core.io.write(f'SOURce:IQCoder:DVBS2:FECFrame {param}')

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.CodingInputSignalInputAsi:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:INPut \n
		Snippet: value: enums.CodingInputSignalInputAsi = driver.source.iqcoder.dvbs2.get_input_py() \n
		No command help available \n
			:return: ipart_nput_sfe: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBS2:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputAsi)

	def set_input_py(self, ipart_nput_sfe: enums.CodingInputSignalInputAsi) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:INPut \n
		Snippet: driver.source.iqcoder.dvbs2.set_input_py(ipart_nput_sfe = enums.CodingInputSignalInputAsi.ASI1) \n
		No command help available \n
			:param ipart_nput_sfe: No help available
		"""
		param = Conversions.enum_scalar_to_str(ipart_nput_sfe, enums.CodingInputSignalInputAsi)
		self._core.io.write(f'SOURce:IQCoder:DVBS2:INPut {param}')

	def get_pilots(self) -> bool:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:PILots \n
		Snippet: value: bool = driver.source.iqcoder.dvbs2.get_pilots() \n
		No command help available \n
			:return: pilots_sfe: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBS2:PILots?')
		return Conversions.str_to_bool(response)

	def set_pilots(self, pilots_sfe: bool) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:PILots \n
		Snippet: driver.source.iqcoder.dvbs2.set_pilots(pilots_sfe = False) \n
		No command help available \n
			:param pilots_sfe: No help available
		"""
		param = Conversions.bool_to_str(pilots_sfe)
		self._core.io.write(f'SOURce:IQCoder:DVBS2:PILots {param}')

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.Dvbs2CodingCoderateSfe:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:RATE \n
		Snippet: value: enums.Dvbs2CodingCoderateSfe = driver.source.iqcoder.dvbs2.get_rate() \n
		No command help available \n
			:return: rate_sfe: No help available
		"""
		response = self._core.io.query_str('SOURce:IQCoder:DVBS2:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2CodingCoderateSfe)

	def set_rate(self, rate_sfe: enums.Dvbs2CodingCoderateSfe) -> None:
		"""SCPI: [SOURce]:[IQCoder]:DVBS2:RATE \n
		Snippet: driver.source.iqcoder.dvbs2.set_rate(rate_sfe = enums.Dvbs2CodingCoderateSfe.R1_2) \n
		No command help available \n
			:param rate_sfe: No help available
		"""
		param = Conversions.enum_scalar_to_str(rate_sfe, enums.Dvbs2CodingCoderateSfe)
		self._core.io.write(f'SOURce:IQCoder:DVBS2:RATE {param}')
