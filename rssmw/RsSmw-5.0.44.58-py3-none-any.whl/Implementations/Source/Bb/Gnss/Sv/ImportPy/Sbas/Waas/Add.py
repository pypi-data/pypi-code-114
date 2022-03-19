from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("add", core, parent)

	def set_dir(self, directory: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:IMPort:SBAS:WAAS:ADD:DIR \n
		Snippet: driver.source.bb.gnss.sv.importPy.sbas.waas.add.set_dir(directory = '1') \n
		Adds a set of *.ems files for EGNOS correction data *.nstb files for WAAS correction data to an import file list in one
		step. \n
			:param directory: string File path
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:IMPort:SBAS:WAAS:ADD:DIR {param}')

	def set_file(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:IMPort:SBAS:WAAS:ADD:FILE \n
		Snippet: driver.source.bb.gnss.sv.importPy.sbas.waas.add.set_file(filename = '1') \n
		Adds *.ems files for EGNOS correction data *.nstb files for WAAS correction data to an import file list. \n
			:param filename: string The Filename string comprises the file directory, filename and extension. For more information about *.ems and *.nstb files, see 'SBAS correction file download links'.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:IMPort:SBAS:WAAS:ADD:FILE {param}')
