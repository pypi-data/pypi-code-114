from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, nbiot_an_pat: List[str], bitcount: int, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:HARQ:PATTern \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.trans.harq.pattern.set(nbiot_an_pat = ['raw1', 'raw2', 'raw3'], bitcount = 1, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Set the ACK/ANCK pattern. \n
			:param nbiot_an_pat: numeric
			:param bitcount: integer Range: 1 to 1
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('nbiot_an_pat', nbiot_an_pat, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:HARQ:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Nbiot_An_Pat: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 1"""
		__meta_args_list = [
			ArgStruct('Nbiot_An_Pat', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nbiot_An_Pat: List[str] = None
			self.Bitcount: int = None

	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:HARQ:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.eutra.uplink.ue.niot.trans.harq.pattern.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Set the ACK/ANCK pattern. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:HARQ:PATTern?', self.__class__.PatternStruct())
