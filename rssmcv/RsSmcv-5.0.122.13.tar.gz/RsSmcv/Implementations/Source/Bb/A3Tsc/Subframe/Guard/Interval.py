from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interval:
	"""Interval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interval", core, parent)

	def set(self, guard_interval: enums.Atsc30GuardInterval, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:GUARd:INTerval \n
		Snippet: driver.source.bb.a3Tsc.subframe.guard.interval.set(guard_interval = enums.Atsc30GuardInterval.G1024, subframe = repcap.Subframe.Default) \n
		Sets the guard interval length. \n
			:param guard_interval: G192| G384| G512| G768| G1024| G1536| G2048| G2432| G3072| G3648| G4096| G4864
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(guard_interval, enums.Atsc30GuardInterval)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:GUARd:INTerval {param}')

	# noinspection PyTypeChecker
	def get(self, subframe=repcap.Subframe.Default) -> enums.Atsc30GuardInterval:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:GUARd:INTerval \n
		Snippet: value: enums.Atsc30GuardInterval = driver.source.bb.a3Tsc.subframe.guard.interval.get(subframe = repcap.Subframe.Default) \n
		Sets the guard interval length. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: guard_interval: G192| G384| G512| G768| G1024| G1536| G2048| G2432| G3072| G3648| G4096| G4864"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:GUARd:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30GuardInterval)
