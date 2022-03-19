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
class Sfbmp:
	"""Sfbmp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfbmp", core, parent)

	def set(self, pattern: List[str], bitcount: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:SFBMp \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rctrl.sfbmp.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the subframe bitmap. \n
			:param pattern: numeric
			:param bitcount: integer Range: 1 to 42
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:SFBMp {param}'.rstrip())

	# noinspection PyTypeChecker
	class SfbmpStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 42"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, userEquipment=repcap.UserEquipment.Default) -> SfbmpStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:SFBMp \n
		Snippet: value: SfbmpStruct = driver.source.bb.eutra.uplink.ue.sl.rctrl.sfbmp.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the subframe bitmap. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: structure: for return value, see the help for SfbmpStruct structure arguments."""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:SFBMp?', self.__class__.SfbmpStruct())
