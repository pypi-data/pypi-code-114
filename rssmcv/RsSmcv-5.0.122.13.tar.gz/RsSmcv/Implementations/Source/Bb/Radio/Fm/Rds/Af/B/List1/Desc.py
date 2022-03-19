from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Desc:
	"""Desc commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AlternaiveFreqList, default value after init: AlternaiveFreqList.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("desc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_alternaiveFreqList_get', 'repcap_alternaiveFreqList_set', repcap.AlternaiveFreqList.Nr1)

	def repcap_alternaiveFreqList_set(self, alternaiveFreqList: repcap.AlternaiveFreqList) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AlternaiveFreqList.Default
		Default value after init: AlternaiveFreqList.Nr1"""
		self._cmd_group.set_repcap_enum_value(alternaiveFreqList)

	def repcap_alternaiveFreqList_get(self) -> repcap.AlternaiveFreqList:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, af_list_1_order: enums.TxAudioBcFmRdsAfBorder, alternaiveFreqList=repcap.AlternaiveFreqList.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST1:DESC<CH> \n
		Snippet: driver.source.bb.radio.fm.rds.af.b.list1.desc.set(af_list_1_order = enums.TxAudioBcFmRdsAfBorder.ASC, alternaiveFreqList = repcap.AlternaiveFreqList.Default) \n
		Sets the frequency order of the corresponding number of the selected list. \n
			:param af_list_1_order: ASC| DESC ASC Ascending order, the same program is carried. DESC Descending order, the alternative frequency points to a program that has regional variants.
			:param alternaiveFreqList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Desc')
		"""
		param = Conversions.enum_scalar_to_str(af_list_1_order, enums.TxAudioBcFmRdsAfBorder)
		alternaiveFreqList_cmd_val = self._cmd_group.get_repcap_cmd_value(alternaiveFreqList, repcap.AlternaiveFreqList)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST1:DESC{alternaiveFreqList_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, alternaiveFreqList=repcap.AlternaiveFreqList.Default) -> enums.TxAudioBcFmRdsAfBorder:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST1:DESC<CH> \n
		Snippet: value: enums.TxAudioBcFmRdsAfBorder = driver.source.bb.radio.fm.rds.af.b.list1.desc.get(alternaiveFreqList = repcap.AlternaiveFreqList.Default) \n
		Sets the frequency order of the corresponding number of the selected list. \n
			:param alternaiveFreqList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Desc')
			:return: af_list_1_order: No help available"""
		alternaiveFreqList_cmd_val = self._cmd_group.get_repcap_cmd_value(alternaiveFreqList, repcap.AlternaiveFreqList)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST1:DESC{alternaiveFreqList_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.TxAudioBcFmRdsAfBorder)

	def clone(self) -> 'Desc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Desc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
