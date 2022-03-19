from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpdcchset:
	"""Mpdcchset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpdcchset", core, parent)

	def set(self, dci_mpdcch_set: enums.EutraPdcchTypeEmtc, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:MPDCchset \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.mpdcchset.set(dci_mpdcch_set = enums.EutraPdcchTypeEmtc.MPD1, allocationNull = repcap.AllocationNull.Default) \n
		Selects the MPDCCH set by which the DCI is carried. \n
			:param dci_mpdcch_set: MPD1| MPD2
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(dci_mpdcch_set, enums.EutraPdcchTypeEmtc)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:MPDCchset {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraPdcchTypeEmtc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:MPDCchset \n
		Snippet: value: enums.EutraPdcchTypeEmtc = driver.source.bb.eutra.downlink.emtc.dci.alloc.mpdcchset.get(allocationNull = repcap.AllocationNull.Default) \n
		Selects the MPDCCH set by which the DCI is carried. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_mpdcch_set: MPD1| MPD2"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:MPDCchset?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPdcchTypeEmtc)
