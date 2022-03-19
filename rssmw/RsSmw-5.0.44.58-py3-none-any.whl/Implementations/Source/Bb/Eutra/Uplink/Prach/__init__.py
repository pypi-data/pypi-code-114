from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 16 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def emtc(self):
		"""emtc commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_emtc'):
			from .Emtc import Emtc
			self._emtc = Emtc(self._core, self._cmd_group)
		return self._emtc

	@property
	def niot(self):
		"""niot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	def get_configuration(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:CONFiguration \n
		Snippet: value: int = driver.source.bb.eutra.uplink.prach.get_configuration() \n
		Sets the PRACH configuration number. \n
			:return: configuration: integer Range: 0 to 63
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:PRACh:CONFiguration?')
		return Conversions.str_to_int(response)

	def set_configuration(self, configuration: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:CONFiguration \n
		Snippet: driver.source.bb.eutra.uplink.prach.set_configuration(configuration = 1) \n
		Sets the PRACH configuration number. \n
			:param configuration: integer Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(configuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:CONFiguration {param}')

	def get_foffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:FOFFset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.prach.get_foffset() \n
		Sets the prach-FrequencyOffset nRAPRBoffset \n
			:return: frequency_offset: integer Range: 0 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:PRACh:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, frequency_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:FOFFset \n
		Snippet: driver.source.bb.eutra.uplink.prach.set_foffset(frequency_offset = 1) \n
		Sets the prach-FrequencyOffset nRAPRBoffset \n
			:param frequency_offset: integer Range: 0 to dynamic
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_rset(self) -> enums.EutraPrachPreambleSet:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:RSET \n
		Snippet: value: enums.EutraPrachPreambleSet = driver.source.bb.eutra.uplink.prach.get_rset() \n
		Enables/disables using of a restricted preamble set. \n
			:return: restricted_set: URES| ARES| BRES| OFF| ON URES|OFF Unrestricted preamble set. ARES|ON Restricted set type A. BRES Restricted set type B.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:PRACh:RSET?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPrachPreambleSet)

	def set_rset(self, restricted_set: enums.EutraPrachPreambleSet) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:RSET \n
		Snippet: driver.source.bb.eutra.uplink.prach.set_rset(restricted_set = enums.EutraPrachPreambleSet.ARES) \n
		Enables/disables using of a restricted preamble set. \n
			:param restricted_set: URES| ARES| BRES| OFF| ON URES|OFF Unrestricted preamble set. ARES|ON Restricted set type A. BRES Restricted set type B.
		"""
		param = Conversions.enum_scalar_to_str(restricted_set, enums.EutraPrachPreambleSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:RSET {param}')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
