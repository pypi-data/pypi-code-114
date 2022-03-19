from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def get_local(self) -> bool:
		"""SCPI: CALibration<HW>:LOSCillator:COUPling:LOCal \n
		Snippet: value: bool = driver.calibration.loscillator.coupling.get_local() \n
		Adjusts the internal LO level at the I/Q modulator automatically, when an external LO signal is fed. \n
			:return: coupling_level: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LOSCillator:COUPling:LOCal?')
		return Conversions.str_to_bool(response)
