from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpControl:
	"""DpControl commands group definition. 11 total commands, 2 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpControl", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def get_aoue(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:AOUE \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_aoue() \n
		Enables power control of the enhanced channels of all active UEs with the settings of UE1. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:AOUE?')
		return Conversions.str_to_bool(response)

	def set_aoue(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:AOUE \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_aoue(state = False) \n
		Enables power control of the enhanced channels of all active UEs with the settings of UE1. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:AOUE {param}')

	# noinspection PyTypeChecker
	def get_assignment(self) -> enums.PowContAssMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:ASSignment \n
		Snippet: value: enums.PowContAssMode = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_assignment() \n
		Enabled for UL-DTX mode only ([:SOURce<hw>]:BB:W3GPp:MSTation:UDTX:STATe ON) . The power control recognizes the UL-DPCCH
		gaps according to 3GPP TS 25.214. Some of the TPC commands sent to the instrument over the external line or by the TPC
		pattern are ignored, whereas others are summed up and applied later. The processing of the TPC commands depends only on
		whether the BS sends the TPC bits on the F-DPCH with slot format 0/ slot format 9 or not. \n
			:return: assignment: NORMal| FDPCh
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:ASSignment?')
		return Conversions.str_to_scalar_enum(response, enums.PowContAssMode)

	def set_assignment(self, assignment: enums.PowContAssMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:ASSignment \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_assignment(assignment = enums.PowContAssMode.FDPCh) \n
		Enabled for UL-DTX mode only ([:SOURce<hw>]:BB:W3GPp:MSTation:UDTX:STATe ON) . The power control recognizes the UL-DPCCH
		gaps according to 3GPP TS 25.214. Some of the TPC commands sent to the instrument over the external line or by the TPC
		pattern are ignored, whereas others are summed up and applied later. The processing of the TPC commands depends only on
		whether the BS sends the TPC bits on the F-DPCH with slot format 0/ slot format 9 or not. \n
			:param assignment: NORMal| FDPCh
		"""
		param = Conversions.enum_scalar_to_str(assignment, enums.PowContAssMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:ASSignment {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_connector() \n
		Determines the input connector at that the instrument expects the external control signal. \n
			:return: connector: LOCal| GLOBal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)

	def set_connector(self, connector: enums.FeedbackConnector) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:CONNector \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_connector(connector = enums.FeedbackConnector.GLOBal) \n
		Determines the input connector at that the instrument expects the external control signal. \n
			:param connector: LOCal| GLOBal
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnector)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:CONNector {param}')

	# noinspection PyTypeChecker
	def get_direction(self) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:DIRection \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_direction() \n
		The command selects the Dynamic Power Control direction. The selected direction determines if the channel power is
		increased (UP) or decreased (DOWN) by control signal with high level. \n
			:return: direction: UP| DOWN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_direction(self, direction: enums.UpDownDirection) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:DIRection \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_direction(direction = enums.UpDownDirection.DOWN) \n
		The command selects the Dynamic Power Control direction. The selected direction determines if the channel power is
		increased (UP) or decreased (DOWN) by control signal with high level. \n
			:param direction: UP| DOWN
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.UpDownDirection)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:DIRection {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowContMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:MODE \n
		Snippet: value: enums.PowContMode = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_mode() \n
		Determines the source of the control signal. \n
			:return: mode: TPC| MANual | EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowContMode)

	def set_mode(self, mode: enums.PowContMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:MODE \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_mode(mode = enums.PowContMode.EXTernal) \n
		Determines the source of the control signal. \n
			:param mode: TPC| MANual | EXTernal
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowContMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_state() \n
		Activates/deactivates Dynamic Power Control. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:STATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.set_state(state = False) \n
		Activates/deactivates Dynamic Power Control. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:STATe {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:[ENHanced]:[DPDCh]:DPControl:[POWer] \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.dpControl.get_power() \n
		The command queries the deviation of the channel power (delta POW) from the set power start value of the DPDCH. \n
			:return: power: float Range: -60 to 60
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DPControl:POWer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DpControl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DpControl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
