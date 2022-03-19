from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shaping:
	"""Shaping commands group definition. 19 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shaping", core, parent)

	@property
	def normalized(self):
		"""normalized commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_normalized'):
			from .Normalized import Normalized
			self._normalized = Normalized(self._core, self._cmd_group)
		return self._normalized

	@property
	def polynomial(self):
		"""polynomial commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_polynomial'):
			from .Polynomial import Polynomial
			self._polynomial = Polynomial(self._core, self._cmd_group)
		return self._polynomial

	@property
	def table(self):
		"""table commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DpdShapeMode:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:MODE \n
		Snippet: value: enums.DpdShapeMode = driver.source.iq.dpd.shaping.get_mode() \n
		Selects the method to define the correction coefficients. \n
			:return: shaping: TABLe| POLYnomial| NORMalized
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:SHAPing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DpdShapeMode)

	def set_mode(self, shaping: enums.DpdShapeMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SHAPing:MODE \n
		Snippet: driver.source.iq.dpd.shaping.set_mode(shaping = enums.DpdShapeMode.NORMalized) \n
		Selects the method to define the correction coefficients. \n
			:param shaping: TABLe| POLYnomial| NORMalized
		"""
		param = Conversions.enum_scalar_to_str(shaping, enums.DpdShapeMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SHAPing:MODE {param}')

	def clone(self) -> 'Shaping':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Shaping(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
