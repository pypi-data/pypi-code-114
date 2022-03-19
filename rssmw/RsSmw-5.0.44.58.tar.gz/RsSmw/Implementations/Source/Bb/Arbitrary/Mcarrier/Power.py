from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	def get_reference(self) -> enums.ArbMultCarrLevRef:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:POWer:REFerence \n
		Snippet: value: enums.ArbMultCarrLevRef = driver.source.bb.arbitrary.mcarrier.power.get_reference() \n
		Defines the way the individual carriers in a composed multi carrier signal are leveled. \n
			:return: reference: RMS| PEAK
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:POWer:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.ArbMultCarrLevRef)

	def set_reference(self, reference: enums.ArbMultCarrLevRef) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:POWer:REFerence \n
		Snippet: driver.source.bb.arbitrary.mcarrier.power.set_reference(reference = enums.ArbMultCarrLevRef.PEAK) \n
		Defines the way the individual carriers in a composed multi carrier signal are leveled. \n
			:param reference: RMS| PEAK
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ArbMultCarrLevRef)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:POWer:REFerence {param}')
