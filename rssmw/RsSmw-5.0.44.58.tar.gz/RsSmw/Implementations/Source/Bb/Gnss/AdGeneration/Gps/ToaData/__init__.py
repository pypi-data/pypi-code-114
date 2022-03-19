from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ToaData:
	"""ToaData commands group definition. 7 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("toaData", core, parent)

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:DURation \n
		Snippet: value: float = driver.source.bb.gnss.adGeneration.gps.toaData.get_duration() \n
		Sets the duration of the assistance data. \n
			:return: duration: float Range: 1E-3 to 5E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:DURation?')
		return Conversions.str_to_float(response)

	def set_duration(self, duration: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:DURation \n
		Snippet: driver.source.bb.gnss.adGeneration.gps.toaData.set_duration(duration = 1.0) \n
		Sets the duration of the assistance data. \n
			:param duration: float Range: 1E-3 to 5E3
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:DURation {param}')

	def get_resolution(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:RESolution \n
		Snippet: value: float = driver.source.bb.gnss.adGeneration.gps.toaData.get_resolution() \n
		Sets the resolution of the assistance data. \n
			:return: resolution: float Range: 1E-3 to 5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:RESolution?')
		return Conversions.str_to_float(response)

	def set_resolution(self, resolution: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:RESolution \n
		Snippet: driver.source.bb.gnss.adGeneration.gps.toaData.set_resolution(resolution = 1.0) \n
		Sets the resolution of the assistance data. \n
			:param resolution: float Range: 1E-3 to 5
		"""
		param = Conversions.decimal_value_to_str(resolution)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:RESolution {param}')

	# noinspection PyTypeChecker
	def get_tbasis(self) -> enums.TimeBasis:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:TBASis \n
		Snippet: value: enums.TimeBasis = driver.source.bb.gnss.adGeneration.gps.toaData.get_tbasis() \n
		Determines the timebase used to enter the time of assistance data parameters. \n
			:return: time_basis: UTC| GPS| GST| GLO| BDT| NAV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:TBASis?')
		return Conversions.str_to_scalar_enum(response, enums.TimeBasis)

	def set_tbasis(self, time_basis: enums.TimeBasis) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:TBASis \n
		Snippet: driver.source.bb.gnss.adGeneration.gps.toaData.set_tbasis(time_basis = enums.TimeBasis.BDT) \n
		Determines the timebase used to enter the time of assistance data parameters. \n
			:param time_basis: UTC| GPS| GST| GLO| BDT| NAV
		"""
		param = Conversions.enum_scalar_to_str(time_basis, enums.TimeBasis)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:TBASis {param}')

	def get_to_week(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:TOWeek \n
		Snippet: value: int = driver.source.bb.gnss.adGeneration.gps.toaData.get_to_week() \n
		Enabled for GPS timebase ([:SOURce<hw>]:BB:GNSS:ADGeneration:GPS:TOAData:TBASis) . Determines the Time of Week (TOW) the
		assistance data is generated for. \n
			:return: tow: integer Range: -604800 to 604800
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:TOWeek?')
		return Conversions.str_to_int(response)

	def set_to_week(self, tow: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:TOWeek \n
		Snippet: driver.source.bb.gnss.adGeneration.gps.toaData.set_to_week(tow = 1) \n
		Enabled for GPS timebase ([:SOURce<hw>]:BB:GNSS:ADGeneration:GPS:TOAData:TBASis) . Determines the Time of Week (TOW) the
		assistance data is generated for. \n
			:param tow: integer Range: -604800 to 604800
		"""
		param = Conversions.decimal_value_to_str(tow)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:TOWeek {param}')

	def get_wnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:WNUMber \n
		Snippet: value: int = driver.source.bb.gnss.adGeneration.gps.toaData.get_wnumber() \n
		Enabled for GPS timebase ([:SOURce<hw>]:BB:GNSS:ADGeneration:QZSS:TOAData:TBASis) . Sets the week number (WN) the
		assistance data is generated for. \n
			:return: week_number: integer Range: 0 to 9999.0*53
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:WNUMber?')
		return Conversions.str_to_int(response)

	def set_wnumber(self, week_number: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:TOAData:WNUMber \n
		Snippet: driver.source.bb.gnss.adGeneration.gps.toaData.set_wnumber(week_number = 1) \n
		Enabled for GPS timebase ([:SOURce<hw>]:BB:GNSS:ADGeneration:QZSS:TOAData:TBASis) . Sets the week number (WN) the
		assistance data is generated for. \n
			:param week_number: integer Range: 0 to 9999.0*53
		"""
		param = Conversions.decimal_value_to_str(week_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:TOAData:WNUMber {param}')

	def clone(self) -> 'ToaData':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ToaData(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
