from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_hh(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:HH \n
		Snippet: value: float = driver.source.fsimulator.scm.los.random.phase.get_hh() \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:return: phase_hh: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:HH?')
		return Conversions.str_to_float(response)

	def set_hh(self, phase_hh: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:HH \n
		Snippet: driver.source.fsimulator.scm.los.random.phase.set_hh(phase_hh = 1.0) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param phase_hh: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_hh)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:HH {param}')

	def get_hv(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:HV \n
		Snippet: value: float = driver.source.fsimulator.scm.los.random.phase.get_hv() \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:return: phase_hv: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:HV?')
		return Conversions.str_to_float(response)

	def set_hv(self, phase_hv: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:HV \n
		Snippet: driver.source.fsimulator.scm.los.random.phase.set_hv(phase_hv = 1.0) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param phase_hv: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_hv)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:HV {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:STATe \n
		Snippet: value: bool = driver.source.fsimulator.scm.los.random.phase.get_state() \n
		If enabled, random subpath start phases are selected. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:STATe \n
		Snippet: driver.source.fsimulator.scm.los.random.phase.set_state(state = False) \n
		If enabled, random subpath start phases are selected. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:STATe {param}')

	def get_vh(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:VH \n
		Snippet: value: float = driver.source.fsimulator.scm.los.random.phase.get_vh() \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:return: phase_vh: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:VH?')
		return Conversions.str_to_float(response)

	def set_vh(self, phase_vh: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:VH \n
		Snippet: driver.source.fsimulator.scm.los.random.phase.set_vh(phase_vh = 1.0) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param phase_vh: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_vh)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:VH {param}')

	def get_vv(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:VV \n
		Snippet: value: float = driver.source.fsimulator.scm.los.random.phase.get_vv() \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:return: phase_vv: float Range: 0 to 359.999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:VV?')
		return Conversions.str_to_float(response)

	def set_vv(self, phase_vv: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:RANDom:PHASe:VV \n
		Snippet: driver.source.fsimulator.scm.los.random.phase.set_vv(phase_vv = 1.0) \n
		Sets the start phase in degree of the LOS signal / the subpath per MIMO channel. \n
			:param phase_vv: float Range: 0 to 359.999
		"""
		param = Conversions.decimal_value_to_str(phase_vv)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:RANDom:PHASe:VV {param}')
