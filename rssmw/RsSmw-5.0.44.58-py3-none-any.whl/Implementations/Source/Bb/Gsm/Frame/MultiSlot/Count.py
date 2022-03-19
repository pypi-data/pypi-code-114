from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:MULTislot<ST0>:COUNt \n
		Snippet: driver.source.bb.gsm.frame.multiSlot.count.set(count = 1, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the number of slots combined in a multislot. Since multislot involves connecting multiple slots to a single user
		channel, this configuration is possible for Normal (Full Rate) bursts Normal (8PSK / EDGE) burst
		(SOUR:BB:GSM:FRAM:SLOT:TYPE NORM|EDGE) and EDGE Evolution bursts. The suffix in MULTislot defines the first slot in a
		multislot group. In a multiframe configuration, this setting applies to the slots in all frames. \n
			:param count: integer Range: 1 to 7
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'MultiSlot')
		"""
		param = Conversions.decimal_value_to_str(count)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:MULTislot{slotNull_cmd_val}:COUNt {param}')

	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:MULTislot<ST0>:COUNt \n
		Snippet: value: int = driver.source.bb.gsm.frame.multiSlot.count.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the number of slots combined in a multislot. Since multislot involves connecting multiple slots to a single user
		channel, this configuration is possible for Normal (Full Rate) bursts Normal (8PSK / EDGE) burst
		(SOUR:BB:GSM:FRAM:SLOT:TYPE NORM|EDGE) and EDGE Evolution bursts. The suffix in MULTislot defines the first slot in a
		multislot group. In a multiframe configuration, this setting applies to the slots in all frames. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'MultiSlot')
			:return: count: integer Range: 1 to 7"""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:MULTislot{slotNull_cmd_val}:COUNt?')
		return Conversions.str_to_int(response)
