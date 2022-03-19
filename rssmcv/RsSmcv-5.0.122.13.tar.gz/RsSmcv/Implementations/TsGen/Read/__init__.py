from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	@property
	def playFile(self):
		"""playFile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_playFile'):
			from .PlayFile import PlayFile
			self._playFile = PlayFile(self._core, self._cmd_group)
		return self._playFile

	def get_fmemory(self) -> int:
		"""SCPI: TSGen:READ:FMEMory \n
		Snippet: value: int = driver.tsGen.read.get_fmemory() \n
		Queries the file size of the TS player file. \n
			:return: fmemory: integer Range: 0 to 10
		"""
		response = self._core.io.query_str('TSGen:READ:FMEMory?')
		return Conversions.str_to_int(response)

	def set_fmemory(self, fmemory: int) -> None:
		"""SCPI: TSGen:READ:FMEMory \n
		Snippet: driver.tsGen.read.set_fmemory(fmemory = 1) \n
		Queries the file size of the TS player file. \n
			:param fmemory: integer Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(fmemory)
		self._core.io.write(f'TSGen:READ:FMEMory {param}')

	def get_orig_ts_rate(self) -> int:
		"""SCPI: TSGen:READ:ORIGtsrate \n
		Snippet: value: int = driver.tsGen.read.get_orig_ts_rate() \n
		Displays the calculated original TS data rate. \n
			:return: orig_ts_rate: integer Range: 1 to 350000000
		"""
		response = self._core.io.query_str('TSGen:READ:ORIGtsrate?')
		return Conversions.str_to_int(response)

	def set_orig_ts_rate(self, orig_ts_rate: int) -> None:
		"""SCPI: TSGen:READ:ORIGtsrate \n
		Snippet: driver.tsGen.read.set_orig_ts_rate(orig_ts_rate = 1) \n
		Displays the calculated original TS data rate. \n
			:param orig_ts_rate: integer Range: 1 to 350000000
		"""
		param = Conversions.decimal_value_to_str(orig_ts_rate)
		self._core.io.write(f'TSGen:READ:ORIGtsrate {param}')

	def clone(self) -> 'Read':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Read(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
