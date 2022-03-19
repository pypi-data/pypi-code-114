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
class SdPattern:
	"""SdPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdPattern", core, parent)

	def set(self, sd_pattern: List[str], bitcount: int, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:SDATa:SDPattern \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.sdata.sdPattern.set(sd_pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the data pattern for data source pattern
		([:SOURce<hw>]:BB:TETRa:SCONfiguration:TMODe<di>:SLOT<st>:LDIRection<ch>:SDATa) . \n
			:param sd_pattern: numeric
			:param bitcount: integer Range: 1 to 64
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('sd_pattern', sd_pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:SDATa:SDPattern {param}'.rstrip())

	# noinspection PyTypeChecker
	class SdPatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Sd_Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 64"""
		__meta_args_list = [
			ArgStruct('Sd_Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sd_Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> SdPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:SDATa:SDPattern \n
		Snippet: value: SdPatternStruct = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.sdata.sdPattern.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the data pattern for data source pattern
		([:SOURce<hw>]:BB:TETRa:SCONfiguration:TMODe<di>:SLOT<st>:LDIRection<ch>:SDATa) . \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: structure: for return value, see the help for SdPatternStruct structure arguments."""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:SDATa:SDPattern?', self.__class__.SdPatternStruct())
