from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcio:
	"""Fcio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcio", core, parent)

	def set(self, fcio: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:FCIO \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpdch.fcio.set(fcio = False, mobileStation = repcap.MobileStation.Default) \n
		The command sets the channelization code to I/0. This mode can only be activated if the overall symbol rate is < 2 x 960
		kbps. \n
			:param fcio: ON| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(fcio)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:FCIO {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:FCIO \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.dpdch.fcio.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the channelization code to I/0. This mode can only be activated if the overall symbol rate is < 2 x 960
		kbps. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: fcio: ON| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:FCIO?')
		return Conversions.str_to_bool(response)
