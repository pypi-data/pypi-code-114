from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lpy:
	"""Lpy commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lpy", core, parent)

	@property
	def rfSignalling(self):
		"""rfSignalling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfSignalling'):
			from .RfSignalling import RfSignalling
			self._rfSignalling = RfSignalling(self._core, self._cmd_group)
		return self._rfSignalling

	# noinspection PyTypeChecker
	def get_constel(self) -> enums.Dvbt2T2SystemL1PostModulation:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:CONStel \n
		Snippet: value: enums.Dvbt2T2SystemL1PostModulation = driver.source.bb.t2Dvb.lpy.get_constel() \n
		Sets the modulation of the L1 post signal. \n
			:return: l_1_post_mod: T2| T4| T16| T64 T2 T4 T16 16 T64 64QAM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2T2SystemL1PostModulation)

	def set_constel(self, l_1_post_mod: enums.Dvbt2T2SystemL1PostModulation) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:CONStel \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_constel(l_1_post_mod = enums.Dvbt2T2SystemL1PostModulation.T16) \n
		Sets the modulation of the L1 post signal. \n
			:param l_1_post_mod: T2| T4| T16| T64 T2 T4 T16 16 T64 64QAM
		"""
		param = Conversions.enum_scalar_to_str(l_1_post_mod, enums.Dvbt2T2SystemL1PostModulation)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:CONStel {param}')

	# noinspection PyTypeChecker
	def get_extension(self) -> enums.SystemPostExtension:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:EXTension \n
		Snippet: value: enums.SystemPostExtension = driver.source.bb.t2Dvb.lpy.get_extension() \n
		Queries the L1 post extension state. The current firmware does not support L1 post extension. \n
			:return: l_1_post_ext: OFF OFF Fixed response of the query.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:EXTension?')
		return Conversions.str_to_scalar_enum(response, enums.SystemPostExtension)

	def set_extension(self, l_1_post_ext: enums.SystemPostExtension) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:EXTension \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_extension(l_1_post_ext = enums.SystemPostExtension.OFF) \n
		Queries the L1 post extension state. The current firmware does not support L1 post extension. \n
			:param l_1_post_ext: OFF OFF Fixed response of the query.
		"""
		param = Conversions.enum_scalar_to_str(l_1_post_ext, enums.SystemPostExtension)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:EXTension {param}')

	def get_repetition(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:REPetition \n
		Snippet: value: bool = driver.source.bb.t2Dvb.lpy.get_repetition() \n
		Enables/disables L1 repetition. \n
			:return: l_1_repetition: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:REPetition?')
		return Conversions.str_to_bool(response)

	def set_repetition(self, l_1_repetition: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:REPetition \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_repetition(l_1_repetition = False) \n
		Enables/disables L1 repetition. \n
			:param l_1_repetition: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(l_1_repetition)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:REPetition {param}')

	def get_scrambled(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:SCRambled \n
		Snippet: value: bool = driver.source.bb.t2Dvb.lpy.get_scrambled() \n
		Enables/disables L1 post scrambling according to T2 version 1.3.1 of specification . You can query the used version via
		[:SOURce<hw>]:BB:T2DVb:L:T2Version. \n
			:return: l_1_post_scr: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:SCRambled?')
		return Conversions.str_to_bool(response)

	def set_scrambled(self, l_1_post_scr: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:SCRambled \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_scrambled(l_1_post_scr = False) \n
		Enables/disables L1 post scrambling according to T2 version 1.3.1 of specification . You can query the used version via
		[:SOURce<hw>]:BB:T2DVb:L:T2Version. \n
			:param l_1_post_scr: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(l_1_post_scr)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:SCRambled {param}')

	def get_t_2_base_lite(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:T2Baselite \n
		Snippet: value: bool = driver.source.bb.t2Dvb.lpy.get_t_2_base_lite() \n
		Enables/disables T2 base lite signaling according to T2 version 1.3.1 of specification . You can query the used version
		via [:SOURce<hw>]:BB:T2DVb:L:T2Version. \n
			:return: t_2_base_lite: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:T2Baselite?')
		return Conversions.str_to_bool(response)

	def set_t_2_base_lite(self, t_2_base_lite: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:T2Baselite \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_t_2_base_lite(t_2_base_lite = False) \n
		Enables/disables T2 base lite signaling according to T2 version 1.3.1 of specification . You can query the used version
		via [:SOURce<hw>]:BB:T2DVb:L:T2Version. \n
			:param t_2_base_lite: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(t_2_base_lite)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:T2Baselite {param}')

	# noinspection PyTypeChecker
	def get_t_2_version(self) -> enums.Dvbt2T2SystemL1T2Version:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:T2Version \n
		Snippet: value: enums.Dvbt2T2SystemL1T2Version = driver.source.bb.t2Dvb.lpy.get_t_2_version() \n
		Sets the version of T2 specification , that is used for transmission. \n
			:return: t_2_version: V111| V121| V131
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:T2Version?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2T2SystemL1T2Version)

	def set_t_2_version(self, t_2_version: enums.Dvbt2T2SystemL1T2Version) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:T2Version \n
		Snippet: driver.source.bb.t2Dvb.lpy.set_t_2_version(t_2_version = enums.Dvbt2T2SystemL1T2Version.V111) \n
		Sets the version of T2 specification , that is used for transmission. \n
			:param t_2_version: V111| V121| V131
		"""
		param = Conversions.enum_scalar_to_str(t_2_version, enums.Dvbt2T2SystemL1T2Version)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:T2Version {param}')

	def clone(self) -> 'Lpy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lpy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
