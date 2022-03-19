from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, pr_errors_value: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:PRERrors:VALue \n
		Snippet: driver.source.bb.gnss.svid.navic.prErrors.value.set(pr_errors_value = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the constant pseudorange error. \n
			:param pr_errors_value: float Range: -1000 to 1000
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(pr_errors_value)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:PRERrors:VALue {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:PRERrors:VALue \n
		Snippet: value: float = driver.source.bb.gnss.svid.navic.prErrors.value.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the constant pseudorange error. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: pr_errors_value: float Range: -1000 to 1000"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:PRERrors:VALue?')
		return Conversions.str_to_float(response)
