from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmode:
	"""Pmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmode", core, parent)

	def set(self, power_mode: enums.PhichPwrMode, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:PMODe \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.phich.pmode.set(power_mode = enums.PhichPwrMode.CONSt, subframeNull = repcap.SubframeNull.Default) \n
		Determines whether the PHICHs in a PHICH group are sent with the same power or enables the adjustment of each PPHICH
		individually. \n
			:param power_mode: CONSt| IND CONSt The power of a PHICH in a PHICH group is set with the command SOUR:BB:EUTR:DL:ENCC:PHIC:POW. IND The power of the individual PHICHs is set separatelly
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.enum_scalar_to_str(power_mode, enums.PhichPwrMode)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default) -> enums.PhichPwrMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:PMODe \n
		Snippet: value: enums.PhichPwrMode = driver.source.bb.eutra.downlink.subf.encc.phich.pmode.get(subframeNull = repcap.SubframeNull.Default) \n
		Determines whether the PHICHs in a PHICH group are sent with the same power or enables the adjustment of each PPHICH
		individually. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: power_mode: CONSt| IND CONSt The power of a PHICH in a PHICH group is set with the command SOUR:BB:EUTR:DL:ENCC:PHIC:POW. IND The power of the individual PHICHs is set separatelly"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PhichPwrMode)
