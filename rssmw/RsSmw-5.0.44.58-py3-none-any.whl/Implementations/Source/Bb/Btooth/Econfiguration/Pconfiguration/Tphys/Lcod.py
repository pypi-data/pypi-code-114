from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcod:
	"""Lcod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcod", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:LCOD:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.tphys.lcod.get_state() \n
		Specifies preferred physical layers in Rx (..:RPHYs:..) or Tx (..:TPHYs:..) direction. Information is signaled via
		LL_PHY_REQ and LL_PHY_RSP. You can enable one or more PHYs: L1M for LE uncoded 1 Msymbol/s PHY, L2M for LE uncoded 2
		Msymbol/s PHY, and LCOD for LE coded 1 Msymbol/s PHY. \n
			:return: tphys: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:LCOD:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, tphys: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:LCOD:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.tphys.lcod.set_state(tphys = False) \n
		Specifies preferred physical layers in Rx (..:RPHYs:..) or Tx (..:TPHYs:..) direction. Information is signaled via
		LL_PHY_REQ and LL_PHY_RSP. You can enable one or more PHYs: L1M for LE uncoded 1 Msymbol/s PHY, L2M for LE uncoded 2
		Msymbol/s PHY, and LCOD for LE coded 1 Msymbol/s PHY. \n
			:param tphys: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tphys)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:LCOD:STATe {param}')
