from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiType:
	"""CqiType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqiType", core, parent)

	def set(self, cqi_type: enums.HsMimoCqiType, mobileStation=repcap.MobileStation.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:TTI<CH0>:CQIType \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.tti.cqiType.set(cqi_type = enums.HsMimoCqiType.TADT, mobileStation = repcap.MobileStation.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Selects the type of the CQI report. \n
			:param cqi_type: TAST| TADT| TB
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
		"""
		param = Conversions.enum_scalar_to_str(cqi_type, enums.HsMimoCqiType)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:TTI{transmTimeIntervalNull_cmd_val}:CQIType {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> enums.HsMimoCqiType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MIMO:TTI<CH0>:CQIType \n
		Snippet: value: enums.HsMimoCqiType = driver.source.bb.w3Gpp.mstation.dpcch.hs.mimo.tti.cqiType.get(mobileStation = repcap.MobileStation.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Selects the type of the CQI report. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
			:return: cqi_type: TAST| TADT| TB"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MIMO:TTI{transmTimeIntervalNull_cmd_val}:CQIType?')
		return Conversions.str_to_scalar_enum(response, enums.HsMimoCqiType)
