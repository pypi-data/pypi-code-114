from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aapto:
	"""Aapto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aapto", core, parent)

	def set(self, block_output: enums.EutraBlockOutput, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:AAPTo \n
		Snippet: driver.source.bb.eutra.uplink.ue.aapto.set(block_output = enums.EutraBlockOutput.OUT0, userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param block_output: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(block_output, enums.EutraBlockOutput)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:AAPTo {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraBlockOutput:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:AAPTo \n
		Snippet: value: enums.EutraBlockOutput = driver.source.bb.eutra.uplink.ue.aapto.get(userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: block_output: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:AAPTo?')
		return Conversions.str_to_scalar_enum(response, enums.EutraBlockOutput)
