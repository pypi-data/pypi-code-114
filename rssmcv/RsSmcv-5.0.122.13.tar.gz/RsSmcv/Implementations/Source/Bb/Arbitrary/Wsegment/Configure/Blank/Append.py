from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Append:
	"""Append commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("append", core, parent)

	def set(self, samp_count: float, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:BLANk:APPend \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.blank.append.set(samp_count = 1.0, frequency = 1.0) \n
		Adds a blank segment to the multi-segment file. \n
			:param samp_count: float Specifies the number of samples. Range: 512 to 1E7
			:param frequency: float Determines the clock rate. Range: 400 Hz to depends on the installed options
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('samp_count', samp_count, DataType.Float), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:BLANk:APPend {param}'.rstrip())
