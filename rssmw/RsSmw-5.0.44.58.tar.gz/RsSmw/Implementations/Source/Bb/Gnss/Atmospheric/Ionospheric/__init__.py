from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ionospheric:
	"""Ionospheric commands group definition. 17 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ionospheric", core, parent)

	@property
	def klobuchar(self):
		"""klobuchar commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_klobuchar'):
			from .Klobuchar import Klobuchar
			self._klobuchar = Klobuchar(self._core, self._cmd_group)
		return self._klobuchar

	@property
	def mops(self):
		"""mops commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_mops'):
			from .Mops import Mops
			self._mops = Mops(self._core, self._cmd_group)
		return self._mops

	@property
	def neQuick(self):
		"""neQuick commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_neQuick'):
			from .NeQuick import NeQuick
			self._neQuick = NeQuick(self._core, self._cmd_group)
		return self._neQuick

	# noinspection PyTypeChecker
	def get_model(self) -> enums.IonModel:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MODel \n
		Snippet: value: enums.IonModel = driver.source.bb.gnss.atmospheric.ionospheric.get_model() \n
		Determines the applied ionospheric model. \n
			:return: model: NONE| KLOBuchar| MOPS| NEQuick
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MODel?')
		return Conversions.str_to_scalar_enum(response, enums.IonModel)

	def set_model(self, model: enums.IonModel) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MODel \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.set_model(model = enums.IonModel.KLOBuchar) \n
		Determines the applied ionospheric model. \n
			:param model: NONE| KLOBuchar| MOPS| NEQuick
		"""
		param = Conversions.enum_scalar_to_str(model, enums.IonModel)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MODel {param}')

	def clone(self) -> 'Ionospheric':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ionospheric(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
