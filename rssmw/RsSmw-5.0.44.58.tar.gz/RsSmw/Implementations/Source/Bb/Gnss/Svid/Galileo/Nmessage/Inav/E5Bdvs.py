from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class E5Bdvs:
	"""E5Bdvs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("e5Bdvs", core, parent)

	def set(self, dvs_e_5_b: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:E5BDVS \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.inav.e5Bdvs.set(dvs_e_5_b = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the data validity status - E5bDVS parameter. \n
			:param dvs_e_5_b: integer Range: -1 to 1
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(dvs_e_5_b)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:E5BDVS {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:E5BDVS \n
		Snippet: value: int = driver.source.bb.gnss.svid.galileo.nmessage.inav.e5Bdvs.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the data validity status - E5bDVS parameter. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: dvs_e_5_b: integer Range: -1 to 1"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:E5BDVS?')
		return Conversions.str_to_int(response)
