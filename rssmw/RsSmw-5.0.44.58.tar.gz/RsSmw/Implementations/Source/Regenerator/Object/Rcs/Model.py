from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Model:
	"""Model commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	def set(self, model: enums.RegRcsModel, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:MODel \n
		Snippet: driver.source.regenerator.object.rcs.model.set(model = enums.RegRcsModel.SWE0, objectIx = repcap.ObjectIx.Default) \n
		Set the model that describes the radar cross-section (PCS) of the object. \n
			:param model: SWE0| SWE1| SWE2| SWE3| SWE4
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.enum_scalar_to_str(model, enums.RegRcsModel)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:MODel {param}')

	# noinspection PyTypeChecker
	def get(self, objectIx=repcap.ObjectIx.Default) -> enums.RegRcsModel:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:MODel \n
		Snippet: value: enums.RegRcsModel = driver.source.regenerator.object.rcs.model.get(objectIx = repcap.ObjectIx.Default) \n
		Set the model that describes the radar cross-section (PCS) of the object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: model: SWE0| SWE1| SWE2| SWE3| SWE4"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:MODel?')
		return Conversions.str_to_scalar_enum(response, enums.RegRcsModel)
