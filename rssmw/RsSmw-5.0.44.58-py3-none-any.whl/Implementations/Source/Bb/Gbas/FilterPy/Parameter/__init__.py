from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Parameter:
	"""Parameter commands group definition. 9 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameter", core, parent)

	@property
	def cosine(self):
		"""cosine commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cosine'):
			from .Cosine import Cosine
			self._cosine = Cosine(self._core, self._cmd_group)
		return self._cosine

	def get_apco_25(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:APCO25 \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_apco_25() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: apco_25: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:APCO25?')
		return Conversions.str_to_float(response)

	def set_apco_25(self, apco_25: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:APCO25 \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_apco_25(apco_25 = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param apco_25: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(apco_25)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:APCO25 {param}')

	def get_gauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:GAUSs \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_gauss() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: gauss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:GAUSs?')
		return Conversions.str_to_float(response)

	def set_gauss(self, gauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:GAUSs \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_gauss(gauss = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param gauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(gauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:GAUSs {param}')

	def get_lpass_evm(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:LPASSEVM \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_lpass_evm() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: lpass_evm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:LPASSEVM?')
		return Conversions.str_to_float(response)

	def set_lpass_evm(self, lpass_evm: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:LPASSEVM \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_lpass_evm(lpass_evm = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param lpass_evm: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(lpass_evm)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:LPASSEVM {param}')

	def get_lpass(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:LPASs \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_lpass() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: lpass: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:LPASs?')
		return Conversions.str_to_float(response)

	def set_lpass(self, lpass: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:LPASs \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_lpass(lpass = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param lpass: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(lpass)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:LPASs {param}')

	def get_pgauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:PGAuss \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_pgauss() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: pgauss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:PGAuss?')
		return Conversions.str_to_float(response)

	def set_pgauss(self, pgauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:PGAuss \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_pgauss(pgauss = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param pgauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(pgauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:PGAuss {param}')

	def get_rcosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:RCOSine \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_rcosine() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: rcosine: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:RCOSine?')
		return Conversions.str_to_float(response)

	def set_rcosine(self, rcosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:RCOSine \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_rcosine(rcosine = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param rcosine: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(rcosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:RCOSine {param}')

	def get_sphase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:SPHase \n
		Snippet: value: float = driver.source.bb.gbas.filterPy.parameter.get_sphase() \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:return: sphase: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:SPHase?')
		return Conversions.str_to_float(response)

	def set_sphase(self, sphase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:FILTer:PARameter:SPHase \n
		Snippet: driver.source.bb.gbas.filterPy.parameter.set_sphase(sphase = 1.0) \n
		Sets the corresponding filter parameter.
			Table Header: Filter Type / Parameter / Parameter Name / min / max / increment / default \n
			- APCO25 / roll-off factor / <Apco25> / 0.05 / 0.99 / 0.01 / 0.2
			- COSine / roll-off factor / <Cosine> / 0.05 / 1.00 / 0.01 / 0.35
			- COSine / bandwidth to symbol rate ratio / <CoFs> / 2 / 2 / 0.01 / 1.00
			- GAUSs / roll-off factor / <Gauss> / 0.15 / 2.5 / 0.01 / 0.3
			- LPASs / cut off frequency / <LPass> / 0.05 / 2 / 0.01 / 0.5
			- LPASSEVM / cut off frequency / <LPassEvm> / 0.05 / 2 / 0.01 / 0.5
			- PGAuss / roll-off factor / <PGauss> / 0.15 / 2.5 / 0.01 / 0.3
			- RCOSine / roll-off factor / <RCosine> / 0.05 / 1.00 / 0.01 / 0.35
			- SPHase / B x T / <SPhase> / 0.15 / 2.5 / 0.01 / 2 \n
			:param sphase: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(sphase)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:FILTer:PARameter:SPHase {param}')

	def clone(self) -> 'Parameter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Parameter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
