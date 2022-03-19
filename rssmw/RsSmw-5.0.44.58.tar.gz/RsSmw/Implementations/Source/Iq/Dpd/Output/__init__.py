from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def error(self):
		"""error commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_error'):
			from .Error import Error
			self._error = Error(self._core, self._cmd_group)
		return self._error

	@property
	def iterations(self):
		"""iterations commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iterations'):
			from .Iterations import Iterations
			self._iterations = Iterations(self._core, self._cmd_group)
		return self._iterations

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:CFACtor \n
		Snippet: value: float = driver.source.iq.dpd.output.get_cfactor() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: crest_factor: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:CFACtor?')
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:LEVel \n
		Snippet: value: float = driver.source.iq.dpd.output.get_level() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: level: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:PEP \n
		Snippet: value: float = driver.source.iq.dpd.output.get_pep() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: pep: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:PEP?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
