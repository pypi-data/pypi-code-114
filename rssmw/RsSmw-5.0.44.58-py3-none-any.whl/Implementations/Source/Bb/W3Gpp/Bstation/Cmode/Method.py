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

	def set(self, method: enums.CmMethDn, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:METHod \n
		Snippet: driver.source.bb.w3Gpp.bstation.cmode.method.set(method = enums.CmMethDn.HLSCheduling, baseStation = repcap.BaseStation.Default) \n
		The command selects compressed mode method. \n
			:param method: PUNCturing| HLSCheduling| SF2 PUNCturing The data is compressed by reducing error protection. HLSCheduling The data is compressed by stopping the transmission of the data stream during the transmission gap. SF2 The data is compressed by halving the spreading factor.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(method, enums.CmMethDn)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:METHod {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.CmMethDn:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:METHod \n
		Snippet: value: enums.CmMethDn = driver.source.bb.w3Gpp.bstation.cmode.method.get(baseStation = repcap.BaseStation.Default) \n
		The command selects compressed mode method. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: method: PUNCturing| HLSCheduling| SF2 PUNCturing The data is compressed by reducing error protection. HLSCheduling The data is compressed by stopping the transmission of the data stream during the transmission gap. SF2 The data is compressed by halving the spreading factor."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.CmMethDn)
