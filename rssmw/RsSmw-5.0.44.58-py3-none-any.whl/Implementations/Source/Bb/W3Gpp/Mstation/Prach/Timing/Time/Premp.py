from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Premp:
	"""Premp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("premp", core, parent)

	def set(self, premp: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:TIMing:TIME:PREMp \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.timing.time.premp.set(premp = 1, mobileStation = repcap.MobileStation.Default) \n
		This command defines the AICH Transmission Timing. This parameter defines the time difference between the preamble and
		the message part. Two modes are defined in the standard. In mode 0, the preamble to message part difference is 3 access
		slots, in mode 1 it is 4 access slots. \n
			:param premp: integer Range: 1 to 14
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(premp)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:TIMing:TIME:PREMp {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:TIMing:TIME:PREMp \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.prach.timing.time.premp.get(mobileStation = repcap.MobileStation.Default) \n
		This command defines the AICH Transmission Timing. This parameter defines the time difference between the preamble and
		the message part. Two modes are defined in the standard. In mode 0, the preamble to message part difference is 3 access
		slots, in mode 1 it is 4 access slots. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: premp: integer Range: 1 to 14"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:TIMing:TIME:PREMp?')
		return Conversions.str_to_int(response)
