from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:TRIGger:[EXTernal]:DELay \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.wsignal.trigger.external.get_delay() \n
		Sets an additional propagation delay besides the fixed DL-UL timing offset of 1024 chip periods.
		The additional propagation delay is obtained by charging the start trigger impulse with the respective delay. \n
			:return: delay: float Range: 0 chips to 65535 chips
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:TRIGger:EXTernal:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:TRIGger:[EXTernal]:DELay \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.trigger.external.set_delay(delay = 1.0) \n
		Sets an additional propagation delay besides the fixed DL-UL timing offset of 1024 chip periods.
		The additional propagation delay is obtained by charging the start trigger impulse with the respective delay. \n
			:param delay: float Range: 0 chips to 65535 chips
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:TRIGger:EXTernal:DELay {param}')
