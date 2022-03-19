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

	def set(self, mode: enums.SystConfOutpMapMatMode, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:BBMM<CH>:CHANnel:MODE \n
		Snippet: driver.sconfiguration.output.mapping.bbmm.channel.mode.set(mode = enums.SystConfOutpMapMatMode.ADD, iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param mode: No help available
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMapMatMode)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:BBMM{iqConnector_cmd_val}:CHANnel:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.SystConfOutpMapMatMode:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:BBMM<CH>:CHANnel:MODE \n
		Snippet: value: enums.SystConfOutpMapMatMode = driver.sconfiguration.output.mapping.bbmm.channel.mode.get(iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: mode: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:BBMM{iqConnector_cmd_val}:CHANnel:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMapMatMode)
