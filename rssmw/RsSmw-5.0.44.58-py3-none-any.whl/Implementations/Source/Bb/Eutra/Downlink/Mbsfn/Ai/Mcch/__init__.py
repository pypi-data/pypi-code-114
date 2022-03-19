from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcch:
	"""Mcch commands group definition. 15 total commands, 5 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcch", core, parent)

	@property
	def aval(self):
		"""aval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aval'):
			from .Aval import Aval
			self._aval = Aval(self._core, self._cmd_group)
		return self._aval

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def npattern(self):
		"""npattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npattern'):
			from .Npattern import Npattern
			self._npattern = Npattern(self._core, self._cmd_group)
		return self._npattern

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def tbSize(self):
		"""tbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbSize'):
			from .TbSize import TbSize
			self._tbSize = TbSize(self._core, self._cmd_group)
		return self._tbSize

	# noinspection PyTypeChecker
	def get_data(self) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_data() \n
		Sets the data source used for the MCCH. \n
			:return: data_source: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def set_data(self, data_source: enums.DataSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:DATA \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_data(data_source = enums.DataSourceA.DLISt) \n
		Sets the data source used for the MCCH. \n
			:param data_source: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE
		"""
		param = Conversions.enum_scalar_to_str(data_source, enums.DataSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:DATA {param}')

	def get_dlist(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:DLISt \n
		Snippet: value: str = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_dlist() \n
		Sets the data list used as data source for MCCH. \n
			:return: data_list: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:DLISt?')
		return trim_str_response(response)

	def set_dlist(self, data_list: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:DLISt \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_dlist(data_list = '1') \n
		Sets the data list used as data source for MCCH. \n
			:param data_list: string
		"""
		param = Conversions.value_to_quoted_str(data_list)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:DLISt {param}')

	# noinspection PyTypeChecker
	def get_mcs(self) -> enums.EutraMcchMcs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MCS \n
		Snippet: value: enums.EutraMcchMcs = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_mcs() \n
		Defines the Modulation and Coding Scheme (MCS) applicable for the subframes indicated by the 'MCCH Allocation value' and
		for the first subframe of each MCH scheduling period (which may contain the MCH scheduling information provided by MAC) . \n
			:return: mcs: MCS19| MCS13| MCS7| MCS2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:MCS?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMcchMcs)

	def set_mcs(self, mcs: enums.EutraMcchMcs) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MCS \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_mcs(mcs = enums.EutraMcchMcs.MCS13) \n
		Defines the Modulation and Coding Scheme (MCS) applicable for the subframes indicated by the 'MCCH Allocation value' and
		for the first subframe of each MCH scheduling period (which may contain the MCH scheduling information provided by MAC) . \n
			:param mcs: MCS19| MCS13| MCS7| MCS2
		"""
		param = Conversions.enum_scalar_to_str(mcs, enums.EutraMcchMcs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:MCS {param}')

	# noinspection PyTypeChecker
	def get_mper(self) -> enums.EutraMcchModPer:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MPER \n
		Snippet: value: enums.EutraMcchModPer = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_mper() \n
		Sets the MCCH Modification Period. \n
			:return: modif_period: MP512| MP1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:MPER?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMcchModPer)

	def set_mper(self, modif_period: enums.EutraMcchModPer) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MPER \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_mper(modif_period = enums.EutraMcchModPer.MP1024) \n
		Sets the MCCH Modification Period. \n
			:param modif_period: MP512| MP1024
		"""
		param = Conversions.enum_scalar_to_str(modif_period, enums.EutraMcchModPer)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:MPER {param}')

	def get_noffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NOFFset \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_noffset() \n
		Defines, together with the [:SOURce<hw>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC, the radio frames in which the MCCH information
		change notification is scheduled. \n
			:return: notif_offset: integer Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NOFFset?')
		return Conversions.str_to_int(response)

	def set_noffset(self, notif_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NOFFset \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_noffset(notif_offset = 1) \n
		Defines, together with the [:SOURce<hw>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC, the radio frames in which the MCCH information
		change notification is scheduled. \n
			:param notif_offset: integer Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(notif_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NOFFset {param}')

	# noinspection PyTypeChecker
	def get_nrc(self) -> enums.EutraMbsfnNotRepCoef:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC \n
		Snippet: value: enums.EutraMbsfnNotRepCoef = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_nrc() \n
		Selects the current change notification repetition period common for all MCCHs that are configured. \n
			:return: notif_repet_coeff: NRC2| NRC4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMbsfnNotRepCoef)

	def set_nrc(self, notif_repet_coeff: enums.EutraMbsfnNotRepCoef) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_nrc(notif_repet_coeff = enums.EutraMbsfnNotRepCoef.NRC2) \n
		Selects the current change notification repetition period common for all MCCHs that are configured. \n
			:param notif_repet_coeff: NRC2| NRC4
		"""
		param = Conversions.enum_scalar_to_str(notif_repet_coeff, enums.EutraMbsfnNotRepCoef)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NRC {param}')

	def get_nsi(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NSI \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_nsi() \n
		Defines the subframe used to transmit MCCH change notifications on PDCCH. \n
			:return: index: integer In FDD: values 1 to 6 correspond with subframes #1, #2, #3, #6, #7 and #8 In TDD: values 1 to 5 correspond with subframe #3, #4, #7, #8 and #9 Range: 1 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NSI?')
		return Conversions.str_to_int(response)

	def set_nsi(self, index: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:NSI \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_nsi(index = 1) \n
		Defines the subframe used to transmit MCCH change notifications on PDCCH. \n
			:param index: integer In FDD: values 1 to 6 correspond with subframes #1, #2, #3, #6, #7 and #8 In TDD: values 1 to 5 correspond with subframe #3, #4, #7, #8 and #9 Range: 1 to dynamic
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:NSI {param}')

	def get_offs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:OFFS \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_offs() \n
		Indicates, together with the [:SOURce<hw>]:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER, the radio frames in which MCCH is scheduled. \n
			:return: mcch_offset: integer Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:OFFS?')
		return Conversions.str_to_int(response)

	def set_offs(self, mcch_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:OFFS \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_offs(mcch_offset = 1) \n
		Indicates, together with the [:SOURce<hw>]:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER, the radio frames in which MCCH is scheduled. \n
			:param mcch_offset: integer Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(mcch_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:OFFS {param}')

	# noinspection PyTypeChecker
	def get_rper(self) -> enums.EutraMcchRepPer:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER \n
		Snippet: value: enums.EutraMcchRepPer = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_rper() \n
		Defines the interval between transmissions of MCCH information in radio frames. \n
			:return: repet_period: RP64| RP32| RP128| RP256
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMcchRepPer)

	def set_rper(self, repet_period: enums.EutraMcchRepPer) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_rper(repet_period = enums.EutraMcchRepPer.RP128) \n
		Defines the interval between transmissions of MCCH information in radio frames. \n
			:param repet_period: RP64| RP32| RP128| RP256
		"""
		param = Conversions.enum_scalar_to_str(repet_period, enums.EutraMcchRepPer)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:RPER {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.get_state() \n
		Enables/disables the MCCH. \n
			:return: mcch_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, mcch_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:STATe \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.ai.mcch.set_state(mcch_state = False) \n
		Enables/disables the MCCH. \n
			:param mcch_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(mcch_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:STATe {param}')

	def clone(self) -> 'Mcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
