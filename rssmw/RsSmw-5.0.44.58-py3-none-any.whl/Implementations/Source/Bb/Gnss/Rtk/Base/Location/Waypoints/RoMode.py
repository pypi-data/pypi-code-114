from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RoMode:
	"""RoMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roMode", core, parent)

	def set(self, ro_mode: enums.ReadOutMode, baseSt=repcap.BaseSt.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:WAYPoints:ROMode \n
		Snippet: driver.source.bb.gnss.rtk.base.location.waypoints.roMode.set(ro_mode = enums.ReadOutMode.CYCLic, baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param ro_mode: No help available
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
		"""
		param = Conversions.enum_scalar_to_str(ro_mode, enums.ReadOutMode)
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:WAYPoints:ROMode {param}')

	# noinspection PyTypeChecker
	def get(self, baseSt=repcap.BaseSt.Default) -> enums.ReadOutMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:WAYPoints:ROMode \n
		Snippet: value: enums.ReadOutMode = driver.source.bb.gnss.rtk.base.location.waypoints.roMode.get(baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:return: ro_mode: No help available"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:WAYPoints:ROMode?')
		return Conversions.str_to_scalar_enum(response, enums.ReadOutMode)
