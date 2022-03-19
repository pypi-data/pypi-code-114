from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Real:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, basebandNull=repcap.BasebandNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:AP<DIR0>:BB<ST0>:REAL \n
		Snippet: value: float = driver.source.bb.eutra.downlink.emtc.alloc.precoding.ap.bb.real.get(allocationNull = repcap.AllocationNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, basebandNull = repcap.BasebandNull.Default) \n
		Defines the mapping of the antenna ports to the physical antennas. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param basebandNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bb')
			:return: data_real: float The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 1"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		basebandNull_cmd_val = self._cmd_group.get_repcap_cmd_value(basebandNull, repcap.BasebandNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:AP{antennaPortNull_cmd_val}:BB{basebandNull_cmd_val}:REAL?')
		return Conversions.str_to_float(response)
