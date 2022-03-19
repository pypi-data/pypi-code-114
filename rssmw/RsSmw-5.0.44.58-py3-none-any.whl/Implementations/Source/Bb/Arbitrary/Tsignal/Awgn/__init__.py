from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	def get_samples(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:AWGN:SAMPles \n
		Snippet: value: int = driver.source.bb.arbitrary.tsignal.awgn.get_samples() \n
		Sets the number of samples generated for the AWGN waveform. \n
			:return: par_awgn_samp: integer Range: 1E6 to 1E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TSIGnal:AWGN:SAMPles?')
		return Conversions.str_to_int(response)

	def set_samples(self, par_awgn_samp: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TSIGnal:AWGN:SAMPles \n
		Snippet: driver.source.bb.arbitrary.tsignal.awgn.set_samples(par_awgn_samp = 1) \n
		Sets the number of samples generated for the AWGN waveform. \n
			:param par_awgn_samp: integer Range: 1E6 to 1E9
		"""
		param = Conversions.decimal_value_to_str(par_awgn_samp)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TSIGnal:AWGN:SAMPles {param}')

	def clone(self) -> 'Awgn':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Awgn(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
