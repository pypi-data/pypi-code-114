from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, plength: enums.PowPreContLen, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:PLENgth \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.plength.set(plength = enums.PowPreContLen.S0, mobileStation = repcap.MobileStation.Default) \n
		The command defines the length of the power control preamble of the PCPCH as a number of slots. \n
			:param plength: S0| S8
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(plength, enums.PowPreContLen)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:PLENgth {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.PowPreContLen:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:PLENgth \n
		Snippet: value: enums.PowPreContLen = driver.source.bb.w3Gpp.mstation.pcpch.plength.get(mobileStation = repcap.MobileStation.Default) \n
		The command defines the length of the power control preamble of the PCPCH as a number of slots. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: plength: S0| S8"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:PLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.PowPreContLen)
