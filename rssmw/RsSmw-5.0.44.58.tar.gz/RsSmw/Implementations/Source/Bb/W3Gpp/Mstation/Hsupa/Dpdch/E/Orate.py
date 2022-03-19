from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orate:
	"""Orate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orate", core, parent)

	def set(self, orate: enums.WcdmaSymbRateEdPdchOverallSymbRate, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPDCh:E:ORATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpdch.e.orate.set(orate = enums.WcdmaSymbRateEdPdchOverallSymbRate.D120k, mobileStation = repcap.MobileStation.Default) \n
		Sets the overall symbol rate of all the E-DPDCH channels. \n
			:param orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2X1920K| D2X960K2X1920K| D2880k| D3840k| D4800k| D5760k
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(orate, enums.WcdmaSymbRateEdPdchOverallSymbRate)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPDCh:E:ORATe {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.WcdmaSymbRateEdPdchOverallSymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPDCh:E:ORATe \n
		Snippet: value: enums.WcdmaSymbRateEdPdchOverallSymbRate = driver.source.bb.w3Gpp.mstation.hsupa.dpdch.e.orate.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the overall symbol rate of all the E-DPDCH channels. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2X1920K| D2X960K2X1920K| D2880k| D3840k| D4800k| D5760k"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPDCh:E:ORATe?')
		return Conversions.str_to_scalar_enum(response, enums.WcdmaSymbRateEdPdchOverallSymbRate)
