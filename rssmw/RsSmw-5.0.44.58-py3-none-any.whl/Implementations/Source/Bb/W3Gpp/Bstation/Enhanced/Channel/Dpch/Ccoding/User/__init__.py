from typing import List

from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel:DPCH:CCODing:USER:CATalog \n
		Snippet: value: List[str] = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.user.get_catalog() \n
		Queries existing files with stored user channel codings. The files are stored with the fixed file extensions *.3g_ccod_dl
		in a directory of the user's choice. The directory applicable to the commands is defined with the command method RsSmw.
		MassMemory.currentDirectory. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel:DPCH:CCODing:USER:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel:DPCH:CCODing:USER:DELete \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.user.delete(filename = '1') \n
		Deletes the specified files with stored user channel codings. The files are stored with the fixed file extensions *.
		3g_ccod_dl in a directory of the user's choice. The directory applicable to the commands is defined with the command
		method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file name,
		without the path and the file extension. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel:DPCH:CCODing:USER:DELete {param}')

	def load(self, filename: str, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:USER:LOAD \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.user.load(filename = '1', channelNull = repcap.ChannelNull.Default) \n
		The command loads the specified files with stored user channel codings. The files are stored with the fixed file
		extensions *.3g_ccod_dl in a directory of the user's choice. The directory applicable to the commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name, without the path and the file extension. \n
			:param filename: user_coding
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(filename)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:USER:LOAD {param}')

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
