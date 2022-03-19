from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wlist:
	"""Wlist commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlist", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	# noinspection PyTypeChecker
	def get_dasr(self) -> enums.ExtSeqPdwRate:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:WLISt:DASR \n
		Snippet: value: enums.ExtSeqPdwRate = driver.source.bb.esequencer.rtci.wlist.get_dasr() \n
		The desired ARB Streaming rate directly influences the Minimum common clock rate all waveforms are resampled to.
		The higher the desired rate, the higher the common sample rate, in order to optimize the ARB PDW Streaming rate. At the
		same time, the required Memory will also increase. \n
			:return: streaming_rate: SR250K| SR750K| SR500K| SR1M
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:RTCI:WLISt:DASR?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqPdwRate)

	def set_dasr(self, streaming_rate: enums.ExtSeqPdwRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:WLISt:DASR \n
		Snippet: driver.source.bb.esequencer.rtci.wlist.set_dasr(streaming_rate = enums.ExtSeqPdwRate.SR1M) \n
		The desired ARB Streaming rate directly influences the Minimum common clock rate all waveforms are resampled to.
		The higher the desired rate, the higher the common sample rate, in order to optimize the ARB PDW Streaming rate. At the
		same time, the required Memory will also increase. \n
			:param streaming_rate: SR250K| SR750K| SR500K| SR1M
		"""
		param = Conversions.enum_scalar_to_str(streaming_rate, enums.ExtSeqPdwRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:WLISt:DASR {param}')

	def clone(self) -> 'Wlist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wlist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
