from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:PRACh:SUBF<CH0>:STATe \n
		Snippet: driver.source.bb.oneweb.uplink.ue.prach.subf.state.set(state = False, userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Enables/disables the PRACH for the selected subframe. The subframes available for configuration depend on the selected
		PRACH configuration. \n
			:param state: 0| 1| OFF| ON
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.bool_to_str(state)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:STATe {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:PRACh:SUBF<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.ue.prach.subf.state.get(userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Enables/disables the PRACH for the selected subframe. The subframes available for configuration depend on the selected
		PRACH configuration. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: state: 0| 1| OFF| ON"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
