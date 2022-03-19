from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	# noinspection PyTypeChecker
	def get_frc(self) -> enums.EutraUlFrcNbiotTcw:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:NIOT:FRC \n
		Snippet: value: enums.EutraUlFrcNbiotTcw = driver.source.bb.eutra.tcw.ws.niot.get_frc() \n
		Sets the FRC of NPUSCH wanted signal (A16-1 to A16-5) . \n
			:return: nbiot_frc: A161| A162| A163| A164| A165
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:NIOT:FRC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUlFrcNbiotTcw)

	def set_frc(self, nbiot_frc: enums.EutraUlFrcNbiotTcw) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:NIOT:FRC \n
		Snippet: driver.source.bb.eutra.tcw.ws.niot.set_frc(nbiot_frc = enums.EutraUlFrcNbiotTcw.A161) \n
		Sets the FRC of NPUSCH wanted signal (A16-1 to A16-5) . \n
			:param nbiot_frc: A161| A162| A163| A164| A165
		"""
		param = Conversions.enum_scalar_to_str(nbiot_frc, enums.EutraUlFrcNbiotTcw)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:NIOT:FRC {param}')
