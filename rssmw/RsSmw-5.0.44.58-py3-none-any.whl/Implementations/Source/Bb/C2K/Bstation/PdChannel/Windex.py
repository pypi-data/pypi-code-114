from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Windex:
	"""Windex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("windex", core, parent)

	def set(self, windex: enums.NumbersG, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:WINDex \n
		Snippet: driver.source.bb.c2K.bstation.pdChannel.windex.set(windex = enums.NumbersG._0, baseStation = repcap.BaseStation.Default) \n
		The command selects a standard Walsh set for F-PDCH. Four different sets are defined in the standard. \n
			:param windex: 0| 1| 2| 3
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(windex, enums.NumbersG)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:WINDex {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.NumbersG:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:WINDex \n
		Snippet: value: enums.NumbersG = driver.source.bb.c2K.bstation.pdChannel.windex.get(baseStation = repcap.BaseStation.Default) \n
		The command selects a standard Walsh set for F-PDCH. Four different sets are defined in the standard. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: windex: 0| 1| 2| 3"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:WINDex?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersG)
