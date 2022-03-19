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

	def set(self, release: enums.ReleaseNbiotDl, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:RELease \n
		Snippet: driver.source.bb.v5G.downlink.user.release.set(release = enums.ReleaseNbiotDl.EMTC, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param release: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(release, enums.ReleaseNbiotDl)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:RELease {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.ReleaseNbiotDl:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:RELease \n
		Snippet: value: enums.ReleaseNbiotDl = driver.source.bb.v5G.downlink.user.release.get(userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: release: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:RELease?')
		return Conversions.str_to_scalar_enum(response, enums.ReleaseNbiotDl)
