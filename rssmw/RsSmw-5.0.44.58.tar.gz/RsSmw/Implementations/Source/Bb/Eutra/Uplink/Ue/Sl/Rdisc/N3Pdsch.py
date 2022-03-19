from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N3Pdsch:
	"""N3Pdsch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n3Pdsch", core, parent)

	def set(self, n_3_pdsch: enums.EutraSlN3Pdsch, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:N3PDsch \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdisc.n3Pdsch.set(n_3_pdsch = enums.EutraSlN3Pdsch._1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the PDSCH resource index. \n
			:param n_3_pdsch: 1| 5
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(n_3_pdsch, enums.EutraSlN3Pdsch)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:N3PDsch {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraSlN3Pdsch:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:N3PDsch \n
		Snippet: value: enums.EutraSlN3Pdsch = driver.source.bb.eutra.uplink.ue.sl.rdisc.n3Pdsch.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the PDSCH resource index. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: n_3_pdsch: 1| 5"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:N3PDsch?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSlN3Pdsch)
