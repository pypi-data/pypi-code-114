from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Satellite:
	"""Satellite commands group definition. 22 total commands, 4 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("satellite", core, parent)

	@property
	def acceleration(self):
		"""acceleration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acceleration'):
			from .Acceleration import Acceleration
			self._acceleration = Acceleration(self._core, self._cmd_group)
		return self._acceleration

	@property
	def position(self):
		"""position commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_position'):
			from .Position import Position
			self._position = Position(self._core, self._cmd_group)
		return self._position

	@property
	def select(self):
		"""select commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def velocity(self):
		"""velocity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_velocity'):
			from .Velocity import Velocity
			self._velocity = Velocity(self._core, self._cmd_group)
		return self._velocity

	def get_azimuth(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:AZIMuth \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_azimuth() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:AZIMuth?')
		return Conversions.str_to_bool(response)

	def set_azimuth(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:AZIMuth \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_azimuth(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:AZIMuth {param}')

	def get_cbias(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:CBIas \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_cbias() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:CBIas?')
		return Conversions.str_to_bool(response)

	def set_cbias(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:CBIas \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_cbias(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:CBIas {param}')

	def get_crange(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:CRANge \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_crange() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:CRANge?')
		return Conversions.str_to_bool(response)

	def set_crange(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:CRANge \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_crange(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:CRANge {param}')

	def get_dshift(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:DSHift \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_dshift() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:DSHift?')
		return Conversions.str_to_bool(response)

	def set_dshift(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:DSHift \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_dshift(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:DSHift {param}')

	def get_elevation(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:ELEVation \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_elevation() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:ELEVation?')
		return Conversions.str_to_bool(response)

	def set_elevation(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:ELEVation \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_elevation(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:ELEVation {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.LogFmtSat:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:FORMat \n
		Snippet: value: enums.LogFmtSat = driver.source.bb.gnss.logging.category.satellite.get_format_py() \n
		Sets the file format in that the logged data is saved. \n
			:return: format_py: CSV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.LogFmtSat)

	def get_idelay(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:IDELay \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_idelay() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:IDELay?')
		return Conversions.str_to_bool(response)

	def set_idelay(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:IDELay \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_idelay(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:IDELay {param}')

	def get_prange(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRANge \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_prange() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRANge?')
		return Conversions.str_to_bool(response)

	def set_prange(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRANge \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_prange(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRANge {param}')

	def get_prb_rate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRBRate \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_prb_rate() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRBRate?')
		return Conversions.str_to_bool(response)

	def set_prb_rate(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRBRate \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_prb_rate(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRBRate {param}')

	def get_pr_bias(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRBias \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_pr_bias() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRBias?')
		return Conversions.str_to_bool(response)

	def set_pr_bias(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRBias \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_pr_bias(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRBias {param}')

	def get_pr_rate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRRate \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_pr_rate() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRRate?')
		return Conversions.str_to_bool(response)

	def set_pr_rate(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:PRRate \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_pr_rate(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:PRRate {param}')

	def get_range(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:RANGe \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_range() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:RANGe?')
		return Conversions.str_to_bool(response)

	def set_range(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:RANGe \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_range(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:RANGe {param}')

	def get_rrate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:RRATe \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_rrate() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:RRATe?')
		return Conversions.str_to_bool(response)

	def set_rrate(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:RRATe \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_rrate(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:RRATe {param}')

	def get_slevel(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:SLEVel \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_slevel() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:SLEVel?')
		return Conversions.str_to_bool(response)

	def set_slevel(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:SLEVel \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_slevel(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:SLEVel {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_state() \n
		Enables the logging of the selected category. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:STATe \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_state(state = False) \n
		Enables the logging of the selected category. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:STATe {param}')

	# noinspection PyTypeChecker
	def get_step(self) -> enums.LogRes:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:STEP \n
		Snippet: value: enums.LogRes = driver.source.bb.gnss.logging.category.satellite.get_step() \n
		Sets the logging step. \n
			:return: resolution: R1S| R2S| R5S| R10S| R02S| R04S| R08S
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:STEP?')
		return Conversions.str_to_scalar_enum(response, enums.LogRes)

	def set_step(self, resolution: enums.LogRes) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:STEP \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_step(resolution = enums.LogRes.R02S) \n
		Sets the logging step. \n
			:param resolution: R1S| R2S| R5S| R10S| R02S| R04S| R08S
		"""
		param = Conversions.enum_scalar_to_str(resolution, enums.LogRes)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:STEP {param}')

	def get_tdelay(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:TDELay \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.satellite.get_tdelay() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:TDELay?')
		return Conversions.str_to_bool(response)

	def set_tdelay(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:SATellite:TDELay \n
		Snippet: driver.source.bb.gnss.logging.category.satellite.set_tdelay(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:SATellite:TDELay {param}')

	def clone(self) -> 'Satellite':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Satellite(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
