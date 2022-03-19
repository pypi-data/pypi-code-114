from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	def get(self, status: bool) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LEVel:UPDated:[STATus] \n
		Snippet: value: bool = driver.source.regenerator.simulation.level.updated.status.get(status = False) \n
		Queries whether the current output level at the dedicated connector is equal to the calculated level.
		To query the calculated level, use the command [:SOURce<hw>]:REGenerator:SIMulation:LEVel?. \n
			:param status: 0| 1| OFF| ON
			:return: status: 0| 1| OFF| ON"""
		param = Conversions.bool_to_str(status)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:SIMulation:LEVel:UPDated:STATus? {param}')
		return Conversions.str_to_bool(response)
