from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Basic:
	"""Basic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("basic", core, parent)

	# noinspection PyTypeChecker
	def get_fec_type(self) -> enums.Atsc30TimeInfoL1BasicFecType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:BASic:FECType \n
		Snippet: value: enums.Atsc30TimeInfoL1BasicFecType = driver.source.bb.a3Tsc.info.bootstrap.basic.get_fec_type() \n
		Queries the FEC type used for the L1 basic signaling in the preamble symbol. \n
			:return: l_1_basic_fec_type: MOD1| MOD2| MOD3| MOD4| MOD5| MOD6| MOD7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:BASic:FECType?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TimeInfoL1BasicFecType)
