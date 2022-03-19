from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Miso:
	"""Miso commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("miso", core, parent)

	def set(self, miso: enums.Atsc30Miso, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:MISO \n
		Snippet: driver.source.bb.a3Tsc.subframe.miso.set(miso = enums.Atsc30Miso.C256, subframe = repcap.Subframe.Default) \n
		Defines the multiple inputs and single output (MISO) option. \n
			:param miso: OFF| C64| C256
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(miso, enums.Atsc30Miso)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:MISO {param}')

	# noinspection PyTypeChecker
	def get(self, subframe=repcap.Subframe.Default) -> enums.Atsc30Miso:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:MISO \n
		Snippet: value: enums.Atsc30Miso = driver.source.bb.a3Tsc.subframe.miso.get(subframe = repcap.Subframe.Default) \n
		Defines the multiple inputs and single output (MISO) option. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: miso: OFF| C64| C256"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:MISO?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30Miso)
