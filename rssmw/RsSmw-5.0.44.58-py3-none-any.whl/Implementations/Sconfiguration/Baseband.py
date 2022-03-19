from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Baseband:
	"""Baseband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("baseband", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SystConfBbConf:
		"""SCPI: SCONfiguration:BASeband:SOURce \n
		Snippet: value: enums.SystConfBbConf = driver.sconfiguration.baseband.get_source() \n
		Determines whether coupled or separated baseband sources are used. \n
			:return: sour_config: SEParate| COUPled| CPENtity SEParate Enabled in LxMxN configurations with L ≤ 2 and M 4 COUPled|CPENtity Enabled in LxMxN configurations with L 2 CPENtity enabled in LxMxN configurations with L 1 and M 1.
		"""
		response = self._core.io.query_str('SCONfiguration:BASeband:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfBbConf)

	def set_source(self, sour_config: enums.SystConfBbConf) -> None:
		"""SCPI: SCONfiguration:BASeband:SOURce \n
		Snippet: driver.sconfiguration.baseband.set_source(sour_config = enums.SystConfBbConf.COUPled) \n
		Determines whether coupled or separated baseband sources are used. \n
			:param sour_config: SEParate| COUPled| CPENtity SEParate Enabled in LxMxN configurations with L ≤ 2 and M 4 COUPled|CPENtity Enabled in LxMxN configurations with L 2 CPENtity enabled in LxMxN configurations with L 1 and M 1.
		"""
		param = Conversions.enum_scalar_to_str(sour_config, enums.SystConfBbConf)
		self._core.io.write(f'SCONfiguration:BASeband:SOURce {param}')
