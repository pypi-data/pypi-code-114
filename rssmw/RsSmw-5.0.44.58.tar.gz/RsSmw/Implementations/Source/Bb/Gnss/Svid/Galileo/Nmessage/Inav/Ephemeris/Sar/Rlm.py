from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlm:
	"""Rlm commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlm", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, sar_rlm_data: int, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:EPHemeris:SAR:RLM<S2US> \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.inav.ephemeris.sar.rlm.set(sar_rlm_data = 1, satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets the 20-bit Search-and-Rescue Service (SAR) return link message (RLM) data for nominal mode operation.
		For more information, refer to specification . \n
			:param sar_rlm_data: integer Range: 0 to 1048575
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rlm')
		"""
		param = Conversions.decimal_value_to_str(sar_rlm_data)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:EPHemeris:SAR:RLM{index_cmd_val} {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:INAV:EPHemeris:SAR:RLM<S2US> \n
		Snippet: value: int = driver.source.bb.gnss.svid.galileo.nmessage.inav.ephemeris.sar.rlm.get(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		Sets the 20-bit Search-and-Rescue Service (SAR) return link message (RLM) data for nominal mode operation.
		For more information, refer to specification . \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rlm')
			:return: sar_rlm_data: integer Range: 0 to 1048575"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:INAV:EPHemeris:SAR:RLM{index_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Rlm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rlm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
