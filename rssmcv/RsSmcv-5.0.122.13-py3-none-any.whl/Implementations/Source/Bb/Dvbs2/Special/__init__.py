from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Special:
	"""Special commands group definition. 5 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("special", core, parent)

	@property
	def dslPrbs(self):
		"""dslPrbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dslPrbs'):
			from .DslPrbs import DslPrbs
			self._dslPrbs = DslPrbs(self._core, self._cmd_group)
		return self._dslPrbs

	@property
	def scramble(self):
		"""scramble commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scramble'):
			from .Scramble import Scramble
			self._scramble = Scramble(self._core, self._cmd_group)
		return self._scramble

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	def get_gold_code(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:GOLDcode \n
		Snippet: value: float = driver.source.bb.dvbs2.special.get_gold_code() \n
		Defines the scrambling code number (n) of the gold code used for physical layer (PL) scrambling. This number in turn
		defines the scrambling sequence within a PL frame. \n
			:return: cold_code: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SPECial:GOLDcode?')
		return Conversions.str_to_float(response)

	def set_gold_code(self, cold_code: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:GOLDcode \n
		Snippet: driver.source.bb.dvbs2.special.set_gold_code(cold_code = 1.0) \n
		Defines the scrambling code number (n) of the gold code used for physical layer (PL) scrambling. This number in turn
		defines the scrambling sequence within a PL frame. \n
			:param cold_code: No help available
		"""
		param = Conversions.decimal_value_to_str(cold_code)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SPECial:GOLDcode {param}')

	def clone(self) -> 'Special':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Special(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
