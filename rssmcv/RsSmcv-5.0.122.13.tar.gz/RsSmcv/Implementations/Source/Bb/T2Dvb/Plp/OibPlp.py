from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OibPlp:
	"""OibPlp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oibPlp", core, parent)

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:OIBPlp \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.oibPlp.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the number of other PLPs signaled within the in-band signaling of the PLP for multi-PLP. Multi-PLP requires
		number of PLPs > 1, see [:SOURce<hw>]:BB:T2DVb:INPut:NPLP?. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: oib_plps: integer Range: 0 to 255"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:OIBPlp?')
		return Conversions.str_to_int(response)
