from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pon:
	"""Pon commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pon", core, parent)

	def set(self, pon: enums.UnchOff, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:PON \n
		Snippet: driver.source.iq.output.digital.bbmm.pon.set(pon = enums.UnchOff.OFF, iqConnector = repcap.IqConnector.Default) \n
		Sets the power-on state of the selected digital I/Q output. \n
			:param pon: OFF| UNCHanged
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.enum_scalar_to_str(pon, enums.UnchOff)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:PON {param}')

	# noinspection PyTypeChecker
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.UnchOff:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:PON \n
		Snippet: value: enums.UnchOff = driver.source.iq.output.digital.bbmm.pon.get(iqConnector = repcap.IqConnector.Default) \n
		Sets the power-on state of the selected digital I/Q output. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: pon: OFF| UNCHanged"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:PON?')
		return Conversions.str_to_scalar_enum(response, enums.UnchOff)
