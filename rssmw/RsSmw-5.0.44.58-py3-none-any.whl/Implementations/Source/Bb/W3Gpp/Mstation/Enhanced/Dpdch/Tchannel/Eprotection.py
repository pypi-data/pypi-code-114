from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eprotection:
	"""Eprotection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eprotection", core, parent)

	def set(self, eprotection: enums.EnhTchErr, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:EPRotection \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.eprotection.set(eprotection = enums.EnhTchErr.CON2, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command determines the error protection. \n
			:param eprotection: NONE| CON2| CON3| TURBo3 NONE No error protection. TURBo3 Turbo Coder of rate 1/3 in accordance with the 3GPP specifications. CON2 | CON3 Convolution Coder of rate ½ or 1/3 with generator polynomials defined by 3GPP.
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.enum_scalar_to_str(eprotection, enums.EnhTchErr)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:EPRotection {param}')

	# noinspection PyTypeChecker
	def get(self, transportChannelNull=repcap.TransportChannelNull.Default) -> enums.EnhTchErr:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:EPRotection \n
		Snippet: value: enums.EnhTchErr = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.eprotection.get(transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command determines the error protection. \n
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: eprotection: NONE| CON2| CON3| TURBo3 NONE No error protection. TURBo3 Turbo Coder of rate 1/3 in accordance with the 3GPP specifications. CON2 | CON3 Convolution Coder of rate ½ or 1/3 with generator polynomials defined by 3GPP."""
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:EPRotection?')
		return Conversions.str_to_scalar_enum(response, enums.EnhTchErr)
