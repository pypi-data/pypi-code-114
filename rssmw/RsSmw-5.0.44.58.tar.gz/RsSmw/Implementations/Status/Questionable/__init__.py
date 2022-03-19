from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Questionable:
	"""Questionable commands group definition. 10 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("questionable", core, parent)

	@property
	def bit(self):
		"""bit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bit'):
			from .Bit import Bit
			self._bit = Bit(self._core, self._cmd_group)
		return self._bit

	def get_condition(self) -> str:
		"""SCPI: STATus:QUEStionable:CONDition \n
		Snippet: value: str = driver.status.questionable.get_condition() \n
		Queries the content of the CONDition part of the STATus:QUEStionable register. This part contains information on the
		action currently being performed in the instrument. The content is not deleted after being read out since it indicates
		the current hardware status. \n
			:return: condition: string
		"""
		response = self._core.io.query_str('STATus:QUEStionable:CONDition?')
		return trim_str_response(response)

	def set_condition(self, condition: str) -> None:
		"""SCPI: STATus:QUEStionable:CONDition \n
		Snippet: driver.status.questionable.set_condition(condition = '1') \n
		Queries the content of the CONDition part of the STATus:QUEStionable register. This part contains information on the
		action currently being performed in the instrument. The content is not deleted after being read out since it indicates
		the current hardware status. \n
			:param condition: string
		"""
		param = Conversions.value_to_quoted_str(condition)
		self._core.io.write(f'STATus:QUEStionable:CONDition {param}')

	def get_enable(self) -> str:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: value: str = driver.status.questionable.get_enable() \n
		Sets the bits of the ENABle part of the STATus:QUEStionable register. The enable part determines which events of the
		STATus:EVENt part are enabled for the summary bit in the status byte. These events can be used for a service request. If
		a bit in the ENABle part is 1, and the correesponding EVENt bit is true, a positive transition occurs in the summary bit.
		This transition is reportet to the next higher level. \n
			:return: enable: string
		"""
		response = self._core.io.query_str('STATus:QUEStionable:ENABle?')
		return trim_str_response(response)

	def set_enable(self, enable: str) -> None:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: driver.status.questionable.set_enable(enable = '1') \n
		Sets the bits of the ENABle part of the STATus:QUEStionable register. The enable part determines which events of the
		STATus:EVENt part are enabled for the summary bit in the status byte. These events can be used for a service request. If
		a bit in the ENABle part is 1, and the correesponding EVENt bit is true, a positive transition occurs in the summary bit.
		This transition is reportet to the next higher level. \n
			:param enable: string
		"""
		param = Conversions.value_to_quoted_str(enable)
		self._core.io.write(f'STATus:QUEStionable:ENABle {param}')

	def get_ntransition(self) -> str:
		"""SCPI: STATus:QUEStionable:NTRansition \n
		Snippet: value: str = driver.status.questionable.get_ntransition() \n
		Sets the bits of the NTRansition part of the STATus:QUEStionable register. If a bit is set, a transition from 1 to 0 in
		the condition part causes an entry to be made in the EVENt part of the register. \n
			:return: ntransition: string
		"""
		response = self._core.io.query_str('STATus:QUEStionable:NTRansition?')
		return trim_str_response(response)

	def set_ntransition(self, ntransition: str) -> None:
		"""SCPI: STATus:QUEStionable:NTRansition \n
		Snippet: driver.status.questionable.set_ntransition(ntransition = '1') \n
		Sets the bits of the NTRansition part of the STATus:QUEStionable register. If a bit is set, a transition from 1 to 0 in
		the condition part causes an entry to be made in the EVENt part of the register. \n
			:param ntransition: string
		"""
		param = Conversions.value_to_quoted_str(ntransition)
		self._core.io.write(f'STATus:QUEStionable:NTRansition {param}')

	def get_ptransition(self) -> str:
		"""SCPI: STATus:QUEStionable:PTRansition \n
		Snippet: value: str = driver.status.questionable.get_ptransition() \n
		Sets the bits of the NTRansition part of the STATus:QUEStionable register. If a bit is set, a transition from 1 to 0 in
		the condition part causes an entry to be made in the EVENt part of the register. \n
			:return: ptransition: string
		"""
		response = self._core.io.query_str('STATus:QUEStionable:PTRansition?')
		return trim_str_response(response)

	def set_ptransition(self, ptransition: str) -> None:
		"""SCPI: STATus:QUEStionable:PTRansition \n
		Snippet: driver.status.questionable.set_ptransition(ptransition = '1') \n
		Sets the bits of the NTRansition part of the STATus:QUEStionable register. If a bit is set, a transition from 1 to 0 in
		the condition part causes an entry to be made in the EVENt part of the register. \n
			:param ptransition: string
		"""
		param = Conversions.value_to_quoted_str(ptransition)
		self._core.io.write(f'STATus:QUEStionable:PTRansition {param}')

	def get_event(self) -> str:
		"""SCPI: STATus:QUEStionable:[EVENt] \n
		Snippet: value: str = driver.status.questionable.get_event() \n
		Queries the content of the EVENt part of the method RsSmw.Status.Questionable.event register. This part contains
		information on the actions performed in the instrument since the last readout. The content of the EVENt part is deleted
		after being read out. \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('STATus:QUEStionable:EVENt?')
		return trim_str_response(response)

	def set_event(self, value: str) -> None:
		"""SCPI: STATus:QUEStionable:[EVENt] \n
		Snippet: driver.status.questionable.set_event(value = '1') \n
		Queries the content of the EVENt part of the method RsSmw.Status.Questionable.event register. This part contains
		information on the actions performed in the instrument since the last readout. The content of the EVENt part is deleted
		after being read out. \n
			:param value: string
		"""
		param = Conversions.value_to_quoted_str(value)
		self._core.io.write(f'STATus:QUEStionable:EVENt {param}')

	def clone(self) -> 'Questionable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Questionable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
