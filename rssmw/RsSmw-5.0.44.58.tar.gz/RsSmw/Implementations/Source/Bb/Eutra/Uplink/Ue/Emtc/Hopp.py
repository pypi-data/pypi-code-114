from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopp:
	"""Hopp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopp", core, parent)

	def set(self, hopping_interval: enums.EutraIotHoppingIvl, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:HOPP \n
		Snippet: driver.source.bb.eutra.uplink.ue.emtc.hopp.set(hopping_interval = enums.EutraIotHoppingIvl.H1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the narrowband hopping interval. \n
			:param hopping_interval: H1| H2| H4| H5| H8| H10| H16| H20| H40
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(hopping_interval, enums.EutraIotHoppingIvl)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:HOPP {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraIotHoppingIvl:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:HOPP \n
		Snippet: value: enums.EutraIotHoppingIvl = driver.source.bb.eutra.uplink.ue.emtc.hopp.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the narrowband hopping interval. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: hopping_interval: H1| H2| H4| H5| H8| H10| H16| H20| H40"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:HOPP?')
		return Conversions.str_to_scalar_enum(response, enums.EutraIotHoppingIvl)
