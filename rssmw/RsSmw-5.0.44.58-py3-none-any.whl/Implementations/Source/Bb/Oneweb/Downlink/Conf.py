from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conf:
	"""Conf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conf", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ScheduleMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CONF:MODE \n
		Snippet: value: enums.ScheduleMode = driver.source.bb.oneweb.downlink.conf.get_mode() \n
		Queries the PDSCH scheduling mode. \n
			:return: scheduling: AUTO Enables the generation of ONEWeb signal and the PDSCH allocations are configured automatically accodring to the configuration of the PDCCH DCIs.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CONF:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ScheduleMode)
