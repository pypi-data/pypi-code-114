from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttiedch:
	"""Ttiedch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttiedch", core, parent)

	def set(self, ttiedch: enums.HsUpaDchTti, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPDCh:E:TTIEdch \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpdch.e.ttiedch.set(ttiedch = enums.HsUpaDchTti._10ms, mobileStation = repcap.MobileStation.Default) \n
		The command sets the value for the TTI (Transmission Time Interval) . \n
			:param ttiedch: 2ms| 10ms
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(ttiedch, enums.HsUpaDchTti)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPDCh:E:TTIEdch {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsUpaDchTti:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPDCh:E:TTIEdch \n
		Snippet: value: enums.HsUpaDchTti = driver.source.bb.w3Gpp.mstation.hsupa.dpdch.e.ttiedch.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the value for the TTI (Transmission Time Interval) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: ttiedch: 2ms| 10ms"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPDCh:E:TTIEdch?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaDchTti)
