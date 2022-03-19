from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pilot", core, parent)

	# noinspection PyTypeChecker
	def get_dx(self) -> enums.Atsc30PilotPattern:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:PILot:DX \n
		Snippet: value: enums.Atsc30PilotPattern = driver.source.bb.a3Tsc.info.bootstrap.pilot.get_dx() \n
		Queries the pilot pattern used for the preamble symbols. \n
			:return: pilot_pattern: D3| D4| D6| D8| D12| D16| D24| D32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:PILot:DX?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30PilotPattern)
