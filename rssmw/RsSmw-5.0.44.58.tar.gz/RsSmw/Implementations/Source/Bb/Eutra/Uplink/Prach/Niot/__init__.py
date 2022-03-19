from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	@property
	def cfg(self):
		"""cfg commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfg'):
			from .Cfg import Cfg
			self._cfg = Cfg(self._core, self._cmd_group)
		return self._cfg

	# noinspection PyTypeChecker
	def get_pfmt(self) -> enums.EutraPracNbiotPreambleFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:PFMT \n
		Snippet: value: enums.EutraPracNbiotPreambleFormat = driver.source.bb.eutra.uplink.prach.niot.get_pfmt() \n
		Select the preamble format. \n
			:return: preamble_format: F0| F1 | 0| 1 | F2| F0A| F1A 0|1 backward compatibility; use F0|F1 instead.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:PFMT?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPracNbiotPreambleFormat)

	def set_pfmt(self, preamble_format: enums.EutraPracNbiotPreambleFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:PFMT \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.set_pfmt(preamble_format = enums.EutraPracNbiotPreambleFormat._0) \n
		Select the preamble format. \n
			:param preamble_format: F0| F1 | 0| 1 | F2| F0A| F1A 0|1 backward compatibility; use F0|F1 instead.
		"""
		param = Conversions.enum_scalar_to_str(preamble_format, enums.EutraPracNbiotPreambleFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:PFMT {param}')

	def clone(self) -> 'Niot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Niot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
