from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaPeriod:
	"""CaPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caPeriod", core, parent)

	def set(self, const_acc_period: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SDYNamics:CAPeriod \n
		Snippet: driver.source.bb.gnss.svid.qzss.sdynamics.caPeriod.set(const_acc_period = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the time duration during that acceleration is applied and thus the velocity varies. \n
			:param const_acc_period: float Range: 0.1 to 10800
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(const_acc_period)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SDYNamics:CAPeriod {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SDYNamics:CAPeriod \n
		Snippet: value: float = driver.source.bb.gnss.svid.qzss.sdynamics.caPeriod.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the time duration during that acceleration is applied and thus the velocity varies. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: const_acc_period: float Range: 0.1 to 10800"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SDYNamics:CAPeriod?')
		return Conversions.str_to_float(response)
