from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dt:
	"""Dt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dt", core, parent)

	def set(self, delta_time: float, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:PRACh:SUBF<CH0>:DT \n
		Snippet: driver.source.bb.v5G.uplink.ue.prach.subf.dt.set(delta_time = 1.0, userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param delta_time: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(delta_time)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:DT {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:PRACh:SUBF<CH0>:DT \n
		Snippet: value: float = driver.source.bb.v5G.uplink.ue.prach.subf.dt.get(userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: delta_time: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:DT?')
		return Conversions.str_to_float(response)
