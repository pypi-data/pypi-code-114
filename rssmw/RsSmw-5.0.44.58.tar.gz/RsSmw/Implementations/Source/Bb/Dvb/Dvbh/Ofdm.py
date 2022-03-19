from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ofdm:
	"""Ofdm commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofdm", core, parent)

	# noinspection PyTypeChecker
	def get_alpha(self) -> enums.NumbersB:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:ALPHa \n
		Snippet: value: enums.NumbersB = driver.source.bb.dvb.dvbh.ofdm.get_alpha() \n
		Selects the α value. This value is used to shape the constellation of the modulation. For DVB-H, this value is always 1. \n
			:return: alpha: 1| 2| 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:OFDM:ALPHa?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersB)

	def set_alpha(self, alpha: enums.NumbersB) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:ALPHa \n
		Snippet: driver.source.bb.dvb.dvbh.ofdm.set_alpha(alpha = enums.NumbersB._1) \n
		Selects the α value. This value is used to shape the constellation of the modulation. For DVB-H, this value is always 1. \n
			:param alpha: 1| 2| 4
		"""
		param = Conversions.enum_scalar_to_str(alpha, enums.NumbersB)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:OFDM:ALPHa {param}')

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.DvbSysBand:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:BWIDth \n
		Snippet: value: enums.DvbSysBand = driver.source.bb.dvb.dvbh.ofdm.get_bandwidth() \n
		Selects the system bandwidth. \n
			:return: bwidth: 5| 6| 7| 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:OFDM:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.DvbSysBand)

	def set_bandwidth(self, bwidth: enums.DvbSysBand) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:BWIDth \n
		Snippet: driver.source.bb.dvb.dvbh.ofdm.set_bandwidth(bwidth = enums.DvbSysBand._5) \n
		Selects the system bandwidth. \n
			:param bwidth: 5| 6| 7| 8
		"""
		param = Conversions.enum_scalar_to_str(bwidth, enums.DvbSysBand)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:OFDM:BWIDth {param}')

	# noinspection PyTypeChecker
	def get_ginterval(self) -> enums.DvbGuardInt:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:GINTerval \n
		Snippet: value: enums.DvbGuardInt = driver.source.bb.dvb.dvbh.ofdm.get_ginterval() \n
		Selects the OFDM/RF guard interval. \n
			:return: ginterval: GI1D4| GI1D8| GI1D16| GI1D32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:OFDM:GINTerval?')
		return Conversions.str_to_scalar_enum(response, enums.DvbGuardInt)

	def set_ginterval(self, ginterval: enums.DvbGuardInt) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:GINTerval \n
		Snippet: driver.source.bb.dvb.dvbh.ofdm.set_ginterval(ginterval = enums.DvbGuardInt.GI1D16) \n
		Selects the OFDM/RF guard interval. \n
			:param ginterval: GI1D4| GI1D8| GI1D16| GI1D32
		"""
		param = Conversions.enum_scalar_to_str(ginterval, enums.DvbGuardInt)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:OFDM:GINTerval {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.ModulationC:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:MODulation \n
		Snippet: value: enums.ModulationC = driver.source.bb.dvb.dvbh.ofdm.get_modulation() \n
		Selects the constellation for the OFDM modulation. \n
			:return: modulation: QPSK| QAM16| QAM64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:OFDM:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationC)

	def set_modulation(self, modulation: enums.ModulationC) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:OFDM:MODulation \n
		Snippet: driver.source.bb.dvb.dvbh.ofdm.set_modulation(modulation = enums.ModulationC.QAM16) \n
		Selects the constellation for the OFDM modulation. \n
			:param modulation: QPSK| QAM16| QAM64
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationC)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:OFDM:MODulation {param}')
