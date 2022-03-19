from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:POWer:ATTenuation \n
		Snippet: value: float = driver.source.iq.doherty.power.attenuation.get_value() \n
		Adds additional digital attenuation to the signal. \n
			:return: attenuation: float Range: -3.522 to 80
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:POWer:ATTenuation?')
		return Conversions.str_to_float(response)

	def set_value(self, attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:POWer:ATTenuation \n
		Snippet: driver.source.iq.doherty.power.attenuation.set_value(attenuation = 1.0) \n
		Adds additional digital attenuation to the signal. \n
			:param attenuation: float Range: -3.522 to 80
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:POWer:ATTenuation {param}')

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
