from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rframe:
	"""Rframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rframe", core, parent)

	def set(self, reference_frame: enums.RefFrame, baseSt=repcap.BaseSt.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:COORdinates:RFRame \n
		Snippet: driver.source.bb.gnss.rtk.base.location.coordinates.rframe.set(reference_frame = enums.RefFrame.PZ90, baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param reference_frame: No help available
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
		"""
		param = Conversions.enum_scalar_to_str(reference_frame, enums.RefFrame)
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:COORdinates:RFRame {param}')

	# noinspection PyTypeChecker
	def get(self, baseSt=repcap.BaseSt.Default) -> enums.RefFrame:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:COORdinates:RFRame \n
		Snippet: value: enums.RefFrame = driver.source.bb.gnss.rtk.base.location.coordinates.rframe.get(baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:return: reference_frame: No help available"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:COORdinates:RFRame?')
		return Conversions.str_to_scalar_enum(response, enums.RefFrame)
