from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sscg:
	"""Sscg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sscg", core, parent)

	def get(self, baseStation=repcap.BaseStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:SSCG \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.sscg.get(baseStation = repcap.BaseStation.Default) \n
		The command queries the secondary synchronization code group. This parameter is specified in the table defined by the
		3GPP standard 'Allocation of SSCs for secondary SCH'. This table assigns a specific spreading code to the synchronization
		code symbol for every slot in the frame. The value is calculated from the scrambling code. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: sscg: integer Range: 0 to 63"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:SSCG?')
		return Conversions.str_to_int(response)
