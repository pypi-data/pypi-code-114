from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:MCONtrol:COPY:EXECute \n
		Snippet: driver.source.bb.gnss.svid.gps.mcontrol.copy.execute.set(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Applies the configuration of the current satellite (SVID<ch>:<GNSS system>) to the satellite defined with the command
		[:SOURce<hw>]:BB:GNSS:SVID<ch>:GPS:MCONtrol:COPY:SVID. Both SV IDs belong to the same GNSS system. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:MCONtrol:COPY:EXECute')

	def set_with_opc(self, satelliteSvid=repcap.SatelliteSvid.Default, opc_timeout_ms: int = -1) -> None:
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:MCONtrol:COPY:EXECute \n
		Snippet: driver.source.bb.gnss.svid.gps.mcontrol.copy.execute.set_with_opc(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Applies the configuration of the current satellite (SVID<ch>:<GNSS system>) to the satellite defined with the command
		[:SOURce<hw>]:BB:GNSS:SVID<ch>:GPS:MCONtrol:COPY:SVID. Both SV IDs belong to the same GNSS system. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:MCONtrol:COPY:EXECute', opc_timeout_ms)
