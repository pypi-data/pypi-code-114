from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Method:
	"""Method commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("method", core, parent)

	def set(self, method: enums.CmMethUp, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:METHod \n
		Snippet: driver.source.bb.w3Gpp.mstation.cmode.method.set(method = enums.CmMethUp.HLSCheduling, mobileStation = repcap.MobileStation.Default) \n
		The command selects compressed mode method. \n
			:param method: HLSCheduling| SF2 SF2 The data is compressed by halving the spreading factor. HLSCheduling The data is compressed by stopping the transmission of the data stream during the transmission gap.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(method, enums.CmMethUp)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:METHod {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.CmMethUp:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:METHod \n
		Snippet: value: enums.CmMethUp = driver.source.bb.w3Gpp.mstation.cmode.method.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects compressed mode method. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: method: HLSCheduling| SF2 SF2 The data is compressed by halving the spreading factor. HLSCheduling The data is compressed by stopping the transmission of the data stream during the transmission gap."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.CmMethUp)
