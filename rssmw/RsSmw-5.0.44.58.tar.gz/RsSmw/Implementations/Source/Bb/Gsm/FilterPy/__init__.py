from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 9 total commands, 7 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def aqPsk(self):
		"""aqPsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aqPsk'):
			from .AqPsk import AqPsk
			self._aqPsk = AqPsk(self._core, self._cmd_group)
		return self._aqPsk

	@property
	def edge(self):
		"""edge commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edge'):
			from .Edge import Edge
			self._edge = Edge(self._core, self._cmd_group)
		return self._edge

	@property
	def h16Qam(self):
		"""h16Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_h16Qam'):
			from .H16Qam import H16Qam
			self._h16Qam = H16Qam(self._core, self._cmd_group)
		return self._h16Qam

	@property
	def h32Qam(self):
		"""h32Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_h32Qam'):
			from .H32Qam import H32Qam
			self._h32Qam = H32Qam(self._core, self._cmd_group)
		return self._h32Qam

	@property
	def hqpsk(self):
		"""hqpsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hqpsk'):
			from .Hqpsk import Hqpsk
			self._hqpsk = Hqpsk(self._core, self._cmd_group)
		return self._hqpsk

	@property
	def n16Qam(self):
		"""n16Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n16Qam'):
			from .N16Qam import N16Qam
			self._n16Qam = N16Qam(self._core, self._cmd_group)
		return self._n16Qam

	@property
	def n32Qam(self):
		"""n32Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n32Qam'):
			from .N32Qam import N32Qam
			self._n32Qam = N32Qam(self._core, self._cmd_group)
		return self._n32Qam

	def get_parameter(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:PARameter \n
		Snippet: value: float = driver.source.bb.gsm.filterPy.get_parameter() \n
		The command sets the filter parameter. For Gaussian filter the BxT is the product of the bandwidth and the symbol
		duration. The default value for GSM modulation is 0.3 and for Gauss Linearized (EDGE) , BT = 0.3. \n
			:return: parameter: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FILTer:PARameter?')
		return Conversions.str_to_float(response)

	def set_parameter(self, parameter: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:PARameter \n
		Snippet: driver.source.bb.gsm.filterPy.set_parameter(parameter = 1.0) \n
		The command sets the filter parameter. For Gaussian filter the BxT is the product of the bandwidth and the symbol
		duration. The default value for GSM modulation is 0.3 and for Gauss Linearized (EDGE) , BT = 0.3. \n
			:param parameter: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(parameter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FILTer:PARameter {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.Gilter:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:TYPE \n
		Snippet: value: enums.Gilter = driver.source.bb.gsm.filterPy.get_type_py() \n
		The command sets the filter type GAUSs. This is the only possible selection in the case of digital standard GSM. \n
			:return: type_py: GAUSs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Gilter)

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
