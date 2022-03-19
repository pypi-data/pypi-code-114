from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loss:
	"""Loss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loss", core, parent)

	def set(self, loss: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:LOSS \n
		Snippet: driver.source.fsimulator.birthDeath.path.loss.set(loss = 1.0, path = repcap.Path.Default) \n
		Sets the loss of the paths with birth death propagation. \n
			:param loss: float Range: 0 to 50, Unit: dB
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(loss)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:LOSS {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:LOSS \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.path.loss.get(path = repcap.Path.Default) \n
		Sets the loss of the paths with birth death propagation. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: loss: float Range: 0 to 50, Unit: dB"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:LOSS?')
		return Conversions.str_to_float(response)
