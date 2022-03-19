from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mean:
	"""Mean commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mean", core, parent)

	def set(self, mean: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:MEAN \n
		Snippet: driver.source.regenerator.object.rcs.mean.set(mean = 1.0, objectIx = repcap.ObjectIx.Default) \n
		Sets the mean RCS value required for the RCS calculation. \n
			:param mean: float Range: -60 to 100
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(mean)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:MEAN {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:MEAN \n
		Snippet: value: float = driver.source.regenerator.object.rcs.mean.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the mean RCS value required for the RCS calculation. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: mean: float Range: -60 to 100"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:MEAN?')
		return Conversions.str_to_float(response)
