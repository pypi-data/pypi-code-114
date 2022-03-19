from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class C1Mode:
	"""C1Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("c1Mode", core, parent)

	def set(self, dc_i_1_cmode: enums.EutraLaadci1Cmode, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:C1Mode \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.burst.c1Mode.set(dc_i_1_cmode = enums.EutraLaadci1Cmode.MANual, cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Defines how the DCI format 1C is sent. \n
			:param dc_i_1_cmode: MANual| N1| N| N1N
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
		"""
		param = Conversions.enum_scalar_to_str(dc_i_1_cmode, enums.EutraLaadci1Cmode)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:C1Mode {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> enums.EutraLaadci1Cmode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:C1Mode \n
		Snippet: value: enums.EutraLaadci1Cmode = driver.source.bb.eutra.downlink.laa.cell.burst.c1Mode.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Defines how the DCI format 1C is sent. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: dc_i_1_cmode: MANual| N1| N| N1N"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:C1Mode?')
		return Conversions.str_to_scalar_enum(response, enums.EutraLaadci1Cmode)
