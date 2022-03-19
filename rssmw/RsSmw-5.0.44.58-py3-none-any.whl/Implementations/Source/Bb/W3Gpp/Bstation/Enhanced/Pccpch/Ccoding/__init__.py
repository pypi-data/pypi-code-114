from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccoding:
	"""Ccoding commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccoding", core, parent)

	@property
	def interleaver(self):
		"""interleaver commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interleaver'):
			from .Interleaver import Interleaver
			self._interleaver = Interleaver(self._core, self._cmd_group)
		return self._interleaver

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.pccpch.ccoding.get_state() \n
		The command activates or deactivates channel coding for the enhanced P-CCPCH. The coding scheme of the P-CCPCH (BCH) is
		defined in the standard. \n
			:return: state: ON| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:STATe \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.pccpch.ccoding.set_state(state = False) \n
		The command activates or deactivates channel coding for the enhanced P-CCPCH. The coding scheme of the P-CCPCH (BCH) is
		defined in the standard. \n
			:param state: ON| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:STATe {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.CodeType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:TYPE \n
		Snippet: value: enums.CodeType = driver.source.bb.w3Gpp.bstation.enhanced.pccpch.ccoding.get_type_py() \n
		The command queries the channel coding scheme in accordance with the 3GPP specification. The coding scheme of the P-CCPCH
		(BCH) is defined in the standard. The channel is generated automatically with the counting system frame number (SFN) .
		The system information after the SFN field is completed from the selected data source. \n
			:return: type_py: BCHSfn
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:PCCPch:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.CodeType)

	def clone(self) -> 'Ccoding':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccoding(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
