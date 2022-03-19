from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tfci:
	"""Tfci commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tfci", core, parent)

	def set(self, tfci: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:TFCI \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.tfci.set(tfci = 1, mobileStation = repcap.MobileStation.Default) \n
		Sets the value of the TFCI (Transport Format Combination Indicator) field. This value selects a combination of 30 bits,
		which are divided into two groups of 15 successive slots. \n
			:param tfci: integer Range: 0 to 1023
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(tfci)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:TFCI {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:TFCI \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.prach.tfci.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the value of the TFCI (Transport Format Combination Indicator) field. This value selects a combination of 30 bits,
		which are divided into two groups of 15 successive slots. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: tfci: integer Range: 0 to 1023"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:TFCI?')
		return Conversions.str_to_int(response)
