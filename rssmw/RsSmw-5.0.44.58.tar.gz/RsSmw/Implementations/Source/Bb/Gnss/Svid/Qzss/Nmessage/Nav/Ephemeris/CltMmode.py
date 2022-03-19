from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CltMmode:
	"""CltMmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cltMmode", core, parent)

	def set(self, code_on_l_2_mode: enums.CodeOnL2, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:NAV:EPHemeris:CLTMode \n
		Snippet: driver.source.bb.gnss.svid.qzss.nmessage.nav.ephemeris.cltMmode.set(code_on_l_2_mode = enums.CodeOnL2.CACode, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the code on L2. \n
			:param code_on_l_2_mode: REServed| PCODe| CACode
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(code_on_l_2_mode, enums.CodeOnL2)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:NAV:EPHemeris:CLTMode {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.CodeOnL2:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:NMESsage:NAV:EPHemeris:CLTMode \n
		Snippet: value: enums.CodeOnL2 = driver.source.bb.gnss.svid.qzss.nmessage.nav.ephemeris.cltMmode.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the code on L2. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: code_on_l_2_mode: REServed| PCODe| CACode"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:NMESsage:NAV:EPHemeris:CLTMode?')
		return Conversions.str_to_scalar_enum(response, enums.CodeOnL2)
