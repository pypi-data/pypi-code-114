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

	def set(self, awgn_mode: enums.NoisAwgnMode, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:MODE \n
		Snippet: driver.source.bb.gnss.awgn.rf.mode.set(awgn_mode = enums.NoisAwgnMode.ADD, path = repcap.Path.Default) \n
		Activates/deactivates the generation of an AWGN signal. The interferer (AWGN or CW interferer, depending on the selected
		mode) is generated after the generator is activated. \n
			:param awgn_mode: ADD| CW
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.enum_scalar_to_str(awgn_mode, enums.NoisAwgnMode)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, path=repcap.Path.Default) -> enums.NoisAwgnMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:MODE \n
		Snippet: value: enums.NoisAwgnMode = driver.source.bb.gnss.awgn.rf.mode.get(path = repcap.Path.Default) \n
		Activates/deactivates the generation of an AWGN signal. The interferer (AWGN or CW interferer, depending on the selected
		mode) is generated after the generator is activated. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: awgn_mode: ADD| CW"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NoisAwgnMode)
