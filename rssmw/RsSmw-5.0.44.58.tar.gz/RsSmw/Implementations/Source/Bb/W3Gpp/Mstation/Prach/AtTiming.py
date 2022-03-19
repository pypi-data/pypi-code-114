from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtTiming:
	"""AtTiming commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atTiming", core, parent)

	def set(self, at_timing: enums.AichTranTim, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:ATTiming \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.atTiming.set(at_timing = enums.AichTranTim.ATT0, mobileStation = repcap.MobileStation.Default) \n
		This command defines which AICH Transmission Timing, time difference between the preamble and the message part or the
		time difference between two successive preambles in access slots, is defined. \n
			:param at_timing: ATT0| ATT1
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(at_timing, enums.AichTranTim)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:ATTiming {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.AichTranTim:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:ATTiming \n
		Snippet: value: enums.AichTranTim = driver.source.bb.w3Gpp.mstation.prach.atTiming.get(mobileStation = repcap.MobileStation.Default) \n
		This command defines which AICH Transmission Timing, time difference between the preamble and the message part or the
		time difference between two successive preambles in access slots, is defined. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: at_timing: ATT0| ATT1"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:ATTiming?')
		return Conversions.str_to_scalar_enum(response, enums.AichTranTim)
