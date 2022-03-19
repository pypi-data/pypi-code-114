from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaver:
	"""Interleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaver", core, parent)
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

	def set(self, interleaver: bool, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:INTerleaver<DI> \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.pccpch.ccoding.interleaver.set(interleaver = False, index = repcap.Index.Default) \n
		The command activates or deactivates channel coding interleaver state 1 or 2 for the P-CCPCH. Note: The interleaver
		states do not cause the symbol rate to change. \n
			:param interleaver: ON| OFF
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Interleaver')
		"""
		param = Conversions.bool_to_str(interleaver)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:INTerleaver{index_cmd_val} {param}')

	def get(self, index=repcap.Index.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:INTerleaver<DI> \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.pccpch.ccoding.interleaver.get(index = repcap.Index.Default) \n
		The command activates or deactivates channel coding interleaver state 1 or 2 for the P-CCPCH. Note: The interleaver
		states do not cause the symbol rate to change. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Interleaver')
			:return: interleaver: ON| OFF"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:INTerleaver{index_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Interleaver':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Interleaver(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
