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

	def set(self, prs_numerology: enums.NumerologyPrs, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:SCSPacing \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.scSpacing.set(prs_numerology = enums.NumerologyPrs.N120, cellNull = repcap.CellNull.Nr0) \n
		Sets the combination of the subcarrier spacing (SCS) and the cyclic prefix (CP) for the DL PRS frequency layer. Set the
		value according to the configured 'Deployment'. \n
			:param prs_numerology: N15| N30| N60| N120| X60| N480| N960 N|X SCS N = Normal CP, X = Extended CP, SCS = SCS in kHz
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(prs_numerology, enums.NumerologyPrs)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.NumerologyPrs:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:SCSPacing \n
		Snippet: value: enums.NumerologyPrs = driver.source.bb.nr5G.node.cell.prs.scSpacing.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the combination of the subcarrier spacing (SCS) and the cyclic prefix (CP) for the DL PRS frequency layer. Set the
		value according to the configured 'Deployment'. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: prs_numerology: N15| N30| N60| N120| X60| N480| N960 N|X SCS N = Normal CP, X = Extended CP, SCS = SCS in kHz"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.NumerologyPrs)
