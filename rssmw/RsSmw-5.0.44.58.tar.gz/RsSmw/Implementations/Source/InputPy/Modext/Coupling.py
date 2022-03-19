from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: InputIx, default value after init: InputIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_inputIx_get', 'repcap_inputIx_set', repcap.InputIx.Nr1)

	def repcap_inputIx_set(self, inputIx: repcap.InputIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputIx.Default
		Default value after init: InputIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(inputIx)

	def repcap_inputIx_get(self) -> repcap.InputIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, coupling: enums.AcDc, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:INPut:MODext:COUPling<CH> \n
		Snippet: driver.source.inputPy.modext.coupling.set(coupling = enums.AcDc.AC, inputIx = repcap.InputIx.Default) \n
		Selects the coupling mode for an externally applied modulation signal. \n
			:param coupling: AC| DC AC Passes the AC signal component of the modulation signal. DC Passes the modulation signal with both components, AC and DC.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coupling')
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.AcDc)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SOURce<HwInstance>:INPut:MODext:COUPling{inputIx_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.AcDc:
		"""SCPI: [SOURce<HW>]:INPut:MODext:COUPling<CH> \n
		Snippet: value: enums.AcDc = driver.source.inputPy.modext.coupling.get(inputIx = repcap.InputIx.Default) \n
		Selects the coupling mode for an externally applied modulation signal. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coupling')
			:return: coupling: AC| DC AC Passes the AC signal component of the modulation signal. DC Passes the modulation signal with both components, AC and DC."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:INPut:MODext:COUPling{inputIx_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.AcDc)

	def clone(self) -> 'Coupling':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Coupling(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
