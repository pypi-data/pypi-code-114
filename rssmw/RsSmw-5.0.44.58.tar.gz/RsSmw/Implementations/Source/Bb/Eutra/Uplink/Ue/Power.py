from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:POWer \n
		Snippet: driver.source.bb.eutra.uplink.ue.power.set(power = 1.0, userEquipment = repcap.UserEquipment.Default) \n
		Sets the power level of the selected UE. \n
			:param power: float Range: -80 to 10
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(power)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:POWer {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:POWer \n
		Snippet: value: float = driver.source.bb.eutra.uplink.ue.power.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the power level of the selected UE. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: power: float Range: -80 to 10"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:POWer?')
		return Conversions.str_to_float(response)
