from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 16 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def defSetting(self):
		"""defSetting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_defSetting'):
			from .DefSetting import DefSetting
			self._defSetting = DefSetting(self._core, self._cmd_group)
		return self._defSetting

	@property
	def ilength(self):
		"""ilength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ilength'):
			from .Ilength import Ilength
			self._ilength = Ilength(self._core, self._cmd_group)
		return self._ilength

	@property
	def osampling(self):
		"""osampling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_osampling'):
			from .Osampling import Osampling
			self._osampling = Osampling(self._core, self._cmd_group)
		return self._osampling

	@property
	def parameter(self):
		"""parameter commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_parameter'):
			from .Parameter import Parameter
			self._parameter = Parameter(self._core, self._cmd_group)
		return self._parameter

	def get_iup_sampling(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:IUPSampling \n
		Snippet: value: bool = driver.source.bb.wlnn.filterPy.get_iup_sampling() \n
		Activates inverted Fast Fourier Transformation (IFFT) upsampling. \n
			:return: ifftupsampling: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:FILTer:IUPSampling?')
		return Conversions.str_to_bool(response)

	def set_iup_sampling(self, ifftupsampling: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:IUPSampling \n
		Snippet: driver.source.bb.wlnn.filterPy.set_iup_sampling(ifftupsampling = False) \n
		Activates inverted Fast Fourier Transformation (IFFT) upsampling. \n
			:param ifftupsampling: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ifftupsampling)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FILTer:IUPSampling {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFilterA:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:TYPE \n
		Snippet: value: enums.DmFilterA = driver.source.bb.wlnn.filterPy.get_type_py() \n
		(for system bandwidth set to 20 MHz only) The command selects the filter type. \n
			:return: type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LPASSEVM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFilterA)

	def set_type_py(self, type_py: enums.DmFilterA) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FILTer:TYPE \n
		Snippet: driver.source.bb.wlnn.filterPy.set_type_py(type_py = enums.DmFilterA.APCO25) \n
		(for system bandwidth set to 20 MHz only) The command selects the filter type. \n
			:param type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LPASSEVM
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFilterA)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
