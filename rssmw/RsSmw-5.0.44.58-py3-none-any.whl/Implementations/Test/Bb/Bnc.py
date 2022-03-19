from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bnc:
	"""Bnc commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bnc", core, parent)

	# noinspection PyTypeChecker
	def get_connection(self) -> enums.Test:
		"""SCPI: TEST:BB:BNC:CONNection \n
		Snippet: value: enums.Test = driver.test.bb.bnc.get_connection() \n
		Queries the BNC connection test result. This is a password-protected function. Unlock the protection level 1 to access it.
		See method RsSmw.System.Protect.State.set. \n
			:return: test_status: 0| 1| RUNning| STOPped
		"""
		response = self._core.io.query_str('TEST:BB:BNC:CONNection?')
		return Conversions.str_to_scalar_enum(response, enums.Test)

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.TestBbBncConn:
		"""SCPI: TEST:BB:BNC:DESTination \n
		Snippet: value: enums.TestBbBncConn = driver.test.bb.bnc.get_destination() \n
		Selects the BNC connection test destination. This is a password-protected function. Unlock the protection level 1 to
		access it. See method RsSmw.System.Protect.State.set. \n
			:return: bnc_destination: AUTO| USER1| USER2| USER3| USER4| USER5| USER6| TRGA| TRGB| C1TMC1| C1TM2| C1TM3| C2TMC4| C2TM5| C2TM6| F1TMC1| F1TM2| F1TM3| F2TMC4| F2TM5| F2TM6| F3TMC1| F3TM2| F3TM3| F4TMC4| F4TM5| F4TM6
		"""
		response = self._core.io.query_str('TEST:BB:BNC:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.TestBbBncConn)

	def set_destination(self, bnc_destination: enums.TestBbBncConn) -> None:
		"""SCPI: TEST:BB:BNC:DESTination \n
		Snippet: driver.test.bb.bnc.set_destination(bnc_destination = enums.TestBbBncConn.AUTO) \n
		Selects the BNC connection test destination. This is a password-protected function. Unlock the protection level 1 to
		access it. See method RsSmw.System.Protect.State.set. \n
			:param bnc_destination: AUTO| USER1| USER2| USER3| USER4| USER5| USER6| TRGA| TRGB| C1TMC1| C1TM2| C1TM3| C2TMC4| C2TM5| C2TM6| F1TMC1| F1TM2| F1TM3| F2TMC4| F2TM5| F2TM6| F3TMC1| F3TM2| F3TM3| F4TMC4| F4TM5| F4TM6
		"""
		param = Conversions.enum_scalar_to_str(bnc_destination, enums.TestBbBncConn)
		self._core.io.write(f'TEST:BB:BNC:DESTination {param}')

	def get_log(self) -> str:
		"""SCPI: TEST:BB:BNC:LOG \n
		Snippet: value: str = driver.test.bb.bnc.get_log() \n
		Queries the log message reported during the BNC connector test. This is a password-protected function.
		Unlock the protection level 1 to access it. See method RsSmw.System.Protect.State.set. \n
			:return: log: string
		"""
		response = self._core.io.query_str('TEST:BB:BNC:LOG?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TestBbBncConn:
		"""SCPI: TEST:BB:BNC:SOURce \n
		Snippet: value: enums.TestBbBncConn = driver.test.bb.bnc.get_source() \n
		Selects the BNC connection test source. This is a password-protected function. Unlock the protection level 1 to access it.
		See method RsSmw.System.Protect.State.set. \n
			:return: bnc_source: AUTO| USER1| USER2| USER3| USER4| USER5| USER6| TRGA| TRGB| C1TMC1| C1TM2| C1TM3| C2TMC4| C2TM5| C2TM6| F1TMC1| F1TM2| F1TM3| F2TMC4| F2TM5| F2TM6| F3TMC1| F3TM2| F3TM3| F4TMC4| F4TM5| F4TM6
		"""
		response = self._core.io.query_str('TEST:BB:BNC:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TestBbBncConn)

	def set_source(self, bnc_source: enums.TestBbBncConn) -> None:
		"""SCPI: TEST:BB:BNC:SOURce \n
		Snippet: driver.test.bb.bnc.set_source(bnc_source = enums.TestBbBncConn.AUTO) \n
		Selects the BNC connection test source. This is a password-protected function. Unlock the protection level 1 to access it.
		See method RsSmw.System.Protect.State.set. \n
			:param bnc_source: AUTO| USER1| USER2| USER3| USER4| USER5| USER6| TRGA| TRGB| C1TMC1| C1TM2| C1TM3| C2TMC4| C2TM5| C2TM6| F1TMC1| F1TM2| F1TM3| F2TMC4| F2TM5| F2TM6| F3TMC1| F3TM2| F3TM3| F4TMC4| F4TM5| F4TM6
		"""
		param = Conversions.enum_scalar_to_str(bnc_source, enums.TestBbBncConn)
		self._core.io.write(f'TEST:BB:BNC:SOURce {param}')
