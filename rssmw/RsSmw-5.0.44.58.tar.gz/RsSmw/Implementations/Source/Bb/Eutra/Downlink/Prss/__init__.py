from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prss:
	"""Prss commands group definition. 8 total commands, 2 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prss", core, parent)

	@property
	def miPattern(self):
		"""miPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_miPattern'):
			from .MiPattern import MiPattern
			self._miPattern = MiPattern(self._core, self._cmd_group)
		return self._miPattern

	@property
	def tprs(self):
		"""tprs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprs'):
			from .Tprs import Tprs
			self._tprs = Tprs(self._core, self._cmd_group)
		return self._tprs

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.EutraCaChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:BW \n
		Snippet: value: enums.EutraCaChannelBandwidth = driver.source.bb.eutra.downlink.prss.get_bw() \n
		Defines the bandwidth in which the PRS is transmitted. \n
			:return: prs_bandwidth: BW1_40| BW3_00| BW5_00| BW10_00| BW15_00| BW20_00
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:BW?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCaChannelBandwidth)

	def set_bw(self, prs_bandwidth: enums.EutraCaChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:BW \n
		Snippet: driver.source.bb.eutra.downlink.prss.set_bw(prs_bandwidth = enums.EutraCaChannelBandwidth.BW1_40) \n
		Defines the bandwidth in which the PRS is transmitted. \n
			:param prs_bandwidth: BW1_40| BW3_00| BW5_00| BW10_00| BW15_00| BW20_00
		"""
		param = Conversions.enum_scalar_to_str(prs_bandwidth, enums.EutraCaChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PRSS:BW {param}')

	def get_ci(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:CI \n
		Snippet: value: int = driver.source.bb.eutra.downlink.prss.get_ci() \n
		Sets the PRS Configuration Index IPRS as defined in 3GPP TS 36.211, table 6.10.4.3-1. \n
			:return: conf_idx: integer Range: 0 to 2399
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:CI?')
		return Conversions.str_to_int(response)

	def set_ci(self, conf_idx: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:CI \n
		Snippet: driver.source.bb.eutra.downlink.prss.set_ci(conf_idx = 1) \n
		Sets the PRS Configuration Index IPRS as defined in 3GPP TS 36.211, table 6.10.4.3-1. \n
			:param conf_idx: integer Range: 0 to 2399
		"""
		param = Conversions.decimal_value_to_str(conf_idx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PRSS:CI {param}')

	def get_dprs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:DPRS \n
		Snippet: value: int = driver.source.bb.eutra.downlink.prss.get_dprs() \n
		Queries the subframe offset of the PRS generation (DeltaPRS) as defined in 3GPP TS 36.211, table 6.10.4.3-1. \n
			:return: delta_prs: integer Range: 0 to 1279
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:DPRS?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_nprs(self) -> enums.Nprs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:NPRS \n
		Snippet: value: enums.Nprs = driver.source.bb.eutra.downlink.prss.get_nprs() \n
		Defines the number of consecutive DL subframes in that PRS are transmitted. \n
			:return: number_prs: 1| 2| 4| 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:NPRS?')
		return Conversions.str_to_scalar_enum(response, enums.Nprs)

	def set_nprs(self, number_prs: enums.Nprs) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:NPRS \n
		Snippet: driver.source.bb.eutra.downlink.prss.set_nprs(number_prs = enums.Nprs._1) \n
		Defines the number of consecutive DL subframes in that PRS are transmitted. \n
			:param number_prs: 1| 2| 4| 6
		"""
		param = Conversions.enum_scalar_to_str(number_prs, enums.Nprs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PRSS:NPRS {param}')

	def get_pow(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:POW \n
		Snippet: value: float = driver.source.bb.eutra.downlink.prss.get_pow() \n
		Sets the power of a PRS resource element relative to the power of a common reference signal resource element. \n
			:return: prs_power: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:POW?')
		return Conversions.str_to_float(response)

	def set_pow(self, prs_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:POW \n
		Snippet: driver.source.bb.eutra.downlink.prss.set_pow(prs_power = 1.0) \n
		Sets the power of a PRS resource element relative to the power of a common reference signal resource element. \n
			:param prs_power: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(prs_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PRSS:POW {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.prss.get_state() \n
		Enables the generation of the PRS. \n
			:return: prs_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PRSS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, prs_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PRSS:STATe \n
		Snippet: driver.source.bb.eutra.downlink.prss.set_state(prs_state = False) \n
		Enables the generation of the PRS. \n
			:param prs_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(prs_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PRSS:STATe {param}')

	def clone(self) -> 'Prss':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prss(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
