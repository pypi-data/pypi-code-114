from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	def set(self, path_loss_state: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:POWer:PLOSs \n
		Snippet: driver.source.bb.gnss.svid.navic.power.ploss.set(path_loss_state = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		If enabled, the power of the SV ID signals is reduced to account for the free space attenuation. \n
			:param path_loss_state: 1| ON| 0| OFF
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.bool_to_str(path_loss_state)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:POWer:PLOSs {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:POWer:PLOSs \n
		Snippet: value: bool = driver.source.bb.gnss.svid.navic.power.ploss.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		If enabled, the power of the SV ID signals is reduced to account for the free space attenuation. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: path_loss_state: 1| ON| 0| OFF"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:POWer:PLOSs?')
		return Conversions.str_to_bool(response)
