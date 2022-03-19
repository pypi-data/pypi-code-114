from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfig:
	"""Pconfig commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconfig", core, parent)

	@property
	def antGain(self):
		"""antGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antGain'):
			from .AntGain import AntGain
			self._antGain = AntGain(self._core, self._cmd_group)
		return self._antGain

	def get_ant_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfig:PCONfig:ANTNumber \n
		Snippet: value: int = driver.source.bb.btooth.econfig.pconfig.get_ant_number() \n
		Specifies the number of antenas for angle of departure (AoD) direction finding method. You select up to four antennas,
		that are used for direction finding. \n
			:return: antenna_num: integer Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfig:PCONfig:ANTNumber?')
		return Conversions.str_to_int(response)

	def set_ant_number(self, antenna_num: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfig:PCONfig:ANTNumber \n
		Snippet: driver.source.bb.btooth.econfig.pconfig.set_ant_number(antenna_num = 1) \n
		Specifies the number of antenas for angle of departure (AoD) direction finding method. You select up to four antennas,
		that are used for direction finding. \n
			:param antenna_num: integer Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(antenna_num)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfig:PCONfig:ANTNumber {param}')

	def clone(self) -> 'Pconfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pconfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
