from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hack:
	"""Hack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hack", core, parent)

	def set(self, hack: enums.HsMimoHarqMode, mobileStation=repcap.MobileStation.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:TTI<CH0>:HACK \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.tti.hack.set(hack = enums.HsMimoHarqMode.AACK, mobileStation = repcap.MobileStation.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Selects the information transmitted during the HARQ-ACK slot of the corresponding TTI. \n
			:param hack: DTX| SACK| SNACk| AACK| ANACk| NACK| NNACk
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
		"""
		param = Conversions.enum_scalar_to_str(hack, enums.HsMimoHarqMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:TTI{transmTimeIntervalNull_cmd_val}:HACK {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> enums.HsMimoHarqMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:TTI<CH0>:HACK \n
		Snippet: value: enums.HsMimoHarqMode = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.tti.hack.get(mobileStation = repcap.MobileStation.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Selects the information transmitted during the HARQ-ACK slot of the corresponding TTI. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
			:return: hack: DTX| SACK| SNACk| AACK| ANACk| NACK| NNACk"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:TTI{transmTimeIntervalNull_cmd_val}:HACK?')
		return Conversions.str_to_scalar_enum(response, enums.HsMimoHarqMode)
