from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.Cdma2KcodMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CCODing:MODE \n
		Snippet: driver.source.bb.c2K.mstation.ccoding.mode.set(mode = enums.Cdma2KcodMode.COMPlete, mobileStation = repcap.MobileStation.Default) \n
		The command selects the channel coding mode. \n
			:param mode: OFF| COMPlete| NOINterleaving| OINTerleaving OFF Channel coding is deactivated. COMPlete The complete channel coding is performed. The channel coding procedure can slightly vary depending on channel type, frame length and data rate. OINTerleaving Except for the block interleaver, the whole channel coding procedure is carried out. NOINterleaving In this mode, only block interleaver is used for coding.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KcodMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CCODing:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.Cdma2KcodMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CCODing:MODE \n
		Snippet: value: enums.Cdma2KcodMode = driver.source.bb.c2K.mstation.ccoding.mode.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the channel coding mode. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mode: OFF| COMPlete| NOINterleaving| OINTerleaving OFF Channel coding is deactivated. COMPlete The complete channel coding is performed. The channel coding procedure can slightly vary depending on channel type, frame length and data rate. OINTerleaving Except for the block interleaver, the whole channel coding procedure is carried out. NOINterleaving In this mode, only block interleaver is used for coding."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CCODing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KcodMode)
