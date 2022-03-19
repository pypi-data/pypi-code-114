from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Release:
	"""Release commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("release", core, parent)

	def set(self, release: enums.EutraUeReleaseDl, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:RELease \n
		Snippet: driver.source.bb.eutra.downlink.user.release.set(release = enums.EutraUeReleaseDl.EM_A, userIx = repcap.UserIx.Default) \n
		Sets the 3GPP release version the UE supports. \n
			:param release: R89 | LADV | EM_A| NIOT| EM_B EM_A = eMTC CE: A and EM_B = eMTC CE: B
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(release, enums.EutraUeReleaseDl)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:RELease {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EutraUeReleaseDl:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:RELease \n
		Snippet: value: enums.EutraUeReleaseDl = driver.source.bb.eutra.downlink.user.release.get(userIx = repcap.UserIx.Default) \n
		Sets the 3GPP release version the UE supports. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: release: R89 | LADV | EM_A| NIOT| EM_B EM_A = eMTC CE: A and EM_B = eMTC CE: B"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:RELease?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUeReleaseDl)
