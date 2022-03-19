from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rblock:
	"""Rblock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rblock", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.Ts25141Bler:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:RBLock:RATE \n
		Snippet: value: enums.Ts25141Bler = driver.source.bb.w3Gpp.ts25141.awgn.rblock.get_rate() \n
		Sets the required block error rate. The possible selection depends on the selected fading configuration. \n
			:return: rate: B0| B01| B001| B0001
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:RBLock:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141Bler)

	def set_rate(self, rate: enums.Ts25141Bler) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:RBLock:RATE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.rblock.set_rate(rate = enums.Ts25141Bler.B0) \n
		Sets the required block error rate. The possible selection depends on the selected fading configuration. \n
			:param rate: B0| B01| B001| B0001
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.Ts25141Bler)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:RBLock:RATE {param}')
