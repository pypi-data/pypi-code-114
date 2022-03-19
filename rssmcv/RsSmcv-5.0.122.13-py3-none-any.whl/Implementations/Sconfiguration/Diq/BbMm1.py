from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbMm1:
	"""BbMm1 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbMm1", core, parent)

	# noinspection PyTypeChecker
	def get_channels(self) -> enums.SystConfHsChannels:
		"""SCPI: SCONfiguration:DIQ:BBMM1:CHANnels \n
		Snippet: value: enums.SystConfHsChannels = driver.sconfiguration.diq.bbMm1.get_channels() \n
		No command help available \n
			:return: dig_iq_hs_bbmm_1_cha: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:DIQ:BBMM1:CHANnels?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfHsChannels)

	def set_channels(self, dig_iq_hs_bbmm_1_cha: enums.SystConfHsChannels) -> None:
		"""SCPI: SCONfiguration:DIQ:BBMM1:CHANnels \n
		Snippet: driver.sconfiguration.diq.bbMm1.set_channels(dig_iq_hs_bbmm_1_cha = enums.SystConfHsChannels.CH0) \n
		No command help available \n
			:param dig_iq_hs_bbmm_1_cha: No help available
		"""
		param = Conversions.enum_scalar_to_str(dig_iq_hs_bbmm_1_cha, enums.SystConfHsChannels)
		self._core.io.write(f'SCONfiguration:DIQ:BBMM1:CHANnels {param}')
