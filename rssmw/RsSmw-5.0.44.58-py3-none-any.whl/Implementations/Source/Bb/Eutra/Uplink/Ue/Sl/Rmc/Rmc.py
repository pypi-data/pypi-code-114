from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmc", core, parent)

	def set(self, rmc: enums.EutraSlV2xRmc, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RMC:RMC \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rmc.rmc.set(rmc = enums.EutraSlV2xRmc.R821, userEquipment = repcap.UserEquipment.Default) \n
		Selects the RMC. \n
			:param rmc: R821| R822| R823
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(rmc, enums.EutraSlV2xRmc)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RMC:RMC {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlV2xRmc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RMC:RMC \n
		Snippet: value: enums.EutraSlV2xRmc = driver.source.bb.eutra.uplink.ue.sl.rmc.rmc.get(userEquipment = repcap.UserEquipment.Default) \n
		Selects the RMC. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: rmc: R821| R822| R823"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RMC:RMC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlV2xRmc)
