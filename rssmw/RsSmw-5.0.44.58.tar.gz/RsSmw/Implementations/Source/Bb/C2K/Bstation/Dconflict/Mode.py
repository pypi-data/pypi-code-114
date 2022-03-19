from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.Cdma2KdomConfModeDn, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:DCONflict:MODE \n
		Snippet: driver.source.bb.c2K.bstation.dconflict.mode.set(mode = enums.Cdma2KdomConfModeDn.BREV, baseStation = repcap.BaseStation.Default) \n
		The command switches the order of the spreading codes. \n
			:param mode: HAD| BREV HAD the code channels are displayed in the order determined by the Hadamard matrix. The codes are numbered as Walsh codes according to the standard. BREV the code channels are displayed in the order defined by the Orthogonal Variable Spreading Factor (OVSF) code tree (3GPP code) .
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KdomConfModeDn)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:DCONflict:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.Cdma2KdomConfModeDn:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:DCONflict:MODE \n
		Snippet: value: enums.Cdma2KdomConfModeDn = driver.source.bb.c2K.bstation.dconflict.mode.get(baseStation = repcap.BaseStation.Default) \n
		The command switches the order of the spreading codes. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: mode: HAD| BREV HAD the code channels are displayed in the order determined by the Hadamard matrix. The codes are numbered as Walsh codes according to the standard. BREV the code channels are displayed in the order defined by the Orthogonal Variable Spreading Factor (OVSF) code tree (3GPP code) ."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:DCONflict:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KdomConfModeDn)
