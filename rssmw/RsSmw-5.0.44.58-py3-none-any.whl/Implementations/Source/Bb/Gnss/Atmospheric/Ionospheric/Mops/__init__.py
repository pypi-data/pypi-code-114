from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mops:
	"""Mops commands group definition. 11 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mops", core, parent)

	@property
	def importPy(self):
		"""importPy commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_importPy'):
			from .ImportPy import ImportPy
			self._importPy = ImportPy(self._core, self._cmd_group)
		return self._importPy

	# noinspection PyTypeChecker
	def get_display(self) -> enums.IonoGridView:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:DISPlay \n
		Snippet: value: enums.IonoGridView = driver.source.bb.gnss.atmospheric.ionospheric.mops.get_display() \n
		Toggles between indication of the vertical delay and GIVEI values. \n
			:return: display_type: GIVei| VDELay
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.IonoGridView)

	def set_display(self, display_type: enums.IonoGridView) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:DISPlay \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.set_display(display_type = enums.IonoGridView.GIVei) \n
		Toggles between indication of the vertical delay and GIVEI values. \n
			:param display_type: GIVei| VDELay
		"""
		param = Conversions.enum_scalar_to_str(display_type, enums.IonoGridView)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:DISPlay {param}')

	def export(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:EXPort \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.export(filename = '1') \n
		Saves the current ionospheric grid configuration in a file. \n
			:param filename: string Specify the file path, filename and extension. Allowed file extensions are *.rs_ion or *.iono_grid.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:EXPort {param}')

	def get_file(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:FILE \n
		Snippet: value: str = driver.source.bb.gnss.atmospheric.ionospheric.mops.get_file() \n
		Select a ionospheric grid file. \n
			:return: filename: string To load a predefined file, specify only the filename. To load a user-defined file, specify the absolute file path with filename and extension (*.iono_grid) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:FILE?')
		return trim_str_response(response)

	def set_file(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:FILE \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.set_file(filename = '1') \n
		Select a ionospheric grid file. \n
			:param filename: string To load a predefined file, specify only the filename. To load a user-defined file, specify the absolute file path with filename and extension (*.iono_grid) .
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:FILE {param}')

	def clone(self) -> 'Mops':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mops(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
