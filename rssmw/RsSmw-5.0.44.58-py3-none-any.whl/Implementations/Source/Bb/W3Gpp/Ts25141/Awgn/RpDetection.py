from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpDetection:
	"""RpDetection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpDetection", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.Ts25141ReqPd:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:RPDetection:RATE \n
		Snippet: value: enums.Ts25141ReqPd = driver.source.bb.w3Gpp.ts25141.awgn.rpDetection.get_rate() \n
		Sets the required probability of detection of preamble (Pd) . The selection determines the ratio Eb/N0. \n
			:return: rate: PD099| PD0999
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:RPDetection:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141ReqPd)

	def set_rate(self, rate: enums.Ts25141ReqPd) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:RPDetection:RATE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.rpDetection.set_rate(rate = enums.Ts25141ReqPd.PD099) \n
		Sets the required probability of detection of preamble (Pd) . The selection determines the ratio Eb/N0. \n
			:param rate: PD099| PD0999
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.Ts25141ReqPd)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:RPDetection:RATE {param}')
