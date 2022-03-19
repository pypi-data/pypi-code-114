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

	def set(self, angle: float, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:FADer<CH>:QUADrature:[ANGLe] \n
		Snippet: driver.source.bb.impairment.fader.quadrature.angle.set(angle = 1.0, digitalIq = repcap.DigitalIq.Default) \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 30 / 30 / 0.01
			- Analog / 10 / 10 / 0.01 \n
			:param angle: float Range: -30 to 30, Unit: DEG
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.decimal_value_to_str(angle)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:BB:IMPairment:FADer{digitalIq_cmd_val}:QUADrature:ANGLe {param}')

	def get(self, digitalIq=repcap.DigitalIq.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:FADer<CH>:QUADrature:[ANGLe] \n
		Snippet: value: float = driver.source.bb.impairment.fader.quadrature.angle.get(digitalIq = repcap.DigitalIq.Default) \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 30 / 30 / 0.01
			- Analog / 10 / 10 / 0.01 \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: angle: float Range: -30 to 30, Unit: DEG"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:FADer{digitalIq_cmd_val}:QUADrature:ANGLe?')
		return Conversions.str_to_float(response)
