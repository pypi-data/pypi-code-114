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

	def set(self, fp_trig_source: enums.SingExtAuto, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: TRIGger<HW>:FPSWeep:SOURce \n
		Snippet: driver.trigger.fpSweep.source.set(fp_trig_source = enums.SingExtAuto.AUTO, inputIx = repcap.InputIx.Default) \n
		Selects the trigger source for the combined RF frequency / level sweep. The parameter names correspond to the manual
		control. If needed, see table Table 'Cross-reference between the manual and remote control' for selecting the trigger
		source with SCPI compliant parameter names. \n
			:param fp_trig_source: AUTO| IMMediate | SINGle| BUS| EXTernal | EAUTo AUTO|IMMediate Executes the combined RF sweep automatically. In this free-running mode, the trigger condition is met continuously. I.e. as soon as a sweep is completed, the next one starts immediately. SINGle|BUS Executes one complete sweep cycle triggered by the GPIB commands [:SOURcehw]:SWEep:COMBined:EXECute or *TRG. The mode has to be set to [:SOURcehw]:SWEep:COMBined:MODE AUTO. EXTernal An external signal triggers the sweep. EAUTo An external signal triggers the sweep. As soon as one sweep is finished, the next sweep starts. A second trigger event stops the sweep at the current frequency and level value pairs, a third trigger event starts the trigger at the start values, and so on.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(fp_trig_source, enums.SingExtAuto)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'TRIGger{inputIx_cmd_val}:FPSWeep:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.SingExtAuto:
		"""SCPI: TRIGger<HW>:FPSWeep:SOURce \n
		Snippet: value: enums.SingExtAuto = driver.trigger.fpSweep.source.get(inputIx = repcap.InputIx.Default) \n
		Selects the trigger source for the combined RF frequency / level sweep. The parameter names correspond to the manual
		control. If needed, see table Table 'Cross-reference between the manual and remote control' for selecting the trigger
		source with SCPI compliant parameter names. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: fp_trig_source: AUTO| IMMediate | SINGle| BUS| EXTernal | EAUTo AUTO|IMMediate Executes the combined RF sweep automatically. In this free-running mode, the trigger condition is met continuously. I.e. as soon as a sweep is completed, the next one starts immediately. SINGle|BUS Executes one complete sweep cycle triggered by the GPIB commands [:SOURcehw]:SWEep:COMBined:EXECute or *TRG. The mode has to be set to [:SOURcehw]:SWEep:COMBined:MODE AUTO. EXTernal An external signal triggers the sweep. EAUTo An external signal triggers the sweep. As soon as one sweep is finished, the next sweep starts. A second trigger event stops the sweep at the current frequency and level value pairs, a third trigger event starts the trigger at the start values, and so on."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'TRIGger{inputIx_cmd_val}:FPSWeep:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SingExtAuto)
