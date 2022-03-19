from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfn:
	"""Sfn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfn", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHeduling:SFN:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.scheduling.sfn.get_state() \n
		Enables the full counting of the system frame number carried by the PBCH block from 0 to 1023, independent from the
		configured ARB 'Sequence Length'. If [:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:TMPH:SFOFfset is set, the counting starts at
		the configured SFN offset value and restarts when the SFN offset value is reached again as follows: offset, (offset+1) ,
		(offset+ 2) , ..., 1023, 0, 1, 2, ..., (offset-1) . \n
			:return: sys_frame_num: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SCHeduling:SFN:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, sys_frame_num: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHeduling:SFN:STATe \n
		Snippet: driver.source.bb.nr5G.scheduling.sfn.set_state(sys_frame_num = False) \n
		Enables the full counting of the system frame number carried by the PBCH block from 0 to 1023, independent from the
		configured ARB 'Sequence Length'. If [:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:TMPH:SFOFfset is set, the counting starts at
		the configured SFN offset value and restarts when the SFN offset value is reached again as follows: offset, (offset+1) ,
		(offset+ 2) , ..., 1023, 0, 1, 2, ..., (offset-1) . \n
			:param sys_frame_num: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(sys_frame_num)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SCHeduling:SFN:STATe {param}')
