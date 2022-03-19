from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pwr:
	"""Pwr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pwr", core, parent)

	def set(self, power: float, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:PWR \n
		Snippet: driver.source.bb.ofdm.user.pwr.set(power = 1.0, userNull = repcap.UserNull.Default) \n
		Applies a power offset. \n
			:param power: float Range: -80 to 10
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(power)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:PWR {param}')

	def get(self, userNull=repcap.UserNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:PWR \n
		Snippet: value: float = driver.source.bb.ofdm.user.pwr.get(userNull = repcap.UserNull.Default) \n
		Applies a power offset. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: power: float Range: -80 to 10"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:PWR?')
		return Conversions.str_to_float(response)
