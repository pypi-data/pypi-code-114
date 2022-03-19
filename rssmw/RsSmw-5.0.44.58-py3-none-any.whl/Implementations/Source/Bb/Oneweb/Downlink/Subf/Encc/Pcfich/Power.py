from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PCFich:POWer \n
		Snippet: driver.source.bb.oneweb.downlink.subf.encc.pcfich.power.set(power = 1.0, subframeNull = repcap.SubframeNull.Default) \n
		Sets the power of the PCFICH (PPCFICH) . \n
			:param power: float Range: -80 to 10
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(power)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PCFich:POWer {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PCFich:POWer \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.subf.encc.pcfich.power.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the power of the PCFICH (PPCFICH) . \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: power: float Range: -80 to 10"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PCFich:POWer?')
		return Conversions.str_to_float(response)
