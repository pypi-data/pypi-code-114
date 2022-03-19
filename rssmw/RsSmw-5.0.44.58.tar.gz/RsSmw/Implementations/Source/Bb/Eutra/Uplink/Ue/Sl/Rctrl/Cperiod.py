from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cperiod:
	"""Cperiod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cperiod", core, parent)

	def set(self, control_period: enums.EutraSlCommControlPeriod, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:CPERiod \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rctrl.cperiod.set(control_period = enums.EutraSlCommControlPeriod._120, userEquipment = repcap.UserEquipment.Default) \n
		Sets the period over which resources are allocated for sidelink control period (SC period) . \n
			:param control_period: 40| 60| 70| 80| 120| 140| 160| 240| 280| 320
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(control_period, enums.EutraSlCommControlPeriod)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:CPERiod {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlCommControlPeriod:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RCTRl:CPERiod \n
		Snippet: value: enums.EutraSlCommControlPeriod = driver.source.bb.eutra.uplink.ue.sl.rctrl.cperiod.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the period over which resources are allocated for sidelink control period (SC period) . \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: control_period: 40| 60| 70| 80| 120| 140| 160| 240| 280| 320"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RCTRl:CPERiod?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlCommControlPeriod)
