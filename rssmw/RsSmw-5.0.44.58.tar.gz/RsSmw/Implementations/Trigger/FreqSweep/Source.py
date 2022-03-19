from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.SingExtAuto, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: TRIGger<HW>:FSWeep:SOURce \n
		Snippet: driver.trigger.freqSweep.source.set(source = enums.SingExtAuto.AUTO, inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Selects the trigger source for the corresponding sweeps: \n
			- FSWeep - RF frequency
			- LFFSweep - LF frequency
			- PSWeep - RF level
			- SWEep - all sweeps
		The source names of the parameters correspond to the values provided in manual control of the instrument. They differ
		from the SCPI-compliant names, but the instrument accepts both variants. Use the SCPI name, if compatibility is an
		important issue. Find the corresponding SCPI-compliant commands in Cross-reference between the manual and remote control. \n
			:param source: AUTO| IMMediate | SINGle| BUS | EXTernal | EAUTo AUTO [IMMediate] Executes a sweep automatically. In this free-running mode, the trigger condition is met continuously. I.e. when a sweep is completed, the next one starts immediately. SINGle [BUS] Executes one complete sweep cycle. The following commands initiate a trigger event: *TRG [:SOURcehw]:SWEep:POWer:EXECute [:SOURcehw]:SWEep[:FREQuency]:EXECute method RsSmw.Trigger.Sweep.Immediate.set, method RsSmw.Trigger.Psweep.Immediate.set and method RsSmw.Trigger.FreqSweep.Immediate.set. Set the sweep mode with the commands: [:SOURcehw]:SWEep:POWer:MODEAUTO|STEP [:SOURcehw]:SWEep[:FREQuency]:MODEAUTO|STEP [:SOURcehw]:LFOutput:SWEep[:FREQuency]:MODEAUTO|STEP In step mode (STEP) , the instrument executes only one step. EXTernal An external signal triggers the sweep. EAUTo An external signal triggers the sweep. When one sweep is finished, the next sweep starts. A second trigger event stops the sweep at the current frequency, a third trigger event starts the trigger at the start frequency, and so on.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SingExtAuto)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'TRIGger{inputIx_cmd_val}:FSWeep:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.SingExtAuto:
		"""SCPI: TRIGger<HW>:FSWeep:SOURce \n
		Snippet: value: enums.SingExtAuto = driver.trigger.freqSweep.source.get(inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Selects the trigger source for the corresponding sweeps: \n
			- FSWeep - RF frequency
			- LFFSweep - LF frequency
			- PSWeep - RF level
			- SWEep - all sweeps
		The source names of the parameters correspond to the values provided in manual control of the instrument. They differ
		from the SCPI-compliant names, but the instrument accepts both variants. Use the SCPI name, if compatibility is an
		important issue. Find the corresponding SCPI-compliant commands in Cross-reference between the manual and remote control. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: source: AUTO| IMMediate | SINGle| BUS | EXTernal | EAUTo AUTO [IMMediate] Executes a sweep automatically. In this free-running mode, the trigger condition is met continuously. I.e. when a sweep is completed, the next one starts immediately. SINGle [BUS] Executes one complete sweep cycle. The following commands initiate a trigger event: *TRG [:SOURcehw]:SWEep:POWer:EXECute [:SOURcehw]:SWEep[:FREQuency]:EXECute method RsSmw.Trigger.Sweep.Immediate.set, method RsSmw.Trigger.Psweep.Immediate.set and method RsSmw.Trigger.FreqSweep.Immediate.set. Set the sweep mode with the commands: [:SOURcehw]:SWEep:POWer:MODEAUTO|STEP [:SOURcehw]:SWEep[:FREQuency]:MODEAUTO|STEP [:SOURcehw]:LFOutput:SWEep[:FREQuency]:MODEAUTO|STEP In step mode (STEP) , the instrument executes only one step. EXTernal An external signal triggers the sweep. EAUTo An external signal triggers the sweep. When one sweep is finished, the next sweep starts. A second trigger event stops the sweep at the current frequency, a third trigger event starts the trigger at the start frequency, and so on."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'TRIGger{inputIx_cmd_val}:FSWeep:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SingExtAuto)
