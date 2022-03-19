from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: str, bitNumberNull=repcap.BitNumberNull.Default) -> None:
		"""SCPI: STATus:OPERation:BIT<BITNR>:ENABle \n
		Snippet: driver.status.operation.bit.enable.set(enable = '1', bitNumberNull = repcap.BitNumberNull.Default) \n
		No command help available \n
			:param enable: No help available
			:param bitNumberNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bit')
		"""
		param = Conversions.value_to_quoted_str(enable)
		bitNumberNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNumberNull, repcap.BitNumberNull)
		self._core.io.write(f'STATus:OPERation:BIT{bitNumberNull_cmd_val}:ENABle {param}')

	def get(self, bitNumberNull=repcap.BitNumberNull.Default) -> str:
		"""SCPI: STATus:OPERation:BIT<BITNR>:ENABle \n
		Snippet: value: str = driver.status.operation.bit.enable.get(bitNumberNull = repcap.BitNumberNull.Default) \n
		No command help available \n
			:param bitNumberNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bit')
			:return: enable: No help available"""
		bitNumberNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNumberNull, repcap.BitNumberNull)
		response = self._core.io.query_str(f'STATus:OPERation:BIT{bitNumberNull_cmd_val}:ENABle?')
		return trim_str_response(response)
