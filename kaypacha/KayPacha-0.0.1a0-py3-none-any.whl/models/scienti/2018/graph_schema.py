# Scienti data model 2018
# SCHEMA version for modification on the relations, it is vertioned as well
from .graph_schema_product import graph_product
from .graph_schema_network import graph_network
from .graph_schema_project import graph_project

graph_schema = {"SCIENTI_MODEL": 2018}
graph_schema["MODELS"] = {}


graph_schema["MODELS"]["network"] = graph_network
graph_schema["MODELS"]["product"] = graph_product
graph_schema["MODELS"]["project"] = graph_project
