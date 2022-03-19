from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TranRecTrigSour:
		"""SCPI: [SOURce<HW>]:BB:GRAPhics:TRIGger:SOURce \n
		Snippet: value: enums.TranRecTrigSour = driver.source.bb.graphics.trigger.get_source() \n
		Defines the trigger for the starting time of the graphic recording. \n
			:return: source: SOFTware| MARKer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GRAPhics:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TranRecTrigSour)

	def set_source(self, source: enums.TranRecTrigSour) -> None:
		"""SCPI: [SOURce<HW>]:BB:GRAPhics:TRIGger:SOURce \n
		Snippet: driver.source.bb.graphics.trigger.set_source(source = enums.TranRecTrigSour.MARKer) \n
		Defines the trigger for the starting time of the graphic recording. \n
			:param source: SOFTware| MARKer
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TranRecTrigSour)
		self._core.io.write(f'SOURce<HwInstance>:BB:GRAPhics:TRIGger:SOURce {param}')
