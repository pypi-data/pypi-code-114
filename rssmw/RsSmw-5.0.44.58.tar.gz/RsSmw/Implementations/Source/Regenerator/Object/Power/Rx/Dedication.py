from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dedication:
	"""Dedication commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dedication", core, parent)

	def set(self, dedication: enums.RegObjPowDedicStartRang, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:POWer:RX:DEDication \n
		Snippet: driver.source.regenerator.object.power.rx.dedication.set(dedication = enums.RegObjPowDedicStartRang.ALL, objectIx = repcap.ObjectIx.Default) \n
		In [:SOURce<hw>]:REGenerator:RADar:POWer:MODE MANual mode and for moving objects, defines how to interpret the value PRX
		set with the command [:SOURce<hw>]:REGenerator:OBJect<ch>:POWer:RX. \n
			:param dedication: STARt| END| ALL STARt PRx, jStartRange = PRX END PRx, jEndRange = PRX ALL PRx, jStartRange = PRx, jEndRange = PRX
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.enum_scalar_to_str(dedication, enums.RegObjPowDedicStartRang)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:POWer:RX:DEDication {param}')

	# noinspection PyTypeChecker
	def get(self, objectIx=repcap.ObjectIx.Default) -> enums.RegObjPowDedicStartRang:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:POWer:RX:DEDication \n
		Snippet: value: enums.RegObjPowDedicStartRang = driver.source.regenerator.object.power.rx.dedication.get(objectIx = repcap.ObjectIx.Default) \n
		In [:SOURce<hw>]:REGenerator:RADar:POWer:MODE MANual mode and for moving objects, defines how to interpret the value PRX
		set with the command [:SOURce<hw>]:REGenerator:OBJect<ch>:POWer:RX. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: dedication: STARt| END| ALL STARt PRx, jStartRange = PRX END PRx, jEndRange = PRX ALL PRx, jStartRange = PRx, jEndRange = PRX"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:POWer:RX:DEDication?')
		return Conversions.str_to_scalar_enum(response, enums.RegObjPowDedicStartRang)
