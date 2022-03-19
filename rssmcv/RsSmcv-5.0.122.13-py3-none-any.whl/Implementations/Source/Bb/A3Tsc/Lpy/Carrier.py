from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	def get_mode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:CARRier:MODE \n
		Snippet: value: int = driver.source.bb.a3Tsc.lpy.carrier.get_mode() \n
		Sets a coefficient for reducing the maximum number of carriers. \n
			:return: red_carr_mode_pre: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:CARRier:MODE?')
		return Conversions.str_to_int(response)

	def set_mode(self, red_carr_mode_pre: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:CARRier:MODE \n
		Snippet: driver.source.bb.a3Tsc.lpy.carrier.set_mode(red_carr_mode_pre = 1) \n
		Sets a coefficient for reducing the maximum number of carriers. \n
			:param red_carr_mode_pre: integer Range: 0 to 4
		"""
		param = Conversions.decimal_value_to_str(red_carr_mode_pre)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:L:CARRier:MODE {param}')
