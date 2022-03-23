from .graph_fields_product import product_fields
from .graph_fields_network import network_fields
from .graph_fields_project import project_fields
graph_fields = {}

# adding fields for every main entity
graph_fields["EN_PRODUCTO"] = product_fields
graph_fields["EN_RED"] = network_fields
graph_fields["EN_PROYECTO"] = project_fields
