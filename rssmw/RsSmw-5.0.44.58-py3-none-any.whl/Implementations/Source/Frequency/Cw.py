from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cw:
	"""Cw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cw", core, parent)

	# noinspection PyTypeChecker
	def get_recall(self) -> enums.InclExcl:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:RCL \n
		Snippet: value: enums.InclExcl = driver.source.frequency.cw.get_recall() \n
		Set whether the RF frequency value is retained or taken from a loaded instrument configuration, when you recall
		instrument settings with command *RCL. The selected mode applies to both RF paths, i.e. a specified suffix is ignored. \n
			:return: rcl: INCLude| EXCLude INCLude Takes the frequency value of the loaded settings. EXCLude Retains the current frequency when an instrument configuration is loaded.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW:RCL?')
		return Conversions.str_to_scalar_enum(response, enums.InclExcl)

	def set_recall(self, rcl: enums.InclExcl) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:RCL \n
		Snippet: driver.source.frequency.cw.set_recall(rcl = enums.InclExcl.EXCLude) \n
		Set whether the RF frequency value is retained or taken from a loaded instrument configuration, when you recall
		instrument settings with command *RCL. The selected mode applies to both RF paths, i.e. a specified suffix is ignored. \n
			:param rcl: INCLude| EXCLude INCLude Takes the frequency value of the loaded settings. EXCLude Retains the current frequency when an instrument configuration is loaded.
		"""
		param = Conversions.enum_scalar_to_str(rcl, enums.InclExcl)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW:RCL {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW] \n
		Snippet: value: float = driver.source.frequency.cw.get_value() \n
		Sets the frequency of the RF output signal in the selected path.
			INTRO_CMD_HELP: The effect depends on the selected mode: \n
			- In CW mode (FREQ:MODE CW | FIXed) , the instrument operates at a fixed frequency.
			- In sweep mode (FREQ:MODE SWE) , the value applies to the sweep frequency. The instrument processes the frequency settings in defined sweep steps.
			- In user mode (FREQ:STEP:MODE USER) , you can vary the current frequency step by step. \n
			:return: fixed: float The following settings influence the value range: An offset set with the command [:SOURcehw]:FREQuency:OFFSet Numerical value Sets the frequency in CW and sweep mode UP|DOWN Varies the frequency step by step in user mode. The frequency is increased or decreased by the value set with the command [:SOURcehw]:FREQuency:STEP[:INCRement]. Range: (RFmin + OFFSet) to (RFmax + OFFSet)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW?')
		return Conversions.str_to_float(response)

	def set_value(self, fixed: float) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW] \n
		Snippet: driver.source.frequency.cw.set_value(fixed = 1.0) \n
		Sets the frequency of the RF output signal in the selected path.
			INTRO_CMD_HELP: The effect depends on the selected mode: \n
			- In CW mode (FREQ:MODE CW | FIXed) , the instrument operates at a fixed frequency.
			- In sweep mode (FREQ:MODE SWE) , the value applies to the sweep frequency. The instrument processes the frequency settings in defined sweep steps.
			- In user mode (FREQ:STEP:MODE USER) , you can vary the current frequency step by step. \n
			:param fixed: float The following settings influence the value range: An offset set with the command [:SOURcehw]:FREQuency:OFFSet Numerical value Sets the frequency in CW and sweep mode UP|DOWN Varies the frequency step by step in user mode. The frequency is increased or decreased by the value set with the command [:SOURcehw]:FREQuency:STEP[:INCRement]. Range: (RFmin + OFFSet) to (RFmax + OFFSet)
		"""
		param = Conversions.decimal_value_to_str(fixed)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW {param}')
