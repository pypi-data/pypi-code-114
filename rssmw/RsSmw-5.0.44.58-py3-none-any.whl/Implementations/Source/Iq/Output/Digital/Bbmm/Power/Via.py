from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Via:
	"""Via commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("via", core, parent)

	def set(self, via: enums.IqOutDispViaType, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:VIA \n
		Snippet: driver.source.iq.output.digital.bbmm.power.via.set(via = enums.IqOutDispViaType.LEVel, iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param via: PEP| LEVel
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.enum_scalar_to_str(via, enums.IqOutDispViaType)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:VIA {param}')

	# noinspection PyTypeChecker
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.IqOutDispViaType:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:VIA \n
		Snippet: value: enums.IqOutDispViaType = driver.source.iq.output.digital.bbmm.power.via.get(iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: via: PEP| LEVel"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:VIA?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutDispViaType)
