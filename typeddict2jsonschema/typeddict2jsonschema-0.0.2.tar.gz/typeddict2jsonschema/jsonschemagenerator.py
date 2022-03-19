"""Jsonschema Generator"""
import ast
import logging
from typing import Union, Any

typing_to_jsonschema = {
    "bool": "boolean",
    "str": "string",
    "int": "integer",
    "Any": "object",
    "Dict": "object"
}

def from_typing_to_typedef(value: Union[str, Any]):
    if isinstance(value, str):
        return {
            "type": typing_to_jsonschema[value]
        }
    else:
        return value


class FromTypedDict(ast.NodeTransformer):
    """
    AST Tree visitor that generates from a typed dict valid json schemas
    """

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("typeddict2jsonschema")
        # The basis object that should be known
        self.known_objects = {
            "TypedDict": {
                "$id": "TypedDict",
                "properties": {},
                "required": []
            }
        }

    def get_known_objects(self):
        return self.known_objects

    def visit_Name(self, node):
        return node.id

    def generic_visit(self, node):
        return node

    def visit_Tuple(self, node):
        to_ret = []
        for t in node.elts:
            to_ret.append(self.visit(t))
        return to_ret


    def visit_Index(self, node):
        self.logger.debug(ast.dump(node))
        return self.visit(node.value)

    def visit_Str(self, node):
        self.logger.debug(__name__)
        return node.s


    def visit_Subscript(self, node):
        self.logger.debug(ast.dump(node))

        self.logger.debug(node.value.id)
        slices = self.visit(node.slice)
        self.logger.debug(node.ctx)
        self.logger.debug(slices)
        if node.value.id == "List":
            return {
                "type": "array",
                "items": from_typing_to_typedef(slices)
            }
        elif node.value.id == "Dict":
            return { "type": "object"}
        elif node.value.id == "Literal":
            return { "enum": slices }
        elif node.value.id == "Union":
            return {
                "anyOf": [
                    from_typing_to_typedef(self.visit(slice))
                    for slice in slices
                ]
            }
        elif node.value.id == "Optional":
            slice = self.visit(slices)
            return {
                "anyOf": [
                    {"type": "null"},
                    from_typing_to_typedef(slice)
                ]
            }
        elif node.value.id == "Tuple":
            return {
                "type": "array",
                "prefixItems": [
                    from_typing_to_typedef(slice)
                    for slice in self.visit(slices)
                ]
            }
        else:
            raise NotImplementedError(f"%{node.value.id} not yet supported")


    def visit_Literal(self, node):
        self.logger.debug(ast.dump(node))
        raise KeyError

    def visit_AnnAssign(self, node):
        # self.logger.debug(ast.dump(node))
        target = self.visit(node.target)
        annotation = self.visit(node.annotation)

        if isinstance(annotation, dict):
            return {
                target: annotation
            }
        elif annotation in self.known_objects:
            return {
                target: {
                    "type": "object",
                    "properties": self.known_objects[annotation]["properties"],
                    "required": self.known_objects[annotation]["required"]
                }
            }
        # It is a basic type
        return {
            target: {
                "type": typing_to_jsonschema[annotation]
            }
        }

    def visit_Keyword(self, node):
        return node

    def visit_NameConstant(self, node):
        return node.value


    def visit_ClassDef(self, node):
        self.logger.debug(ast.dump(node))

        type_annotation = {}

        super_class_required_fields = []
        super_class_properties = {}

        for b in node.bases:
            to_add = self.known_objects[self.visit(b)]
            super_class_required_fields += to_add["required"]
            super_class_properties = { **super_class_properties, **to_add["properties"]}

        this_properties = {}
        keywords = self.visit(node.keywords)
        total = True
        for k in keywords:
            if k.arg == "total":
                total = self.visit(k.value)

        for n in node.body:
            if isinstance(n, ast.AnnAssign):
                res = self.visit(n)
                this_properties = { **this_properties, **res }

        if total:
            required_keys = super_class_required_fields +  list(this_properties.keys())
        else:
            required_keys = super_class_required_fields

        type_annotation = { **this_properties, **super_class_properties}

        this = {
                "$id": node.name,
                "properties": type_annotation,
                "required": required_keys
        }
        self.known_objects[node.name] = this

        return {
            node.name: this
        }


def analyze(program: str):
    parsed_program = ast.parse(program)
    statement_list = parsed_program.body

    analyzer = FromTypedDict()
    for stmt in statement_list:
        analyzer.visit(stmt)
    return analyzer.get_known_objects()