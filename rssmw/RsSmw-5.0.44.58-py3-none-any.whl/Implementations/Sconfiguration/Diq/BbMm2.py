from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbMm2:
	"""BbMm2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbMm2", core, parent)

	# noinspection PyTypeChecker
	def get_channels(self) -> enums.SystConfHsChannels:
		"""SCPI: SCONfiguration:DIQ:BBMM2:CHANnels \n
		Snippet: value: enums.SystConfHsChannels = driver.sconfiguration.diq.bbMm2.get_channels() \n
		In method RsSmw.Sconfiguration.Output.modeHSDigital|HSAL, sets the number of digital channels on the HS DIG I/Q interface.
		The total number of enabled channels on all HS DIG I/Q interface must not exceed 8. \n
			:return: dig_iq_hs_bbmm_2_cha: CH0| CH1| CH2| CH3| CH4| CH5| CH6| CH7| CH8
		"""
		response = self._core.io.query_str('SCONfiguration:DIQ:BBMM2:CHANnels?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfHsChannels)

	def set_channels(self, dig_iq_hs_bbmm_2_cha: enums.SystConfHsChannels) -> None:
		"""SCPI: SCONfiguration:DIQ:BBMM2:CHANnels \n
		Snippet: driver.sconfiguration.diq.bbMm2.set_channels(dig_iq_hs_bbmm_2_cha = enums.SystConfHsChannels.CH0) \n
		In method RsSmw.Sconfiguration.Output.modeHSDigital|HSAL, sets the number of digital channels on the HS DIG I/Q interface.
		The total number of enabled channels on all HS DIG I/Q interface must not exceed 8. \n
			:param dig_iq_hs_bbmm_2_cha: CH0| CH1| CH2| CH3| CH4| CH5| CH6| CH7| CH8
		"""
		param = Conversions.enum_scalar_to_str(dig_iq_hs_bbmm_2_cha, enums.SystConfHsChannels)
		self._core.io.write(f'SCONfiguration:DIQ:BBMM2:CHANnels {param}')
