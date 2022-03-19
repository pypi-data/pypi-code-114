from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, auto_config_state: enums.AutoManualMode, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:CONFig \n
		Snippet: driver.source.bb.gnss.awgn.rf.config.set(auto_config_state = enums.AutoManualMode.AUTO, path = repcap.Path.Default) \n
		Defines how noise bandwidth and noise center frequency are set. \n
			:param auto_config_state: AUTO| MANual AUTO Sets bandwidth and center frequency automatically. MANual Enables configuration of noise and CW parameters.
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.enum_scalar_to_str(auto_config_state, enums.AutoManualMode)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:CONFig {param}')

	# noinspection PyTypeChecker
	def get(self, path=repcap.Path.Default) -> enums.AutoManualMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:CONFig \n
		Snippet: value: enums.AutoManualMode = driver.source.bb.gnss.awgn.rf.config.get(path = repcap.Path.Default) \n
		Defines how noise bandwidth and noise center frequency are set. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: auto_config_state: AUTO| MANual AUTO Sets bandwidth and center frequency automatically. MANual Enables configuration of noise and CW parameters."""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
