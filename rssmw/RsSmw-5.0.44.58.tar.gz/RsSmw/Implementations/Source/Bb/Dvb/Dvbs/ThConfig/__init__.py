from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThConfig:
	"""ThConfig commands group definition. 9 total commands, 4 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thConfig", core, parent)

	@property
	def afield(self):
		"""afield commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_afield'):
			from .Afield import Afield
			self._afield = Afield(self._core, self._cmd_group)
		return self._afield

	@property
	def payload(self):
		"""payload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import Payload
			self._payload = Payload(self._core, self._cmd_group)
		return self._payload

	@property
	def pid(self):
		"""pid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pid'):
			from .Pid import Pid
			self._pid = Pid(self._core, self._cmd_group)
		return self._pid

	@property
	def teIndication(self):
		"""teIndication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_teIndication'):
			from .TeIndication import TeIndication
			self._teIndication = TeIndication(self._core, self._cmd_group)
		return self._teIndication

	def get_ccounter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:CCOunter \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.thConfig.get_ccounter() \n
		Sets the sequence number of the first payload packet. \n
			:return: ccounter: integer Range: 0 to 15
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:CCOunter?')
		return Conversions.str_to_int(response)

	def set_ccounter(self, ccounter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:CCOunter \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.set_ccounter(ccounter = 1) \n
		Sets the sequence number of the first payload packet. \n
			:param ccounter: integer Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(ccounter)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:CCOunter {param}')

	def get_pus(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:PUS \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.thConfig.get_pus() \n
		If enabled, the PES (packetized elementary streams) , PSI (program specific information) , or DVB-MIP (megaframe
		initialization) packet begin immediately after the header. \n
			:return: psu_indication: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:PUS?')
		return Conversions.str_to_bool(response)

	def set_pus(self, psu_indication: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:PUS \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.set_pus(psu_indication = False) \n
		If enabled, the PES (packetized elementary streams) , PSI (program specific information) , or DVB-MIP (megaframe
		initialization) packet begin immediately after the header. \n
			:param psu_indication: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(psu_indication)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:PUS {param}')

	def get_scontrol(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:SCONtrol \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.thConfig.get_scontrol() \n
		Sets the scrambling information. \n
			:return: scontrol: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:SCONtrol?')
		return Conversions.str_to_int(response)

	def set_scontrol(self, scontrol: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:SCONtrol \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.set_scontrol(scontrol = 1) \n
		Sets the scrambling information. \n
			:param scontrol: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(scontrol)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:SCONtrol {param}')

	def get_tpriority(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:TPRiority \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.thConfig.get_tpriority() \n
		Marks the current packet as high priority packet compared to packets with the same PID. \n
			:return: tpriority: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:TPRiority?')
		return Conversions.str_to_int(response)

	def set_tpriority(self, tpriority: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:TPRiority \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.set_tpriority(tpriority = 1) \n
		Marks the current packet as high priority packet compared to packets with the same PID. \n
			:param tpriority: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(tpriority)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:TPRiority {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.thConfig.get_state() \n
		Inserts header information in the transport stream. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.set_state(state = False) \n
		Inserts header information in the transport stream. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:STATe {param}')

	def clone(self) -> 'ThConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ThConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
