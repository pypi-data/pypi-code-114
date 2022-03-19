from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Point:
	"""Point commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("point", core, parent)

	def get(self, name: str) -> str:
		"""SCPI: DIAGnostic<HW>:[MEASure]:POINt \n
		Snippet: value: str = driver.diagnostic.measure.point.get(name = '1') \n
		Triggers the voltage measurement at the specified test point and returns the measured voltage. For more information, see
		R&S SMW Service Manual. \n
			:param name: test point identifier Test point name, as queried with the command method RsSmw.Diagnostic.Point.catalog
			:return: value: valueunit"""
		param = Conversions.value_to_quoted_str(name)
		response = self._core.io.query_str(f'DIAGnostic<HwInstance>:MEASure:POINt? {param}')
		return trim_str_response(response)
