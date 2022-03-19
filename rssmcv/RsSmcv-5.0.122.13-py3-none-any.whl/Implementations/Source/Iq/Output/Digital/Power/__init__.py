from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:LEVel \n
		Snippet: value: float = driver.source.iq.output.digital.power.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:LEVel \n
		Snippet: driver.source.iq.output.digital.power.set_level(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:LEVel {param}')

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:PEP \n
		Snippet: value: float = driver.source.iq.output.digital.power.get_pep() \n
		No command help available \n
			:return: pep: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:PEP?')
		return Conversions.str_to_float(response)

	def set_pep(self, pep: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:PEP \n
		Snippet: driver.source.iq.output.digital.power.set_pep(pep = 1.0) \n
		No command help available \n
			:param pep: No help available
		"""
		param = Conversions.decimal_value_to_str(pep)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:PEP {param}')

	# noinspection PyTypeChecker
	def get_via(self) -> enums.IqOutDispViaType:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:POWer:VIA \n
		Snippet: value: enums.IqOutDispViaType = driver.source.iq.output.digital.power.get_via() \n
		Selects the respective level entry field for the I/Q output. \n
			:return: via: PEP| LEVel
		"""
		response = self._core.io.query_str('SOURce:IQ:OUTPut:DIGital:POWer:VIA?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutDispViaType)

	def set_via(self, via: enums.IqOutDispViaType) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:POWer:VIA \n
		Snippet: driver.source.iq.output.digital.power.set_via(via = enums.IqOutDispViaType.LEVel) \n
		Selects the respective level entry field for the I/Q output. \n
			:param via: PEP| LEVel
		"""
		param = Conversions.enum_scalar_to_str(via, enums.IqOutDispViaType)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:POWer:VIA {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
