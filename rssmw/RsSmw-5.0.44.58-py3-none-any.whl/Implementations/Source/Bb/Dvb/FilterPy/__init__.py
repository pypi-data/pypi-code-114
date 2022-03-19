from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 12 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def parameter(self):
		"""parameter commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_parameter'):
			from .Parameter import Parameter
			self._parameter = Parameter(self._core, self._cmd_group)
		return self._parameter

	# noinspection PyTypeChecker
	def get_ro_factor(self) -> enums.DvbS2XrollOff:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:ROFactor \n
		Snippet: value: enums.DvbS2XrollOff = driver.source.bb.dvb.filterPy.get_ro_factor() \n
		Sets the filter parameter. \n
			:return: roff: RO35| RO25| RO20| RO15| RO10| RO05
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:FILTer:ROFactor?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XrollOff)

	def set_ro_factor(self, roff: enums.DvbS2XrollOff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:ROFactor \n
		Snippet: driver.source.bb.dvb.filterPy.set_ro_factor(roff = enums.DvbS2XrollOff.RO05) \n
		Sets the filter parameter. \n
			:param roff: RO35| RO25| RO20| RO15| RO10| RO05
		"""
		param = Conversions.enum_scalar_to_str(roff, enums.DvbS2XrollOff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:FILTer:ROFactor {param}')

	# noinspection PyTypeChecker
	def get_ro_range(self) -> enums.LowHigh:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:RORange \n
		Snippet: value: enums.LowHigh = driver.source.bb.dvb.filterPy.get_ro_range() \n
		Sets whether the high or the low filter roll-off range is used. \n
			:return: ro_range: HIGH| LOW
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:FILTer:RORange?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ro_range(self, ro_range: enums.LowHigh) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:RORange \n
		Snippet: driver.source.bb.dvb.filterPy.set_ro_range(ro_range = enums.LowHigh.HIGH) \n
		Sets whether the high or the low filter roll-off range is used. \n
			:param ro_range: HIGH| LOW
		"""
		param = Conversions.enum_scalar_to_str(ro_range, enums.LowHigh)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:FILTer:RORange {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFilterA:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:TYPE \n
		Snippet: value: enums.DmFilterA = driver.source.bb.dvb.filterPy.get_type_py() \n
		Selects the filter type. \n
			:return: type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LPASSEVM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFilterA)

	def set_type_py(self, type_py: enums.DmFilterA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:FILTer:TYPE \n
		Snippet: driver.source.bb.dvb.filterPy.set_type_py(type_py = enums.DmFilterA.APCO25) \n
		Selects the filter type. \n
			:param type_py: RCOSine| COSine| GAUSs| LGAuss| CONE| COF705| COEQualizer| COFequalizer| C2K3x| APCO25| SPHase| RECTangle| PGAuss| LPASs| DIRac| ENPShape| EWPShape| LPASSEVM
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFilterA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
