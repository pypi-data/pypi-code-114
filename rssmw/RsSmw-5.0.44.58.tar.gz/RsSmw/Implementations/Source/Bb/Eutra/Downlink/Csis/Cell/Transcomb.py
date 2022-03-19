from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transcomb:
	"""Transcomb commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transcomb", core, parent)
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

	def set(self, csi_rs_trans_comb: enums.EutraCsiRsTransComb, cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:TRANscomb<ST_OPTIONAL> \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.transcomb.set(csi_rs_trans_comb = enums.EutraCsiRsTransComb._0, cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the parameter NZP-TransmissionComb. \n
			:param csi_rs_trans_comb: 0| 1| 2
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Transcomb')
		"""
		param = Conversions.enum_scalar_to_str(csi_rs_trans_comb, enums.EutraCsiRsTransComb)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:TRANscomb{indexNull_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> enums.EutraCsiRsTransComb:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:TRANscomb<ST_OPTIONAL> \n
		Snippet: value: enums.EutraCsiRsTransComb = driver.source.bb.eutra.downlink.csis.cell.transcomb.get(cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the parameter NZP-TransmissionComb. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Transcomb')
			:return: csi_rs_trans_comb: 0| 1| 2"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:TRANscomb{indexNull_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCsiRsTransComb)

	def clone(self) -> 'Transcomb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Transcomb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
