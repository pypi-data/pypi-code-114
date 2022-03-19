from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	def set_create(self, create_wv_file: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:WAVeform:CREate \n
		Snippet: driver.source.bb.arbitrary.cfr.waveform.set_create(create_wv_file = '1') \n
		With enabled signal generation, triggers the instrument to save the current settings in a waveform file. Waveform files
		can be further processed. The filename and the directory it is saved in are user-definable; the predefined file extension
		for waveform files is *.wv. \n
			:param create_wv_file: string
		"""
		param = Conversions.value_to_quoted_str(create_wv_file)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:WAVeform:CREate {param}')
