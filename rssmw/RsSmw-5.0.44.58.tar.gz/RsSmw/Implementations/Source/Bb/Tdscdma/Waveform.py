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
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:WAVeform:CREate \n
		Snippet: driver.source.bb.tdscdma.waveform.set_create(filename = '1') \n
		Stores the current settings as an ARB signal in a waveform file (*.wv) . For general information on file handling in the
		default and in a specific directory, see section 'MMEMory Subsystem' in the R&S SMW operating manual. \n
			:param filename: string Filename or complete file path; file extension is assigned automatically
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:WAVeform:CREate {param}')
