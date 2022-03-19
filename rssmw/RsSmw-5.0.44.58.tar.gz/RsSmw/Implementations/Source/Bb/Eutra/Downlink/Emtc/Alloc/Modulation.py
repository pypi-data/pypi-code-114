from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.ModulationA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:MODulation \n
		Snippet: value: enums.ModulationA = driver.source.bb.eutra.downlink.emtc.alloc.modulation.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the used modulation scheme. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: modulation: QAM16| QPSK"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationA)
