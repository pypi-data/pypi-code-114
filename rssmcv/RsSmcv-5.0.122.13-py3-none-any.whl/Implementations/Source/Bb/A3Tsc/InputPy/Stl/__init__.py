from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stl:
	"""Stl commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stl", core, parent)

	@property
	def resetLog(self):
		"""resetLog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resetLog'):
			from .ResetLog import ResetLog
			self._resetLog = ResetLog(self._core, self._cmd_group)
		return self._resetLog

	def get_interface(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:STL:INTerface \n
		Snippet: value: bool = driver.source.bb.a3Tsc.inputPy.stl.get_interface() \n
		Activates the interface. \n
			:return: stl_interface: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:STL:INTerface?')
		return Conversions.str_to_bool(response)

	def set_interface(self, stl_interface: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:STL:INTerface \n
		Snippet: driver.source.bb.a3Tsc.inputPy.stl.set_interface(stl_interface = False) \n
		Activates the interface. \n
			:param stl_interface: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(stl_interface)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:STL:INTerface {param}')

	def clone(self) -> 'Stl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
