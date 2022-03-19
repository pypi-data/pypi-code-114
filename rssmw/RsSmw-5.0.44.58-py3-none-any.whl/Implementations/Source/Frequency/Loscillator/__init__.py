from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loscillator:
	"""Loscillator commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loscillator", core, parent)

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LoModeW:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:MODE \n
		Snippet: value: enums.LoModeW = driver.source.frequency.loscillator.get_mode() \n
		Selects the mode of the local oscillator coupling. Cross-reference between <Mode> and the manual operation
			Table Header: <Mode> / Parameter in manual operation / Description \n
			- INTernal / A&B Internal / Internal (one path instrument) / Uses the internal oscillator signal in both paths.
			- EXTernal / A External & B Internal (one path instrument) / Uses an external signal in path A. B uses its internal signal.
			- COUPled / A Internal & A->B Coupled / Assigns the internal oscillator signal of path A also to path B.
			- ECOupled / A External & A->B Coupled / Assigns an externally supplied signal to both paths.
			- BOFF / A Internal & B RF Off / Uses the internal local oscillator signal of path A, if the selected frequency exceeds the maximum frequency of path B.
			- EBOFf / A External & B RF Off / Uses the LO IN signal for path A, if the selected RF frequency exceeds the maximum frequency of path B.
			- AOFF / A RF Off & B External / Uses the LO IN signal for path B, if the selected RF frequency exceeds the maximum frequency of path A. \n
			:return: mode: INTernal| EXTernal| COUPled| ECOupled| BOFF| AOFF See Table 'Cross-reference between Mode and the manual operation'
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:LOSCillator:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LoModeW)

	def set_mode(self, mode: enums.LoModeW) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:MODE \n
		Snippet: driver.source.frequency.loscillator.set_mode(mode = enums.LoModeW.AOFF) \n
		Selects the mode of the local oscillator coupling. Cross-reference between <Mode> and the manual operation
			Table Header: <Mode> / Parameter in manual operation / Description \n
			- INTernal / A&B Internal / Internal (one path instrument) / Uses the internal oscillator signal in both paths.
			- EXTernal / A External & B Internal (one path instrument) / Uses an external signal in path A. B uses its internal signal.
			- COUPled / A Internal & A->B Coupled / Assigns the internal oscillator signal of path A also to path B.
			- ECOupled / A External & A->B Coupled / Assigns an externally supplied signal to both paths.
			- BOFF / A Internal & B RF Off / Uses the internal local oscillator signal of path A, if the selected frequency exceeds the maximum frequency of path B.
			- EBOFf / A External & B RF Off / Uses the LO IN signal for path A, if the selected RF frequency exceeds the maximum frequency of path B.
			- AOFF / A RF Off & B External / Uses the LO IN signal for path B, if the selected RF frequency exceeds the maximum frequency of path A. \n
			:param mode: INTernal| EXTernal| COUPled| ECOupled| BOFF| AOFF See Table 'Cross-reference between Mode and the manual operation'
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LoModeW)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:LOSCillator:MODE {param}')

	def clone(self) -> 'Loscillator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Loscillator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
