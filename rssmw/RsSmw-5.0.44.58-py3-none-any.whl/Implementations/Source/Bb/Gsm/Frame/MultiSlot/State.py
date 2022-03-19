from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:MULTislot<ST0>:STATe \n
		Snippet: driver.source.bb.gsm.frame.multiSlot.state.set(state = False, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Switches the multislot configuration on. The suffix in MULTislot defines the first slot in a multislot group.
		In a multiframe configuration, this setting applies to the slots in all frames. \n
			:param state: 1| ON| 0| OFF
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'MultiSlot')
		"""
		param = Conversions.bool_to_str(state)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:MULTislot{slotNull_cmd_val}:STATe {param}')

	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:MULTislot<ST0>:STATe \n
		Snippet: value: bool = driver.source.bb.gsm.frame.multiSlot.state.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Switches the multislot configuration on. The suffix in MULTislot defines the first slot in a multislot group.
		In a multiframe configuration, this setting applies to the slots in all frames. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'MultiSlot')
			:return: state: 1| ON| 0| OFF"""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:MULTislot{slotNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
