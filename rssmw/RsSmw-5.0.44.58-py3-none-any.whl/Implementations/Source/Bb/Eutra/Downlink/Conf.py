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
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CONF:MODE \n
		Snippet: value: enums.PdschSchedMode = driver.source.bb.eutra.downlink.conf.get_mode() \n
		Determines how the scheduling of the different PDSCH allocations inside of the DL allocation table is performed. \n
			:return: scheduling: MANual| AUTO| ASEQuence MANual No cross-reference between the settings made for the PDCCH DCIs and the PDSCHs settings. Configure the PDSCH allocations manually. AUTO Precoding for spatial multiplexing according to and the selected parameters. ASEQuence According to the required HARQ processes and redundancy versions
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:CONF:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PdschSchedMode)

	def set_mode(self, scheduling: enums.PdschSchedMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CONF:MODE \n
		Snippet: driver.source.bb.eutra.downlink.conf.set_mode(scheduling = enums.PdschSchedMode.ASEQuence) \n
		Determines how the scheduling of the different PDSCH allocations inside of the DL allocation table is performed. \n
			:param scheduling: MANual| AUTO| ASEQuence MANual No cross-reference between the settings made for the PDCCH DCIs and the PDSCHs settings. Configure the PDSCH allocations manually. AUTO Precoding for spatial multiplexing according to and the selected parameters. ASEQuence According to the required HARQ processes and redundancy versions
		"""
		param = Conversions.enum_scalar_to_str(scheduling, enums.PdschSchedMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CONF:MODE {param}')
