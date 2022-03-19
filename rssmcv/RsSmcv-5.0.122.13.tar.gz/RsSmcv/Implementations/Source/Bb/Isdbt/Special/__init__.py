from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Special:
	"""Special commands group definition. 6 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("special", core, parent)

	@property
	def alert(self):
		"""alert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alert'):
			from .Alert import Alert
			self._alert = Alert(self._core, self._cmd_group)
		return self._alert

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def tmcc(self):
		"""tmcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmcc'):
			from .Tmcc import Tmcc
			self._tmcc = Tmcc(self._core, self._cmd_group)
		return self._tmcc

	# noinspection PyTypeChecker
	def get_ac_data_2(self) -> enums.SpecialAcData:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:ACData2 \n
		Snippet: value: enums.SpecialAcData = driver.source.bb.isdbt.special.get_ac_data_2() \n
		Sets the carrier modulation. \n
			:return: ac_data_2: ALL1| PRBS ALL1 Sets all carriers to 1. PRBS Sets PRBS modulated carriers. You can set the PRBS length via [:SOURcehw]:BB:ISDBt:PRBS[:SEQuence].
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SPECial:ACData2?')
		return Conversions.str_to_scalar_enum(response, enums.SpecialAcData)

	def set_ac_data_2(self, ac_data_2: enums.SpecialAcData) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:ACData2 \n
		Snippet: driver.source.bb.isdbt.special.set_ac_data_2(ac_data_2 = enums.SpecialAcData.ALL1) \n
		Sets the carrier modulation. \n
			:param ac_data_2: ALL1| PRBS ALL1 Sets all carriers to 1. PRBS Sets PRBS modulated carriers. You can set the PRBS length via [:SOURcehw]:BB:ISDBt:PRBS[:SEQuence].
		"""
		param = Conversions.enum_scalar_to_str(ac_data_2, enums.SpecialAcData)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SPECial:ACData2 {param}')

	def get_reed_solomon(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:REEDsolomon \n
		Snippet: value: bool = driver.source.bb.isdbt.special.get_reed_solomon() \n
		Enables/disables the Reed-Solomon encoder. \n
			:return: reed_solomon: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SPECial:REEDsolomon?')
		return Conversions.str_to_bool(response)

	def set_reed_solomon(self, reed_solomon: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:REEDsolomon \n
		Snippet: driver.source.bb.isdbt.special.set_reed_solomon(reed_solomon = False) \n
		Enables/disables the Reed-Solomon encoder. \n
			:param reed_solomon: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(reed_solomon)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SPECial:REEDsolomon {param}')

	# noinspection PyTypeChecker
	def get_tx_param(self) -> enums.IsdbtSpecialTxParam:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:TXParam \n
		Snippet: value: enums.IsdbtSpecialTxParam = driver.source.bb.isdbt.special.get_tx_param() \n
		Defines the static setting of the transmission parameter switching indicator. \n
			:return: tx_param_sw_ind: N1| N2| N11| N12| N13| N14| N15| NORMal| N2| N4| N5| N6| N7| N8| N9| N10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SPECial:TXParam?')
		return Conversions.str_to_scalar_enum(response, enums.IsdbtSpecialTxParam)

	def set_tx_param(self, tx_param_sw_ind: enums.IsdbtSpecialTxParam) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:TXParam \n
		Snippet: driver.source.bb.isdbt.special.set_tx_param(tx_param_sw_ind = enums.IsdbtSpecialTxParam.N1) \n
		Defines the static setting of the transmission parameter switching indicator. \n
			:param tx_param_sw_ind: N1| N2| N11| N12| N13| N14| N15| NORMal| N2| N4| N5| N6| N7| N8| N9| N10
		"""
		param = Conversions.enum_scalar_to_str(tx_param_sw_ind, enums.IsdbtSpecialTxParam)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SPECial:TXParam {param}')

	def clone(self) -> 'Special':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Special(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
