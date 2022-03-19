from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.FbiMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:FBI:MODE \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.fbi.mode.set(mode = enums.FbiMode.D1B, mobileStation = repcap.MobileStation.Default) \n
		The command sets the number of bits (1 or 2) for the FBI field. With OFF, the field is not used.
			INTRO_CMD_HELP: The FBI pattern automatically sets the associated slot format: \n
			- FBI OFF = Slot format 0
			- FBI 1 bit = Slot format 1
			- FBI 2 bits = Slot format 2 \n
			:param mode: OFF| D1B| D2B
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FbiMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:FBI:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.FbiMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:FBI:MODE \n
		Snippet: value: enums.FbiMode = driver.source.bb.w3Gpp.mstation.pcpch.fbi.mode.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the number of bits (1 or 2) for the FBI field. With OFF, the field is not used.
			INTRO_CMD_HELP: The FBI pattern automatically sets the associated slot format: \n
			- FBI OFF = Slot format 0
			- FBI 1 bit = Slot format 1
			- FBI 2 bits = Slot format 2 \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mode: OFF| D1B| D2B"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:FBI:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FbiMode)
