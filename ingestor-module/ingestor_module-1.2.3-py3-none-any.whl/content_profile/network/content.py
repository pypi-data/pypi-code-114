from typing import ClassVar

from graphdb import GraphDb, GraphDbConnection
from graphdb.schema import Node, Relationship
from pandas import DataFrame

# LABEL NODE NAME & VARIABLE NAME
from ingestor.common.constants import LABEL, PROPERTIES, RELATIONSHIP, CONTENT, CATEGORY, SUBCATEGORY, COUNTRY, \
    CONTENT_ID, HOMEPAGE, ACTORS, TAGS, PACKAGES, PRODUCTS, ACTOR, PRODUCT, PACKAGE
# RELATIONSHIP NAME
from ingestor.content_profile.config import content_node_properties, HAS_CATEGORY, HAS_SUBCATEGORY, HAS_COUNTRY, \
    HAS_ACTOR, HAS_TAG, HAS_PRODUCT, HAS_PACKAGE, HAS_HOMEPAGE


class ContentNetworkGenerator:

    def __init__(
            self,
            connection_class: GraphDbConnection
    ):
        self.graph = GraphDb.from_connection(connection_class)

    @classmethod
    def from_connection_uri(
            cls,
            connection_uri: str
    ) -> ClassVar:
        """Create new object based on connection uri
        :param connection_uri: string connection uri
        :return: object class
        """
        return cls(GraphDbConnection.from_uri(connection_uri))

    @classmethod
    def from_connection_class(
            cls,
            connection_class: GraphDbConnection
    ) -> ClassVar:
        """Define new class based on object connection
        :param connection_class: object connection class
        :return: object class
        """
        return cls(connection_class)

    def create_content_node(self, payload: DataFrame):
        for property_num, property_val in payload.iterrows():
            content_node = None
            if property_val[CONTENT_ID] and property_val[CONTENT_ID] is not None \
                    and property_val[CONTENT_ID] != '':
                content_node_property = content_node_properties(property_val)
                content_node = Node(**{LABEL: CONTENT, PROPERTIES: content_node_property})
                self.graph.create_node(content_node)

        return content_node

    def child_network_generator(self, feature, label, relationship, payload: DataFrame):
        content_node = self.create_content_node(payload=payload)
        for pros in payload[feature].loc[0]:
            static_node = Node(**{LABEL: label, PROPERTIES: pros})
            node_in_graph = self.graph.find_node(static_node)
            if len(node_in_graph) == 0:
                print("Record not available in static network for node {0}".format(static_node))
            else:
                self.graph.create_relationship_without_upsert(content_node, node_in_graph[0],
                                                              Relationship(**{RELATIONSHIP: relationship}))
        return content_node

    def content_creator_updater_network(self, payload: DataFrame) -> bool:
        print("Generating content to category network")
        self.child_network_generator(CATEGORY, CATEGORY, HAS_CATEGORY, payload=payload)
        print("Generating content to subcategory network")
        self.child_network_generator(SUBCATEGORY, SUBCATEGORY, HAS_SUBCATEGORY, payload=payload)
        print("Generating content to country network")
        self.child_network_generator(COUNTRY, COUNTRY, HAS_COUNTRY, payload=payload)
        print("Generating content to actor network")
        self.child_network_generator(ACTORS, ACTOR, HAS_ACTOR, payload=payload)
        print("Generating content to tag network")
        self.child_network_generator(TAGS, TAGS, HAS_TAG, payload=payload)
        print("Generating content to product network")
        self.child_network_generator(PRODUCTS, PRODUCT, HAS_PRODUCT, payload=payload)
        print("Generating content to package network")
        self.child_network_generator(PACKAGES, PACKAGE, HAS_PACKAGE, payload=payload)
        print("Generating content to homepage network")
        self.child_network_generator(HOMEPAGE, HOMEPAGE, HAS_HOMEPAGE, payload=payload)
        return True
