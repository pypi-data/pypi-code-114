from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsp:
	"""Tsp commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsp", core, parent)

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import Update
			self._update = Update(self._core, self._cmd_group)
		return self._update

	def get_date(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:DATE \n
		Snippet: value: str = driver.source.bb.t2Dvb.delay.tsp.get_date() \n
		Queries the UTC date from the last UTC reference update. \n
			:return: tsp_date: string Format yyyy-mm-dd
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:DELay:TSP:DATE?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SfnMode:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:MODE \n
		Snippet: value: enums.SfnMode = driver.source.bb.t2Dvb.delay.tsp.get_mode() \n
		Queries the type of the currently received T2-MI timestamps. \n
			:return: timestamp_mode: RELative| ABSolute RELative Received T2-MI stream has T2-MI packets with relative timestamps. ABSolute Received T2-MI stream has T2-MI packets with absolute timestamps. If received, the following subparameters are displayed.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:DELay:TSP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SfnMode)

	def get_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:OFFSet \n
		Snippet: value: int = driver.source.bb.t2Dvb.delay.tsp.get_offset() \n
		Modifies the UTC/ leap seconds offset. \n
			:return: tsp_offset: integer Range: -255 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:DELay:TSP:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, tsp_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:OFFSet \n
		Snippet: driver.source.bb.t2Dvb.delay.tsp.set_offset(tsp_offset = 1) \n
		Modifies the UTC/ leap seconds offset. \n
			:param tsp_offset: integer Range: -255 to 255
		"""
		param = Conversions.decimal_value_to_str(tsp_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:DELay:TSP:OFFSet {param}')

	def get_seconds(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:SEConds \n
		Snippet: value: int = driver.source.bb.t2Dvb.delay.tsp.get_seconds() \n
		Queries the elapsed time in seconds since 2000. The value is based on the value of the last UTC reference update. \n
			:return: tsp_seconds: integer Range: 0 to 1099511627775
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:DELay:TSP:SEConds?')
		return Conversions.str_to_int(response)

	def get_time(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:DELay:TSP:TIME \n
		Snippet: value: str = driver.source.bb.t2Dvb.delay.tsp.get_time() \n
		Queries the UTC time from the last UTC reference update. \n
			:return: tsp_time: string Format hour:minute:second
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:DELay:TSP:TIME?')
		return trim_str_response(response)

	def clone(self) -> 'Tsp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
