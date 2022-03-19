from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Return:
	"""Return commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("return", core, parent)

	# noinspection PyTypeChecker
	def get_channel(self) -> enums.Atsc30LowLevelSignaling:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:RETurn:[CHANnel] \n
		Snippet: value: enums.Atsc30LowLevelSignaling = driver.source.bb.a3Tsc.return.get_channel() \n
		Queries, if a dedicated return channel (DRC) is present or absent. \n
			:return: return_channel: ABSent| PRESent
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:RETurn:CHANnel?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30LowLevelSignaling)
