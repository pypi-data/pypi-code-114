from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class End:
	"""End commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("end", core, parent)

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:POWer:RX:END \n
		Snippet: value: float = driver.source.regenerator.object.power.rx.end.get(objectIx = repcap.ObjectIx.Default) \n
		Queries the radar Rx power PRx. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: radar_power_rx_end: float Range: -465 to 578"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:POWer:RX:END?')
		return Conversions.str_to_float(response)
