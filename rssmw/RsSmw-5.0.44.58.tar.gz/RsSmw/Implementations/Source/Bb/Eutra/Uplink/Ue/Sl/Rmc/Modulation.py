from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.ModulationD:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RMC:MODulation \n
		Snippet: value: enums.ModulationD = driver.source.bb.eutra.uplink.ue.sl.rmc.modulation.get(userEquipment = repcap.UserEquipment.Default) \n
		Queries the used modulation scheme. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: rmc_modulation: QPSK| QAM16| QAM64| QAM256| QAM1024"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RMC:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationD)
