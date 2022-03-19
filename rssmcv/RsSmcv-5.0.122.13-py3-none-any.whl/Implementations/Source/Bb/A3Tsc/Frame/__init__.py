from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 7 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import Additional
			self._additional = Additional(self._core, self._cmd_group)
		return self._additional

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	def get_ex_final(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:EXFinal \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.get_ex_final() \n
		Queries the excess samples that are inserted immediately following the final OFDM symbol of the final subframe. \n
			:return: final_exc_samples: integer Range: 0 to 32767
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:EXFinal?')
		return Conversions.str_to_int(response)

	def get_ex_symbol(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:EXSYmbol \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.get_ex_symbol() \n
		Queries the additional number of excess samples included in the guard interval of each non-preamble symbol of the
		post-bootstrap portion. \n
			:return: excess_symbol: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:EXSYmbol?')
		return Conversions.str_to_int(response)

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:LENGth \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.get_length() \n
		Sets the time period measured from the beginning of the first sample of the bootstrap to the end of the final sample of
		the frame. \n
			:return: frame_length: integer Range: 50 to 5000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, frame_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:LENGth \n
		Snippet: driver.source.bb.a3Tsc.frame.set_length(frame_length = 1) \n
		Sets the time period measured from the beginning of the first sample of the bootstrap to the end of the final sample of
		the frame. \n
			:param frame_length: integer Range: 50 to 5000
		"""
		param = Conversions.decimal_value_to_str(frame_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:FRAMe:LENGth {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Atsc30FrameLengthMode:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:MODE \n
		Snippet: value: enums.Atsc30FrameLengthMode = driver.source.bb.a3Tsc.frame.get_mode() \n
		Sets how the frame length is aligned. \n
			:return: frame_mode: TIME| SYMBol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30FrameLengthMode)

	def set_mode(self, frame_mode: enums.Atsc30FrameLengthMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:MODE \n
		Snippet: driver.source.bb.a3Tsc.frame.set_mode(frame_mode = enums.Atsc30FrameLengthMode.SYMBol) \n
		Sets how the frame length is aligned. \n
			:param frame_mode: TIME| SYMBol
		"""
		param = Conversions.enum_scalar_to_str(frame_mode, enums.Atsc30FrameLengthMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:FRAMe:MODE {param}')

	def get_nsub_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:FRAMe:NSUBframes \n
		Snippet: value: int = driver.source.bb.a3Tsc.frame.get_nsub_frames() \n
		Queries the number of subframes. \n
			:return: num_subframes: integer Range: 1 to 256
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:FRAMe:NSUBframes?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Frame':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frame(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
