from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edge:
	"""Edge commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edge", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.GilterEdge:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:EDGE:TYPE \n
		Snippet: value: enums.GilterEdge = driver.source.bb.gsm.filterPy.edge.get_type_py() \n
		The command sets the filter type LGAuss. This is the only possible selection in the case of digital standard GSM EDGE. \n
			:return: type_py: LGAuss
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FILTer:EDGE:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.GilterEdge)
