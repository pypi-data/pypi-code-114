from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcoverage:
	"""Tcoverage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcoverage", core, parent)

	def set(self, test_coverage: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:TCOVerage \n
		Snippet: driver.source.regenerator.object.rcs.tcoverage.set(test_coverage = 1.0, objectIx = repcap.ObjectIx.Default) \n
		Sets the test coverage. \n
			:param test_coverage: float Range: 0.01 to 99.99
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(test_coverage)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:TCOVerage {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:TCOVerage \n
		Snippet: value: float = driver.source.regenerator.object.rcs.tcoverage.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the test coverage. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: test_coverage: float Range: 0.01 to 99.99"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:TCOVerage?')
		return Conversions.str_to_float(response)
