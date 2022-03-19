from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 9 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def hddStreaming(self):
		"""hddStreaming commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hddStreaming'):
			from .HddStreaming import HddStreaming
			self._hddStreaming = HddStreaming(self._core, self._cmd_group)
		return self._hddStreaming

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:DELete \n
		Snippet: driver.source.bb.arbitrary.waveform.delete(filename = '1') \n
		Deletes the specified waveform file. If the file is not on the default path, the path must be specified at the same time.
		The file extension may be omitted. Only files with the file extension *.wv are deleted. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WAVeform:DELete {param}')

	def get_free(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:FREE \n
		Snippet: value: int = driver.source.bb.arbitrary.waveform.get_free() \n
		Queries the free disk space on the default path of the instrument's hard disk. \n
			:return: free: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:FREE?')
		return Conversions.str_to_int(response)

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:POINts \n
		Snippet: value: int = driver.source.bb.arbitrary.waveform.get_points() \n
		Queries the number of samples (the number of I/Q values pairs) in the selected waveform file. \n
			:return: points: waveform filename Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:POINts?')
		return Conversions.str_to_int(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:SELect \n
		Snippet: value: str = driver.source.bb.arbitrary.waveform.get_select() \n
		Selects an existing waveform file, i.e. file with extension *.wv. \n
			:return: filename: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:SELect \n
		Snippet: driver.source.bb.arbitrary.waveform.set_select(filename = '1') \n
		Selects an existing waveform file, i.e. file with extension *.wv. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WAVeform:SELect {param}')

	def get_tag(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:TAG \n
		Snippet: value: str = driver.source.bb.arbitrary.waveform.get_tag() \n
		Queries the content of the specified tag of the selected waveform file (see also 'Tags for waveforms, data and control
		lists') . \n
			:return: tag: 'comment'| 'copyright'| 'date'| 'lacpfilter'| 'marker name'| 'poweroffset'| 'samples'
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:TAG?')
		return trim_str_response(response)

	def clone(self) -> 'Waveform':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Waveform(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
