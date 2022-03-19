from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)

	# noinspection PyTypeChecker
	def get_esegment(self) -> enums.ArbWaveSegmRest:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:ESEGment \n
		Snippet: value: enums.ArbWaveSegmRest = driver.source.bb.arbitrary.wsegment.configure.marker.get_esegment() \n
		Enables/disables the generation of an additional marker restart signal at the beginning of the first segment (FSEGment)
		or at the beginning of each segment (ESEGment) . If additional marker generation is enabled, the existing marker signals
		in the individual segment waveform files are not considered. \n
			:return: mode: OFF| MRK1| MRK2| MRK3| MRK4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:ESEGment?')
		return Conversions.str_to_scalar_enum(response, enums.ArbWaveSegmRest)

	def set_esegment(self, mode: enums.ArbWaveSegmRest) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:ESEGment \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.marker.set_esegment(mode = enums.ArbWaveSegmRest.MRK1) \n
		Enables/disables the generation of an additional marker restart signal at the beginning of the first segment (FSEGment)
		or at the beginning of each segment (ESEGment) . If additional marker generation is enabled, the existing marker signals
		in the individual segment waveform files are not considered. \n
			:param mode: OFF| MRK1| MRK2| MRK3| MRK4
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbWaveSegmRest)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:ESEGment {param}')

	# noinspection PyTypeChecker
	def get_fsegment(self) -> enums.ArbWaveSegmRest:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:FSEGment \n
		Snippet: value: enums.ArbWaveSegmRest = driver.source.bb.arbitrary.wsegment.configure.marker.get_fsegment() \n
		Enables/disables the generation of an additional marker restart signal at the beginning of the first segment (FSEGment)
		or at the beginning of each segment (ESEGment) . If additional marker generation is enabled, the existing marker signals
		in the individual segment waveform files are not considered. \n
			:return: mode: OFF| MRK1| MRK2| MRK3| MRK4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:FSEGment?')
		return Conversions.str_to_scalar_enum(response, enums.ArbWaveSegmRest)

	def set_fsegment(self, mode: enums.ArbWaveSegmRest) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:FSEGment \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.marker.set_fsegment(mode = enums.ArbWaveSegmRest.MRK1) \n
		Enables/disables the generation of an additional marker restart signal at the beginning of the first segment (FSEGment)
		or at the beginning of each segment (ESEGment) . If additional marker generation is enabled, the existing marker signals
		in the individual segment waveform files are not considered. \n
			:param mode: OFF| MRK1| MRK2| MRK3| MRK4
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbWaveSegmRest)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:FSEGment {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbWaveSegmMarkMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:MODE \n
		Snippet: value: enums.ArbWaveSegmMarkMode = driver.source.bb.arbitrary.wsegment.configure.marker.get_mode() \n
		Defines the way the marker information within the separate segments is processed. \n
			:return: mode: IGNore| TAKE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbWaveSegmMarkMode)

	def set_mode(self, mode: enums.ArbWaveSegmMarkMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:MARKer:MODE \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.marker.set_mode(mode = enums.ArbWaveSegmMarkMode.IGNore) \n
		Defines the way the marker information within the separate segments is processed. \n
			:param mode: IGNore| TAKE
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbWaveSegmMarkMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:MARKer:MODE {param}')
