from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmType:
	"""CmType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmType", core, parent)

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2InputSignalCm:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:CMTYpe \n
		Snippet: value: enums.Dvbt2InputSignalCm = driver.source.bb.t2Dvb.plp.cmType.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the type for multi-PLP. Multi-PLP requires number of PLPs > 1, see [:SOURce<hw>]:BB:T2DVb:INPut:NPLP?. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: cm_type: CCM| ACM CCM Constant coding and modulation. The setting implies identical settings for all s of the commands: [:SOURcehw]:BB:T2DVb:PLPch:FECFrame [:SOURcehw]:BB:T2DVb:PLPch:RATE [:SOURcehw]:BB:T2DVb:PLPch:CONStel [:SOURcehw]:BB:T2DVb:PLPch:CROTation ACM Variable coding and modulation. Not all PLPs use the same coding and modulation."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:CMTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2InputSignalCm)
