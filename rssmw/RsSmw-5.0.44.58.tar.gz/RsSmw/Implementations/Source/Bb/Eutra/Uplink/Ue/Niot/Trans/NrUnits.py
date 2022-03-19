from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrUnits:
	"""NrUnits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrUnits", core, parent)

	def set(self, resource_units: enums.EutraIotRu, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:NRUNits \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.trans.nrUnits.set(resource_units = enums.EutraIotRu.RU1, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the number of allocated resource units. \n
			:param resource_units: RU1| RU2| RU3| RU4| RU5| RU6| RU8| RU10
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = Conversions.enum_scalar_to_str(resource_units, enums.EutraIotRu)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:NRUNits {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> enums.EutraIotRu:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:TRANs<CH>:NRUNits \n
		Snippet: value: enums.EutraIotRu = driver.source.bb.eutra.uplink.ue.niot.trans.nrUnits.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Sets the number of allocated resource units. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: resource_units: RU1| RU2| RU3| RU4| RU5| RU6| RU8| RU10"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:TRANs{transmission_cmd_val}:NRUNits?')
		return Conversions.str_to_scalar_enum(response, enums.EutraIotRu)
