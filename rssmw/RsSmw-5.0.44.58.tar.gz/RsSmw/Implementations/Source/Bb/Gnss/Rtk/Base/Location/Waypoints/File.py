from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, waypoints: str, baseSt=repcap.BaseSt.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:WAYPoints:FILE \n
		Snippet: driver.source.bb.gnss.rtk.base.location.waypoints.file.set(waypoints = '1', baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param waypoints: No help available
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
		"""
		param = Conversions.value_to_quoted_str(waypoints)
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:WAYPoints:FILE {param}')

	def get(self, baseSt=repcap.BaseSt.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:WAYPoints:FILE \n
		Snippet: value: str = driver.source.bb.gnss.rtk.base.location.waypoints.file.get(baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:return: waypoints: No help available"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:WAYPoints:FILE?')
		return trim_str_response(response)
