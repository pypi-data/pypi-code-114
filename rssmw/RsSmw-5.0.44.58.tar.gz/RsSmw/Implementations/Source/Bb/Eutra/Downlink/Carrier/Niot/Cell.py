from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, cell_id: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:CELL \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.cell.set(cell_id = 1, carrier = repcap.Carrier.Default) \n
		Sets the narrowband physical cell identifier. \n
			:param cell_id: integer Range: 0 to 503
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:CELL {param}')

	def get(self, carrier=repcap.Carrier.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:CELL \n
		Snippet: value: int = driver.source.bb.eutra.downlink.carrier.niot.cell.get(carrier = repcap.Carrier.Default) \n
		Sets the narrowband physical cell identifier. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: cell_id: integer Range: 0 to 503"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:CELL?')
		return Conversions.str_to_int(response)
