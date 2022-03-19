from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	def set_create(self, wv_file_create: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:WAVeform:CREate \n
		Snippet: driver.source.bb.v5G.waveform.set_create(wv_file_create = '1') \n
		Stores the current settings as an ARB signal in a waveform file (*.wv) . Refer to 'Accessing Files in the Default or
		Specified Directory' for general information on file handling in the default and in a specific directory. \n
			:param wv_file_create: string Filename or complete file path; file extension is assigned automatically
		"""
		param = Conversions.value_to_quoted_str(wv_file_create)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:WAVeform:CREate {param}')
