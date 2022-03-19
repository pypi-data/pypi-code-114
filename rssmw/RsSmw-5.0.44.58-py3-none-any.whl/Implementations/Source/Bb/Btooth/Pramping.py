from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramping:
	"""Pramping commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramping", core, parent)

	def get_foffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:FOFFset \n
		Snippet: value: int = driver.source.bb.btooth.pramping.get_foffset() \n
		Sets the offset of the falling edge of a burst. The offset is specified by the selected number of symbols.
		Negative values shift the falling edge to earlier positions, which results in a corresponding number of skipped symbols
		at the end of the burst. Positive values shift the falling edge to later positions, which results in a corresponding
		number of added 0 padding symbols following the burst. \n
			:return: foffset: integer Range: -32 to 32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PRAMping:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, foffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:FOFFset \n
		Snippet: driver.source.bb.btooth.pramping.set_foffset(foffset = 1) \n
		Sets the offset of the falling edge of a burst. The offset is specified by the selected number of symbols.
		Negative values shift the falling edge to earlier positions, which results in a corresponding number of skipped symbols
		at the end of the burst. Positive values shift the falling edge to later positions, which results in a corresponding
		number of added 0 padding symbols following the burst. \n
			:param foffset: integer Range: -32 to 32
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PRAMping:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_rfunction(self) -> enums.RampFunc:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:RFUNction \n
		Snippet: value: enums.RampFunc = driver.source.bb.btooth.pramping.get_rfunction() \n
		The command selects the form of the transmitted power, i.e. the shape of the rising and falling edges during power ramp
		control. \n
			:return: rfunction: LINear| COSine
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PRAMping:RFUNction?')
		return Conversions.str_to_scalar_enum(response, enums.RampFunc)

	def set_rfunction(self, rfunction: enums.RampFunc) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:RFUNction \n
		Snippet: driver.source.bb.btooth.pramping.set_rfunction(rfunction = enums.RampFunc.COSine) \n
		The command selects the form of the transmitted power, i.e. the shape of the rising and falling edges during power ramp
		control. \n
			:param rfunction: LINear| COSine
		"""
		param = Conversions.enum_scalar_to_str(rfunction, enums.RampFunc)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PRAMping:RFUNction {param}')

	def get_roffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:ROFFset \n
		Snippet: value: int = driver.source.bb.btooth.pramping.get_roffset() \n
		Sets the offset of the rising edge of a burst. The offset is specified by the selected number of symbols. Negative values
		shift the rising edge to earlier positions, which results in a corresponding number of added 0 padding symbols before the
		burst. Positive values shift the rising edge to later positions, which results in a corresponding number of skipped
		symbols at the beginning of the burst. \n
			:return: roffset: integer Range: -32 to 32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PRAMping:ROFFset?')
		return Conversions.str_to_int(response)

	def set_roffset(self, roffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:ROFFset \n
		Snippet: driver.source.bb.btooth.pramping.set_roffset(roffset = 1) \n
		Sets the offset of the rising edge of a burst. The offset is specified by the selected number of symbols. Negative values
		shift the rising edge to earlier positions, which results in a corresponding number of added 0 padding symbols before the
		burst. Positive values shift the rising edge to later positions, which results in a corresponding number of skipped
		symbols at the beginning of the burst. \n
			:param roffset: integer Range: -32 to 32
		"""
		param = Conversions.decimal_value_to_str(roffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PRAMping:ROFFset {param}')

	def get_rtime(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:RTIMe \n
		Snippet: value: int = driver.source.bb.btooth.pramping.get_rtime() \n
		Sets the ramp time, which extends the burst by a corresponding number of 0 padding symbols at the beginning and the end
		of a burst. During this period of time, power ramping is based on the specified ramp function. \n
			:return: rtime: integer Range: 1 to 32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PRAMping:RTIMe?')
		return Conversions.str_to_int(response)

	def set_rtime(self, rtime: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PRAMping:RTIMe \n
		Snippet: driver.source.bb.btooth.pramping.set_rtime(rtime = 1) \n
		Sets the ramp time, which extends the burst by a corresponding number of 0 padding symbols at the beginning and the end
		of a burst. During this period of time, power ramping is based on the specified ramp function. \n
			:param rtime: integer Range: 1 to 32
		"""
		param = Conversions.decimal_value_to_str(rtime)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PRAMping:RTIMe {param}')
