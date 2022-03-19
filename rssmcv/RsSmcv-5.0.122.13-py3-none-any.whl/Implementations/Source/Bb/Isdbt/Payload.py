from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Payload:
	"""Payload commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("payload", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PAYLoad:A \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.isdbt.payload.get_a() \n
		Defines the payload area content of the packet. \n
			:return: payload: HFF| H00| PRBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:PAYLoad:A?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_a(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PAYLoad:A \n
		Snippet: driver.source.bb.isdbt.payload.set_a(payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param payload: HFF| H00| PRBS
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:PAYLoad:A {param}')
