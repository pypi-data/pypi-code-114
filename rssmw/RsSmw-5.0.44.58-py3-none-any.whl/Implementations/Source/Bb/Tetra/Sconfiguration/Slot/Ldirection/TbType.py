from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TbType:
	"""TbType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbType", core, parent)

	def set(self, tb_type: enums.TetraT2BurstType, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:SLOT<ST>:LDIRection<CH>:TBTYpe \n
		Snippet: driver.source.bb.tetra.sconfiguration.slot.ldirection.tbType.set(tb_type = enums.TetraT2BurstType.CU16, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the burst type for 'Test Mode T2'. \n
			:param tb_type: NCDB| SCDB| NDDB| SDDB| ND4| ND16| ND64| NUB| CUB| NU4| NU16| NU64| CU4| CU16| CU64| RAB
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.enum_scalar_to_str(tb_type, enums.TetraT2BurstType)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:TBTYpe {param}')

	# noinspection PyTypeChecker
	def get(self, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> enums.TetraT2BurstType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:SLOT<ST>:LDIRection<CH>:TBTYpe \n
		Snippet: value: enums.TetraT2BurstType = driver.source.bb.tetra.sconfiguration.slot.ldirection.tbType.get(slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Selects the burst type for 'Test Mode T2'. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: tb_type: NCDB| SCDB| NDDB| SDDB| ND4| ND16| ND64| NUB| CUB| NU4| NU16| NU64| CU4| CU16| CU64| RAB"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:TBTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraT2BurstType)
