from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoMode:
	"""PoMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poMode", core, parent)

	def set(self, po_mode: enums.AutoUser, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:POMode \n
		Snippet: driver.source.bb.w3Gpp.mstation.cmode.poMode.set(po_mode = enums.AutoUser.AUTO, mobileStation = repcap.MobileStation.Default) \n
		The command selects the power offset mode. \n
			:param po_mode: AUTO| USER AUTO The power offset is obtained by pilot bit ratio as follows: Number of pilots bits of non-compressed slots / Number of pilot bits by compressed slots. USER The power offset is defined by command [:SOURcehw]:BB:W3GPp:BSTationst|MSTationst:CMODe:POFFset.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(po_mode, enums.AutoUser)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:POMode {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.AutoUser:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CMODe:POMode \n
		Snippet: value: enums.AutoUser = driver.source.bb.w3Gpp.mstation.cmode.poMode.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the power offset mode. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: po_mode: AUTO| USER AUTO The power offset is obtained by pilot bit ratio as follows: Number of pilots bits of non-compressed slots / Number of pilot bits by compressed slots. USER The power offset is defined by command [:SOURcehw]:BB:W3GPp:BSTationst|MSTationst:CMODe:POFFset."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CMODe:POMode?')
		return Conversions.str_to_scalar_enum(response, enums.AutoUser)
