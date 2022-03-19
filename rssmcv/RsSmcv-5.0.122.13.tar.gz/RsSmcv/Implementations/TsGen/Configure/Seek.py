from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Seek:
	"""Seek commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seek", core, parent)

	def get_position(self) -> float:
		"""SCPI: TSGen:CONFigure:SEEK:POSition \n
		Snippet: value: float = driver.tsGen.configure.seek.get_position() \n
		Sets the position, that is the current playing time position. You can select a value in a 10-hour range. \n
			:return: position: float Range: 0 to 36000000
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEEK:POSition?')
		return Conversions.str_to_float(response)

	def set_position(self, position: float) -> None:
		"""SCPI: TSGen:CONFigure:SEEK:POSition \n
		Snippet: driver.tsGen.configure.seek.set_position(position = 1.0) \n
		Sets the position, that is the current playing time position. You can select a value in a 10-hour range. \n
			:param position: float Range: 0 to 36000000
		"""
		param = Conversions.decimal_value_to_str(position)
		self._core.io.write(f'TSGen:CONFigure:SEEK:POSition {param}')

	def reset(self) -> None:
		"""SCPI: TSGen:CONFigure:SEEK:RESet \n
		Snippet: driver.tsGen.configure.seek.reset() \n
			INTRO_CMD_HELP: Resets the following parameters to their default state: \n
			- method RsSmcv.TsGen.Configure.Seek.start
			- method RsSmcv.TsGen.Configure.Seek.stop \n
		"""
		self._core.io.write(f'TSGen:CONFigure:SEEK:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: TSGen:CONFigure:SEEK:RESet \n
		Snippet: driver.tsGen.configure.seek.reset_with_opc() \n
			INTRO_CMD_HELP: Resets the following parameters to their default state: \n
			- method RsSmcv.TsGen.Configure.Seek.start
			- method RsSmcv.TsGen.Configure.Seek.stop \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TSGen:CONFigure:SEEK:RESet', opc_timeout_ms)

	def get_start(self) -> float:
		"""SCPI: TSGen:CONFigure:SEEK:STARt \n
		Snippet: value: float = driver.tsGen.configure.seek.get_start() \n
		Sets an individual start time. You can select a value in a 10-hour range. \n
			:return: start: float Range: 0 to 36000000
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEEK:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: TSGen:CONFigure:SEEK:STARt \n
		Snippet: driver.tsGen.configure.seek.set_start(start = 1.0) \n
		Sets an individual start time. You can select a value in a 10-hour range. \n
			:param start: float Range: 0 to 36000000
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'TSGen:CONFigure:SEEK:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: TSGen:CONFigure:SEEK:STOP \n
		Snippet: value: float = driver.tsGen.configure.seek.get_stop() \n
		Sets an individual stop time. You can select a value in a 10-hour range. \n
			:return: stop: float Range: 0 to 36000000
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEEK:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop: float) -> None:
		"""SCPI: TSGen:CONFigure:SEEK:STOP \n
		Snippet: driver.tsGen.configure.seek.set_stop(stop = 1.0) \n
		Sets an individual stop time. You can select a value in a 10-hour range. \n
			:param stop: float Range: 0 to 36000000
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'TSGen:CONFigure:SEEK:STOP {param}')
