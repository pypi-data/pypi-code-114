import io
import json

from drb import DrbNode
from drb.factory import DrbFactory
from drb_impl_http import DrbHttpNode
from drb_impl_json import JsonNode

from .odata_nodes import ODataServiceNode, ODataProductNode


class OdataFactory(DrbFactory):
    def _create(self, node: DrbNode) -> DrbNode:
        if isinstance(node, DrbHttpNode):
            if '$format=json' not in node.path.original_path:
                if '?' not in node.path.original_path:
                    node._path = node.path.original_path + '?&$format=json'
                else:
                    node._path = node.path.original_path + '&$format=json'
            req = node.get_impl(io.BytesIO).read().decode()
            json_node = JsonNode(json.loads(req))
            return [ODataProductNode(source=node.path.original_path,
                                     auth=node.auth,
                                     data=e.value
                                     ) for e in json_node['value', :]]
        return ODataServiceNode(node.path.name)
