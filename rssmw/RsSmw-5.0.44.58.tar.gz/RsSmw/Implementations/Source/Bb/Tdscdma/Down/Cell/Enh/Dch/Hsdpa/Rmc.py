from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmc", core, parent)

	def set(self, rmc: enums.TdscdmaEnhHsRmcMode, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:RMC \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.rmc.set(rmc = enums.TdscdmaEnhHsRmcMode.HRMC_0M5_QPSK, cell = repcap.Cell.Default) \n
		Enables a predefined set of RMC channels or fully configurable user mode. \n
			:param rmc: HRMC_0M5_QPSK| HRMC_1M1_QPSK| HRMC_1M1_16QAM| HRMC_1M6_QPSK| HRMC_1M6_16QAM| HRMC_2M2_QPSK| HRMC_2M2_16QAM| HRMC_2M8_QPSK| HRMC_2M8_16QAM| HRMC_64QAM_16UE| HRMC_64QAM_19UE| HRMC_64QAM_22UE| USER
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(rmc, enums.TdscdmaEnhHsRmcMode)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:RMC {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaEnhHsRmcMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:RMC \n
		Snippet: value: enums.TdscdmaEnhHsRmcMode = driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.rmc.get(cell = repcap.Cell.Default) \n
		Enables a predefined set of RMC channels or fully configurable user mode. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: rmc: HRMC_0M5_QPSK| HRMC_1M1_QPSK| HRMC_1M1_16QAM| HRMC_1M6_QPSK| HRMC_1M6_16QAM| HRMC_2M2_QPSK| HRMC_2M2_16QAM| HRMC_2M8_QPSK| HRMC_2M8_16QAM| HRMC_64QAM_16UE| HRMC_64QAM_19UE| HRMC_64QAM_22UE| USER"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:RMC?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaEnhHsRmcMode)
