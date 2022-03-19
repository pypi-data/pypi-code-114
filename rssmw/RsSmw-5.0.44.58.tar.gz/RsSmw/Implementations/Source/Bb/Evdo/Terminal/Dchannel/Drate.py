from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drate:
	"""Drate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drate", core, parent)

	def set(self, drate: enums.EvdoDataRate, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:DRATe \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.drate.set(drate = enums.EvdoDataRate.DR1075K2, terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in access mode) Selects the data rate for the Data Channel. \n
			:param drate: DR4K8| DR9K6| DR19K2| DR38K4| DR76K8| DR153K6| DR307K2| DR614K4| DR921K6| DR1228K8| DR1536K| DR1843K2| DR2457K6| DR3072K| DR460K8| DR768K| DR1075K2| DR2150K4| DR3686K4| DR4300K8| DR4915K2
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(drate, enums.EvdoDataRate)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:DRATe {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.EvdoDataRate:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:DRATe \n
		Snippet: value: enums.EvdoDataRate = driver.source.bb.evdo.terminal.dchannel.drate.get(terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in access mode) Selects the data rate for the Data Channel. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: drate: DR4K8| DR9K6| DR19K2| DR38K4| DR76K8| DR153K6| DR307K2| DR614K4| DR921K6| DR1228K8| DR1536K| DR1843K2| DR2457K6| DR3072K| DR460K8| DR768K| DR1075K2| DR2150K4| DR3686K4| DR4300K8| DR4915K2"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:DRATe?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoDataRate)
