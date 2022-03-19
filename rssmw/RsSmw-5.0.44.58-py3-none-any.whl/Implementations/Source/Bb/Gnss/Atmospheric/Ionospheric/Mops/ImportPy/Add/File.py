from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set_ems(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:EMS \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.importPy.add.file.set_ems(filename = '1') \n
		Add *.ems, *.nstb or *.iono_grid files to an import file list. \n
			:param filename: string The Filename string comprises the file directory, filename and extension. For more information about *.ems and *.nstb files, see'SBAS correction file download links' . *.iono_grid files, see Example 'Ionospheric grid file content (extract) '.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:EMS {param}')

	def set_grid(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:GRID \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.importPy.add.file.set_grid(filename = '1') \n
		Add *.ems, *.nstb or *.iono_grid files to an import file list. \n
			:param filename: string The Filename string comprises the file directory, filename and extension. For more information about *.ems and *.nstb files, see'SBAS correction file download links' . *.iono_grid files, see Example 'Ionospheric grid file content (extract) '.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:GRID {param}')

	def set_nstb(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:NSTB \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.mops.importPy.add.file.set_nstb(filename = '1') \n
		Add *.ems, *.nstb or *.iono_grid files to an import file list. \n
			:param filename: string The Filename string comprises the file directory, filename and extension. For more information about *.ems and *.nstb files, see'SBAS correction file download links' . *.iono_grid files, see Example 'Ionospheric grid file content (extract) '.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:ADD:FILE:NSTB {param}')
