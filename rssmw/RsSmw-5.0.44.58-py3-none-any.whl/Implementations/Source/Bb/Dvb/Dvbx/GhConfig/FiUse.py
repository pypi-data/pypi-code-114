from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FiUse:
	"""FiUse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fiUse", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:FIUSe:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.ghConfig.fiUse.get_state() \n
		Includes a PDU fragment in the GSE packet. \n
			:return: fi_use: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:FIUSe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, fi_use: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:FIUSe:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.fiUse.set_state(fi_use = False) \n
		Includes a PDU fragment in the GSE packet. \n
			:param fi_use: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(fi_use)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:FIUSe:STATe {param}')
