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
class Tpattern:
	"""Tpattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpattern", core, parent)

	def set(self, tpattern: List[str], bitcount: int, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:TPATtern \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.tpattern.set(tpattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Enters a user-defined TSC. The length of the training sequences depends on the burst type. The first user bit is
		equivalent to the first bit of the training sequence. All further will be inserted successively. \n
			:param tpattern: numeric
			:param bitcount: integer Range: 1 to 96
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('tpattern', tpattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:TPATtern {param}'.rstrip())

	# noinspection PyTypeChecker
	class TpatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Tpattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 96"""
		__meta_args_list = [
			ArgStruct('Tpattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tpattern: List[str] = None
			self.Bitcount: int = None

	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> TpatternStruct:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:TPATtern \n
		Snippet: value: TpatternStruct = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.tpattern.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Enters a user-defined TSC. The length of the training sequences depends on the burst type. The first user bit is
		equivalent to the first bit of the training sequence. All further will be inserted successively. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: structure: for return value, see the help for TpatternStruct structure arguments."""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:TPATtern?', self.__class__.TpatternStruct())
