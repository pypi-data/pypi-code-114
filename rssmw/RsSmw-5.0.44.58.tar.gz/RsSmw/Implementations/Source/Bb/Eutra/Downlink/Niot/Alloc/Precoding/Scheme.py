from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scheme:
	"""Scheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scheme", core, parent)

	def set(self, prec_ant_scheme: enums.DlecpRecScheme, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:PRECoding:SCHeme \n
		Snippet: driver.source.bb.eutra.downlink.niot.alloc.precoding.scheme.set(prec_ant_scheme = enums.DlecpRecScheme.NONE, allocationNull = repcap.AllocationNull.Default) \n
		Sets the precoding scheme. \n
			:param prec_ant_scheme: NONE| TXD
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(prec_ant_scheme, enums.DlecpRecScheme)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:PRECoding:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.DlecpRecScheme:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:PRECoding:SCHeme \n
		Snippet: value: enums.DlecpRecScheme = driver.source.bb.eutra.downlink.niot.alloc.precoding.scheme.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the precoding scheme. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: prec_ant_scheme: NONE| TXD"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:PRECoding:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.DlecpRecScheme)
