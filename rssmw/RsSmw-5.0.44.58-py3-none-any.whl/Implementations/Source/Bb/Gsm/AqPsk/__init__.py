from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AqPsk:
	"""AqPsk commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aqPsk", core, parent)

	@property
	def angle(self):
		"""angle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_angle'):
			from .Angle import Angle
			self._angle = Angle(self._core, self._cmd_group)
		return self._angle

	@property
	def scpir(self):
		"""scpir commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scpir'):
			from .Scpir import Scpir
			self._scpir = Scpir(self._core, self._cmd_group)
		return self._scpir

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.GsmModTypeAqpsk:
		"""SCPI: [SOURce<HW>]:BB:GSM:AQPSk:FORMat \n
		Snippet: value: enums.GsmModTypeAqpsk = driver.source.bb.gsm.aqPsk.get_format_py() \n
		The command queries the modulation type. The modulation type is permanently set to AQPSK. \n
			:return: format_py: AQPSk
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:AQPSk:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.GsmModTypeAqpsk)

	def clone(self) -> 'AqPsk':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AqPsk(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
