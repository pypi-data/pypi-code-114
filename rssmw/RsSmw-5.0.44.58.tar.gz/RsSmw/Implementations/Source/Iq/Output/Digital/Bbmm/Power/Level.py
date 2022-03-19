from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:LEVel \n
		Snippet: driver.source.iq.output.digital.bbmm.power.level.set(level = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Enters the RMS level of the output signal. \n
			:param level: float Range: -80 to 0
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.decimal_value_to_str(level)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:LEVel {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:LEVel \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.power.level.get(iqConnector = repcap.IqConnector.Default) \n
		Enters the RMS level of the output signal. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: level: float Range: -80 to 0"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:LEVel?')
		return Conversions.str_to_float(response)
