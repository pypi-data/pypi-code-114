from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 10 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def amam(self):
		"""amam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	# noinspection PyTypeChecker
	def get_interp(self) -> enums.Interpolation:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:TABLe:INTerp \n
		Snippet: value: enums.Interpolation = driver.source.iq.dpd.shaping.table.get_interp() \n
		Enables a linear (voltage or power) interpolation between the defined correction values. \n
			:return: ipart_interpolation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:SHAPing:TABLe:INTerp?')
		return Conversions.str_to_scalar_enum(response, enums.Interpolation)

	def set_interp(self, ipart_interpolation: enums.Interpolation) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:TABLe:INTerp \n
		Snippet: driver.source.iq.dpd.shaping.table.set_interp(ipart_interpolation = enums.Interpolation.LINear) \n
		Enables a linear (voltage or power) interpolation between the defined correction values. \n
			:param ipart_interpolation: OFF| POWer| LINear POWer Linear power interpolation LINear Linear voltage interpolation
		"""
		param = Conversions.enum_scalar_to_str(ipart_interpolation, enums.Interpolation)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SHAPing:TABLe:INTerp {param}')

	def get_invert(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:[TABLe]:INVert \n
		Snippet: value: bool = driver.source.iq.dpd.shaping.table.get_invert() \n
		Inverts the defined correction values. \n
			:return: ipart_invert_values: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:SHAPing:TABLe:INVert?')
		return Conversions.str_to_bool(response)

	def set_invert(self, ipart_invert_values: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:[TABLe]:INVert \n
		Snippet: driver.source.iq.dpd.shaping.table.set_invert(ipart_invert_values = False) \n
		Inverts the defined correction values. \n
			:param ipart_invert_values: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ipart_invert_values)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SHAPing:TABLe:INVert {param}')

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
