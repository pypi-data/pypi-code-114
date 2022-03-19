from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfreq:
	"""Dfreq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfreq", core, parent)

	def set(self, delta_freq: float, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:DFReq \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.dfreq.set(delta_freq = 1.0, userEquipment = repcap.UserEquipment.Default) \n
		Sets the frequency offset between the NB-IoT carrier and the LTE center frequency. \n
			:param delta_freq: float Range: -1E7 to 1E7, Unit: MHz
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(delta_freq)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:DFReq {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:DFReq \n
		Snippet: value: float = driver.source.bb.eutra.uplink.ue.niot.dfreq.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the frequency offset between the NB-IoT carrier and the LTE center frequency. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: delta_freq: float Range: -1E7 to 1E7, Unit: MHz"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:DFReq?')
		return Conversions.str_to_float(response)
