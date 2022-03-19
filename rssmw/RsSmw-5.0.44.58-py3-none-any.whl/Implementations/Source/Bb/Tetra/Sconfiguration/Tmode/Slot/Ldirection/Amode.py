from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amode:
	"""Amode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amode", core, parent)

	def set(self, amode: enums.TetraAachqMode, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:AMODe \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.amode.set(amode = enums.TetraAachqMode.AAPDu, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		(enabled for Frame 1- 17) Sets the AACH-Q Mode element that indicates whether the Access-Assign PDU follows in the AACH-Q.
		The AACH-Q (Access Assignment Channel, QAM) channel is present on all transmitted downlink slots (except slots containing
		BLCH-Q) and is used to indicate on each QAM physical channel the assignment of the uplink and downlink slots. \n
			:param amode: AAPDu| RELement AAPDu The value of the AACH-Q Mode element is set to 0, i.e. contents of Access-Assign PDU are present. The Access-Assign PDU is used to convey information about the downlink slot in which it appears and also the access rights for the corresponding (same-numbered) uplink slot. The fields of the 'Access-Assign PDU' are defined with the corresponding parameters. RELement The value shall be set to all zeros.
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.enum_scalar_to_str(amode, enums.TetraAachqMode)
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:AMODe {param}')

	# noinspection PyTypeChecker
	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> enums.TetraAachqMode:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:AMODe \n
		Snippet: value: enums.TetraAachqMode = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.amode.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		(enabled for Frame 1- 17) Sets the AACH-Q Mode element that indicates whether the Access-Assign PDU follows in the AACH-Q.
		The AACH-Q (Access Assignment Channel, QAM) channel is present on all transmitted downlink slots (except slots containing
		BLCH-Q) and is used to indicate on each QAM physical channel the assignment of the uplink and downlink slots. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: amode: AAPDu| RELement AAPDu The value of the AACH-Q Mode element is set to 0, i.e. contents of Access-Assign PDU are present. The Access-Assign PDU is used to convey information about the downlink slot in which it appears and also the access rights for the corresponding (same-numbered) uplink slot. The fields of the 'Access-Assign PDU' are defined with the corresponding parameters. RELement The value shall be set to all zeros."""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraAachqMode)
