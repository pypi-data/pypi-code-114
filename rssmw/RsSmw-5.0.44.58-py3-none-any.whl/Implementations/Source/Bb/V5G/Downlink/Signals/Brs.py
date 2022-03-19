from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Brs:
	"""Brs commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("brs", core, parent)

	# noinspection PyTypeChecker
	def get_btr_period(self) -> enums.BrsTransPeriod:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SIGNals:BRS:BTRPeriod \n
		Snippet: value: enums.BrsTransPeriod = driver.source.bb.v5G.downlink.signals.brs.get_btr_period() \n
		Specifies the beam reference signal transmission period signaled via . \n
			:return: trans_period: P00| P01| P10| P11 P00: single-slot ( 5 ms) , maximum 7 downlink transmitting beams per antenna port P01: single-subframe (= 5 ms) , maximum 14 downlink transmitting beams per antenna port P10: two-subframe (= 10 ms) , maximum 28 downlink transmitting beams per antenna port P11: four-subframe (= 20 ms) , maximum 56 downlink transmitting beams per antenna port
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SIGNals:BRS:BTRPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.BrsTransPeriod)

	def set_btr_period(self, trans_period: enums.BrsTransPeriod) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SIGNals:BRS:BTRPeriod \n
		Snippet: driver.source.bb.v5G.downlink.signals.brs.set_btr_period(trans_period = enums.BrsTransPeriod.P00) \n
		Specifies the beam reference signal transmission period signaled via . \n
			:param trans_period: P00| P01| P10| P11 P00: single-slot ( 5 ms) , maximum 7 downlink transmitting beams per antenna port P01: single-subframe (= 5 ms) , maximum 14 downlink transmitting beams per antenna port P10: two-subframe (= 10 ms) , maximum 28 downlink transmitting beams per antenna port P11: four-subframe (= 20 ms) , maximum 56 downlink transmitting beams per antenna port
		"""
		param = Conversions.enum_scalar_to_str(trans_period, enums.BrsTransPeriod)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SIGNals:BRS:BTRPeriod {param}')

	# noinspection PyTypeChecker
	def get_nap(self) -> enums.CsiRsNumAp:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SIGNals:BRS:NAP \n
		Snippet: value: enums.CsiRsNumAp = driver.source.bb.v5G.downlink.signals.brs.get_nap() \n
		Specifies the number of antenna ports (one, two, four or eight) the BRSs are transmitted on. \n
			:return: brs_num_ap: AP1| AP2| AP4| AP8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SIGNals:BRS:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.CsiRsNumAp)

	def set_nap(self, brs_num_ap: enums.CsiRsNumAp) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SIGNals:BRS:NAP \n
		Snippet: driver.source.bb.v5G.downlink.signals.brs.set_nap(brs_num_ap = enums.CsiRsNumAp.AP1) \n
		Specifies the number of antenna ports (one, two, four or eight) the BRSs are transmitted on. \n
			:param brs_num_ap: AP1| AP2| AP4| AP8
		"""
		param = Conversions.enum_scalar_to_str(brs_num_ap, enums.CsiRsNumAp)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SIGNals:BRS:NAP {param}')
