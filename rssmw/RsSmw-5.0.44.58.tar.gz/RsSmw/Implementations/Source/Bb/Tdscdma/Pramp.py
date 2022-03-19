from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramp", core, parent)

	def get_bb_only(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:BBONly \n
		Snippet: value: bool = driver.source.bb.tdscdma.pramp.get_bb_only() \n
		Activates or deactivates power ramping for the baseband signals. \n
			:return: bb_only: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:PRAMp:BBONly?')
		return Conversions.str_to_bool(response)

	def get_fdelay(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:FDELay \n
		Snippet: value: int = driver.source.bb.tdscdma.pramp.get_fdelay() \n
		Sets the offset in the falling edge of the envelope at the end of a burst. A positive value delays the ramp and a
		negative value causes an advance. \n
			:return: fdelay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:PRAMp:FDELay?')
		return Conversions.str_to_int(response)

	def set_fdelay(self, fdelay: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:FDELay \n
		Snippet: driver.source.bb.tdscdma.pramp.set_fdelay(fdelay = 1) \n
		Sets the offset in the falling edge of the envelope at the end of a burst. A positive value delays the ramp and a
		negative value causes an advance. \n
			:param fdelay: integer Range: -4 to 4
		"""
		param = Conversions.decimal_value_to_str(fdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:PRAMp:FDELay {param}')

	def get_rdelay(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:RDELay \n
		Snippet: value: int = driver.source.bb.tdscdma.pramp.get_rdelay() \n
		Sets the offset in the falling edge of the envelope at the end of a burst. A positive value delays the ramp and a
		negative value causes an advance. \n
			:return: rdelay: integer Range: -4 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:PRAMp:RDELay?')
		return Conversions.str_to_int(response)

	def set_rdelay(self, rdelay: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:RDELay \n
		Snippet: driver.source.bb.tdscdma.pramp.set_rdelay(rdelay = 1) \n
		Sets the offset in the falling edge of the envelope at the end of a burst. A positive value delays the ramp and a
		negative value causes an advance. \n
			:param rdelay: integer Range: -4 to 4
		"""
		param = Conversions.decimal_value_to_str(rdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:PRAMp:RDELay {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.RampFunc:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:SHAPe \n
		Snippet: value: enums.RampFunc = driver.source.bb.tdscdma.pramp.get_shape() \n
		Selects the form of the transmitted power, i.e. the shape of the rising and falling edges during power ramp control. \n
			:return: shape: LINear| COSine
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:PRAMp:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.RampFunc)

	def set_shape(self, shape: enums.RampFunc) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:SHAPe \n
		Snippet: driver.source.bb.tdscdma.pramp.set_shape(shape = enums.RampFunc.COSine) \n
		Selects the form of the transmitted power, i.e. the shape of the rising and falling edges during power ramp control. \n
			:param shape: LINear| COSine
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.RampFunc)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:PRAMp:SHAPe {param}')

	def get_time(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:TIME \n
		Snippet: value: int = driver.source.bb.tdscdma.pramp.get_time() \n
		Sets the power ramping rise time and fall time for a burst. \n
			:return: time: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:PRAMp:TIME?')
		return Conversions.str_to_int(response)

	def set_time(self, time: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRAMp:TIME \n
		Snippet: driver.source.bb.tdscdma.pramp.set_time(time = 1) \n
		Sets the power ramping rise time and fall time for a burst. \n
			:param time: integer Range: 0 to 4
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:PRAMp:TIME {param}')
