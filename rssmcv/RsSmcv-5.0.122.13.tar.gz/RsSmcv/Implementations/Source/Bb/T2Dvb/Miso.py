from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Miso:
	"""Miso commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("miso", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:MISO:MODE \n
		Snippet: value: enums.AutoManualMode = driver.source.bb.t2Dvb.miso.get_mode() \n
		Sets the group mode, that allows to set the MISO group of the modulator manually. \n
			:return: group_mode: MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:MISO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	# noinspection PyTypeChecker
	def get_group(self) -> enums.Dvbt2T2SystemMisoGroupScpi:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:MISO:[GROup] \n
		Snippet: value: enums.Dvbt2T2SystemMisoGroupScpi = driver.source.bb.t2Dvb.miso.get_group() \n
		Sets the group. \n
			:return: miso_group: G1| G2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:MISO:GROup?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2T2SystemMisoGroupScpi)

	def set_group(self, miso_group: enums.Dvbt2T2SystemMisoGroupScpi) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:MISO:[GROup] \n
		Snippet: driver.source.bb.t2Dvb.miso.set_group(miso_group = enums.Dvbt2T2SystemMisoGroupScpi.G1) \n
		Sets the group. \n
			:param miso_group: G1| G2
		"""
		param = Conversions.enum_scalar_to_str(miso_group, enums.Dvbt2T2SystemMisoGroupScpi)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:MISO:GROup {param}')
