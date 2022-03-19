from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdcch:
	"""Pdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	def set(self, dci_pdcch_fmt: enums.EutraMpdcchFormat, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PDCCh \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.pdcch.set(dci_pdcch_fmt = enums.EutraMpdcchFormat._0, allocationNull = repcap.AllocationNull.Default) \n
		Selects one of the five MPDCCH formats \n
			:param dci_pdcch_fmt: 0| 1| 2| 3| 4| 5 The available values depend on the search space.
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(dci_pdcch_fmt, enums.EutraMpdcchFormat)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PDCCh {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraMpdcchFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PDCCh \n
		Snippet: value: enums.EutraMpdcchFormat = driver.source.bb.eutra.downlink.emtc.dci.alloc.pdcch.get(allocationNull = repcap.AllocationNull.Default) \n
		Selects one of the five MPDCCH formats \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_pdcch_fmt: 0| 1| 2| 3| 4| 5 The available values depend on the search space."""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PDCCh?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMpdcchFormat)
