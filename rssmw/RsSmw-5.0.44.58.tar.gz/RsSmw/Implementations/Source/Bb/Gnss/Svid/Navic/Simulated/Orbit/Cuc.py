from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cuc:
	"""Cuc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cuc", core, parent)

	def set(self, cuc: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:ORBit:CUC \n
		Snippet: driver.source.bb.gnss.svid.navic.simulated.orbit.cuc.set(cuc = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the cosine difference of latitude. \n
			:param cuc: float
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(cuc)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:ORBit:CUC {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:SIMulated:ORBit:CUC \n
		Snippet: value: float = driver.source.bb.gnss.svid.navic.simulated.orbit.cuc.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the cosine difference of latitude. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: cuc: float"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:SIMulated:ORBit:CUC?')
		return Conversions.str_to_float(response)
