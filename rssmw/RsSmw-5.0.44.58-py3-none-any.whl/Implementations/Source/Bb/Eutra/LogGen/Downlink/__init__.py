from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 9 total commands, 3 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

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

	def get_ed_logging(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:EDLogging \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_ed_logging() \n
		Enables the generation of a logfile with extended information regarding the DCI/UCI mapping. \n
			:return: ext_dci_log: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:EDLogging?')
		return Conversions.str_to_bool(response)

	def set_ed_logging(self, ext_dci_log: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:EDLogging \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_ed_logging(ext_dci_log = False) \n
		Enables the generation of a logfile with extended information regarding the DCI/UCI mapping. \n
			:param ext_dci_log: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ext_dci_log)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:EDLogging {param}')

	def get_encc(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:ENCC \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_encc() \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:return: encc_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:ENCC?')
		return Conversions.str_to_bool(response)

	def set_encc(self, encc_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:ENCC \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_encc(encc_log_state = False) \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:param encc_log_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(encc_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:ENCC {param}')

	def get_nwus(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:NWUS \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_nwus() \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:return: nwus: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:NWUS?')
		return Conversions.str_to_bool(response)

	def set_nwus(self, nwus: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:NWUS \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_nwus(nwus = False) \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:param nwus: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(nwus)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:NWUS {param}')

	def get_pbch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PBCH \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_pbch() \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:return: pbch_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PBCH?')
		return Conversions.str_to_bool(response)

	def set_pbch(self, pbch_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PBCH \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_pbch(pbch_log_state = False) \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:param pbch_log_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pbch_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PBCH {param}')

	def get_pdsch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PDSCh \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_pdsch() \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:return: pdsch_log_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PDSCh?')
		return Conversions.str_to_bool(response)

	def set_pdsch(self, pdsch_log_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PDSCh \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_pdsch(pdsch_log_state = False) \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:param pdsch_log_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pdsch_log_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PDSCh {param}')

	def get_pmch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PMCH \n
		Snippet: value: bool = driver.source.bb.eutra.logGen.downlink.get_pmch() \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PMCH?')
		return Conversions.str_to_bool(response)

	def set_pmch(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LOGGen:DL:PMCH \n
		Snippet: driver.source.bb.eutra.logGen.downlink.set_pmch(state = False) \n
		Enables the channel or reference signal for that logfiles are generated. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LOGGen:DL:PMCH {param}')

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
