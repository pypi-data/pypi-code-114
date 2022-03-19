from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)

	def set(self, angle: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:BBMM<CH>:QUADrature:[ANGLe] \n
		Snippet: driver.source.bb.impairment.bbmm.quadrature.angle.set(angle = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 30 / 30 / 0.01
			- Analog / 10 / 10 / 0.01 \n
			:param angle: float Range: -30 to 30, Unit: DEG
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.decimal_value_to_str(angle)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:BB:IMPairment:BBMM{iqConnector_cmd_val}:QUADrature:ANGLe {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:BBMM<CH>:QUADrature:[ANGLe] \n
		Snippet: value: float = driver.source.bb.impairment.bbmm.quadrature.angle.get(iqConnector = repcap.IqConnector.Default) \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 30 / 30 / 0.01
			- Analog / 10 / 10 / 0.01 \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: angle: float Range: -30 to 30, Unit: DEG"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:BBMM{iqConnector_cmd_val}:QUADrature:ANGLe?')
		return Conversions.str_to_float(response)
