from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnPattern:
	"""AnPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPattern, default value after init: AntennaPattern.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anPattern", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPattern_get', 'repcap_antennaPattern_set', repcap.AntennaPattern.Nr0)

	def repcap_antennaPattern_set(self, antennaPattern: repcap.AntennaPattern) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPattern.Default
		Default value after init: AntennaPattern.Nr0"""
		self._cmd_group.set_repcap_enum_value(antennaPattern)

	def repcap_antennaPattern_get(self) -> repcap.AntennaPattern:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, an_pattern: str, subframeNull=repcap.SubframeNull.Default, antennaPattern=repcap.AntennaPattern.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:ANPattern<GR0> \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.phich.anPattern.set(an_pattern = '1', subframeNull = repcap.SubframeNull.Default, antennaPattern = repcap.AntennaPattern.Default) \n
		No command help available \n
			:param an_pattern: No help available
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param antennaPattern: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AnPattern')
		"""
		param = Conversions.value_to_quoted_str(an_pattern)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		antennaPattern_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPattern, repcap.AntennaPattern)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:ANPattern{antennaPattern_cmd_val} {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, antennaPattern=repcap.AntennaPattern.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:ANPattern<GR0> \n
		Snippet: value: str = driver.source.bb.eutra.downlink.subf.encc.phich.anPattern.get(subframeNull = repcap.SubframeNull.Default, antennaPattern = repcap.AntennaPattern.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param antennaPattern: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AnPattern')
			:return: an_pattern: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		antennaPattern_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPattern, repcap.AntennaPattern)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:ANPattern{antennaPattern_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'AnPattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AnPattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
