from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.TdscdmaDchCoding, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:TYPE \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.typePy.set(type_py = enums.TdscdmaDchCoding.HRMC526K, cell = repcap.Cell.Default) \n
		The command sets the channel coding type. \n
			:param type_py: RMC12K2| RMC64K| RMC144K| RMC384K| RMC2048K| HRMC526K| HRMC730K| UP_RMC12K2| UP_RMC64K| UP_RMC144K| UP_RMC384K| HSDPA| HSUPA| HS_SICH| PLCCH| USER| USER
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TdscdmaDchCoding)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaDchCoding:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:TYPE \n
		Snippet: value: enums.TdscdmaDchCoding = driver.source.bb.tdscdma.up.cell.enh.dch.typePy.get(cell = repcap.Cell.Default) \n
		The command sets the channel coding type. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: type_py: RMC12K2| RMC64K| RMC144K| RMC384K| RMC2048K| HRMC526K| HRMC730K| UP_RMC12K2| UP_RMC64K| UP_RMC144K| UP_RMC384K| HSDPA| HSUPA| HS_SICH| PLCCH| USER| USER"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaDchCoding)
