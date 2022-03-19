from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BsAttenuation:
	"""BsAttenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsAttenuation", core, parent)

	def set(self, bs_attenuation: enums.AntennaNr, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:BSATtenuation \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.bsAttenuation.set(bs_attenuation = enums.AntennaNr.A1, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the level attenuation for the 'Slot Level' Attenuated setting. \n
			:param bs_attenuation: A1| A2| A3| A4
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.enum_scalar_to_str(bs_attenuation, enums.AntennaNr)
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:BSATtenuation {param}')

	# noinspection PyTypeChecker
	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> enums.AntennaNr:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:BSATtenuation \n
		Snippet: value: enums.AntennaNr = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.bsAttenuation.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the level attenuation for the 'Slot Level' Attenuated setting. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: bs_attenuation: A1| A2| A3| A4"""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:BSATtenuation?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaNr)
