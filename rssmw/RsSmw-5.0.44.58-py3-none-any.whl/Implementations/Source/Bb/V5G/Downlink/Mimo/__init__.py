from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def apm(self):
		"""apm commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_apm'):
			from .Apm import Apm
			self._apm = Apm(self._core, self._cmd_group)
		return self._apm

	# noinspection PyTypeChecker
	def get_antenna(self) -> enums.SimAnt:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:MIMO:ANTenna \n
		Snippet: value: enums.SimAnt = driver.source.bb.v5G.downlink.mimo.get_antenna() \n
		No command help available \n
			:return: antenna: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:MIMO:ANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.SimAnt)

	def set_antenna(self, antenna: enums.SimAnt) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:MIMO:ANTenna \n
		Snippet: driver.source.bb.v5G.downlink.mimo.set_antenna(antenna = enums.SimAnt.ANT1) \n
		No command help available \n
			:param antenna: No help available
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.SimAnt)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:MIMO:ANTenna {param}')

	# noinspection PyTypeChecker
	def get_configuration(self) -> enums.GlobMimoConf:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:MIMO:CONFiguration \n
		Snippet: value: enums.GlobMimoConf = driver.source.bb.v5G.downlink.mimo.get_configuration() \n
		No command help available \n
			:return: configuration: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:MIMO:CONFiguration?')
		return Conversions.str_to_scalar_enum(response, enums.GlobMimoConf)

	def set_configuration(self, configuration: enums.GlobMimoConf) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:MIMO:CONFiguration \n
		Snippet: driver.source.bb.v5G.downlink.mimo.set_configuration(configuration = enums.GlobMimoConf.SIBF) \n
		No command help available \n
			:param configuration: No help available
		"""
		param = Conversions.enum_scalar_to_str(configuration, enums.GlobMimoConf)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:MIMO:CONFiguration {param}')

	def clone(self) -> 'Mimo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mimo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
