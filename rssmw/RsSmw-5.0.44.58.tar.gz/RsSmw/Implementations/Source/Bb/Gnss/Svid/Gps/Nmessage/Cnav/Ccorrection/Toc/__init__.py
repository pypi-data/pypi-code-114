from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Toc:
	"""Toc commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("toc", core, parent)

	@property
	def unscaled(self):
		"""unscaled commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unscaled'):
			from .Unscaled import Unscaled
			self._unscaled = Unscaled(self._core, self._cmd_group)
		return self._unscaled

	def set(self, toc: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:CCORrection:TOC \n
		Snippet: driver.source.bb.gnss.svid.gps.nmessage.cnav.ccorrection.toc.set(toc = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time of clock. \n
			:param toc: integer
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.decimal_value_to_str(toc)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:CCORrection:TOC {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:NMESsage:CNAV:CCORrection:TOC \n
		Snippet: value: int = driver.source.bb.gnss.svid.gps.nmessage.cnav.ccorrection.toc.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time of clock. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: toc: integer"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:NMESsage:CNAV:CCORrection:TOC?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Toc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Toc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
