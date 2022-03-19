from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	def set(self, sbas_system: enums.SbasSystem, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SYSTem \n
		Snippet: driver.source.bb.gnss.svid.sbas.system.set(sbas_system = enums.SbasSystem.EGNOS, satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param sbas_system: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(sbas_system, enums.SbasSystem)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SYSTem {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.SbasSystem:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SYSTem \n
		Snippet: value: enums.SbasSystem = driver.source.bb.gnss.svid.sbas.system.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: sbas_system: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SYSTem?')
		return Conversions.str_to_scalar_enum(response, enums.SbasSystem)
