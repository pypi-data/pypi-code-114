from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Satellite:
	"""Satellite commands group definition. 32 total commands, 4 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("satellite", core, parent)

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def trigger(self):
		"""trigger commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:DELay \n
		Snippet: value: float = driver.source.bb.sirius.satellite.get_delay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:SATellite:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:DELay \n
		Snippet: driver.source.bb.sirius.satellite.set_delay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:SATellite:DELay {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.SiriusSatMod:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:MODulation \n
		Snippet: value: enums.SiriusSatMod = driver.source.bb.sirius.satellite.get_modulation() \n
		No command help available \n
			:return: modulation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:SATellite:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.SiriusSatMod)

	def set_modulation(self, modulation: enums.SiriusSatMod) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:MODulation \n
		Snippet: driver.source.bb.sirius.satellite.set_modulation(modulation = enums.SiriusSatMod.P8INV) \n
		No command help available \n
			:param modulation: No help available
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.SiriusSatMod)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:SATellite:MODulation {param}')

	def get_oa_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:OAOFfset \n
		Snippet: value: int = driver.source.bb.sirius.satellite.get_oa_offset() \n
		No command help available \n
			:return: oa_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:SATellite:OAOFfset?')
		return Conversions.str_to_int(response)

	def set_oa_offset(self, oa_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:SATellite:OAOFfset \n
		Snippet: driver.source.bb.sirius.satellite.set_oa_offset(oa_offset = 1) \n
		No command help available \n
			:param oa_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(oa_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:SATellite:OAOFfset {param}')

	def clone(self) -> 'Satellite':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Satellite(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
