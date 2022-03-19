from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpdch:
	"""Dpdch commands group definition. 37 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpdch", core, parent)

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def derror(self):
		"""derror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import Derror
			self._derror = Derror(self._core, self._cmd_group)
		return self._derror

	@property
	def tchannel(self):
		"""tchannel commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_tchannel'):
			from .Tchannel import Tchannel
			self._tchannel = Tchannel(self._core, self._cmd_group)
		return self._tchannel

	@property
	def dpControl(self):
		"""dpControl commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_dpControl'):
			from .DpControl import DpControl
			self._dpControl = DpControl(self._core, self._cmd_group)
		return self._dpControl

	def get_bp_frame(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:BPFRame \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.get_bp_frame() \n
		The command queries the number of data bits in the DPDCH component of the frame at the physical layer. The number of data
		bits depends on the overall symbol rate. \n
			:return: bp_frame: integer Range: 150 to 9600
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:BPFRame?')
		return Conversions.str_to_int(response)

	def get_interleaver_2(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2 \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.get_interleaver_2() \n
		The command activates or deactivates channel coding interleaver state 2 for all the transport channels. Interleaver state
		1 can be activated and deactivated for each channel individually
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<di0>:INTerleaver) . Note: The interleaver states do not cause
		the symbol rate to change \n
			:return: interleaver_2: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2?')
		return Conversions.str_to_bool(response)

	def set_interleaver_2(self, interleaver_2: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2 \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.set_interleaver_2(interleaver_2 = False) \n
		The command activates or deactivates channel coding interleaver state 2 for all the transport channels. Interleaver state
		1 can be activated and deactivated for each channel individually
		([:SOURce<hw>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<di0>:INTerleaver) . Note: The interleaver states do not cause
		the symbol rate to change \n
			:param interleaver_2: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(interleaver_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:INTerleaver2 {param}')

	# noinspection PyTypeChecker
	def get_orate(self) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.get_orate() \n
		The command queries the overall symbol rate (Overall Symbol Rate) of the enhanced channels. The value is set with the
		command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPDCh:ORATe. This setting also defines the number of active channels, their
		symbol rates and channelization codes. \n
			:return: orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)

	def set_orate(self, orate: enums.SymbRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.set_orate(orate = enums.SymbRate.D120k) \n
		The command queries the overall symbol rate (Overall Symbol Rate) of the enhanced channels. The value is set with the
		command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPDCh:ORATe. This setting also defines the number of active channels, their
		symbol rates and channelization codes. \n
			:param orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k
		"""
		param = Conversions.enum_scalar_to_str(orate, enums.SymbRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:ORATe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.get_state() \n
		Queries the enhanced state of the station. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:STATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.set_state(state = False) \n
		Queries the enhanced state of the station. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:STATe {param}')

	def clone(self) -> 'Dpdch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpdch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
