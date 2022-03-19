from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OcqiMin:
	"""OcqiMin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ocqiMin", core, parent)

	def set(self, chan_cod_ocqi_min: int, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:[CELL<CCIDX>]:PUACh:CCODing:OCQimin \n
		Snippet: driver.source.bb.oneweb.uplink.ue.cell.puach.ccoding.ocqiMin.set(chan_cod_ocqi_min = 1, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For PUSCH/PUACH channel coding and multiplexing mode UCI only, sets the parameter O_CQI-Min. \n
			:param chan_cod_ocqi_min: integer Range: 1 to 472
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(chan_cod_ocqi_min)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUACh:CCODing:OCQimin {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:[CELL<CCIDX>]:PUACh:CCODing:OCQimin \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.ue.cell.puach.ccoding.ocqiMin.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For PUSCH/PUACH channel coding and multiplexing mode UCI only, sets the parameter O_CQI-Min. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: chan_cod_ocqi_min: integer Range: 1 to 472"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUACh:CCODing:OCQimin?')
		return Conversions.str_to_int(response)
