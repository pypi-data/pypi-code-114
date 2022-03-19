from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N1Pdsch:
	"""N1Pdsch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n1Pdsch", core, parent)

	def set(self, n_1_pdsch: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:N1PDsch \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdisc.n1Pdsch.set(n_1_pdsch = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the PDSCH resource index. \n
			:param n_1_pdsch: integer Range: 1 to 200
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(n_1_pdsch)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:N1PDsch {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:N1PDsch \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdisc.n1Pdsch.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the PDSCH resource index. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: n_1_pdsch: integer Range: 1 to 200"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:N1PDsch?')
		return Conversions.str_to_int(response)
