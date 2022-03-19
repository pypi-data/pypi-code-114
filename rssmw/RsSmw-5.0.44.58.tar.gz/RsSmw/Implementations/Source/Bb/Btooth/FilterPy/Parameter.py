from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Parameter:
	"""Parameter commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameter", core, parent)

	def get_apco_25(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:APCO25 \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_apco_25() \n
		Sets the roll-off factor for filter type APCO25. \n
			:return: apco_25: float Range: 0.05 to 0.99
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:APCO25?')
		return Conversions.str_to_float(response)

	def set_apco_25(self, apco_25: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:APCO25 \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_apco_25(apco_25 = 1.0) \n
		Sets the roll-off factor for filter type APCO25. \n
			:param apco_25: float Range: 0.05 to 0.99
		"""
		param = Conversions.decimal_value_to_str(apco_25)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:APCO25 {param}')

	def get_cosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:COSine \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_cosine() \n
		Sets the roll-off factor for the Cosine filter type. \n
			:return: cosine: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:COSine?')
		return Conversions.str_to_float(response)

	def set_cosine(self, cosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:COSine \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_cosine(cosine = 1.0) \n
		Sets the roll-off factor for the Cosine filter type. \n
			:param cosine: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(cosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:COSine {param}')

	def get_fgauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:FGAuss \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_fgauss() \n
		Sets the B x T for the Gauss filter type. \n
			:return: fgauss: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:FGAuss?')
		return Conversions.str_to_float(response)

	def set_fgauss(self, fgauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:FGAuss \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_fgauss(fgauss = 1.0) \n
		Sets the B x T for the Gauss filter type. \n
			:param fgauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(fgauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:FGAuss {param}')

	def get_gauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:GAUSs \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_gauss() \n
		Sets the B x T for the Gauss filter type. \n
			:return: gauss: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:GAUSs?')
		return Conversions.str_to_float(response)

	def set_gauss(self, gauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:GAUSs \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_gauss(gauss = 1.0) \n
		Sets the B x T for the Gauss filter type. \n
			:param gauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(gauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:GAUSs {param}')

	def get_lpass(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:LPASs \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_lpass() \n
		Sets the cut off frequency factor for a lowpass filter (ACP Opt.) . \n
			:return: lpass: float Range: 0.05 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:LPASs?')
		return Conversions.str_to_float(response)

	def set_lpass(self, lpass: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:LPASs \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_lpass(lpass = 1.0) \n
		Sets the cut off frequency factor for a lowpass filter (ACP Opt.) . \n
			:param lpass: float Range: 0.05 to 2
		"""
		param = Conversions.decimal_value_to_str(lpass)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:LPASs {param}')

	def get_pgauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:PGAuss \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_pgauss() \n
		Sets the B x T for the Pure Gauss filter type. \n
			:return: pgauss: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:PGAuss?')
		return Conversions.str_to_float(response)

	def set_pgauss(self, pgauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:PGAuss \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_pgauss(pgauss = 1.0) \n
		Sets the B x T for the Pure Gauss filter type. \n
			:param pgauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(pgauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:PGAuss {param}')

	def get_rcosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:RCOSine \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_rcosine() \n
		Sets the roll-off factor for the Root Cosine filter type. \n
			:return: rcosine: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:RCOSine?')
		return Conversions.str_to_float(response)

	def set_rcosine(self, rcosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:RCOSine \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_rcosine(rcosine = 1.0) \n
		Sets the roll-off factor for the Root Cosine filter type. \n
			:param rcosine: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(rcosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:RCOSine {param}')

	def get_sphase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:SPHase \n
		Snippet: value: float = driver.source.bb.btooth.filterPy.parameter.get_sphase() \n
		Sets the BxT for the split phase filter type. \n
			:return: sphase: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:SPHase?')
		return Conversions.str_to_float(response)

	def set_sphase(self, sphase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:FILTer:PARameter:SPHase \n
		Snippet: driver.source.bb.btooth.filterPy.parameter.set_sphase(sphase = 1.0) \n
		Sets the BxT for the split phase filter type. \n
			:param sphase: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(sphase)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:FILTer:PARameter:SPHase {param}')
