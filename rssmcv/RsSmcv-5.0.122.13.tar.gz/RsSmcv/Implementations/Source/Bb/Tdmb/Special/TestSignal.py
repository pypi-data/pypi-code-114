from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TestSignal:
	"""TestSignal commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("testSignal", core, parent)

	def get_scid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TESTsignal:SCID \n
		Snippet: value: int = driver.source.bb.tdmb.special.testSignal.get_scid() \n
		Sets the ID of a subchannel (stream) that transmits a test signal (PRBS) instead of data. This setting takes effect, if
		special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:return: scid: integer Range: 0 to 64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:SPECial:TESTsignal:SCID?')
		return Conversions.str_to_int(response)

	def set_scid(self, scid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TESTsignal:SCID \n
		Snippet: driver.source.bb.tdmb.special.testSignal.set_scid(scid = 1) \n
		Sets the ID of a subchannel (stream) that transmits a test signal (PRBS) instead of data. This setting takes effect, if
		special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:param scid: integer Range: 0 to 64
		"""
		param = Conversions.decimal_value_to_str(scid)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:SPECial:TESTsignal:SCID {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TESTsignal:[STATe] \n
		Snippet: value: bool = driver.source.bb.tdmb.special.testSignal.get_state() \n
		Activates transfer of a PRBS test signal to a subchannel instead of ETI input data. This setting takes effect, if special
		settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:return: prbs_test_signal: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:SPECial:TESTsignal:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, prbs_test_signal: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TESTsignal:[STATe] \n
		Snippet: driver.source.bb.tdmb.special.testSignal.set_state(prbs_test_signal = False) \n
		Activates transfer of a PRBS test signal to a subchannel instead of ETI input data. This setting takes effect, if special
		settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:param prbs_test_signal: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(prbs_test_signal)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:SPECial:TESTsignal:STATe {param}')
