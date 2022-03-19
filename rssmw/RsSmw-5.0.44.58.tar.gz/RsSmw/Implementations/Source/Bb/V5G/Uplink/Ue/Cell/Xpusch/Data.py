from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: enums.DataSourceA, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:[CELL<CCIDX>]:XPUSch:DATA \n
		Snippet: driver.source.bb.v5G.uplink.ue.cell.xpusch.data.set(data = enums.DataSourceA.DLISt, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Selects the xPUSCH data source of the selected UE. For the selected UE, this data source is used for the xPUSCH channel
		in every subframe where this channel is configured. \n
			:param data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE ZERO / ONE All 0 or all 1 pattern PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:V5G:UL:UEst[:CELLccidx]:XPUSch:PATTern PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:V5G:UL:UEst[:CELLccidx]:XPUSch:DSELect
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:XPUSch:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:UE<ST>:[CELL<CCIDX>]:XPUSch:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.v5G.uplink.ue.cell.xpusch.data.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Selects the xPUSCH data source of the selected UE. For the selected UE, this data source is used for the xPUSCH channel
		in every subframe where this channel is configured. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE ZERO / ONE All 0 or all 1 pattern PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:V5G:UL:UEst[:CELLccidx]:XPUSch:PATTern PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:V5G:UL:UEst[:CELLccidx]:XPUSch:DSELect"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:XPUSch:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)
