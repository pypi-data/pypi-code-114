from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stuffing:
	"""Stuffing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stuffing", core, parent)

	def set(self, stuffing: bool, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:STUFfing \n
		Snippet: driver.source.bb.t2Dvb.plp.inputPy.stuffing.set(stuffing = False, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Activates stuffing. \n
			:param stuffing: OFF| ON ON Inserts null packets and corrects the values. OFF The data rate of the transport stream source must match the data rate required for the current modulation parameters.
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.bool_to_str(stuffing)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:STUFfing {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:STUFfing \n
		Snippet: value: bool = driver.source.bb.t2Dvb.plp.inputPy.stuffing.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Activates stuffing. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: stuffing: OFF| ON ON Inserts null packets and corrects the values. OFF The data rate of the transport stream source must match the data rate required for the current modulation parameters."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:STUFfing?')
		return Conversions.str_to_bool(response)
