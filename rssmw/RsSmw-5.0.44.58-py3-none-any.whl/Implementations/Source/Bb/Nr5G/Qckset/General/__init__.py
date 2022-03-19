from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class General:
	"""General commands group definition. 16 total commands, 1 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("general", core, parent)

	@property
	def es(self):
		"""es commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_es'):
			from .Es import Es
			self._es = Es(self._core, self._cmd_group)
		return self._es

	# noinspection PyTypeChecker
	def get_cardeply(self) -> enums.Nr5GcarDep:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CARDeply \n
		Snippet: value: enums.Nr5GcarDep = driver.source.bb.nr5G.qckset.general.get_cardeply() \n
		Selects one of the frequency ranges, specified for 5G NR transmission. \n
			:return: qck_set_car_deply: FR1LT3| FR1GT3| FR2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CARDeply?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5GcarDep)

	def set_cardeply(self, qck_set_car_deply: enums.Nr5GcarDep) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CARDeply \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_cardeply(qck_set_car_deply = enums.Nr5GcarDep.BT36) \n
		Selects one of the frequency ranges, specified for 5G NR transmission. \n
			:param qck_set_car_deply: FR1LT3| FR1GT3| FR2
		"""
		param = Conversions.enum_scalar_to_str(qck_set_car_deply, enums.Nr5GcarDep)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CARDeply {param}')

	# noinspection PyTypeChecker
	def get_cbw(self) -> enums.Nr5Gcbw:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CBW \n
		Snippet: value: enums.Nr5Gcbw = driver.source.bb.nr5G.qckset.general.get_cbw() \n
		Selects the bandwidth of the node carrier. \n
			:return: qck_set_channel_bw: BW5| BW10| BW15| BW20| BW25| BW30| BW40| BW50| BW60| BW70| BW80| BW90| BW100| BW200| BW400
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CBW?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5Gcbw)

	def set_cbw(self, qck_set_channel_bw: enums.Nr5Gcbw) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CBW \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_cbw(qck_set_channel_bw = enums.Nr5Gcbw.BW10) \n
		Selects the bandwidth of the node carrier. \n
			:param qck_set_channel_bw: BW5| BW10| BW15| BW20| BW25| BW30| BW40| BW50| BW60| BW70| BW80| BW90| BW100| BW200| BW400
		"""
		param = Conversions.enum_scalar_to_str(qck_set_channel_bw, enums.Nr5Gcbw)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CBW {param}')

	def get_cct_model(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CCTModel \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.general.get_cct_model() \n
		Creates a copy of a component carrier based on a test model configuration.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a single carrier ([:SOURce<hw>]:BB:NR5G:QCKSet:GENeral:NCARier) .
			- Select a test model ([:SOURce<hw>]:BB:NR5G:SETTing:TMODel:DL / [:SOURce<hw>]:BB:NR5G:SETTing:TMODel:UL) . \n
			:return: qck_set_use_tm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CCTModel?')
		return Conversions.str_to_bool(response)

	def set_cct_model(self, qck_set_use_tm: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CCTModel \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_cct_model(qck_set_use_tm = False) \n
		Creates a copy of a component carrier based on a test model configuration.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a single carrier ([:SOURce<hw>]:BB:NR5G:QCKSet:GENeral:NCARier) .
			- Select a test model ([:SOURce<hw>]:BB:NR5G:SETTing:TMODel:DL / [:SOURce<hw>]:BB:NR5G:SETTing:TMODel:UL) . \n
			:param qck_set_use_tm: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(qck_set_use_tm)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CCTModel {param}')

	# noinspection PyTypeChecker
	def get_ch_raster(self) -> enums.AllChannelRaster:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CHRaster \n
		Snippet: value: enums.AllChannelRaster = driver.source.bb.nr5G.qckset.general.get_ch_raster() \n
		Sets the 'Channel Raster' based on the set 'Deployment'. If 'Deployment' is set to 'FR1 ≤ 3GHz' or 'FR1 > 3GHz' the
		'Channel Raster' can be set to 15 kHz or 100 kHz. If 'Deployment' is set to 'FR2' the 'Channel Raster' is set to 60 kHz.
		'Channel Raster' is not displayed when the 'Number of Carriers' is shown inactive. \n
			:return: channel_raster: R15| R60| R100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CHRaster?')
		return Conversions.str_to_scalar_enum(response, enums.AllChannelRaster)

	def set_ch_raster(self, channel_raster: enums.AllChannelRaster) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CHRaster \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_ch_raster(channel_raster = enums.AllChannelRaster.R100) \n
		Sets the 'Channel Raster' based on the set 'Deployment'. If 'Deployment' is set to 'FR1 ≤ 3GHz' or 'FR1 > 3GHz' the
		'Channel Raster' can be set to 15 kHz or 100 kHz. If 'Deployment' is set to 'FR2' the 'Channel Raster' is set to 60 kHz.
		'Channel Raster' is not displayed when the 'Number of Carriers' is shown inactive. \n
			:param channel_raster: R15| R60| R100
		"""
		param = Conversions.enum_scalar_to_str(channel_raster, enums.AllChannelRaster)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CHRaster {param}')

	def get_ch_spacing(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CHSPacing \n
		Snippet: value: int = driver.source.bb.nr5G.qckset.general.get_ch_spacing() \n
		Queries or sets the value for the 'Channel Spacing'. It is by default automatically calculated by the set 'Channel
		Raster' and the set 'Channel Bandwidth'. The value can be manually adjusted, but is recalculated if the 'Channel Raster'
		or the 'Channel Bandwidth' is adjusted. 'Channel Spacing' is not displayed when the 'Number of Carriers' is shown
		inactive. In this case, it is used like 'Carrier Spacing' equals 0. \n
			:return: channel_spacing: integer Range: 0 to 400E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CHSPacing?')
		return Conversions.str_to_int(response)

	def set_ch_spacing(self, channel_spacing: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:CHSPacing \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_ch_spacing(channel_spacing = 1) \n
		Queries or sets the value for the 'Channel Spacing'. It is by default automatically calculated by the set 'Channel
		Raster' and the set 'Channel Bandwidth'. The value can be manually adjusted, but is recalculated if the 'Channel Raster'
		or the 'Channel Bandwidth' is adjusted. 'Channel Spacing' is not displayed when the 'Number of Carriers' is shown
		inactive. In this case, it is used like 'Carrier Spacing' equals 0. \n
			:param channel_spacing: integer Range: 0 to 400E6
		"""
		param = Conversions.decimal_value_to_str(channel_spacing)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:CHSPacing {param}')

	# noinspection PyTypeChecker
	def get_duplexing(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:DUPLexing \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.nr5G.qckset.general.get_duplexing() \n
		Selects the duplexing mode. \n
			:return: qck_set_duplexing: TDD| FDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplexing(self, qck_set_duplexing: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:DUPLexing \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_duplexing(qck_set_duplexing = enums.EutraDuplexMode.FDD) \n
		Selects the duplexing mode. \n
			:param qck_set_duplexing: TDD| FDD
		"""
		param = Conversions.enum_scalar_to_str(qck_set_duplexing, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:DUPLexing {param}')

	def get_ecp_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ECPState \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.general.get_ecp_state() \n
		Show if the extended cyclic prefix is enabled or disabled. \n
			:return: qss_cs_ecp_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ECPState?')
		return Conversions.str_to_bool(response)

	def set_ecp_state(self, qss_cs_ecp_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ECPState \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_ecp_state(qss_cs_ecp_state = False) \n
		Show if the extended cyclic prefix is enabled or disabled. \n
			:param qss_cs_ecp_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(qss_cs_ecp_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ECPState {param}')

	def get_ncarrier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:NCARier \n
		Snippet: value: int = driver.source.bb.nr5G.qckset.general.get_ncarrier() \n
		Selects the number of carriers. Needed for carrier aggregation. \n
			:return: qck_set_num_carrier: integer Range: 1 to 16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:NCARier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, qck_set_num_carrier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:NCARier \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_ncarrier(qck_set_num_carrier = 1) \n
		Selects the number of carriers. Needed for carrier aggregation. \n
			:param qck_set_num_carrier: integer Range: 1 to 16
		"""
		param = Conversions.decimal_value_to_str(qck_set_num_carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:NCARier {param}')

	# noinspection PyTypeChecker
	def get_sc_spacing(self) -> enums.QucjSettingsScsAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:SCSPacing \n
		Snippet: value: enums.QucjSettingsScsAll = driver.source.bb.nr5G.qckset.general.get_sc_spacing() \n
		Sets the subcarrier spacing. \n
			:return: qck_set_scs: SCS15| SCS30| SCS60| SCS120| SCS240| SCS480| SCS960
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.QucjSettingsScsAll)

	def set_sc_spacing(self, qck_set_scs: enums.QucjSettingsScsAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:SCSPacing \n
		Snippet: driver.source.bb.nr5G.qckset.general.set_sc_spacing(qck_set_scs = enums.QucjSettingsScsAll.N120) \n
		Sets the subcarrier spacing. \n
			:param qck_set_scs: SCS15| SCS30| SCS60| SCS120| SCS240| SCS480| SCS960
		"""
		param = Conversions.enum_scalar_to_str(qck_set_scs, enums.QucjSettingsScsAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:SCSPacing {param}')

	def clone(self) -> 'General':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = General(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
