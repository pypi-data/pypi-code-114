from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NzConfig:
	"""NzConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nzConfig", core, parent)

	def set(self, non_zero_pwr_conf: enums.NumbersE, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:NZConfig \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.csirs.nzConfig.set(non_zero_pwr_conf = enums.NumbersE._0, cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the CSI-RS configuration. \n
			:param non_zero_pwr_conf: 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25| 26| 27| 28| 29| 30| 31 Values outside the permitted discrete values are rounded down.
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
		"""
		param = Conversions.enum_scalar_to_str(non_zero_pwr_conf, enums.NumbersE)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZConfig {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> enums.NumbersE:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:NZConfig \n
		Snippet: value: enums.NumbersE = driver.source.bb.eutra.downlink.drs.cell.csirs.nzConfig.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the CSI-RS configuration. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: non_zero_pwr_conf: 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25| 26| 27| 28| 29| 30| 31 Values outside the permitted discrete values are rounded down."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZConfig?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersE)
