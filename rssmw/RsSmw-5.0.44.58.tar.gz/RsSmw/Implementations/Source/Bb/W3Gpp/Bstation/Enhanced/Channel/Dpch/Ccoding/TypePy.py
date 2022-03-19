from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.ChanCodType, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:TYPE \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.typePy.set(type_py = enums.ChanCodType.AMR, channelNull = repcap.ChannelNull.Default) \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. The 3GPP specification defines 4
		reference measurement channel coding types, which differ in the input data bit rate to be processed (12.2, 64, 144 and
		384 ksps) . The additional AMR CODER coding scheme generates the coding of a voice channel. The BTFD coding types with
		different data rates are also defined in the 3GPP specification (TS 34.121) . They are used for the receiver quality test
		Blind Transport Format Detection. When a channel coding type conforms to the standard and channel coding is activated,
		(BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:STAT) the slot format (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:SFOR) and thus the symbol
		rate (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:SRAT) , the bits per frame, (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:BPFR) , the pilot
		length (BB:W3GP:BST1:CHAN<n>:DPCC:PLEN) and the TFCI state (BB:W3GP:BST1:CHAN<n>:DPCC:TFCI:STAT) are set to the
		associated values. \n
			:param type_py: M12K2| M64K| M144k| M384k| AMR| BTFD1| BTFD2| BTFD3 M12K2 Measurement channel with an input data bit rate of 12.2 ksps. M64K Measurement channel with an input data bit rate of 64 ksps. M144k Measurement channel with an input data bit rate of 144 ksps. M384k Measurement channel with an input data bit rate of 384 ksps. AMR Channel coding for the AMR Coder (coding a voice channel) . USER This parameter cannot be set. USER is returned whenever a user-defined channel coding is active, that is to say, after a channel coding parameter has been changed or a user coding file has been loaded. The file is loaded by the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:CCODing:USER:LOAD. BTFD1 Blind Transport Format Detection Rate 1 (12.2 kbps) . BTFD2 Blind Transport Format Detection Rate 2 (7.95 kbps) . BTFD3 Blind Transport Format Detection Rate 3 (1.95 kbps) .
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanCodType)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default) -> enums.ChanCodType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:TYPE \n
		Snippet: value: enums.ChanCodType = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.typePy.get(channelNull = repcap.ChannelNull.Default) \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. The 3GPP specification defines 4
		reference measurement channel coding types, which differ in the input data bit rate to be processed (12.2, 64, 144 and
		384 ksps) . The additional AMR CODER coding scheme generates the coding of a voice channel. The BTFD coding types with
		different data rates are also defined in the 3GPP specification (TS 34.121) . They are used for the receiver quality test
		Blind Transport Format Detection. When a channel coding type conforms to the standard and channel coding is activated,
		(BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:STAT) the slot format (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:SFOR) and thus the symbol
		rate (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:SRAT) , the bits per frame, (BB:W3GP:BST:ENH:CHAN<n>:DPCH:CCOD:BPFR) , the pilot
		length (BB:W3GP:BST1:CHAN<n>:DPCC:PLEN) and the TFCI state (BB:W3GP:BST1:CHAN<n>:DPCC:TFCI:STAT) are set to the
		associated values. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: type_py: M12K2| M64K| M144k| M384k| AMR| BTFD1| BTFD2| BTFD3 M12K2 Measurement channel with an input data bit rate of 12.2 ksps. M64K Measurement channel with an input data bit rate of 64 ksps. M144k Measurement channel with an input data bit rate of 144 ksps. M384k Measurement channel with an input data bit rate of 384 ksps. AMR Channel coding for the AMR Coder (coding a voice channel) . USER This parameter cannot be set. USER is returned whenever a user-defined channel coding is active, that is to say, after a channel coding parameter has been changed or a user coding file has been loaded. The file is loaded by the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:CCODing:USER:LOAD. BTFD1 Blind Transport Format Detection Rate 1 (12.2 kbps) . BTFD2 Blind Transport Format Detection Rate 2 (7.95 kbps) . BTFD3 Blind Transport Format Detection Rate 3 (1.95 kbps) ."""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodType)
