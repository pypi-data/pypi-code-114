from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scan:
	"""Scan commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scan", core, parent)

	@property
	def usensor(self):
		"""usensor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usensor'):
			from .Usensor import Usensor
			self._usensor = Usensor(self._core, self._cmd_group)
		return self._usensor

	def set_lsensor(self, ip: str) -> None:
		"""SCPI: SLISt:SCAN:LSENsor \n
		Snippet: driver.slist.scan.set_lsensor(ip = '1') \n
		Scans for R&S NRP power sensors connected in the LAN. \n
			:param ip: string
		"""
		param = Conversions.value_to_quoted_str(ip)
		self._core.io.write(f'SLISt:SCAN:LSENsor {param}')

	def get_state(self) -> bool:
		"""SCPI: SLISt:SCAN:[STATe] \n
		Snippet: value: bool = driver.slist.scan.get_state() \n
		Starts the search for R&S NRP power sensors, connected in the LAN or via the USBTMC protocol. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SLISt:SCAN:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SLISt:SCAN:[STATe] \n
		Snippet: driver.slist.scan.set_state(state = False) \n
		Starts the search for R&S NRP power sensors, connected in the LAN or via the USBTMC protocol. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SLISt:SCAN:STATe {param}')

	def clone(self) -> 'Scan':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scan(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
