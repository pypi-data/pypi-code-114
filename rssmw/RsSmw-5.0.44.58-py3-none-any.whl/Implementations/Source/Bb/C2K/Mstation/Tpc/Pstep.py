from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstep:
	"""Pstep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstep", core, parent)

	def set(self, pstep: float, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:PSTep \n
		Snippet: driver.source.bb.c2K.mstation.tpc.pstep.set(pstep = 1.0, mobileStation = repcap.MobileStation.Default) \n
		The command defines the step width for the change of channel powers in the case of 'mis-' use of the power control bits. \n
			:param pstep: float Range: -10 to 10 dB
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(pstep)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:PSTep {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:PSTep \n
		Snippet: value: float = driver.source.bb.c2K.mstation.tpc.pstep.get(mobileStation = repcap.MobileStation.Default) \n
		The command defines the step width for the change of channel powers in the case of 'mis-' use of the power control bits. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: pstep: float Range: -10 to 10 dB"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:PSTep?')
		return Conversions.str_to_float(response)
