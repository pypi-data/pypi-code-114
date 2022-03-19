from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccoding:
	"""Ccoding commands group definition. 6 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccoding", core, parent)

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.ccoding.get_state() \n
		The command activates or deactivates channel coding for the enhanced channels. When channel coding is activated, the
		overall symbol rate ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe) is set to the value predetermined by the
		selected channel coding type ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE) . \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.ccoding.set_state(state = False) \n
		The command activates or deactivates channel coding for the enhanced channels. When channel coding is activated, the
		overall symbol rate ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe) is set to the value predetermined by the
		selected channel coding type ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE) . \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.ChanCodType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE \n
		Snippet: value: enums.ChanCodType = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.ccoding.get_type_py() \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. The channel coding scheme
		selected predetermines the overall symbol rate.
		When channel coding is activated ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe) the overall symbol rate
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe) is set to the value predetermined by the selected channel coding
		type. \n
			:return: type_py: M12K2| M64K| M144k| M384k| AMR M12K2 Measurement channel with an input data bit rate of 12.2 ksps. M64K Measurement channel with an input data bit rate of 64 ksps. M144K Measurement channel with an input data bit rate of 144 ksps. M384K Measurement channel with an input data bit rate of 384 ksps. AMR Channel coding for the AMR Coder (coding a voice channel) . USER This parameter cannot be set. USER is returned whenever a user-defined channel coding is active, that is to say, after a channel coding parameter has been changed or a user coding file has been loaded. The file is loaded by the command [:SOURcehw]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:USER:LOAD.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodType)

	def set_type_py(self, type_py: enums.ChanCodType) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.ccoding.set_type_py(type_py = enums.ChanCodType.AMR) \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. The channel coding scheme
		selected predetermines the overall symbol rate.
		When channel coding is activated ([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:STATe) the overall symbol rate
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe) is set to the value predetermined by the selected channel coding
		type. \n
			:param type_py: M12K2| M64K| M144k| M384k| AMR M12K2 Measurement channel with an input data bit rate of 12.2 ksps. M64K Measurement channel with an input data bit rate of 64 ksps. M144K Measurement channel with an input data bit rate of 144 ksps. M384K Measurement channel with an input data bit rate of 384 ksps. AMR Channel coding for the AMR Coder (coding a voice channel) . USER This parameter cannot be set. USER is returned whenever a user-defined channel coding is active, that is to say, after a channel coding parameter has been changed or a user coding file has been loaded. The file is loaded by the command [:SOURcehw]:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:USER:LOAD.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanCodType)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:CCODing:TYPE {param}')

	def clone(self) -> 'Ccoding':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccoding(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
