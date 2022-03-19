from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_amss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:POWer:AMSS \n
		Snippet: value: float = driver.source.bb.xmRadio.terrestrial.power.get_amss() \n
		No command help available \n
			:return: amss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:TERRestrial:POWer:AMSS?')
		return Conversions.str_to_float(response)

	def set_amss(self, amss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:POWer:AMSS \n
		Snippet: driver.source.bb.xmRadio.terrestrial.power.set_amss(amss = 1.0) \n
		No command help available \n
			:param amss: No help available
		"""
		param = Conversions.decimal_value_to_str(amss)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:POWer:AMSS {param}')

	def get_mcm(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:POWer:MCM \n
		Snippet: value: float = driver.source.bb.xmRadio.terrestrial.power.get_mcm() \n
		No command help available \n
			:return: mcm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:TERRestrial:POWer:MCM?')
		return Conversions.str_to_float(response)

	def set_mcm(self, mcm: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:POWer:MCM \n
		Snippet: driver.source.bb.xmRadio.terrestrial.power.set_mcm(mcm = 1.0) \n
		No command help available \n
			:param mcm: No help available
		"""
		param = Conversions.decimal_value_to_str(mcm)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:POWer:MCM {param}')
