from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iip:
	"""Iip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iip", core, parent)

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:IIP:PID \n
		Snippet: value: int = driver.source.bb.isdbt.iip.get_pid() \n
		Defines the for packets, that contain ISDB-T initialization packet (IIP) data. \n
			:return: iip_pid: integer Range: #H0000 to #H1FFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:IIP:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, iip_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:IIP:PID \n
		Snippet: driver.source.bb.isdbt.iip.set_pid(iip_pid = 1) \n
		Defines the for packets, that contain ISDB-T initialization packet (IIP) data. \n
			:param iip_pid: integer Range: #H0000 to #H1FFF
		"""
		param = Conversions.decimal_value_to_str(iip_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:IIP:PID {param}')
