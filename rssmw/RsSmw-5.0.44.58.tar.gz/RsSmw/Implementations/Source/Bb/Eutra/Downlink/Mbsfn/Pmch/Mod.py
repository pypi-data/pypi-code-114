from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mod:
	"""Mod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mod", core, parent)

	# noinspection PyTypeChecker
	def get(self, indexNull=repcap.IndexNull.Default) -> enums.ModulationD:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:MOD \n
		Snippet: value: enums.ModulationD = driver.source.bb.eutra.downlink.mbsfn.pmch.mod.get(indexNull = repcap.IndexNull.Default) \n
		Queries the used modulation. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: pmch_mod: QPSK| QAM16| QAM64 | QAM256"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:MOD?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationD)
