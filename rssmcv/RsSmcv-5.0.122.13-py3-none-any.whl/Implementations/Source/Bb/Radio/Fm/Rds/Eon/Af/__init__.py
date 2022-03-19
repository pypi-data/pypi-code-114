from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Af:
	"""Af commands group definition. 6 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("af", core, parent)

	@property
	def a(self):
		"""a commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import A
			self._a = A(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_b'):
			from .B import B
			self._b = B(self._core, self._cmd_group)
		return self._b

	# noinspection PyTypeChecker
	def get_method(self) -> enums.TxAudioBcFmRdsEonAfMethod:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:METHod \n
		Snippet: value: enums.TxAudioBcFmRdsEonAfMethod = driver.source.bb.radio.fm.rds.eon.af.get_method() \n
		No command help available \n
			:return: eon_af_method: MAPF| A
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.TxAudioBcFmRdsEonAfMethod)

	def set_method(self, eon_af_method: enums.TxAudioBcFmRdsEonAfMethod) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:AF:METHod \n
		Snippet: driver.source.bb.radio.fm.rds.eon.af.set_method(eon_af_method = enums.TxAudioBcFmRdsEonAfMethod.A) \n
		No command help available \n
			:param eon_af_method: MAPF| A
		"""
		param = Conversions.enum_scalar_to_str(eon_af_method, enums.TxAudioBcFmRdsEonAfMethod)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:AF:METHod {param}')

	def clone(self) -> 'Af':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Af(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
