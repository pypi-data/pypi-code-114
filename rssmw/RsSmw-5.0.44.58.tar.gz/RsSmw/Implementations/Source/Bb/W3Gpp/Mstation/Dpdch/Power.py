from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:POWer \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpdch.power.set(power = 1.0, mobileStation = repcap.MobileStation.Default) \n
		Sets the channel power of the DPDCHs. The power entered is relative to the powers of the other channels. If 'Adjust Total
		Power to 0 dB' is executed ([:SOURce<hw>]:BB:W3GPp:POWer:ADJust) , the power is normalized to a total power for all
		channels of 0 dB. The power ratios of the individual channels remains unchanged. Note: The uplink channels are not
		blanked in this mode (duty cycle 100%) . \n
			:param power: float Range: -80 to 0
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(power)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:POWer {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.dpdch.power.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the channel power of the DPDCHs. The power entered is relative to the powers of the other channels. If 'Adjust Total
		Power to 0 dB' is executed ([:SOURce<hw>]:BB:W3GPp:POWer:ADJust) , the power is normalized to a total power for all
		channels of 0 dB. The power ratios of the individual channels remains unchanged. Note: The uplink channels are not
		blanked in this mode (duty cycle 100%) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: power: float Range: -80 to 0"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:POWer?')
		return Conversions.str_to_float(response)
