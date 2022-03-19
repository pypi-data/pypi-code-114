from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lrf:
	"""Lrf commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrf", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	# noinspection PyTypeChecker
	def get_adjust(self) -> enums.Test:
		"""SCPI: [SOURce<HW>]:IQ:DPD:LRF:ADJust \n
		Snippet: value: enums.Test = driver.source.iq.dpd.lrf.get_adjust() \n
		Calculates the predistortion values for the current frequency. \n
			:return: adjust_result: 0| 1| RUNning| STOPped
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:LRF:ADJust?')
		return Conversions.str_to_scalar_enum(response, enums.Test)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:LRF:STATe \n
		Snippet: value: bool = driver.source.iq.dpd.lrf.get_state() \n
		Activates linearization of the RF. \n
			:return: linearize_rf: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:LRF:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, linearize_rf: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:LRF:STATe \n
		Snippet: driver.source.iq.dpd.lrf.set_state(linearize_rf = False) \n
		Activates linearization of the RF. \n
			:param linearize_rf: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(linearize_rf)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:LRF:STATe {param}')

	def clone(self) -> 'Lrf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lrf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
