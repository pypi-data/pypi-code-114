from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def set(self, name: str, state: bool) -> None:
		"""SCPI: CALibration<HW>:SELected:STEP \n
		Snippet: driver.calibration.selected.step.set(name = '1', state = False) \n
		No command help available \n
			:param name: No help available
			:param state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('state', state, DataType.Boolean))
		self._core.io.write(f'CALibration<HwInstance>:SELected:STEP {param}'.rstrip())

	def get(self) -> bool:
		"""SCPI: CALibration<HW>:SELected:STEP \n
		Snippet: value: bool = driver.calibration.selected.step.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'CALibration<HwInstance>:SELected:STEP?')
		return Conversions.str_to_bool(response)
