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
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:FOFFset \n
		Snippet: value: int = driver.source.bb.tetra.pramping.get_foffset() \n
		Sets the offset in the falling edge of the envelope at the end of a frame. A positive value gives rise to a delay and a
		negative value causes an advance. The setting is expressed in symbols. \n
			:return: foffset: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:PRAMping:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, foffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:FOFFset \n
		Snippet: driver.source.bb.tetra.pramping.set_foffset(foffset = 1) \n
		Sets the offset in the falling edge of the envelope at the end of a frame. A positive value gives rise to a delay and a
		negative value causes an advance. The setting is expressed in symbols. \n
			:param foffset: integer Range: 0 to 4
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:PRAMping:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_rfunction(self) -> enums.RampFunc:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:RFUNction \n
		Snippet: value: enums.RampFunc = driver.source.bb.tetra.pramping.get_rfunction() \n
		Enters the form of the transmitted power during the switching operation, i.e. the shape of the rising and falling edges
		of the envelope. \n
			:return: rfunction: LINear| COSine LINear The transmitted power rises and falls linear fashion. COSine The transmitted power rises and falls with a cosine-shaped edge. This gives rise to a more favorable spectrum than the 'Linear' setting.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:PRAMping:RFUNction?')
		return Conversions.str_to_scalar_enum(response, enums.RampFunc)

	def set_rfunction(self, rfunction: enums.RampFunc) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:RFUNction \n
		Snippet: driver.source.bb.tetra.pramping.set_rfunction(rfunction = enums.RampFunc.COSine) \n
		Enters the form of the transmitted power during the switching operation, i.e. the shape of the rising and falling edges
		of the envelope. \n
			:param rfunction: LINear| COSine LINear The transmitted power rises and falls linear fashion. COSine The transmitted power rises and falls with a cosine-shaped edge. This gives rise to a more favorable spectrum than the 'Linear' setting.
		"""
		param = Conversions.enum_scalar_to_str(rfunction, enums.RampFunc)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:PRAMping:RFUNction {param}')

	def get_roffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:ROFFset \n
		Snippet: value: int = driver.source.bb.tetra.pramping.get_roffset() \n
		Sets the offset in the rising edge of the envelope at the start of a frame. A positive value gives rise to a delay and a
		negative value causes an advance. The setting is expressed in symbols. \n
			:return: roffset: integer Range: -4 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:PRAMping:ROFFset?')
		return Conversions.str_to_int(response)

	def set_roffset(self, roffset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:ROFFset \n
		Snippet: driver.source.bb.tetra.pramping.set_roffset(roffset = 1) \n
		Sets the offset in the rising edge of the envelope at the start of a frame. A positive value gives rise to a delay and a
		negative value causes an advance. The setting is expressed in symbols. \n
			:param roffset: integer Range: -4 to 0
		"""
		param = Conversions.decimal_value_to_str(roffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:PRAMping:ROFFset {param}')

	def get_rtime(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:RTIMe \n
		Snippet: value: int = driver.source.bb.tetra.pramping.get_rtime() \n
		Enters the power ramping rise time and fall time for a frame. The setting is expressed in symbols. The transmitted power
		must not be switched abruptly at the start and end of a frame, because the switching operation would otherwise generate
		excessively strong non-harmonics; the switching operation is therefore stretched over several symbol clocks. \n
			:return: rtime: integer Range: 1 to 13|16, depends on test mode
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:PRAMping:RTIMe?')
		return Conversions.str_to_int(response)

	def set_rtime(self, rtime: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRAMping:RTIMe \n
		Snippet: driver.source.bb.tetra.pramping.set_rtime(rtime = 1) \n
		Enters the power ramping rise time and fall time for a frame. The setting is expressed in symbols. The transmitted power
		must not be switched abruptly at the start and end of a frame, because the switching operation would otherwise generate
		excessively strong non-harmonics; the switching operation is therefore stretched over several symbol clocks. \n
			:param rtime: integer Range: 1 to 13|16, depends on test mode
		"""
		param = Conversions.decimal_value_to_str(rtime)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:PRAMping:RTIMe {param}')
