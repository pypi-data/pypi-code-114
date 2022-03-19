from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def get_step(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation:ADDitional:TDELay:STEP \n
		Snippet: value: int = driver.source.bb.c2K.mstation.additional.tdelay.get_step() \n
		Sets the step width for the time delay of the additional mobile stations to one another. The start value returns the time
		delay of MS4. \n
			:return: step: integer Range: 0 to 1535 (1 frame) , Unit: chip
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:MSTation:ADDitional:TDELay:STEP?')
		return Conversions.str_to_int(response)

	def set_step(self, step: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation:ADDitional:TDELay:STEP \n
		Snippet: driver.source.bb.c2K.mstation.additional.tdelay.set_step(step = 1) \n
		Sets the step width for the time delay of the additional mobile stations to one another. The start value returns the time
		delay of MS4. \n
			:param step: integer Range: 0 to 1535 (1 frame) , Unit: chip
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation:ADDitional:TDELay:STEP {param}')
