from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdevice:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	def get(self, iqConnector=repcap.IqConnector.Default) -> str:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CDEVice \n
		Snippet: value: str = driver.source.iq.output.digital.bbmm.cdevice.get(iqConnector = repcap.IqConnector.Default) \n
		Queries information on the connected device. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: cdevice: string"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CDEVice?')
		return trim_str_response(response)
