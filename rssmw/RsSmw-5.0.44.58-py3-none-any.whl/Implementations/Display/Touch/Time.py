from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set_charge(self, charge_time: int) -> None:
		"""SCPI: DISPlay:TOUCh:TIME:CHARge \n
		Snippet: driver.display.touch.time.set_charge(charge_time = 1) \n
		No command help available \n
			:param charge_time: No help available
		"""
		param = Conversions.decimal_value_to_str(charge_time)
		self._core.io.write(f'DISPlay:TOUCh:TIME:CHARge {param}')
