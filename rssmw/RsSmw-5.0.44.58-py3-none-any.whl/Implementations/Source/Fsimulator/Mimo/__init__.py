from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 427 total commands, 6 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def copy(self):
		"""copy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_copy'):
			from .Copy import Copy
			self._copy = Copy(self._core, self._cmd_group)
		return self._copy

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def scwi(self):
		"""scwi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scwi'):
			from .Scwi import Scwi
			self._scwi = Scwi(self._core, self._cmd_group)
		return self._scwi

	@property
	def tap(self):
		"""tap commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_tap'):
			from .Tap import Tap
			self._tap = Tap(self._core, self._cmd_group)
		return self._tap

	@property
	def tgn(self):
		"""tgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tgn'):
			from .Tgn import Tgn
			self._tgn = Tgn(self._core, self._cmd_group)
		return self._tgn

	def get_capability(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:CAPability \n
		Snippet: value: str = driver.source.fsimulator.mimo.get_capability() \n
		Queries the supported MIMO configurations. \n
			:return: mimo_capability: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:CAPability?')
		return trim_str_response(response)

	def copy_all(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:COPY:ALL \n
		Snippet: driver.source.fsimulator.mimo.copy_all() \n
		Applies the matrix values of the current tap to all taps. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:COPY:ALL')

	def copy_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:COPY:ALL \n
		Snippet: driver.source.fsimulator.mimo.copy_all_with_opc() \n
		Applies the matrix values of the current tap to all taps. \n
		Same as copy_all, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:MIMO:COPY:ALL', opc_timeout_ms)

	def set_md_load(self, md_load: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:MDLoad \n
		Snippet: driver.source.fsimulator.mimo.set_md_load(md_load = '1') \n
		Loads file with saved MIMO settings. \n
			:param md_load: string
		"""
		param = Conversions.value_to_quoted_str(md_load)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:MDLoad {param}')

	def set_md_store(self, md_store: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:MDSTore \n
		Snippet: driver.source.fsimulator.mimo.set_md_store(md_store = '1') \n
		Saves the MIMO settings in a file. \n
			:param md_store: string
		"""
		param = Conversions.value_to_quoted_str(md_store)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:MDSTore {param}')

	def get_mpower(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:MPOWer \n
		Snippet: value: float = driver.source.fsimulator.mimo.get_mpower() \n
		No command help available \n
			:return: mpower: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:MPOWer?')
		return Conversions.str_to_float(response)

	def set_mpower(self, mpower: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:MPOWer \n
		Snippet: driver.source.fsimulator.mimo.set_mpower(mpower = 1.0) \n
		No command help available \n
			:param mpower: No help available
		"""
		param = Conversions.decimal_value_to_str(mpower)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:MPOWer {param}')

	# noinspection PyTypeChecker
	def get_subset(self) -> enums.FadMimoSubSet:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SUBSet \n
		Snippet: value: enums.FadMimoSubSet = driver.source.fsimulator.mimo.get_subset() \n
		In 8x8 MIMO configuration, sets the subset of MIMO channels that is calculated by the particular R&S SMW. \n
			:return: subset: SET2| SET1 | ALL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:SUBSet?')
		return Conversions.str_to_scalar_enum(response, enums.FadMimoSubSet)

	def set_subset(self, subset: enums.FadMimoSubSet) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:SUBSet \n
		Snippet: driver.source.fsimulator.mimo.set_subset(subset = enums.FadMimoSubSet.ALL) \n
		In 8x8 MIMO configuration, sets the subset of MIMO channels that is calculated by the particular R&S SMW. \n
			:param subset: SET2| SET1 | ALL
		"""
		param = Conversions.enum_scalar_to_str(subset, enums.FadMimoSubSet)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:SUBSet {param}')

	def clone(self) -> 'Mimo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mimo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
