from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstep:
	"""Pstep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstep", core, parent)

	def set(self, pstep: float, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:PSTep \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.pstep.set(pstep = 1.0, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command defines the step width for the change of channel powers in the case of 'mis-' use of the TPC field. \n
			:param pstep: float Range: -10.0 dB to 10.0 dB
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(pstep)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:PSTep {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:PSTep \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.pstep.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command defines the step width for the change of channel powers in the case of 'mis-' use of the TPC field. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: pstep: float Range: -10.0 dB to 10.0 dB"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:PSTep?')
		return Conversions.str_to_float(response)
