from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: enums.PageInd, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:PINDicator:COUNt \n
		Snippet: driver.source.bb.w3Gpp.bstation.pindicator.count.set(count = enums.PageInd.D144, baseStation = repcap.BaseStation.Default) \n
		The command sets the number of page indicators (PI) per frame in the page indicator channel (PICH) . \n
			:param count: D18| D36| D72| D144
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(count, enums.PageInd)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:PINDicator:COUNt {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.PageInd:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:PINDicator:COUNt \n
		Snippet: value: enums.PageInd = driver.source.bb.w3Gpp.bstation.pindicator.count.get(baseStation = repcap.BaseStation.Default) \n
		The command sets the number of page indicators (PI) per frame in the page indicator channel (PICH) . \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: count: D18| D36| D72| D144"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:PINDicator:COUNt?')
		return Conversions.str_to_scalar_enum(response, enums.PageInd)
