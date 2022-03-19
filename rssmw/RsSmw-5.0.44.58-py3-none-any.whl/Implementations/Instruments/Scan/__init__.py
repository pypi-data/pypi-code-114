from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scan:
	"""Scan commands group definition. 5 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scan", core, parent)

	@property
	def snet(self):
		"""snet commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_snet'):
			from .Snet import Snet
			self._snet = Snet(self._core, self._cmd_group)
		return self._snet

	def get_hn_prefix(self) -> str:
		"""SCPI: INSTruments:SCAN:HNPRefix \n
		Snippet: value: str = driver.instruments.scan.get_hn_prefix() \n
		No command help available \n
			:return: prefix: No help available
		"""
		response = self._core.io.query_str('INSTruments:SCAN:HNPRefix?')
		return trim_str_response(response)

	def set_hn_prefix(self, prefix: str) -> None:
		"""SCPI: INSTruments:SCAN:HNPRefix \n
		Snippet: driver.instruments.scan.set_hn_prefix(prefix = '1') \n
		No command help available \n
			:param prefix: No help available
		"""
		param = Conversions.value_to_quoted_str(prefix)
		self._core.io.write(f'INSTruments:SCAN:HNPRefix {param}')

	def get_value(self) -> float:
		"""SCPI: INSTruments:SCAN \n
		Snippet: value: float = driver.instruments.scan.get_value() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('INSTruments:SCAN?')
		return Conversions.str_to_float(response)

	def set_value(self, state: float) -> None:
		"""SCPI: INSTruments:SCAN \n
		Snippet: driver.instruments.scan.set_value(state = 1.0) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.decimal_value_to_str(state)
		self._core.io.write(f'INSTruments:SCAN {param}')

	def clone(self) -> 'Scan':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scan(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
