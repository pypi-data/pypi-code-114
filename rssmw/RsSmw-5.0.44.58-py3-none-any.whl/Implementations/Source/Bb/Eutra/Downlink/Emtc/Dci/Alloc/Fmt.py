from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fmt:
	"""Fmt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmt", core, parent)

	def set(self, dci_format: enums.EutraDciFormatEmtc, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:FMT \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.fmt.set(dci_format = enums.EutraDciFormatEmtc.F3, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param dci_format: F3| F3A| F60A| F60B| F61A| F61B| F62
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(dci_format, enums.EutraDciFormatEmtc)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:FMT {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraDciFormatEmtc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:FMT \n
		Snippet: value: enums.EutraDciFormatEmtc = driver.source.bb.eutra.downlink.emtc.dci.alloc.fmt.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_format: F3| F3A| F60A| F60B| F61A| F61B| F62"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:FMT?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDciFormatEmtc)
