from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layer", core, parent)

	def set(self, layer: enums.EnhBitErr, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:BIT:LAYer \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.bit.layer.set(layer = enums.EnhBitErr.PHYSical, cell = repcap.Cell.Default) \n
		Sets the layer in the coding process at which bit errors are inserted. \n
			:param layer: TRANsport| PHYSical
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(layer, enums.EnhBitErr)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:BIT:LAYer {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.EnhBitErr:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:BIT:LAYer \n
		Snippet: value: enums.EnhBitErr = driver.source.bb.tdscdma.down.cell.enh.dch.bit.layer.get(cell = repcap.Cell.Default) \n
		Sets the layer in the coding process at which bit errors are inserted. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: layer: TRANsport| PHYSical"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:BIT:LAYer?')
		return Conversions.str_to_scalar_enum(response, enums.EnhBitErr)
