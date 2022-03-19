from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfi:
	"""Sfi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfi", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:SSC:SFI:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.frmFormat.ssc.sfi.get_state() \n
		Turns usage of the special slot format on and off. If on, select a special frame as defined by 3GPP with
		[:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:SLFMt.
			INTRO_CMD_HELP: If off, select the number of symbols with \n
			- Downlink: [:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:NDLSymbols
			- Uplink: [:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:NULSymbols \n
			:return: qck_set_use_slot: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:SSC:SFI:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qck_set_use_slot: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:SSC:SFI:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.frmFormat.ssc.sfi.set_state(qck_set_use_slot = False) \n
		Turns usage of the special slot format on and off. If on, select a special frame as defined by 3GPP with
		[:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:SLFMt.
			INTRO_CMD_HELP: If off, select the number of symbols with \n
			- Downlink: [:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:NDLSymbols
			- Uplink: [:SOURce<hw>]:BB:NR5G:QCKSet:FRMFormat:SSC:NULSymbols \n
			:param qck_set_use_slot: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(qck_set_use_slot)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:SSC:SFI:STATe {param}')
