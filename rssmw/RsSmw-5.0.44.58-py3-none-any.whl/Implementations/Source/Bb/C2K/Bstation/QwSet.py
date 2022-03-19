from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QwSet:
	"""QwSet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qwSet", core, parent)

	def set(self, qw_set: int, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:QWSet \n
		Snippet: driver.source.bb.c2K.bstation.qwSet.set(qw_set = 1, baseStation = repcap.BaseStation.Default) \n
		The command selects the quasi orthogonal Walsh code set. The standard defines three different sets. The quasi-orthogonal
		Walsh codes are used for a given channel if [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:QWCode:STATe is ON. \n
			:param qw_set: integer Range: 1 to 3
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.decimal_value_to_str(qw_set)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:QWSet {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:QWSet \n
		Snippet: value: int = driver.source.bb.c2K.bstation.qwSet.get(baseStation = repcap.BaseStation.Default) \n
		The command selects the quasi orthogonal Walsh code set. The standard defines three different sets. The quasi-orthogonal
		Walsh codes are used for a given channel if [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:QWCode:STATe is ON. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: qw_set: integer Range: 1 to 3"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:QWSet?')
		return Conversions.str_to_int(response)
