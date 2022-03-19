from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	def set_create(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:WAVeform:CREate \n
		Snippet: driver.source.bb.gbas.waveform.set_create(filename = '1') \n
		With enabled signal generation, triggers the instrument to save the current settings of an arbitrary waveform signal in a
		waveform file with predefined extension *.wv. You can define the filename and the directory, in that you want to save the
		file. Using the ARB modulation source, you can play back waveform files and/or process the file to generate multi-carrier
		or multi-segment signals. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:WAVeform:CREate {param}')
