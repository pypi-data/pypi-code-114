from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unscaled:
	"""Unscaled commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unscaled", core, parent)

	def set(self, beta_unscaled: int, betaNull=repcap.BetaNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:NAVic:NMESsage:NAV:IONospheric:BETA<CH0>:UNSCaled \n
		Snippet: driver.source.bb.gnss.atmospheric.navic.nmessage.nav.ionospheric.beta.unscaled.set(beta_unscaled = 1, betaNull = repcap.BetaNull.Default) \n
		Sets the parameters beta_0 to beta_3 of the satellite's navigation message. \n
			:param beta_unscaled: No help available
			:param betaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Beta')
		"""
		param = Conversions.decimal_value_to_str(beta_unscaled)
		betaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(betaNull, repcap.BetaNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:NAVic:NMESsage:NAV:IONospheric:BETA{betaNull_cmd_val}:UNSCaled {param}')

	def get(self, betaNull=repcap.BetaNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:NAVic:NMESsage:NAV:IONospheric:BETA<CH0>:UNSCaled \n
		Snippet: value: int = driver.source.bb.gnss.atmospheric.navic.nmessage.nav.ionospheric.beta.unscaled.get(betaNull = repcap.BetaNull.Default) \n
		Sets the parameters beta_0 to beta_3 of the satellite's navigation message. \n
			:param betaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Beta')
			:return: beta_unscaled: No help available"""
		betaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(betaNull, repcap.BetaNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:NAVic:NMESsage:NAV:IONospheric:BETA{betaNull_cmd_val}:UNSCaled?')
		return Conversions.str_to_int(response)
