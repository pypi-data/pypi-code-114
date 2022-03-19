from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.ArbSignType:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:SIGNal:TYPE \n
		Snippet: value: enums.ArbSignType = driver.source.bb.arbitrary.signal.get_type_py() \n
		Selects the type of test signal. \n
			:return: arb_signal_type: SINE| RECT| CIQ | AWGN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:SIGNal:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbSignType)

	def set_type_py(self, arb_signal_type: enums.ArbSignType) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:SIGNal:TYPE \n
		Snippet: driver.source.bb.arbitrary.signal.set_type_py(arb_signal_type = enums.ArbSignType.AWGN) \n
		Selects the type of test signal. \n
			:param arb_signal_type: SINE| RECT| CIQ | AWGN
		"""
		param = Conversions.enum_scalar_to_str(arb_signal_type, enums.ArbSignType)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:SIGNal:TYPE {param}')
