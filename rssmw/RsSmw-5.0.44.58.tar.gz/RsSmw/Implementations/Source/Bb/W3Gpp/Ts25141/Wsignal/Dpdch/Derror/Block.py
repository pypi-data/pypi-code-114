from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Block:
	"""Block commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("block", core, parent)

	def get_rate(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:DERRor:BLOCk:RATE \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.derror.block.get_rate() \n
		Sets the block error rate. \n
			:return: rate: float Range: 0 to 0.1
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:DERRor:BLOCk:RATE?')
		return Conversions.str_to_float(response)

	def set_rate(self, rate: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:DERRor:BLOCk:RATE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.derror.block.set_rate(rate = 1.0) \n
		Sets the block error rate. \n
			:param rate: float Range: 0 to 0.1
		"""
		param = Conversions.decimal_value_to_str(rate)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:DERRor:BLOCk:RATE {param}')
