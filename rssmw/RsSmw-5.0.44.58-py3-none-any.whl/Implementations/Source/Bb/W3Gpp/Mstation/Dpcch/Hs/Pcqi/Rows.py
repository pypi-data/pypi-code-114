from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rows:
	"""Rows commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rows", core, parent)

	def set(self, row_count: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:PCQI:ROWS \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.pcqi.rows.set(row_count = 1, mobileStation = repcap.MobileStation.Default) \n
		Determines the number of the rows in the HARQ-ACK respectively in the PCI/CQI scheduling table. \n
			:param row_count: integer Range: 1 to 32
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(row_count)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:PCQI:ROWS {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:PCQI:ROWS \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.pcqi.rows.get(mobileStation = repcap.MobileStation.Default) \n
		Determines the number of the rows in the HARQ-ACK respectively in the PCI/CQI scheduling table. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: row_count: integer Range: 1 to 32"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:PCQI:ROWS?')
		return Conversions.str_to_int(response)
