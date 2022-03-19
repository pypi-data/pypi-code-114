from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30LdmInjectionLayer:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:LAYer:LEVel \n
		Snippet: value: enums.Atsc30LdmInjectionLayer = driver.source.bb.a3Tsc.plp.layer.level.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the enhanced layer injection levels relative to the core in dB. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: ldm_inj_level: L00| L05| L10| L15| L20| L25| L30| L35| L40| L45| L50| L60| L70| L80| L90| L100| L110| L120| L130| L140| L150| L160| L170| L180| L190| L200| L210| L220| L230| L240| L250 Level Lx with x/10 meaning the level in dB"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:LAYer:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30LdmInjectionLayer)
