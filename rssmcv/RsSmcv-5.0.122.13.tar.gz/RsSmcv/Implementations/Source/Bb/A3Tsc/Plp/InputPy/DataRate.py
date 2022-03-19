from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataRate:
	"""DataRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dataRate", core, parent)

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:[INPut]:DATarate \n
		Snippet: value: float = driver.source.bb.a3Tsc.plp.inputPy.dataRate.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'LAN' connector (TSoverIP)
			- External IP stream input at 'LAN' connector \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: measured_dr: float Range: 0 to 999999999"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:INPut:DATarate?')
		return Conversions.str_to_float(response)
