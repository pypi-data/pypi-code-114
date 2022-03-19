from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.Cdma2KtxDivMode, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:TDIVersity:MODE \n
		Snippet: driver.source.bb.c2K.bstation.tdiversity.mode.set(mode = enums.Cdma2KtxDivMode.OTD, baseStation = repcap.BaseStation.Default) \n
		The command selects the diversity scheme. Command [:SOURce<hw>]:BB:C2K:BSTation<st>:TDIVersity activates transmit
		diversity and selects the antenna. \n
			:param mode: OTD| STS OTD Orthogonal Transmit Diversity Mode. STS Space Time Spreading Mode.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KtxDivMode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:TDIVersity:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.Cdma2KtxDivMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:TDIVersity:MODE \n
		Snippet: value: enums.Cdma2KtxDivMode = driver.source.bb.c2K.bstation.tdiversity.mode.get(baseStation = repcap.BaseStation.Default) \n
		The command selects the diversity scheme. Command [:SOURce<hw>]:BB:C2K:BSTation<st>:TDIVersity activates transmit
		diversity and selects the antenna. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: mode: OTD| STS OTD Orthogonal Transmit Diversity Mode. STS Space Time Spreading Mode."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:TDIVersity:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KtxDivMode)
