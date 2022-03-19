from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apm:
	"""Apm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apm", core, parent)

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.BfapMapMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:APM \n
		Snippet: value: enums.BfapMapMode = driver.source.bb.eutra.downlink.emtc.alloc.precoding.apm.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the antenna port mapping method. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: ant_port_map: CB| RCB| FW CB = codebook RCB = random codebook FW = fixed weights"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:APM?')
		return Conversions.str_to_scalar_enum(response, enums.BfapMapMode)
