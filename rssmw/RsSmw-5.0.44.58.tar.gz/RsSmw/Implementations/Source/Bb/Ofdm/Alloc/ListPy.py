from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def set(self, data_list: str, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:LIST \n
		Snippet: driver.source.bb.ofdm.alloc.listPy.set(data_list = '1', allocationNull = repcap.AllocationNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param data_list: string file name incl. file extension or complete file path
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.value_to_quoted_str(data_list)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:LIST {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:LIST \n
		Snippet: value: str = driver.source.bb.ofdm.alloc.listPy.get(allocationNull = repcap.AllocationNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: data_list: string file name incl. file extension or complete file path"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:LIST?')
		return trim_str_response(response)
