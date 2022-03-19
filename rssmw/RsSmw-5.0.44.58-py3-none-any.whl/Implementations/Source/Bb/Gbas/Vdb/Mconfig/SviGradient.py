from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SviGradient:
	"""SviGradient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sviGradient", core, parent)

	def set(self, svig: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:SVIGradient \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.sviGradient.set(svig = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the Sigma_vert_iono_gradient. \n
			:param svig: float Range: 0 to 2.55E-05
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(svig)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:SVIGradient {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:SVIGradient \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.sviGradient.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the Sigma_vert_iono_gradient. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: svig: float Range: 0 to 2.55E-05"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:SVIGradient?')
		return Conversions.str_to_float(response)
