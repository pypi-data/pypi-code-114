from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bit:
	"""Bit commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bit", core, parent)

	# noinspection PyTypeChecker
	def get_layer(self) -> enums.EnhBitErr:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:LAYer \n
		Snippet: value: enums.EnhBitErr = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.get_layer() \n
		The command selects the layer at which bit errors are inserted. \n
			:return: layer: TRANsport| PHYSical TRANsport Transport Layer (Layer 2) . This layer is only available when channel coding is active. PHYSical Physical layer (Layer 1)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:LAYer?')
		return Conversions.str_to_scalar_enum(response, enums.EnhBitErr)

	def set_layer(self, layer: enums.EnhBitErr) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:LAYer \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.set_layer(layer = enums.EnhBitErr.PHYSical) \n
		The command selects the layer at which bit errors are inserted. \n
			:param layer: TRANsport| PHYSical TRANsport Transport Layer (Layer 2) . This layer is only available when channel coding is active. PHYSical Physical layer (Layer 1)
		"""
		param = Conversions.enum_scalar_to_str(layer, enums.EnhBitErr)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:LAYer {param}')

	def get_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:RATE \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.get_rate() \n
		Sets the bit error rate. \n
			:return: rate: float Range: 1E-7 to 0.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:RATE?')
		return Conversions.str_to_float(response)

	def set_rate(self, rate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:RATE \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.set_rate(rate = 1.0) \n
		Sets the bit error rate. \n
			:param rate: float Range: 1E-7 to 0.5
		"""
		param = Conversions.decimal_value_to_str(rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:RATE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.get_state() \n
		The command activates or deactivates bit error generation. Bit errors are inserted into the data fields of the enhanced
		channels. When channel coding is active, it is possible to select the layer in which the errors are inserted (physical or
		transport layer) . When the data source is read out, individual bits are deliberately inverted at random points in the
		data bit stream at the specified error rate in order to simulate an invalid signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:STATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.derror.bit.set_state(state = False) \n
		The command activates or deactivates bit error generation. Bit errors are inserted into the data fields of the enhanced
		channels. When channel coding is active, it is possible to select the layer in which the errors are inserted (physical or
		transport layer) . When the data source is read out, individual bits are deliberately inverted at random points in the
		data bit stream at the specified error rate in order to simulate an invalid signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:DERRor:BIT:STATe {param}')
