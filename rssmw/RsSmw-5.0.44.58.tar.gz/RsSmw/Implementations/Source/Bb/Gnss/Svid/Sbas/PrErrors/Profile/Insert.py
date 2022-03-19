from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:PRERrors:PROFile<GR>:INSert \n
		Snippet: driver.source.bb.gnss.svid.sbas.prErrors.profile.insert.set(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Inserts a row before the selected pseudorange error. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Profile')
		"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:PRERrors:PROFile{index_cmd_val}:INSert')

	def set_with_opc(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default, opc_timeout_ms: int = -1) -> None:
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:PRERrors:PROFile<GR>:INSert \n
		Snippet: driver.source.bb.gnss.svid.sbas.prErrors.profile.insert.set_with_opc(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Inserts a row before the selected pseudorange error. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Profile')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:PRERrors:PROFile{index_cmd_val}:INSert', opc_timeout_ms)
