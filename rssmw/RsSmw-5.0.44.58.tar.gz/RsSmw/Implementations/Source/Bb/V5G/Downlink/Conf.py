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
	def get_mode(self) -> enums.PdschSchedMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CONF:MODE \n
		Snippet: value: enums.PdschSchedMode = driver.source.bb.v5G.downlink.conf.get_mode() \n
		Selects manual or automatic scheduling mode. \n
			:return: scheduling: MANual| AUTO
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:CONF:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PdschSchedMode)

	def set_mode(self, scheduling: enums.PdschSchedMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CONF:MODE \n
		Snippet: driver.source.bb.v5G.downlink.conf.set_mode(scheduling = enums.PdschSchedMode.ASEQuence) \n
		Selects manual or automatic scheduling mode. \n
			:param scheduling: MANual| AUTO
		"""
		param = Conversions.enum_scalar_to_str(scheduling, enums.PdschSchedMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CONF:MODE {param}')
