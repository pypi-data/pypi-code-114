from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	def set(self, signal: enums.OutpConnGlbSignalb, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: OUTPut<HW>:USER<CH>:SIGNal \n
		Snippet: driver.output.user.signal.set(signal = enums.OutpConnGlbSignalb.MARKA1, userIx = repcap.UserIx.Default) \n
		Sets the control signal that is output at the selected connector. To define the connector direction, use the command
		method RsSmcv.Output.User.Direction.set. \n
			:param signal: MARKA1| NONE
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.OutpConnGlbSignalb)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.OutpConnGlbSignalb:
		"""SCPI: OUTPut<HW>:USER<CH>:SIGNal \n
		Snippet: value: enums.OutpConnGlbSignalb = driver.output.user.signal.get(userIx = repcap.UserIx.Default) \n
		Sets the control signal that is output at the selected connector. To define the connector direction, use the command
		method RsSmcv.Output.User.Direction.set. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: signal: MARKA1| NONE"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.OutpConnGlbSignalb)
