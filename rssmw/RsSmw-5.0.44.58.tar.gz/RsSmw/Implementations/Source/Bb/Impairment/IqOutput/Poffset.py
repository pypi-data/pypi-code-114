from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, phase_offset: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:IQOutput<CH>:POFFset \n
		Snippet: driver.source.bb.impairment.iqOutput.poffset.set(phase_offset = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Adds an additional phase offset after the stream mapper.
			INTRO_CMD_HELP: You can shift the phase at the different stages in the signal generation flow, see: \n
			- [:SOURce<hw>]:BB:POFFset
			- method RsSmw.Sconfiguration.Output.Mapping.Stream.Poffset.set \n
			:param phase_offset: float Range: -999.99 to 999.99
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IqOutput')
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:BB:IMPairment:IQOutput{iqConnector_cmd_val}:POFFset {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:IQOutput<CH>:POFFset \n
		Snippet: value: float = driver.source.bb.impairment.iqOutput.poffset.get(iqConnector = repcap.IqConnector.Default) \n
		Adds an additional phase offset after the stream mapper.
			INTRO_CMD_HELP: You can shift the phase at the different stages in the signal generation flow, see: \n
			- [:SOURce<hw>]:BB:POFFset
			- method RsSmw.Sconfiguration.Output.Mapping.Stream.Poffset.set \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IqOutput')
			:return: phase_offset: float Range: -999.99 to 999.99"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:IQOutput{iqConnector_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
