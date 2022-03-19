from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 6 total commands, 1 Subgroups, 2 group commands"""

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
	def get_antenna(self) -> enums.OneWebSimAnt:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:ANTenna \n
		Snippet: value: enums.OneWebSimAnt = driver.source.bb.oneweb.downlink.mimo.get_antenna() \n
		Queries the simulated antenna. \n
			:return: antenna: ANT1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:ANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebSimAnt)

	# noinspection PyTypeChecker
	def get_configuration(self) -> enums.OneWebGlobMimoConf:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:CONFiguration \n
		Snippet: value: enums.OneWebGlobMimoConf = driver.source.bb.oneweb.downlink.mimo.get_configuration() \n
		Queries the global MIMO configuration. \n
			:return: configuration: TX1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:CONFiguration?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebGlobMimoConf)

	def clone(self) -> 'Mimo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mimo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
