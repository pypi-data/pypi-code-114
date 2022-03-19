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

	def set(self, phase_offset: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:POFFset \n
		Snippet: driver.source.bb.impairment.rf.poffset.set(phase_offset = 1.0, path = repcap.Path.Default) \n
		Adds an additional phase offset after the stream mapper.
			INTRO_CMD_HELP: You can shift the phase at the different stages in the signal generation flow, see: \n
			- [:SOURce<hw>]:BB:POFFset
			- method RsSmw.Sconfiguration.Output.Mapping.Stream.Poffset.set \n
			:param phase_offset: float Range: -999.99 to 999.99
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce:BB:IMPairment:RF{path_cmd_val}:POFFset {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:POFFset \n
		Snippet: value: float = driver.source.bb.impairment.rf.poffset.get(path = repcap.Path.Default) \n
		Adds an additional phase offset after the stream mapper.
			INTRO_CMD_HELP: You can shift the phase at the different stages in the signal generation flow, see: \n
			- [:SOURce<hw>]:BB:POFFset
			- method RsSmw.Sconfiguration.Output.Mapping.Stream.Poffset.set \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: phase_offset: float Range: -999.99 to 999.99"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:RF{path_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
