from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spare:
	"""Spare commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spare", core, parent)

	def set(self, spare_data: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:EPHemeris:SAR:SPARe \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.inav.ephemeris.sar.spare.set(spare_data = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the 21-bit Search-and-Rescue Service (SAR) spare data. For more information, refer to specification . \n
			:param spare_data: integer Range: 0 to 2097151
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(spare_data)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:EPHemeris:SAR:SPARe {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:EPHemeris:SAR:SPARe \n
		Snippet: value: int = driver.source.bb.gnss.svid.galileo.nmessage.inav.ephemeris.sar.spare.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the 21-bit Search-and-Rescue Service (SAR) spare data. For more information, refer to specification . \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: spare_data: integer Range: 0 to 2097151"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:EPHemeris:SAR:SPARe?')
		return Conversions.str_to_int(response)
