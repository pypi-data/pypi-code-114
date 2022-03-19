from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frc:
	"""Frc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frc", core, parent)

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraUlFrc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:INTRacell:UE<CH>:FRC \n
		Snippet: value: enums.EutraUlFrc = driver.source.bb.eutra.tcw.ws.intracell.ue.frc.get(userEquipment = repcap.UserEquipment.Default) \n
		Queries the intra cell fixed reference channel used for UE wanted signal. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: intra_cell_ue_frc: A11| A12| A13| A14| A15| A21| A22| A23| A31| A32| A33| A34| A35| A36| A37| A41| A42| A43| A44| A45| A46| A47| A48| A51| A52| A53| A54| A55| A56| A57| A71| A72| A73| A74| A75| A76| A81| A82| A83| A84| A85| A86| UE11| UE12| UE21| UE22| UE3| A16| A17| A121| A122| A123| A124| A125| A126| A131| A132| A133| A134| A135| A136| A171| A172| A173| A174| A175| A176| A181| A182| A183| A184| A185| A186| A191| A192| A193| A194| A195| A196| A211| A212| A213| A214| A215| A216| A221| A222| A223| A224"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:INTRacell:UE{userEquipment_cmd_val}:FRC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUlFrc)
