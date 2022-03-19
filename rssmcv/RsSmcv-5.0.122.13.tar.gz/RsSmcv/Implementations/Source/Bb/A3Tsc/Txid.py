from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Txid:
	"""Txid commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txid", core, parent)

	def get_address(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:ADDRess \n
		Snippet: value: int = driver.source.bb.a3Tsc.txid.get_address() \n
		Sets the transmitter identification address. \n
			:return: tx_id_adress: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:TXId:ADDRess?')
		return Conversions.str_to_int(response)

	def set_address(self, tx_id_adress: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:ADDRess \n
		Snippet: driver.source.bb.a3Tsc.txid.set_address(tx_id_adress = 1) \n
		Sets the transmitter identification address. \n
			:param tx_id_adress: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(tx_id_adress)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:TXId:ADDRess {param}')

	# noinspection PyTypeChecker
	def get_level(self) -> enums.Atsc30TxIdInjectionLevel:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:LEVel \n
		Snippet: value: enums.Atsc30TxIdInjectionLevel = driver.source.bb.a3Tsc.txid.get_level() \n
		Sets the injection levels for injecting a TxID signal into the host preamble. \n
			:return: tx_id_inj_level: OFF| L450| L420| L390| L360| L330| L300| L270| L240| L210| L180| L150| L120| L90 Level Lx with x meaning the level in dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:TXId:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TxIdInjectionLevel)

	def set_level(self, tx_id_inj_level: enums.Atsc30TxIdInjectionLevel) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:LEVel \n
		Snippet: driver.source.bb.a3Tsc.txid.set_level(tx_id_inj_level = enums.Atsc30TxIdInjectionLevel.L120) \n
		Sets the injection levels for injecting a TxID signal into the host preamble. \n
			:param tx_id_inj_level: OFF| L450| L420| L390| L360| L330| L300| L270| L240| L210| L180| L150| L120| L90 Level Lx with x meaning the level in dB
		"""
		param = Conversions.enum_scalar_to_str(tx_id_inj_level, enums.Atsc30TxIdInjectionLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:TXId:LEVel {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Atsc30TxIdMode:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:MODE \n
		Snippet: value: enums.Atsc30TxIdMode = driver.source.bb.a3Tsc.txid.get_mode() \n
		Sets the Tx ID mode. The mode affects the setting of the 'TxID Address' and 'TxID Injection Level'. \n
			:return: tx_id_mode: MANual| AUTo| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:TXId:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TxIdMode)

	def set_mode(self, tx_id_mode: enums.Atsc30TxIdMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TXId:MODE \n
		Snippet: driver.source.bb.a3Tsc.txid.set_mode(tx_id_mode = enums.Atsc30TxIdMode.AUTo) \n
		Sets the Tx ID mode. The mode affects the setting of the 'TxID Address' and 'TxID Injection Level'. \n
			:param tx_id_mode: MANual| AUTo| OFF
		"""
		param = Conversions.enum_scalar_to_str(tx_id_mode, enums.Atsc30TxIdMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:TXId:MODE {param}')
