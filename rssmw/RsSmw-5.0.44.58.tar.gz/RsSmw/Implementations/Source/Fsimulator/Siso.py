from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Siso:
	"""Siso commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("siso", core, parent)

	# noinspection PyTypeChecker
	def get_copy(self) -> enums.FadCopyHwdEst:
		"""SCPI: [SOURce<HW>]:FSIMulator:SISO:COPY \n
		Snippet: value: enums.FadCopyHwdEst = driver.source.fsimulator.siso.get_copy() \n
		In 'System Configurations' with multiple entities (L > 2) , copies the settings of the current fading simulator to all or
		to the selected entities. \n
			:return: copy_to_dest: FADB| FADA| FADC| FADD| FADF| FADE| FADG| FADH| ALL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SISO:COPY?')
		return Conversions.str_to_scalar_enum(response, enums.FadCopyHwdEst)

	def set_copy(self, copy_to_dest: enums.FadCopyHwdEst) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SISO:COPY \n
		Snippet: driver.source.fsimulator.siso.set_copy(copy_to_dest = enums.FadCopyHwdEst.ALL) \n
		In 'System Configurations' with multiple entities (L > 2) , copies the settings of the current fading simulator to all or
		to the selected entities. \n
			:param copy_to_dest: FADB| FADA| FADC| FADD| FADF| FADE| FADG| FADH| ALL
		"""
		param = Conversions.enum_scalar_to_str(copy_to_dest, enums.FadCopyHwdEst)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SISO:COPY {param}')
