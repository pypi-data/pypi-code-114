from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValSubFrames:
	"""ValSubFrames commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: SubframeNull, default value after init: SubframeNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("valSubFrames", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subframeNull_get', 'repcap_subframeNull_set', repcap.SubframeNull.Nr0)

	def repcap_subframeNull_set(self, subframeNull: repcap.SubframeNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubframeNull.Default
		Default value after init: SubframeNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(subframeNull)

	def repcap_subframeNull_get(self) -> repcap.SubframeNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, nprs_bmp_valid_sf: bool, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:BMP:VALSubframes<CH> \n
		Snippet: driver.source.bb.eutra.downlink.niot.nprs.bmp.valSubFrames.set(nprs_bmp_valid_sf = False, subframeNull = repcap.SubframeNull.Default) \n
		Sets a subframe as valid and used for NPRS transmission. \n
			:param nprs_bmp_valid_sf: 1| ON| 0| OFF
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'ValSubFrames')
		"""
		param = Conversions.bool_to_str(nprs_bmp_valid_sf)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:BMP:VALSubframes{subframeNull_cmd_val} {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:BMP:VALSubframes<CH> \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.nprs.bmp.valSubFrames.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets a subframe as valid and used for NPRS transmission. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'ValSubFrames')
			:return: nprs_bmp_valid_sf: 1| ON| 0| OFF"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:BMP:VALSubframes{subframeNull_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'ValSubFrames':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ValSubFrames(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
