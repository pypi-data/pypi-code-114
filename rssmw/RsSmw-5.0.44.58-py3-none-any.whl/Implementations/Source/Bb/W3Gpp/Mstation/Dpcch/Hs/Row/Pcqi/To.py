from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class To:
	"""To commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("to", core, parent)

	def set(self, pcqi_to: int, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI:TO \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.to.set(pcqi_to = 1, mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default) \n
		(Release 8 and later) Defines the beginning / end of the PCI/CQI transmissions inside the PCI/CQI cycle. The range is
		specified in multiples of intervals (Inter-TTI distance) . \n
			:param pcqi_to: integer Range: 0 to dynamic
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(pcqi_to)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI:TO {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:PCQI:TO \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.row.pcqi.to.get(mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default) \n
		(Release 8 and later) Defines the beginning / end of the PCI/CQI transmissions inside the PCI/CQI cycle. The range is
		specified in multiples of intervals (Inter-TTI distance) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: pcqi_to: integer Range: 0 to dynamic"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:PCQI:TO?')
		return Conversions.str_to_int(response)
