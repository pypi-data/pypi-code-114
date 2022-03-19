from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 8 total commands, 2 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	# noinspection PyTypeChecker
	def get_denable(self) -> enums.BertMask:
		"""SCPI: BERT:SETup:DENable \n
		Snippet: value: enums.BertMask = driver.bert.setup.get_denable() \n
		Activates the Data Enable signal and, if activated, sets its polarity. The signal marks the data that is evaluated by the
		BERT/BLER measurement. Does not evaluate data supplied by the DUT, that is additional to the PRBS sequence (e.g. sync,
		preambles, other channels, etc.) . \n
			:return: denable: HIGH| LOW OFF Ignore any signal at the data enable input; use all data at the BERT/BLER data input for the measurement. HIGH Use the data enable signal. Only measures the data at the BERT/BLER data input during a high level of the data enable signal. Interrupts the measurement during a low level. LOW Use the data enable signal. Only measures the data at the BERT/BLER data input during a low level of the data enable signal. Interrupts the measurement during a high level.
		"""
		response = self._core.io.query_str('BERT:SETup:DENable?')
		return Conversions.str_to_scalar_enum(response, enums.BertMask)

	def set_denable(self, denable: enums.BertMask) -> None:
		"""SCPI: BERT:SETup:DENable \n
		Snippet: driver.bert.setup.set_denable(denable = enums.BertMask.HIGH) \n
		Activates the Data Enable signal and, if activated, sets its polarity. The signal marks the data that is evaluated by the
		BERT/BLER measurement. Does not evaluate data supplied by the DUT, that is additional to the PRBS sequence (e.g. sync,
		preambles, other channels, etc.) . \n
			:param denable: HIGH| LOW OFF Ignore any signal at the data enable input; use all data at the BERT/BLER data input for the measurement. HIGH Use the data enable signal. Only measures the data at the BERT/BLER data input during a high level of the data enable signal. Interrupts the measurement during a low level. LOW Use the data enable signal. Only measures the data at the BERT/BLER data input during a low level of the data enable signal. Interrupts the measurement during a high level.
		"""
		param = Conversions.enum_scalar_to_str(denable, enums.BertMask)
		self._core.io.write(f'BERT:SETup:DENable {param}')

	# noinspection PyTypeChecker
	def get_ignore(self) -> enums.BertPattIgn:
		"""SCPI: BERT:SETup:IGNore \n
		Snippet: value: enums.BertPattIgn = driver.bert.setup.get_ignore() \n
		Activates ignoring of pure '0' or '1' bit sequences of at least 32 bits, so that faulty frames are excluded from the
		measurement. Some mobile radio standards indicate faulty frames with pure '0' or '1' bit sequences when errors (e.g.
		an incorrect checksum) are detected. \n
			:return: ignore: OFF| ZERO| ONE OFF Pattern ignore is not active. ZERO Ignore bit sequences of 32 or more consecutive '0' for the BERT measurement. ONE Ignore bit sequences of 32 or more consecutive '1' for the BERT measurement.
		"""
		response = self._core.io.query_str('BERT:SETup:IGNore?')
		return Conversions.str_to_scalar_enum(response, enums.BertPattIgn)

	def set_ignore(self, ignore: enums.BertPattIgn) -> None:
		"""SCPI: BERT:SETup:IGNore \n
		Snippet: driver.bert.setup.set_ignore(ignore = enums.BertPattIgn.OFF) \n
		Activates ignoring of pure '0' or '1' bit sequences of at least 32 bits, so that faulty frames are excluded from the
		measurement. Some mobile radio standards indicate faulty frames with pure '0' or '1' bit sequences when errors (e.g.
		an incorrect checksum) are detected. \n
			:param ignore: OFF| ZERO| ONE OFF Pattern ignore is not active. ZERO Ignore bit sequences of 32 or more consecutive '0' for the BERT measurement. ONE Ignore bit sequences of 32 or more consecutive '1' for the BERT measurement.
		"""
		param = Conversions.enum_scalar_to_str(ignore, enums.BertPattIgn)
		self._core.io.write(f'BERT:SETup:IGNore {param}')

	def get_mcount(self) -> int:
		"""SCPI: BERT:SETup:MCOunt \n
		Snippet: value: int = driver.bert.setup.get_mcount() \n
		Enters the number of transmitted data bits/data blocks to be checked before the measurement is terminated. A BERT/BLER
		measurement does not count data suppressed by method RsSmw.Bert.Setup.denable|method RsSmw.Bler.Setup.denable.
		This termination criteria always terminates the measurement after the specified number of data bits/data blocks. Starting
		from this point, outputs the fourth value with 1 (= terminate measurement) if the result is queried. For the continuous
		measurement mode, the measurement restarts once the results have been queried. \n
			:return: mcount: integer Range: 0 to 4294967295
		"""
		response = self._core.io.query_str('BERT:SETup:MCOunt?')
		return Conversions.str_to_int(response)

	def set_mcount(self, mcount: int) -> None:
		"""SCPI: BERT:SETup:MCOunt \n
		Snippet: driver.bert.setup.set_mcount(mcount = 1) \n
		Enters the number of transmitted data bits/data blocks to be checked before the measurement is terminated. A BERT/BLER
		measurement does not count data suppressed by method RsSmw.Bert.Setup.denable|method RsSmw.Bler.Setup.denable.
		This termination criteria always terminates the measurement after the specified number of data bits/data blocks. Starting
		from this point, outputs the fourth value with 1 (= terminate measurement) if the result is queried. For the continuous
		measurement mode, the measurement restarts once the results have been queried. \n
			:param mcount: integer Range: 0 to 4294967295
		"""
		param = Conversions.decimal_value_to_str(mcount)
		self._core.io.write(f'BERT:SETup:MCOunt {param}')

	def get_merror(self) -> int:
		"""SCPI: BERT:SETup:MERRor \n
		Snippet: value: int = driver.bert.setup.get_merror() \n
		Enters the number of errors to occur before the measurement is terminated. This termination criterion always terminates
		the measurement after the specified number of errors. Starting from this point, outputs the fourth value with 1 (=
		terminate measurement) if the measurement result is queried. \n
			:return: merror: integer Range: 0 to 4294967295
		"""
		response = self._core.io.query_str('BERT:SETup:MERRor?')
		return Conversions.str_to_int(response)

	def set_merror(self, merror: int) -> None:
		"""SCPI: BERT:SETup:MERRor \n
		Snippet: driver.bert.setup.set_merror(merror = 1) \n
		Enters the number of errors to occur before the measurement is terminated. This termination criterion always terminates
		the measurement after the specified number of errors. Starting from this point, outputs the fourth value with 1 (=
		terminate measurement) if the measurement result is queried. \n
			:param merror: integer Range: 0 to 4294967295
		"""
		param = Conversions.decimal_value_to_str(merror)
		self._core.io.write(f'BERT:SETup:MERRor {param}')

	def get_timeout(self) -> float:
		"""SCPI: BERT:SETup:TIMeout \n
		Snippet: value: float = driver.bert.setup.get_timeout() \n
		Sets the timeout. \n
			:return: timeout: float Range: 0.1 to 1
		"""
		response = self._core.io.query_str('BERT:SETup:TIMeout?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: BERT:SETup:TIMeout \n
		Snippet: driver.bert.setup.set_timeout(timeout = 1.0) \n
		Sets the timeout. \n
			:param timeout: float Range: 0.1 to 1
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'BERT:SETup:TIMeout {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.BertPrbs:
		"""SCPI: BERT:SETup:TYPE \n
		Snippet: value: enums.BertPrbs = driver.bert.setup.get_type_py() \n
		Selects the PRBS sequence. The data generated by the PRBS generator is used as a reference for the measurement. \n
			:return: type_py: PRBS9| PRBS11| PRBS15| PRBS16| PRBS20| PRBS21| PRBS23
		"""
		response = self._core.io.query_str('BERT:SETup:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.BertPrbs)

	def set_type_py(self, type_py: enums.BertPrbs) -> None:
		"""SCPI: BERT:SETup:TYPE \n
		Snippet: driver.bert.setup.set_type_py(type_py = enums.BertPrbs.PN11) \n
		Selects the PRBS sequence. The data generated by the PRBS generator is used as a reference for the measurement. \n
			:param type_py: PRBS9| PRBS11| PRBS15| PRBS16| PRBS20| PRBS21| PRBS23
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.BertPrbs)
		self._core.io.write(f'BERT:SETup:TYPE {param}')

	def clone(self) -> 'Setup':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Setup(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
