from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, srate: enums.SymbRate, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:SRATe \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.symbolRate.set(srate = enums.SymbRate.D120k, mobileStation = repcap.MobileStation.Default) \n
		The command sets the symbol rate of the PRACH. A change of symbol rate leads to an automatic change of slot format
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:PRACh:SFORmat. \n
			:param srate: D15K| D30K| D60K| D120k
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(srate, enums.SymbRate)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:SRATe {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:SRATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.mstation.prach.symbolRate.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the symbol rate of the PRACH. A change of symbol rate leads to an automatic change of slot format
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:PRACh:SFORmat. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: srate: D15K| D30K| D60K| D120k"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)
