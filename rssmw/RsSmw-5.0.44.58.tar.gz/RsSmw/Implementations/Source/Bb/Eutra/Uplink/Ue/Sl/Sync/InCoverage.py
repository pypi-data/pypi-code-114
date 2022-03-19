from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InCoverage:
	"""InCoverage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inCoverage", core, parent)

	def set(self, in_coverage: bool, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SYNC:INCoverage \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sync.inCoverage.set(in_coverage = False, userEquipment = repcap.UserEquipment.Default) \n
		Sets the in-coverage flag. \n
			:param in_coverage: 1| ON| 0| OFF
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.bool_to_str(in_coverage)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SYNC:INCoverage {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SYNC:INCoverage \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.ue.sl.sync.inCoverage.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the in-coverage flag. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: in_coverage: 1| ON| 0| OFF"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SYNC:INCoverage?')
		return Conversions.str_to_bool(response)
