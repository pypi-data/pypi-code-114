from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_noise(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:POWer:NOISe \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.awgn.power.get_noise() \n
		Sets/queries the noise level. \n
			:return: noise: float
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:POWer:NOISe?')
		return Conversions.str_to_float(response)

	def set_noise(self, noise: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:POWer:NOISe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.power.set_noise(noise = 1.0) \n
		Sets/queries the noise level. \n
			:param noise: float
		"""
		param = Conversions.decimal_value_to_str(noise)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:POWer:NOISe {param}')
