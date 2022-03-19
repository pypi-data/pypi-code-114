from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitHigh:
	"""BitHigh commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitHigh", core, parent)

	def set(self, pattern: List[str], bitcount: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:BITHigh \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.v2X.bitHigh.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the subframe bitmap. [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITHigh is enabled,
		if [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BMPLength60|100. \n
			:param pattern: numeric
			:param bitcount: integer Range: 0 to 50
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:BITHigh {param}'.rstrip())

	# noinspection PyTypeChecker
	class BitHighStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 0 to 50"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, userEquipment=repcap.UserEquipment.Default) -> BitHighStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:BITHigh \n
		Snippet: value: BitHighStruct = driver.source.bb.eutra.uplink.ue.sl.v2X.bitHigh.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the subframe bitmap. [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BITHigh is enabled,
		if [:SOURce<hw>]:BB:EUTRa:UL:UE<st>:SL:V2X:BMPLength60|100. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: structure: for return value, see the help for BitHighStruct structure arguments."""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:BITHigh?', self.__class__.BitHighStruct())
