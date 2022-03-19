from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cphase:
	"""Cphase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cphase", core, parent)

	def set(self, cphase: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SDYNamics:CPHase \n
		Snippet: driver.source.bb.gnss.svid.glonass.sdynamics.cphase.set(cphase = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the initial carrier phase. \n
			:param cphase: float Range: 0 to 6.28
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(cphase)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SDYNamics:CPHase {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SDYNamics:CPHase \n
		Snippet: value: float = driver.source.bb.gnss.svid.glonass.sdynamics.cphase.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the initial carrier phase. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: cphase: float Range: 0 to 6.28"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SDYNamics:CPHase?')
		return Conversions.str_to_float(response)
