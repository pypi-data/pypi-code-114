from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impairment:
	"""Impairment commands group definition. 5 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impairment", core, parent)

	@property
	def iqRatio(self):
		"""iqRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqRatio'):
			from .IqRatio import IqRatio
			self._iqRatio = IqRatio(self._core, self._cmd_group)
		return self._iqRatio

	@property
	def leakage(self):
		"""leakage commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_leakage'):
			from .Leakage import Leakage
			self._leakage = Leakage(self._core, self._cmd_group)
		return self._leakage

	@property
	def quadrature(self):
		"""quadrature commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_quadrature'):
			from .Quadrature import Quadrature
			self._quadrature = Quadrature(self._core, self._cmd_group)
		return self._quadrature

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:[STATe] \n
		Snippet: value: bool = driver.source.iq.impairment.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:[STATe] \n
		Snippet: driver.source.iq.impairment.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:STATe {param}')

	def clone(self) -> 'Impairment':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impairment(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
