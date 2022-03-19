from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:USEFul:[RATE]:MAX \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.useful.rate.max.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the maximum data rate, that is derived from the current modulation parameter settings. The value is the optimal
		value at the TS input interface, that is necessary for the modulator. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: max_py: integer Range: 0 to 999999999"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:USEFul:RATE:MAX?')
		return Conversions.str_to_int(response)
