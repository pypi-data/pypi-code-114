from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Laa:
	"""Laa commands group definition. 9 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("laa", core, parent)

	@property
	def cell(self):
		"""cell commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	# noinspection PyTypeChecker
	def get_ce_index(self) -> enums.EutraCcIndexS:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CEINdex \n
		Snippet: value: enums.EutraCcIndexS = driver.source.bb.eutra.downlink.laa.get_ce_index() \n
		Selects the LAA SCell for that the LAA is configured. \n
			:return: cell_index: SC1| SC2| SC3| SC4| NONE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:LAA:CEINdex?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCcIndexS)

	def set_ce_index(self, cell_index: enums.EutraCcIndexS) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CEINdex \n
		Snippet: driver.source.bb.eutra.downlink.laa.set_ce_index(cell_index = enums.EutraCcIndexS.NONE) \n
		Selects the LAA SCell for that the LAA is configured. \n
			:param cell_index: SC1| SC2| SC3| SC4| NONE
		"""
		param = Conversions.enum_scalar_to_str(cell_index, enums.EutraCcIndexS)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CEINdex {param}')

	def clone(self) -> 'Laa':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Laa(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
