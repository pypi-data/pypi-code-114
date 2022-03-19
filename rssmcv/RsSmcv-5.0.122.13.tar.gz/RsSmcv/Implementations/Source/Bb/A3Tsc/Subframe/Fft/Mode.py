from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, fft_mode: enums.Atsc30FftSize, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:FFT:MODE \n
		Snippet: driver.source.bb.a3Tsc.subframe.fft.mode.set(fft_mode = enums.Atsc30FftSize.M16K, subframe = repcap.Subframe.Default) \n
		Defines the size. \n
			:param fft_mode: M16K| M8K| M32K | M8K| M16K| M32K
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(fft_mode, enums.Atsc30FftSize)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:FFT:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, subframe=repcap.Subframe.Default) -> enums.Atsc30FftSize:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:FFT:MODE \n
		Snippet: value: enums.Atsc30FftSize = driver.source.bb.a3Tsc.subframe.fft.mode.get(subframe = repcap.Subframe.Default) \n
		Defines the size. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: fft_mode: M16K| M8K| M32K | M8K| M16K| M32K"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:FFT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30FftSize)
