from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScSpacing:
	"""ScSpacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scSpacing", core, parent)

	def set(self, sc_spacing: enums.Numerology, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:SCSPacing \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.scSpacing.set(sc_spacing = enums.Numerology.N120, cellNull = repcap.CellNull.Nr0) \n
		Selects a combination of the subcarrier spacing (SCS) and the cyclic prefix (CP) , where the available values depend on
		the 'Deployment'. See Table 'Supported combinations of SCS and CP per frequency range'. \n
			:param sc_spacing: N15| N30| N60| X60| N120| N240| N480| N960
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(sc_spacing, enums.Numerology)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.Numerology:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:SCSPacing \n
		Snippet: value: enums.Numerology = driver.source.bb.nr5G.node.cell.dumRes.scSpacing.get(cellNull = repcap.CellNull.Nr0) \n
		Selects a combination of the subcarrier spacing (SCS) and the cyclic prefix (CP) , where the available values depend on
		the 'Deployment'. See Table 'Supported combinations of SCS and CP per frequency range'. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: sc_spacing: N15| N30| N60| X60| N120| N240| N480| N960"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.Numerology)
