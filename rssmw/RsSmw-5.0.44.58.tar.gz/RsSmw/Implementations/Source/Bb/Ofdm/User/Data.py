from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data_source: enums.DataSourceA, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:DATA \n
		Snippet: driver.source.bb.ofdm.user.data.set(data_source = enums.DataSourceA.DLISt, userNull = repcap.UserNull.Default) \n
		Sets the data source per user. \n
			:param data_source: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(data_source, enums.DataSourceA)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.ofdm.user.data.get(userNull = repcap.UserNull.Default) \n
		Sets the data source per user. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: data_source: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)
