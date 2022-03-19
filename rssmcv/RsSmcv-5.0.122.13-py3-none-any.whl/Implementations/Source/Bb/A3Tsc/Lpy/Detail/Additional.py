from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Additional:
	"""Additional commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("additional", core, parent)

	# noinspection PyTypeChecker
	def get_parity(self) -> enums.Atsc30L1DetailAdditionalParityMode:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:L:DETail:ADDitional:[PARity] \n
		Snippet: value: enums.Atsc30L1DetailAdditionalParityMode = driver.source.bb.a3Tsc.lpy.detail.additional.get_parity() \n
		Queries the L1 detail additional parity mode, that is disabled by default. \n
			:return: l_1_detail_add_par: OFF| K1| K2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:L:DETail:ADDitional:PARity?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30L1DetailAdditionalParityMode)
