from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, file: str, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:FILE \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.file.set(file = '1', carrier = repcap.Carrier.Default) \n
		Selects the file with I/Q data to be modulated onto the selected carrier. \n
			:param file: file name
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
		"""
		param = Conversions.value_to_quoted_str(file)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:FILE {param}')

	def get(self, carrier=repcap.Carrier.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:FILE \n
		Snippet: value: str = driver.source.bb.arbitrary.mcarrier.carrier.file.get(carrier = repcap.Carrier.Default) \n
		Selects the file with I/Q data to be modulated onto the selected carrier. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
			:return: file: file name"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:FILE?')
		return trim_str_response(response)
