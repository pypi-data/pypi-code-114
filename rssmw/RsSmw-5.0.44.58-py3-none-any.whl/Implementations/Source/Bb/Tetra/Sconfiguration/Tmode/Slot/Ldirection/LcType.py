from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LcType:
	"""LcType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcType", core, parent)

	def set(self, lc_type: enums.TetraLgChType, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:LCTYpe \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.lcType.set(lc_type = enums.TetraLgChType.B16H, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the logical channel type. The available channels depend on the selected test mode and link direction. \n
			:param lc_type: T72| T48| T24| TCHF| TCHH| STCH| SSTCh| SCHF| T108| SP8F| SSHD| BSHD| SBNCh| BBNCh| S8HD| D4H| D16H| D64H| D64M| D16U| D64U| B4H| B16H| B64H| B64M| B16U| B64U| SSHU| S8HU| S4S8| S8S4| U4H| U16H| U64H| U64M| U16U| U64U| H4H| H16H| H64H| H64M| H16U| H64U| SQRA| D4U| U4U
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.enum_scalar_to_str(lc_type, enums.TetraLgChType)
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:LCTYpe {param}')

	# noinspection PyTypeChecker
	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> enums.TetraLgChType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:LCTYpe \n
		Snippet: value: enums.TetraLgChType = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.lcType.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the logical channel type. The available channels depend on the selected test mode and link direction. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: lc_type: T72| T48| T24| TCHF| TCHH| STCH| SSTCh| SCHF| T108| SP8F| SSHD| BSHD| SBNCh| BBNCh| S8HD| D4H| D16H| D64H| D64M| D16U| D64U| B4H| B16H| B64H| B64M| B16U| B64U| SSHU| S8HU| S4S8| S8S4| U4H| U16H| U64H| U64M| U16U| U64U| H4H| H16H| H64H| H64M| H16U| H64U| SQRA| D4U| U4U"""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:LCTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraLgChType)
