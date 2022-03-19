from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impedance:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: InputIx, default value after init: InputIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)
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

	def set(self, impedance: enums.ImpG50High, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:INPut:MODext:IMPedance<CH> \n
		Snippet: driver.source.inputPy.modext.impedance.set(impedance = enums.ImpG50High.G50, inputIx = repcap.InputIx.Default) \n
		Sets the impedance (50 kOhm or High = 100 kOhm to ground) for the externally supplied modulation signal. \n
			:param impedance: G50| HIGH
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Impedance')
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.ImpG50High)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SOURce<HwInstance>:INPut:MODext:IMPedance{inputIx_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.ImpG50High:
		"""SCPI: [SOURce<HW>]:INPut:MODext:IMPedance<CH> \n
		Snippet: value: enums.ImpG50High = driver.source.inputPy.modext.impedance.get(inputIx = repcap.InputIx.Default) \n
		Sets the impedance (50 kOhm or High = 100 kOhm to ground) for the externally supplied modulation signal. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Impedance')
			:return: impedance: G50| HIGH"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:INPut:MODext:IMPedance{inputIx_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.ImpG50High)

	def clone(self) -> 'Impedance':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impedance(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
