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

	def set(self, type_py: enums.ChanCodTypeEnhPrac, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:ENHanced:PRACh:CCODing:TYPE \n
		Snippet: driver.source.bb.w3Gpp.mstation.enhanced.prach.ccoding.typePy.set(type_py = enums.ChanCodTypeEnhPrac.TB168, mobileStation = repcap.MobileStation.Default) \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. \n
			:param type_py: TB168| TB360| TU168| TU360 TB168 RACH RMC (TB size 168 bits) TB360 RACH RMC (TB size 360 bits)
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanCodTypeEnhPrac)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:ENHanced:PRACh:CCODing:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.ChanCodTypeEnhPrac:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:ENHanced:PRACh:CCODing:TYPE \n
		Snippet: value: enums.ChanCodTypeEnhPrac = driver.source.bb.w3Gpp.mstation.enhanced.prach.ccoding.typePy.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the channel coding scheme in accordance with the 3GPP specification. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: type_py: TB168| TB360| TU168| TU360 TB168 RACH RMC (TB size 168 bits) TB360 RACH RMC (TB size 360 bits)"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:ENHanced:PRACh:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodTypeEnhPrac)
