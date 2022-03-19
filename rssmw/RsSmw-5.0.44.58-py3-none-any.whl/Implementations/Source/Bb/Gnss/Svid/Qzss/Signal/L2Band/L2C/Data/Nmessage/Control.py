from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	def set(self, nav_msg_control: enums.NavMsgCtrl, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L2Band:L2C:DATA:NMESsage:CONTrol \n
		Snippet: driver.source.bb.gnss.svid.qzss.signal.l2Band.l2C.data.nmessage.control.set(nav_msg_control = enums.NavMsgCtrl.AUTO, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Defines whether the navigation message parameters can be changed or not. \n
			:param nav_msg_control: OFF| EDIT| AUTO | OFF| EDIT| AUTO OFF Disables sending the navigation message. EDIT Enables configuration of the navigation message. AUTO Navigation message is generated automatically.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(nav_msg_control, enums.NavMsgCtrl)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L2Band:L2C:DATA:NMESsage:CONTrol {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.NavMsgCtrl:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L2Band:L2C:DATA:NMESsage:CONTrol \n
		Snippet: value: enums.NavMsgCtrl = driver.source.bb.gnss.svid.qzss.signal.l2Band.l2C.data.nmessage.control.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Defines whether the navigation message parameters can be changed or not. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: nav_msg_control: OFF| EDIT| AUTO | OFF| EDIT| AUTO OFF Disables sending the navigation message. EDIT Enables configuration of the navigation message. AUTO Navigation message is generated automatically."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L2Band:L2C:DATA:NMESsage:CONTrol?')
		return Conversions.str_to_scalar_enum(response, enums.NavMsgCtrl)
