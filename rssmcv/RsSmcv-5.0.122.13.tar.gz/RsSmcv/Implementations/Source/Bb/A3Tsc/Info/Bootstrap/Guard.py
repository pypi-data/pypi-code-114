from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Guard:
	"""Guard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("guard", core, parent)

	# noinspection PyTypeChecker
	def get_interval(self) -> enums.Atsc30GuardInterval:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:GUARd:INTerval \n
		Snippet: value: enums.Atsc30GuardInterval = driver.source.bb.a3Tsc.info.bootstrap.guard.get_interval() \n
		Queries the number of guard interval samples of the preamble symbols. \n
			:return: guard_interval: G192| G384| G512| G768| G1024| G1536| G2048| G2432| G3072| G3648| G4096| G4864
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:GUARd:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30GuardInterval)
