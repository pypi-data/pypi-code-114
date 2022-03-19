from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orate:
	"""Orate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orate", core, parent)

	def set(self, orate: enums.SymbRate, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:ORATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpdch.orate.set(orate = enums.SymbRate.D120k, mobileStation = repcap.MobileStation.Default) \n
		The command sets the overall symbol rate. The overall symbol rate determines the number of DPDCHs as well as their symbol
		rate and channelization codes. \n
			:param orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k D15K ... D5760K 15 ksps ... 6 x 960 ksps
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(orate, enums.SymbRate)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:ORATe {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPDCh:ORATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.mstation.dpdch.orate.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the overall symbol rate. The overall symbol rate determines the number of DPDCHs as well as their symbol
		rate and channelization codes. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: orate: D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k D15K ... D5760K 15 ksps ... 6 x 960 ksps"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPDCh:ORATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)
