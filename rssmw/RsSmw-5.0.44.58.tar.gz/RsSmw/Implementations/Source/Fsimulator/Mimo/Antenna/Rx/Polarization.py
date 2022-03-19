from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Polarization:
	"""Polarization commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polarization", core, parent)

	# noinspection PyTypeChecker
	def get_angle(self) -> enums.AntModPolAngle:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:POLarization:ANGLe \n
		Snippet: value: enums.AntModPolAngle = driver.source.fsimulator.mimo.antenna.rx.polarization.get_angle() \n
		Set the antenna element polarization slant angle. \n
			:return: ant_rx_pol_angle: No help available
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:MIMO:ANTenna:RX:POLarization:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.AntModPolAngle)

	def set_angle(self, ant_rx_pol_angle: enums.AntModPolAngle) -> None:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:POLarization:ANGLe \n
		Snippet: driver.source.fsimulator.mimo.antenna.rx.polarization.set_angle(ant_rx_pol_angle = enums.AntModPolAngle.POLCO0) \n
		Set the antenna element polarization slant angle. \n
			:param ant_rx_pol_angle: POLCROSS45| POLCROSS90| POLCO0| POLCO90 POLCROSS45 | POLCROSS90 cross-poliarization 45°/90° POLCO0 | POLCO90 co-poliarization 0°/90° (vertical/horizontal poliarization)
		"""
		param = Conversions.enum_scalar_to_str(ant_rx_pol_angle, enums.AntModPolAngle)
		self._core.io.write(f'SOURce:FSIMulator:MIMO:ANTenna:RX:POLarization:ANGLe {param}')
