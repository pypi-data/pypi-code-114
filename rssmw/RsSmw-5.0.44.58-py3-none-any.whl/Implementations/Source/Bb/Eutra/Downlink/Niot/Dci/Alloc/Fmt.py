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

	def set(self, format_py: enums.EutraNbiotDciFormat, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:FMT \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.fmt.set(format_py = enums.EutraNbiotDciFormat.N0, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param format_py: N0| N1| N2
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.EutraNbiotDciFormat)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:FMT {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraNbiotDciFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:FMT \n
		Snippet: value: enums.EutraNbiotDciFormat = driver.source.bb.eutra.downlink.niot.dci.alloc.fmt.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI format for the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: format_py: N0| N1| N2"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:FMT?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotDciFormat)
