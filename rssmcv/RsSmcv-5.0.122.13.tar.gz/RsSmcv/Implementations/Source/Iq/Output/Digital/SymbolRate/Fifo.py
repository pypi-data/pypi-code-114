from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fifo:
	"""Fifo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fifo", core, parent)

	# noinspection PyTypeChecker
	def get_status(self) -> enums.SampRateFifoStatus:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:SRATe:FIFO:[STATus] \n
		Snippet: value: enums.SampRateFifoStatus = driver.source.iq.output.digital.symbolRate.fifo.get_status() \n
		No command help available \n
			:return: status: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:SRATe:FIFO:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.SampRateFifoStatus)
