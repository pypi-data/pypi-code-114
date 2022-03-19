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

	def set(self, ai_unscaled: float, aiOrder=repcap.AiOrder.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:NMESsage:FNAV:IONospheric:AI<CH0>:UNSCaled \n
		Snippet: driver.source.bb.gnss.atmospheric.galileo.nmessage.fnav.ionospheric.ai.unscaled.set(ai_unscaled = 1.0, aiOrder = repcap.AiOrder.Default) \n
		Sets the parameters effective ionization level 1st to 3rd order of the satellite's navigation message. \n
			:param ai_unscaled: integer Range: a_i0 (0 to 2047) , a_i1 (-1024 to 1023) , a_i2 (-8192 to 8191)
			:param aiOrder: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ai')
		"""
		param = Conversions.decimal_value_to_str(ai_unscaled)
		aiOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(aiOrder, repcap.AiOrder)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:NMESsage:FNAV:IONospheric:AI{aiOrder_cmd_val}:UNSCaled {param}')

	def get(self, aiOrder=repcap.AiOrder.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:NMESsage:FNAV:IONospheric:AI<CH0>:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.atmospheric.galileo.nmessage.fnav.ionospheric.ai.unscaled.get(aiOrder = repcap.AiOrder.Default) \n
		Sets the parameters effective ionization level 1st to 3rd order of the satellite's navigation message. \n
			:param aiOrder: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ai')
			:return: ai_unscaled: No help available"""
		aiOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(aiOrder, repcap.AiOrder)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:NMESsage:FNAV:IONospheric:AI{aiOrder_cmd_val}:UNSCaled?')
		return Conversions.str_to_float(response)
