from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plevel:
	"""Plevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plevel", core, parent)

	def get(self, userEquipment=repcap.UserEquipment.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:INTRacell:UE<CH>:PLEVel \n
		Snippet: value: str = driver.source.bb.eutra.tcw.ws.intracell.ue.plevel.get(userEquipment = repcap.UserEquipment.Default) \n
		Queries the intra cell power level used for UE wanted signal. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: intra_cell_pow_lev: string"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:INTRacell:UE{userEquipment_cmd_val}:PLEVel?')
		return trim_str_response(response)
