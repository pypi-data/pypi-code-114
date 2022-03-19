from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bsr:
	"""Bsr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsr", core, parent)

	def get_coefficient(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:BSR:COEFficient \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.bootstrap.bsr.get_coefficient() \n
		Queries the sample rate used for the post-bootstrap portion of the current physical layer frame. \n
			:return: bsr_coefficient: integer Range: 0 to 127
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:BSR:COEFficient?')
		return Conversions.str_to_int(response)
