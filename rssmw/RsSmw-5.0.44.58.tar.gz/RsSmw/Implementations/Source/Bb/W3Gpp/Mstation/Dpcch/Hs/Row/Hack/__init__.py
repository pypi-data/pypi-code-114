from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hack:
	"""Hack commands group definition. 3 total commands, 2 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hack", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def fromPy(self):
		"""fromPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fromPy'):
			from .FromPy import FromPy
			self._fromPy = FromPy(self._core, self._cmd_group)
		return self._fromPy

	@property
	def to(self):
		"""to commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_to'):
			from .To import To
			self._to = To(self._core, self._cmd_group)
		return self._to

	def set(self, harq_ack: enums.HsRel8HarqMode, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:HACK<DI> \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.row.hack.set(harq_ack = enums.HsRel8HarqMode.A, mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, indexNull = repcap.IndexNull.Default) \n
		(Release 8 and Later) Sets the information transmitted during the HARQ-ACK slots of the TTIs during the corresponding
		specified HARQ-ACK From/To range. For detailed description, see 'HS-DPCCH 1/2, HARQ-ACK 1/2/3/4'.
		The Table 'Cross-reference between the used GUI terms and abbreviations in the SCPI command' provides the necessary
		cross-reference information. Cross-reference between the used GUI terms and abbreviations in the SCPI command
			Table Header: Value name / Parameter value \n
			- 'DTX' / DTX | D_DTX
			- 'PRE, POST' / PRE | POST
			- 'A, N' / A | N
			- 'AA, AN, NA, NN' / M_A | M_N | M_AA | M_AN | M_NA | M_NN
			- 'A/D, N/A, …' (different combinations possible) / S_A_D | S_N_A | ... (different combinations possible)
			- 'A/D/D, N/D/D, …' (different combinations possible) / S2_N_N_N | S2_N_N_A | ... (different combinations possible)
			- 'AN/NN, D/AA, …' (different combinations possible) / MS_AA_AA | MS_D_AA ... (different combinations possible) \n
			:param harq_ack: DTX| PRE| POST| A| N| M_A| M_N| M_AA| M_AN| M_NA| M_NN| S_A_D| S_N_D| S_D_A| S_D_N| S_A_A| S_A_N| S_N_A| S_N_N| MS_A_D| MS_N_D| MS_AA_D| MS_AN_D| MS_NA_D| MS_NN_D| MS_D_A| MS_D_N| MS_D_AA| MS_D_AN| MS_D_NA| MS_D_NN| MS_A_A| MS_A_N| MS_N_A| MS_N_N| MS_A_AA| MS_A_AN| MS_A_NA| MS_A_NN| MS_N_AA| MS_N_AN| MS_N_NA| MS_N_NN| MS_AA_A| MS_AA_N| MS_AN_A| MS_AN_N| MS_NA_A| MS_NA_N| MS_NN_A| MS_NN_N| MS_AA_AA| MS_AA_AN| MS_AA_NA| MS_AA_NN| MS_AN_AA| MS_AN_AN| MS_AN_NA| MS_AN_NN| MS_NA_AA| MS_NA_AN| MS_NA_NA| MS_NA_NN| MS_NN_AA| MS_NN_AN| MS_NN_NA| MS_NN_NN| S2_A_D_D| S2_N_D_D| S2_D_A_D| S2_D_N_D| S2_D_D_A| S2_D_D_N| S2_A_A_D| S2_A_N_D| S2_N_A_D| S2_N_N_D| S2_A_D_A| S2_A_D_N| S2_N_D_A| S2_N_D_N| S2_D_A_A| S2_D_A_N| S2_D_N_A| S2_D_N_N| S2_A_A_A| S2_A_A_N| S2_A_N_A| S2_A_N_N| S2_N_A_A| S2_N_A_N| S2_N_N_A| S2_N_N_N| D_DTX
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Hack')
		"""
		param = Conversions.enum_scalar_to_str(harq_ack, enums.HsRel8HarqMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:HACK{indexNull_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, indexNull=repcap.IndexNull.Default) -> enums.HsRel8HarqMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:HACK<DI> \n
		Snippet: value: enums.HsRel8HarqMode = driver.source.bb.w3Gpp.mstation.dpcch.hs.row.hack.get(mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, indexNull = repcap.IndexNull.Default) \n
		(Release 8 and Later) Sets the information transmitted during the HARQ-ACK slots of the TTIs during the corresponding
		specified HARQ-ACK From/To range. For detailed description, see 'HS-DPCCH 1/2, HARQ-ACK 1/2/3/4'.
		The Table 'Cross-reference between the used GUI terms and abbreviations in the SCPI command' provides the necessary
		cross-reference information. Cross-reference between the used GUI terms and abbreviations in the SCPI command
			Table Header: Value name / Parameter value \n
			- 'DTX' / DTX | D_DTX
			- 'PRE, POST' / PRE | POST
			- 'A, N' / A | N
			- 'AA, AN, NA, NN' / M_A | M_N | M_AA | M_AN | M_NA | M_NN
			- 'A/D, N/A, …' (different combinations possible) / S_A_D | S_N_A | ... (different combinations possible)
			- 'A/D/D, N/D/D, …' (different combinations possible) / S2_N_N_N | S2_N_N_A | ... (different combinations possible)
			- 'AN/NN, D/AA, …' (different combinations possible) / MS_AA_AA | MS_D_AA ... (different combinations possible) \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Hack')
			:return: harq_ack: DTX| PRE| POST| A| N| M_A| M_N| M_AA| M_AN| M_NA| M_NN| S_A_D| S_N_D| S_D_A| S_D_N| S_A_A| S_A_N| S_N_A| S_N_N| MS_A_D| MS_N_D| MS_AA_D| MS_AN_D| MS_NA_D| MS_NN_D| MS_D_A| MS_D_N| MS_D_AA| MS_D_AN| MS_D_NA| MS_D_NN| MS_A_A| MS_A_N| MS_N_A| MS_N_N| MS_A_AA| MS_A_AN| MS_A_NA| MS_A_NN| MS_N_AA| MS_N_AN| MS_N_NA| MS_N_NN| MS_AA_A| MS_AA_N| MS_AN_A| MS_AN_N| MS_NA_A| MS_NA_N| MS_NN_A| MS_NN_N| MS_AA_AA| MS_AA_AN| MS_AA_NA| MS_AA_NN| MS_AN_AA| MS_AN_AN| MS_AN_NA| MS_AN_NN| MS_NA_AA| MS_NA_AN| MS_NA_NA| MS_NA_NN| MS_NN_AA| MS_NN_AN| MS_NN_NA| MS_NN_NN| S2_A_D_D| S2_N_D_D| S2_D_A_D| S2_D_N_D| S2_D_D_A| S2_D_D_N| S2_A_A_D| S2_A_N_D| S2_N_A_D| S2_N_N_D| S2_A_D_A| S2_A_D_N| S2_N_D_A| S2_N_D_N| S2_D_A_A| S2_D_A_N| S2_D_N_A| S2_D_N_N| S2_A_A_A| S2_A_A_N| S2_A_N_A| S2_A_N_N| S2_N_A_A| S2_N_A_N| S2_N_N_A| S2_N_N_N| D_DTX"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:HACK{indexNull_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.HsRel8HarqMode)

	def clone(self) -> 'Hack':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hack(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
