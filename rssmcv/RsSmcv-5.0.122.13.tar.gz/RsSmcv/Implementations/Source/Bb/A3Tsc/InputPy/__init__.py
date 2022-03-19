from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 9 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def destination(self):
		"""destination commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_destination'):
			from .Destination import Destination
			self._destination = Destination(self._core, self._cmd_group)
		return self._destination

	@property
	def stl(self):
		"""stl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_stl'):
			from .Stl import Stl
			self._stl = Stl(self._core, self._cmd_group)
		return self._stl

	def get_ccheck(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:CCHeck \n
		Snippet: value: bool = driver.source.bb.a3Tsc.inputPy.get_ccheck() \n
		Sets the depth of inspection for the conformance check. \n
			:return: conf_check: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:CCHeck?')
		return Conversions.str_to_bool(response)

	def set_ccheck(self, conf_check: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:CCHeck \n
		Snippet: driver.source.bb.a3Tsc.inputPy.set_ccheck(conf_check = False) \n
		Sets the depth of inspection for the conformance check. \n
			:param conf_check: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(conf_check)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:CCHeck {param}')

	def get_nplp(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:NPLP \n
		Snippet: value: int = driver.source.bb.a3Tsc.inputPy.get_nplp() \n
		Queries the number of s, that is the total number of the layer configuration. \n
			:return: number_plp: integer Range: 1 to 64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:NPLP?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.Atsc30Protocol:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:PROTocol \n
		Snippet: value: enums.Atsc30Protocol = driver.source.bb.a3Tsc.inputPy.get_protocol() \n
		Displays the used protocol. \n
			:return: protocol: UDP| RTP| AUTO UDP Protocol type for IP-based stream (, or ) with deactivated interface. UDP|RTP Protocol type for IP-based STL stream with activated STL interface. AUTO Protocol type is UDP or UDP/RTP for IP-based transport stream (TSoverIP) with deactivated STL interface.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30Protocol)

	def get_status(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:STATus \n
		Snippet: value: str = driver.source.bb.a3Tsc.inputPy.get_status() \n
		Queries the ATSC 3.0 coder status. \n
			:return: status: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:STATus?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.Atsc30InputType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:TYPE \n
		Snippet: value: enums.Atsc30InputType = driver.source.bb.a3Tsc.inputPy.get_type_py() \n
		Specifies the input type. \n
			:return: input_type: IP| TS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30InputType)

	def set_type_py(self, input_type: enums.Atsc30InputType) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:TYPE \n
		Snippet: driver.source.bb.a3Tsc.inputPy.set_type_py(input_type = enums.Atsc30InputType.IP) \n
		Specifies the input type. \n
			:param input_type: IP| TS
		"""
		param = Conversions.enum_scalar_to_str(input_type, enums.Atsc30InputType)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:TYPE {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
