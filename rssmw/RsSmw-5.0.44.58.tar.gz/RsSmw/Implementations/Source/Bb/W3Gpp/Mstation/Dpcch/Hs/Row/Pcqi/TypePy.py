from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, cqi_type: enums.HsRel8CqiType, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI<DI>:TYPE \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.typePy.set(cqi_type = enums.HsRel8CqiType.CCQI, mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		Selects the type of the PCI/CQI report. \n
			:param cqi_type: DTX| CQI| TAST| TADT| TB| CCQI TAST|TADT Type A Single TB, Type A Double TB TB Type B CCQI Composite CQI
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcqi')
		"""
		param = Conversions.enum_scalar_to_str(cqi_type, enums.HsRel8CqiType)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI{channelQualId_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> enums.HsRel8CqiType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI<DI>:TYPE \n
		Snippet: value: enums.HsRel8CqiType = driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.typePy.get(mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		Selects the type of the PCI/CQI report. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcqi')
			:return: cqi_type: DTX| CQI| TAST| TADT| TB| CCQI TAST|TADT Type A Single TB, Type A Double TB TB Type B CCQI Composite CQI"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI{channelQualId_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.HsRel8CqiType)
