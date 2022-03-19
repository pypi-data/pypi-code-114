from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfactor:
	"""Cfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfactor", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbMultCarrCresMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CFACtor:MODE \n
		Snippet: value: enums.ArbMultCarrCresMode = driver.source.bb.arbitrary.mcarrier.cfactor.get_mode() \n
		Sets the mode for optimizing the crest factor by calculating the carrier phases. \n
			:return: mode: OFF| MIN| MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CFACtor:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbMultCarrCresMode)

	def set_mode(self, mode: enums.ArbMultCarrCresMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CFACtor:MODE \n
		Snippet: driver.source.bb.arbitrary.mcarrier.cfactor.set_mode(mode = enums.ArbMultCarrCresMode.MAX) \n
		Sets the mode for optimizing the crest factor by calculating the carrier phases. \n
			:param mode: OFF| MIN| MAX
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbMultCarrCresMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CFACtor:MODE {param}')
