from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Misuse:
	"""Misuse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("misuse", core, parent)

	def set(self, misuse: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:MISuse \n
		Snippet: driver.source.bb.c2K.mstation.tpc.misuse.set(misuse = False, mobileStation = repcap.MobileStation.Default) \n
		The command activates/deactives the use of the power control data for controlling the mobile station output power. On the
		uplink, the power control bits are used exclusively for controlling the mobile station output power. Power control
		puncturing is not defined for controlling the base station power. The bit pattern (see commands BB:C2K:MSTation<n>:TPC...
		) of the power control bits w is used to control the channel power. A '1' leads to an increase of channel powers, a '0'
		to a reduction of channel powers. Channel power is limited to the range 0 dB to -80 dB. The step width of the change is
		defined with the command [:SOURce<hw>]:BB:C2K:MSTation<st>:TPC:PSTep. \n
			:param misuse: 1| ON| 0| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(misuse)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:MISuse {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:MISuse \n
		Snippet: value: bool = driver.source.bb.c2K.mstation.tpc.misuse.get(mobileStation = repcap.MobileStation.Default) \n
		The command activates/deactives the use of the power control data for controlling the mobile station output power. On the
		uplink, the power control bits are used exclusively for controlling the mobile station output power. Power control
		puncturing is not defined for controlling the base station power. The bit pattern (see commands BB:C2K:MSTation<n>:TPC...
		) of the power control bits w is used to control the channel power. A '1' leads to an increase of channel powers, a '0'
		to a reduction of channel powers. Channel power is limited to the range 0 dB to -80 dB. The step width of the change is
		defined with the command [:SOURce<hw>]:BB:C2K:MSTation<st>:TPC:PSTep. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: misuse: 1| ON| 0| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:MISuse?')
		return Conversions.str_to_bool(response)
