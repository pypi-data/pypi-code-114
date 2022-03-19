from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protation:
	"""Protation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protation", core, parent)

	def set(self, protation: enums.TdscdmaPhasRot, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:PROTation \n
		Snippet: driver.source.bb.tdscdma.down.cell.protation.set(protation = enums.TdscdmaPhasRot.AUTO, cell = repcap.Cell.Default) \n
		Selects the phase rotation for the downlink pilots. \n
			:param protation: AUTO| S1| S2 AUTO Default phase rotation sequence according to the presence of the P-CCPCH. S1 There is a P-CCPCH in the next four subframes. S2 There is no P-CCPCH in the next four subframes.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(protation, enums.TdscdmaPhasRot)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:PROTation {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaPhasRot:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:PROTation \n
		Snippet: value: enums.TdscdmaPhasRot = driver.source.bb.tdscdma.down.cell.protation.get(cell = repcap.Cell.Default) \n
		Selects the phase rotation for the downlink pilots. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: protation: AUTO| S1| S2 AUTO Default phase rotation sequence according to the presence of the P-CCPCH. S1 There is a P-CCPCH in the next four subframes. S2 There is no P-CCPCH in the next four subframes."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:PROTation?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaPhasRot)
