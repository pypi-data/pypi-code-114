from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	# noinspection PyTypeChecker
	def get_impedance(self) -> enums.InputImpRf:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:EXTernal:IMPedance \n
		Snippet: value: enums.InputImpRf = driver.source.pulm.trigger.external.get_impedance() \n
		Sets the impedance for the external pulse trigger. \n
			:return: impedance: G50| G10K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TRIGger:EXTernal:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.InputImpRf)

	def set_impedance(self, impedance: enums.InputImpRf) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:EXTernal:IMPedance \n
		Snippet: driver.source.pulm.trigger.external.set_impedance(impedance = enums.InputImpRf.G10K) \n
		Sets the impedance for the external pulse trigger. \n
			:param impedance: G50| G10K
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.InputImpRf)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TRIGger:EXTernal:IMPedance {param}')
