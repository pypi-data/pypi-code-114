from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 10 total commands, 3 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def dall(self):
		"""dall commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dall'):
			from .Dall import Dall
			self._dall = Dall(self._core, self._cmd_group)
		return self._dall

	@property
	def eall(self):
		"""eall commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eall'):
			from .Eall import Eall
			self._eall = Eall(self._core, self._cmd_group)
		return self._eall

	@property
	def logPoint(self):
		"""logPoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logPoint'):
			from .LogPoint import LogPoint
			self._logPoint = LogPoint(self._core, self._cmd_group)
		return self._logPoint

	def get_eu_logging(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:EULogging \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_eu_logging() \n
		No command help available \n
			:return: ext_uci_log: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:EULogging?')
		return Conversions.str_to_bool(response)

	def set_eu_logging(self, ext_uci_log: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:EULogging \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_eu_logging(ext_uci_log = False) \n
		No command help available \n
			:param ext_uci_log: No help available
		"""
		param = Conversions.bool_to_str(ext_uci_log)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:EULogging {param}')

	def get_prach(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PRACh \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_prach() \n
		No command help available \n
			:return: prach_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:PRACh?')
		return Conversions.str_to_bool(response)

	def set_prach(self, prach_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PRACh \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_prach(prach_log_state = False) \n
		No command help available \n
			:param prach_log_state: No help available
		"""
		param = Conversions.bool_to_str(prach_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:PRACh {param}')

	def get_pucch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUCCh \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_pucch() \n
		No command help available \n
			:return: pucch_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUCCh?')
		return Conversions.str_to_bool(response)

	def set_pucch(self, pucch_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUCCh \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_pucch(pucch_log_state = False) \n
		No command help available \n
			:param pucch_log_state: No help available
		"""
		param = Conversions.bool_to_str(pucch_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUCCh {param}')

	def get_pucdrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUCDrs \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_pucdrs() \n
		No command help available \n
			:return: pusch_drs_log: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUCDrs?')
		return Conversions.str_to_bool(response)

	def set_pucdrs(self, pusch_drs_log: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUCDrs \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_pucdrs(pusch_drs_log = False) \n
		No command help available \n
			:param pusch_drs_log: No help available
		"""
		param = Conversions.bool_to_str(pusch_drs_log)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUCDrs {param}')

	def get_pusch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUSCh \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_pusch() \n
		No command help available \n
			:return: pusch_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUSCh?')
		return Conversions.str_to_bool(response)

	def set_pusch(self, pusch_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUSCh \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_pusch(pusch_log_state = False) \n
		No command help available \n
			:param pusch_log_state: No help available
		"""
		param = Conversions.bool_to_str(pusch_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUSCh {param}')

	def get_pusdrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUSDrs \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_pusdrs() \n
		No command help available \n
			:return: pusch_drs_log: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUSDrs?')
		return Conversions.str_to_bool(response)

	def set_pusdrs(self, pusch_drs_log: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:PUSDrs \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_pusdrs(pusch_drs_log = False) \n
		No command help available \n
			:param pusch_drs_log: No help available
		"""
		param = Conversions.bool_to_str(pusch_drs_log)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:PUSDrs {param}')

	def get_srs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:SRS \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.uplink.get_srs() \n
		No command help available \n
			:return: srs_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:UL:SRS?')
		return Conversions.str_to_bool(response)

	def set_srs(self, srs_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:UL:SRS \n
		Snippet: driver.source.bb.v5G.logGen.uplink.set_srs(srs_state = False) \n
		No command help available \n
			:param srs_state: No help available
		"""
		param = Conversions.bool_to_str(srs_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:UL:SRS {param}')

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
