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
		"""SCPI: [SOURce<HW>]:BB:W3GPp:WAVeform:CREate \n
		Snippet: driver.source.bb.w3Gpp.waveform.set_create(filename = '1') \n
		This command creates a waveform using the current settings of the 3GPP FDD menu. The file name is entered with the
		command. The file is stored with the predefined file extension *.wv. The file name and the directory it is stored in are
		user-definable. \n
			:param filename: file_name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:WAVeform:CREate {param}')
