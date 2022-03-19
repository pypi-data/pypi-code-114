from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tgl:
	"""Tgl commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: TransmGapLength, default value after init: TransmGapLength.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tgl", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_transmGapLength_get', 'repcap_transmGapLength_set', repcap.TransmGapLength.Nr1)

	def repcap_transmGapLength_set(self, transmGapLength: repcap.TransmGapLength) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TransmGapLength.Default
		Default value after init: TransmGapLength.Nr1"""
		self._cmd_group.set_repcap_enum_value(transmGapLength)

	def repcap_transmGapLength_get(self) -> repcap.TransmGapLength:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, tgl: int, baseStation=repcap.BaseStation.Default, patternIx=repcap.PatternIx.Default, transmGapLength=repcap.TransmGapLength.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:PATTern<CH>:TGL<DI> \n
		Snippet: driver.source.bb.w3Gpp.bstation.cmode.pattern.tgl.set(tgl = 1, baseStation = repcap.BaseStation.Default, patternIx = repcap.PatternIx.Default, transmGapLength = repcap.TransmGapLength.Default) \n
		Sets the transmission gap lengths. \n
			:param tgl: integer Range: 3 to 14
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:param transmGapLength: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tgl')
		"""
		param = Conversions.decimal_value_to_str(tgl)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		transmGapLength_cmd_val = self._cmd_group.get_repcap_cmd_value(transmGapLength, repcap.TransmGapLength)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGL{transmGapLength_cmd_val} {param}')

	def get(self, baseStation=repcap.BaseStation.Default, patternIx=repcap.PatternIx.Default, transmGapLength=repcap.TransmGapLength.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:PATTern<CH>:TGL<DI> \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.cmode.pattern.tgl.get(baseStation = repcap.BaseStation.Default, patternIx = repcap.PatternIx.Default, transmGapLength = repcap.TransmGapLength.Default) \n
		Sets the transmission gap lengths. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param patternIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:param transmGapLength: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tgl')
			:return: tgl: integer Range: 3 to 14"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		patternIx_cmd_val = self._cmd_group.get_repcap_cmd_value(patternIx, repcap.PatternIx)
		transmGapLength_cmd_val = self._cmd_group.get_repcap_cmd_value(transmGapLength, repcap.TransmGapLength)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:PATTern{patternIx_cmd_val}:TGL{transmGapLength_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Tgl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tgl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
