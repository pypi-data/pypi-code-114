from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 6 total commands, 2 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	@property
	def fifo(self):
		"""fifo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fifo'):
			from .Fifo import Fifo
			self._fifo = Fifo(self._core, self._cmd_group)
		return self._fifo

	def get_max(self) -> int:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:SRATe:MAX \n
		Snippet: value: int = driver.source.iq.output.digital.symbolRate.get_max() \n
		Queries the maximum supported sample rate. \n
			:return: dig_iqhs_in_sr_max: integer Range: 400 to depends on options The maximum value depends on the connected receiving device. For more information, see data sheet.
		"""
		response = self._core.io.query_str('SOURce:IQ:OUTPut:DIGital:SRATe:MAX?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BboutClocSour:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:SRATe:SOURce \n
		Snippet: value: enums.BboutClocSour = driver.source.iq.output.digital.symbolRate.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:SRATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BboutClocSour)

	def set_source(self, source: enums.BboutClocSour) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:SRATe:SOURce \n
		Snippet: driver.source.iq.output.digital.symbolRate.set_source(source = enums.BboutClocSour.DIN) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BboutClocSour)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:SRATe:SOURce {param}')

	def get_sum(self) -> int:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:SRATe:SUM \n
		Snippet: value: int = driver.source.iq.output.digital.symbolRate.get_sum() \n
		Queries the maximum supported sample rate. \n
			:return: dig_iqhs_in_sr_sum: integer Range: 400 to depends on options The maximum value depends on the connected receiving device. For more information, see data sheet.
		"""
		response = self._core.io.query_str('SOURce:IQ:OUTPut:DIGital:SRATe:SUM?')
		return Conversions.str_to_int(response)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:SRATe \n
		Snippet: value: float = driver.source.iq.output.digital.symbolRate.get_value() \n
		Sets the sample rate of the digital I/Q output signal. \n
			:return: srate: float Range: 400 to depends on options, Unit: Hz The maximum value depends on the connected receiving device. For more information, see data sheet.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:SRATe?')
		return Conversions.str_to_float(response)

	def set_value(self, srate: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:SRATe \n
		Snippet: driver.source.iq.output.digital.symbolRate.set_value(srate = 1.0) \n
		Sets the sample rate of the digital I/Q output signal. \n
			:param srate: float Range: 400 to depends on options, Unit: Hz The maximum value depends on the connected receiving device. For more information, see data sheet.
		"""
		param = Conversions.decimal_value_to_str(srate)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:SRATe {param}')

	def clone(self) -> 'SymbolRate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
