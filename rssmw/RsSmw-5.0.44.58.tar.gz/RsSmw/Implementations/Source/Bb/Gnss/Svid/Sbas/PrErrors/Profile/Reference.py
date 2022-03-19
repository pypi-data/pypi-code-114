from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, profile_ref_time: float, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:PRERrors:PROFile<GR>:REFerence \n
		Snippet: driver.source.bb.gnss.svid.sbas.prErrors.profile.reference.set(profile_ref_time = 1.0, satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets the reference time for the pseudorange error. \n
			:param profile_ref_time: float Range: 0 to 86400
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Profile')
		"""
		param = Conversions.decimal_value_to_str(profile_ref_time)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:PRERrors:PROFile{index_cmd_val}:REFerence {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:PRERrors:PROFile<GR>:REFerence \n
		Snippet: value: float = driver.source.bb.gnss.svid.sbas.prErrors.profile.reference.get(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets the reference time for the pseudorange error. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Profile')
			:return: profile_ref_time: float Range: 0 to 86400"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:PRERrors:PROFile{index_cmd_val}:REFerence?')
		return Conversions.str_to_float(response)
