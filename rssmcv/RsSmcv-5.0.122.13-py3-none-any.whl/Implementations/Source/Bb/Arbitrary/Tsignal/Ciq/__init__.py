from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ciq:
	"""Ciq commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ciq", core, parent)

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	def get_icomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:CIQ:I \n
		Snippet: value: float = driver.source.bb.arbitrary.tsignal.ciq.get_icomponent() \n
		Sets the value for the I and Q component of the test signal \n
			:return: ipart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TSIGnal:CIQ:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, ipart: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:CIQ:I \n
		Snippet: driver.source.bb.arbitrary.tsignal.ciq.set_icomponent(ipart = 1.0) \n
		Sets the value for the I and Q component of the test signal \n
			:param ipart: float Range: -1 to 1, Unit: FS
		"""
		param = Conversions.decimal_value_to_str(ipart)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TSIGnal:CIQ:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:CIQ:Q \n
		Snippet: value: float = driver.source.bb.arbitrary.tsignal.ciq.get_qcomponent() \n
		Sets the value for the I and Q component of the test signal \n
			:return: tsig: float Range: -1 to 1, Unit: FS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TSIGnal:CIQ:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, tsig: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:CIQ:Q \n
		Snippet: driver.source.bb.arbitrary.tsignal.ciq.set_qcomponent(tsig = 1.0) \n
		Sets the value for the I and Q component of the test signal \n
			:param tsig: float Range: -1 to 1, Unit: FS
		"""
		param = Conversions.decimal_value_to_str(tsig)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TSIGnal:CIQ:Q {param}')

	def clone(self) -> 'Ciq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ciq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
