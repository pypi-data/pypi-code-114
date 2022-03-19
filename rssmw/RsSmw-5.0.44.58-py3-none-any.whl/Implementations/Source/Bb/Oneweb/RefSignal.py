from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefSignal:
	"""RefSignal commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refSignal", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:REFSignal:CATalog \n
		Snippet: value: List[str] = driver.source.bb.oneweb.refSignal.get_catalog() \n
		Queries the available reference signals files in the default directory. Only predefined files are listed. \n
			:return: ref_sig_cata_log: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:REFSignal:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:REFSignal \n
		Snippet: value: str = driver.source.bb.oneweb.refSignal.get_value() \n
		Selects and loads a predefined reference signal. \n
			:return: ref_signal: string Filename as returned by the query [:SOURcehw]:BB:ONEWeb:REFSignal:CATalog?. File extension is omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:REFSignal?')
		return trim_str_response(response)

	def set_value(self, ref_signal: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:REFSignal \n
		Snippet: driver.source.bb.oneweb.refSignal.set_value(ref_signal = '1') \n
		Selects and loads a predefined reference signal. \n
			:param ref_signal: string Filename as returned by the query [:SOURcehw]:BB:ONEWeb:REFSignal:CATalog?. File extension is omitted.
		"""
		param = Conversions.value_to_quoted_str(ref_signal)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:REFSignal {param}')
