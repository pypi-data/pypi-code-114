from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cosine:
	"""Cosine commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cosine", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:FILTer:PARameter:COSine:BANDwidth \n
		Snippet: value: float = driver.source.bb.dm.filterPy.parameter.cosine.get_bandwidth() \n
		Sets the filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / Min / Max / Increment / Default \n
			- APCO25 / Roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- APCO25Lsm / Cut off frequency for the lowpass/gauss filter (LOWPass/:GAUSs) / <Cosine> / 400 / 25E6 / 1E-3 / 270833.333
			- COSine / Bandwidth / <FiltParm> / 400 / depends on the installed options*) / 1E-3 / 270833.333
			- COSine / Roll-off factor / <Cosine> / 0.05 / 1 / 0.01 / 0.35
			- GAUSs / Roll-off factor / <Gauss> / 0.15 / 100000 / 0.01 / 0.3
			- LPASs / Cut-off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / Cut-off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / Roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / Roll-off factor / <RCosine> / 0.05 / 1 / 0.001 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2
		*) 120E6 (R&S SMCVB-K521) / 160E6 (R&S SMCVB-K522) / 240E6 (R&S SMCVB-K522) \n
			:return: bandwidth: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FILTer:PARameter:COSine:BANDwidth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, bandwidth: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FILTer:PARameter:COSine:BANDwidth \n
		Snippet: driver.source.bb.dm.filterPy.parameter.cosine.set_bandwidth(bandwidth = 1.0) \n
		Sets the filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / Min / Max / Increment / Default \n
			- APCO25 / Roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- APCO25Lsm / Cut off frequency for the lowpass/gauss filter (LOWPass/:GAUSs) / <Cosine> / 400 / 25E6 / 1E-3 / 270833.333
			- COSine / Bandwidth / <FiltParm> / 400 / depends on the installed options*) / 1E-3 / 270833.333
			- COSine / Roll-off factor / <Cosine> / 0.05 / 1 / 0.01 / 0.35
			- GAUSs / Roll-off factor / <Gauss> / 0.15 / 100000 / 0.01 / 0.3
			- LPASs / Cut-off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / Cut-off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / Roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / Roll-off factor / <RCosine> / 0.05 / 1 / 0.001 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2
		*) 120E6 (R&S SMCVB-K521) / 160E6 (R&S SMCVB-K522) / 240E6 (R&S SMCVB-K522) \n
			:param bandwidth: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FILTer:PARameter:COSine:BANDwidth {param}')

	def get_rolloff(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:FILTer:PARameter:COSine:[ROLLoff] \n
		Snippet: value: float = driver.source.bb.dm.filterPy.parameter.cosine.get_rolloff() \n
		Sets the filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / Min / Max / Increment / Default \n
			- APCO25 / Roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- APCO25Lsm / Cut off frequency for the lowpass/gauss filter (LOWPass/:GAUSs) / <Cosine> / 400 / 25E6 / 1E-3 / 270833.333
			- COSine / Bandwidth / <FiltParm> / 400 / depends on the installed options*) / 1E-3 / 270833.333
			- COSine / Roll-off factor / <Cosine> / 0.05 / 1 / 0.01 / 0.35
			- GAUSs / Roll-off factor / <Gauss> / 0.15 / 100000 / 0.01 / 0.3
			- LPASs / Cut-off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / Cut-off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / Roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / Roll-off factor / <RCosine> / 0.05 / 1 / 0.001 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2
		*) 120E6 (R&S SMCVB-K521) / 160E6 (R&S SMCVB-K522) / 240E6 (R&S SMCVB-K522) \n
			:return: cosine: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FILTer:PARameter:COSine:ROLLoff?')
		return Conversions.str_to_float(response)

	def set_rolloff(self, cosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FILTer:PARameter:COSine:[ROLLoff] \n
		Snippet: driver.source.bb.dm.filterPy.parameter.cosine.set_rolloff(cosine = 1.0) \n
		Sets the filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / Min / Max / Increment / Default \n
			- APCO25 / Roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- APCO25Lsm / Cut off frequency for the lowpass/gauss filter (LOWPass/:GAUSs) / <Cosine> / 400 / 25E6 / 1E-3 / 270833.333
			- COSine / Bandwidth / <FiltParm> / 400 / depends on the installed options*) / 1E-3 / 270833.333
			- COSine / Roll-off factor / <Cosine> / 0.05 / 1 / 0.01 / 0.35
			- GAUSs / Roll-off factor / <Gauss> / 0.15 / 100000 / 0.01 / 0.3
			- LPASs / Cut-off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / Cut-off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / Roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / Roll-off factor / <RCosine> / 0.05 / 1 / 0.001 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2
		*) 120E6 (R&S SMCVB-K521) / 160E6 (R&S SMCVB-K522) / 240E6 (R&S SMCVB-K522) \n
			:param cosine: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(cosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FILTer:PARameter:COSine:ROLLoff {param}')
