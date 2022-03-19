from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeMode:
	"""UeMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueMode", core, parent)

	def set(self, ue_mode: enums.UeMode, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:UEMode \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.ueMode.set(ue_mode = enums.UeMode.PRACh, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field mode and defines if the DCI format 6-1A/B is used for PDSCH or PRACH. \n
			:param ue_mode: STD| PRACh
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(ue_mode, enums.UeMode)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:UEMode {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.UeMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:UEMode \n
		Snippet: value: enums.UeMode = driver.source.bb.eutra.downlink.emtc.dci.alloc.ueMode.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field mode and defines if the DCI format 6-1A/B is used for PDSCH or PRACH. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: ue_mode: STD| PRACh"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:UEMode?')
		return Conversions.str_to_scalar_enum(response, enums.UeMode)
