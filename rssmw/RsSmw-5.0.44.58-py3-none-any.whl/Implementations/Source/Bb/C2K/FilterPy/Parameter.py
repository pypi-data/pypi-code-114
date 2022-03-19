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
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:APCO25 \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_apco_25() \n
		Sets the roll-off factor for filter type APCO25. \n
			:return: apco_25: float Range: 0.05 to 0.99
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:APCO25?')
		return Conversions.str_to_float(response)

	def set_apco_25(self, apco_25: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:APCO25 \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_apco_25(apco_25 = 1.0) \n
		Sets the roll-off factor for filter type APCO25. \n
			:param apco_25: float Range: 0.05 to 0.99
		"""
		param = Conversions.decimal_value_to_str(apco_25)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:APCO25 {param}')

	def get_cosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:COSine \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_cosine() \n
		Sets the roll-off factor for the Cosine filter type. \n
			:return: cosine: float Range: 0 to 1.0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:COSine?')
		return Conversions.str_to_float(response)

	def set_cosine(self, cosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:COSine \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_cosine(cosine = 1.0) \n
		Sets the roll-off factor for the Cosine filter type. \n
			:param cosine: float Range: 0 to 1.0
		"""
		param = Conversions.decimal_value_to_str(cosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:COSine {param}')

	def get_gauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:GAUSs \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_gauss() \n
		Sets the roll-off factor for the Gauss filter type. \n
			:return: gauss: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:GAUSs?')
		return Conversions.str_to_float(response)

	def set_gauss(self, gauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:GAUSs \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_gauss(gauss = 1.0) \n
		Sets the roll-off factor for the Gauss filter type. \n
			:param gauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(gauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:GAUSs {param}')

	def get_lpass_evm(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:LPASSEVM \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_lpass_evm() \n
		The command sets the cut-off frequency factor for the Lowpass (EVM Opt.) filter type. \n
			:return: lpass_evm: float Range: 0.05 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:LPASSEVM?')
		return Conversions.str_to_float(response)

	def set_lpass_evm(self, lpass_evm: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:LPASSEVM \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_lpass_evm(lpass_evm = 1.0) \n
		The command sets the cut-off frequency factor for the Lowpass (EVM Opt.) filter type. \n
			:param lpass_evm: float Range: 0.05 to 2
		"""
		param = Conversions.decimal_value_to_str(lpass_evm)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:LPASSEVM {param}')

	def get_lpass(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:LPASs \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_lpass() \n
		The command sets the cut-off frequency factor for the Lowpass (ACP Opt.) filter type. \n
			:return: lpass: float Range: 0.05 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:LPASs?')
		return Conversions.str_to_float(response)

	def set_lpass(self, lpass: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:LPASs \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_lpass(lpass = 1.0) \n
		The command sets the cut-off frequency factor for the Lowpass (ACP Opt.) filter type. \n
			:param lpass: float Range: 0.05 to 2
		"""
		param = Conversions.decimal_value_to_str(lpass)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:LPASs {param}')

	def get_pgauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:PGAuss \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_pgauss() \n
		The command sets the roll-off factor for the Pure Gauss filter type. \n
			:return: pgauss: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:PGAuss?')
		return Conversions.str_to_float(response)

	def set_pgauss(self, pgauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:PGAuss \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_pgauss(pgauss = 1.0) \n
		The command sets the roll-off factor for the Pure Gauss filter type. \n
			:param pgauss: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(pgauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:PGAuss {param}')

	def get_rcosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:RCOSine \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_rcosine() \n
		The command sets the roll-off factor for the Root Cosine filter type. \n
			:return: rcosine: float Range: 0.00 to 1.0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:RCOSine?')
		return Conversions.str_to_float(response)

	def set_rcosine(self, rcosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:RCOSine \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_rcosine(rcosine = 1.0) \n
		The command sets the roll-off factor for the Root Cosine filter type. \n
			:param rcosine: float Range: 0.00 to 1.0
		"""
		param = Conversions.decimal_value_to_str(rcosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:RCOSine {param}')

	def get_sphase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:SPHase \n
		Snippet: value: float = driver.source.bb.c2K.filterPy.parameter.get_sphase() \n
		The command sets B x T for the Split Phase filter type. \n
			:return: sphase: float Range: 0.15 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:FILTer:PARameter:SPHase?')
		return Conversions.str_to_float(response)

	def set_sphase(self, sphase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:FILTer:PARameter:SPHase \n
		Snippet: driver.source.bb.c2K.filterPy.parameter.set_sphase(sphase = 1.0) \n
		The command sets B x T for the Split Phase filter type. \n
			:param sphase: float Range: 0.15 to 2.5
		"""
		param = Conversions.decimal_value_to_str(sphase)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:FILTer:PARameter:SPHase {param}')
