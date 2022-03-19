from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Seamless:
	"""Seamless commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seamless", core, parent)

	def get_cc(self) -> bool:
		"""SCPI: TSGen:CONFigure:SEAMless:CC \n
		Snippet: value: bool = driver.tsGen.configure.seamless.get_cc() \n
		Activates the correction of the continuity counters in the replayed TS data stream. The correction allows you to decode
		the stream without interruption when the play file is looping. \n
			:return: cc: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEAMless:CC?')
		return Conversions.str_to_bool(response)

	def set_cc(self, cc: bool) -> None:
		"""SCPI: TSGen:CONFigure:SEAMless:CC \n
		Snippet: driver.tsGen.configure.seamless.set_cc(cc = False) \n
		Activates the correction of the continuity counters in the replayed TS data stream. The correction allows you to decode
		the stream without interruption when the play file is looping. \n
			:param cc: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(cc)
		self._core.io.write(f'TSGen:CONFigure:SEAMless:CC {param}')

	def get_pcr(self) -> bool:
		"""SCPI: TSGen:CONFigure:SEAMless:PCR \n
		Snippet: value: bool = driver.tsGen.configure.seamless.get_pcr() \n
		Activates the correction of time stamps in the replayed TS data stream. The correction allows you to decode the stream
		without interruption when the play file is looping. \n
			:return: pcr: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEAMless:PCR?')
		return Conversions.str_to_bool(response)

	def set_pcr(self, pcr: bool) -> None:
		"""SCPI: TSGen:CONFigure:SEAMless:PCR \n
		Snippet: driver.tsGen.configure.seamless.set_pcr(pcr = False) \n
		Activates the correction of time stamps in the replayed TS data stream. The correction allows you to decode the stream
		without interruption when the play file is looping. \n
			:param pcr: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pcr)
		self._core.io.write(f'TSGen:CONFigure:SEAMless:PCR {param}')

	def get_tt(self) -> bool:
		"""SCPI: TSGen:CONFigure:SEAMless:TT \n
		Snippet: value: bool = driver.tsGen.configure.seamless.get_tt() \n
		Activates the correction of the time and date table in the replayed TS data stream. The correction allows you to decode
		the stream without interruption when the play file is looping. \n
			:return: tt: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('TSGen:CONFigure:SEAMless:TT?')
		return Conversions.str_to_bool(response)

	def set_tt(self, tt: bool) -> None:
		"""SCPI: TSGen:CONFigure:SEAMless:TT \n
		Snippet: driver.tsGen.configure.seamless.set_tt(tt = False) \n
		Activates the correction of the time and date table in the replayed TS data stream. The correction allows you to decode
		the stream without interruption when the play file is looping. \n
			:param tt: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tt)
		self._core.io.write(f'TSGen:CONFigure:SEAMless:TT {param}')
