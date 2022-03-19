from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbsfn:
	"""Mbsfn commands group definition. 37 total commands, 4 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbsfn", core, parent)

	@property
	def ai(self):
		"""ai commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ai'):
			from .Ai import Ai
			self._ai = Ai(self._core, self._cmd_group)
		return self._ai

	@property
	def mtch(self):
		"""mtch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mtch'):
			from .Mtch import Mtch
			self._mtch = Mtch(self._core, self._cmd_group)
		return self._mtch

	@property
	def pmch(self):
		"""pmch commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmch'):
			from .Pmch import Pmch
			self._pmch = Pmch(self._core, self._cmd_group)
		return self._pmch

	@property
	def sc(self):
		"""sc commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_sc'):
			from .Sc import Sc
			self._sc = Sc(self._core, self._cmd_group)
		return self._sc

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EutraMbsfnType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:MODE \n
		Snippet: value: enums.EutraMbsfnType = driver.source.bb.eutra.downlink.mbsfn.get_mode() \n
		Enables the MBSFN transmission and selects a mixed MBSFN Mode. \n
			:return: mbsfn_mode: OFF| MIXed
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMbsfnType)

	def set_mode(self, mbsfn_mode: enums.EutraMbsfnType) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:MODE \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.set_mode(mbsfn_mode = enums.EutraMbsfnType.MIXed) \n
		Enables the MBSFN transmission and selects a mixed MBSFN Mode. \n
			:param mbsfn_mode: OFF| MIXed
		"""
		param = Conversions.enum_scalar_to_str(mbsfn_mode, enums.EutraMbsfnType)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:MODE {param}')

	def get_rhoa(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:RHOA \n
		Snippet: value: float = driver.source.bb.eutra.downlink.mbsfn.get_rhoa() \n
		Defines the power of the MBSFN channels relative to the common Reference Signals. \n
			:return: rhoa: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:RHOA?')
		return Conversions.str_to_float(response)

	def set_rhoa(self, rhoa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:RHOA \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.set_rhoa(rhoa = 1.0) \n
		Defines the power of the MBSFN channels relative to the common Reference Signals. \n
			:param rhoa: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(rhoa)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:RHOA {param}')

	# noinspection PyTypeChecker
	def get_uec(self) -> enums.UeCat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:UEC \n
		Snippet: value: enums.UeCat = driver.source.bb.eutra.downlink.mbsfn.get_uec() \n
		Defines the UE category as defined in . \n
			:return: ue_category: C1| C2| C3| C4| C5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:UEC?')
		return Conversions.str_to_scalar_enum(response, enums.UeCat)

	def set_uec(self, ue_category: enums.UeCat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:UEC \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.set_uec(ue_category = enums.UeCat.C1) \n
		Defines the UE category as defined in . \n
			:param ue_category: C1| C2| C3| C4| C5
		"""
		param = Conversions.enum_scalar_to_str(ue_category, enums.UeCat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:UEC {param}')

	def clone(self) -> 'Mbsfn':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbsfn(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
