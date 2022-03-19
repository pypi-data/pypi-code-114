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

	def set(self, mode: enums.FadMimoMatMode, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:MODE \n
		Snippet: driver.source.fsimulator.mimo.tap.matrix.mode.set(mode = enums.FadMimoMatMode.AOAaod, mimoTap = repcap.MimoTap.Default) \n
		Sets the input mode for the Rx and Tx correlation values (matrix mode) . \n
			:param mode: INDividual| KRONecker| AOAaod | SCWI
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadMimoMatMode)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mimoTap=repcap.MimoTap.Default) -> enums.FadMimoMatMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:MODE \n
		Snippet: value: enums.FadMimoMatMode = driver.source.fsimulator.mimo.tap.matrix.mode.get(mimoTap = repcap.MimoTap.Default) \n
		Sets the input mode for the Rx and Tx correlation values (matrix mode) . \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: mode: INDividual| KRONecker| AOAaod | SCWI"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadMimoMatMode)
