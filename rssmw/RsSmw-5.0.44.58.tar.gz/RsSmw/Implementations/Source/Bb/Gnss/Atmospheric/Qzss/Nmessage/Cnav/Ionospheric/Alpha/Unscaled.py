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

	def set(self, alpha_unscaled: float, alphaNull=repcap.AlphaNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:QZSS:NMESsage:CNAV:IONospheric:ALPHa<CH0>:UNSCaled \n
		Snippet: driver.source.bb.gnss.atmospheric.qzss.nmessage.cnav.ionospheric.alpha.unscaled.set(alpha_unscaled = 1.0, alphaNull = repcap.AlphaNull.Default) \n
		Sets the parameters alpha_0 to alpha_3 of the satellite's navigation message. \n
			:param alpha_unscaled: No help available
			:param alphaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alpha')
		"""
		param = Conversions.decimal_value_to_str(alpha_unscaled)
		alphaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(alphaNull, repcap.AlphaNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:QZSS:NMESsage:CNAV:IONospheric:ALPHa{alphaNull_cmd_val}:UNSCaled {param}')

	def get(self, alphaNull=repcap.AlphaNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:QZSS:NMESsage:CNAV:IONospheric:ALPHa<CH0>:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.atmospheric.qzss.nmessage.cnav.ionospheric.alpha.unscaled.get(alphaNull = repcap.AlphaNull.Default) \n
		Sets the parameters alpha_0 to alpha_3 of the satellite's navigation message. \n
			:param alphaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alpha')
			:return: alpha_unscaled: No help available"""
		alphaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(alphaNull, repcap.AlphaNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:QZSS:NMESsage:CNAV:IONospheric:ALPHa{alphaNull_cmd_val}:UNSCaled?')
		return Conversions.str_to_float(response)
