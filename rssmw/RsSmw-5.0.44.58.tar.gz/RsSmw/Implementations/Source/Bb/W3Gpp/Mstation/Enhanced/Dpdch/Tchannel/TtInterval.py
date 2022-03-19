from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtInterval:
	"""TtInterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttInterval", core, parent)

	def set(self, tt_interval: enums.TchTranTimInt, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:TTINterval \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.ttInterval.set(tt_interval = enums.TchTranTimInt._10MS, transportChannelNull = repcap.TransportChannelNull.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param tt_interval: 10MS| 20MS| 40MS
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.enum_scalar_to_str(tt_interval, enums.TchTranTimInt)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:TTINterval {param}')

	# noinspection PyTypeChecker
	def get(self, transportChannelNull=repcap.TransportChannelNull.Default) -> enums.TchTranTimInt:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel<DI0>:TTINterval \n
		Snippet: value: enums.TchTranTimInt = driver.source.bb.w3Gpp.mstation.enhanced.dpdch.tchannel.ttInterval.get(transportChannelNull = repcap.TransportChannelNull.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: tt_interval: 10MS| 20MS| 40MS"""
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation:ENHanced:DPDCh:TCHannel{transportChannelNull_cmd_val}:TTINterval?')
		return Conversions.str_to_scalar_enum(response, enums.TchTranTimInt)
