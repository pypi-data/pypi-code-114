from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdiversity:
	"""Tdiversity commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdiversity", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, tdiversity: enums.Cdma2KtxDiv, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:TDIVersity \n
		Snippet: driver.source.bb.c2K.bstation.tdiversity.set(tdiversity = enums.Cdma2KtxDiv.ANT1, baseStation = repcap.BaseStation.Default) \n
		The command activates and deactivates signal calculation with transmit diversity (OFF) . To activate transmit diversity,
		the antenna must be specified whose signals are to be simulated (ANT1 or ANT2) . The diversity scheme is selected using
		command [:SOURce<hw>]:BB:C2K:BSTation<st>:TDIVersity:MODE. \n
			:param tdiversity: OFF| ANT1| ANT2 OFF No transmit diversity. ANT1 Calculate and apply the output signal for antenna 1. ANT2 Calculate and apply the output signal for antenna 2.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(tdiversity, enums.Cdma2KtxDiv)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:TDIVersity {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.Cdma2KtxDiv:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:TDIVersity \n
		Snippet: value: enums.Cdma2KtxDiv = driver.source.bb.c2K.bstation.tdiversity.get(baseStation = repcap.BaseStation.Default) \n
		The command activates and deactivates signal calculation with transmit diversity (OFF) . To activate transmit diversity,
		the antenna must be specified whose signals are to be simulated (ANT1 or ANT2) . The diversity scheme is selected using
		command [:SOURce<hw>]:BB:C2K:BSTation<st>:TDIVersity:MODE. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: tdiversity: OFF| ANT1| ANT2 OFF No transmit diversity. ANT1 Calculate and apply the output signal for antenna 1. ANT2 Calculate and apply the output signal for antenna 2."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:TDIVersity?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KtxDiv)

	def clone(self) -> 'Tdiversity':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdiversity(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
