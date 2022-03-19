from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpdch:
	"""Dpdch commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpdch", core, parent)

	@property
	def ccoding(self):
		"""ccoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def derror(self):
		"""derror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import Derror
			self._derror = Derror(self._core, self._cmd_group)
		return self._derror

	# noinspection PyTypeChecker
	def get_orate(self) -> enums.SymbRate:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:ORATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.get_orate() \n
		Sets the overall symbol rate. \n
			:return: orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k 15 ksps ... 6 x 960 ksps
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:ORATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)

	def set_orate(self, orate: enums.SymbRate) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:ORATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.set_orate(orate = enums.SymbRate.D120k) \n
		Sets the overall symbol rate. \n
			:param orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k 15 ksps ... 6 x 960 ksps
		"""
		param = Conversions.enum_scalar_to_str(orate, enums.SymbRate)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:ORATe {param}')

	def clone(self) -> 'Dpdch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpdch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
