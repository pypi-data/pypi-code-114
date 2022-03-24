from itertools import chain
from typing import ClassVar

from graphdb import GraphDb, GraphDbConnection
from graphdb.schema import Node, Relationship
from pandas import DataFrame

# LABEL NODE NAME & VARIABLE NAME
from ingestor.common.constants import LABEL, PROPERTIES, RELATIONSHIP, CONTENT, CATEGORY, SUBCATEGORY, COUNTRY, \
    CONTENT_ID, HOMEPAGE, ACTORS, TAGS, PACKAGES, PRODUCTS, ACTOR, PRODUCT, PACKAGE, CONTENT_CORE, CONTENT_CORE_ID, \
    CONTENT_CORE_TITLE, CONTENT_CORE_EPISODE, CONTENT_CORE_SYNOPSIS, CONTENT_CORE_SYNOPSIS_EN, SEASON_ID, SEASON, \
    SEASON_NAME, HOMEPAGE_ID, CC_SIMILARITY_SCORE, ALL_SIMILARITY_SCORE
# RELATIONSHIP NAME
from ingestor.content_profile.config import content_node_properties, HAS_CATEGORY, HAS_SUBCATEGORY, HAS_COUNTRY, \
    HAS_ACTOR, HAS_TAG, HAS_PRODUCT, HAS_PACKAGE, HAS_HOMEPAGE, HAS_CONTENT_CORE
from ingestor.content_profile.content_similarity import cluster_data_to_df, generate_new_features, \
    generate_tfidf_matrix, calculate_cosine_similarity, cluster_data_to_single_df, combine_features, create_tfidf_df, \
    calculate_single_cosine_similarity


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
        if feature in payload.columns:
            for props in payload[feature].loc[0]:
                static_node = Node(**{LABEL: label, PROPERTIES: props})
                node_in_graph = self.graph.find_node(static_node)
                if len(node_in_graph) == 0:
                    print("Record not available in static network for node {0}".format(static_node))
                else:
                    self.graph.create_relationship_without_upsert(content_node, node_in_graph[0],
                                                                  Relationship(**{RELATIONSHIP: relationship}))
        else:
            print("Feature not available")
        return content_node

    def child_network_generator_2(self, content_node, feature, label, relationship, payload: DataFrame):
        if feature in payload.columns:
            for props in payload[feature].loc[0]:
                final_content_core_props = self.prepare_content_core_properties(props)
                final_content_core_node = Node(**{LABEL: label, PROPERTIES: final_content_core_props})

                final_content_core_node = self.graph.create_node(final_content_core_node)

                self.graph.create_relationship_without_upsert(content_node, final_content_core_node,
                                                              Relationship(**{RELATIONSHIP: relationship}))
        else:
            print("Feature not available")

        return content_node

    def prepare_content_core_properties(self, props):
        final_content_core_props = {}
        if CONTENT_CORE_ID in props:
            self.add_content_core_properties(final_content_core_props, props)

            self.add_content_core_synopsis(final_content_core_props, props)
            self.add_season(final_content_core_props, props)
        return final_content_core_props

    def add_season(self, final_content_core_props, props):
        if SEASON_ID in props:
            node_content_season = Node(**{LABEL: SEASON, PROPERTIES: {SEASON_ID: props[SEASON_ID]}})
            node_content_season = self.graph.find_node(node_content_season)
            final_content_core_props[SEASON_NAME] = node_content_season[0].properties[SEASON_NAME]

    def add_content_core_synopsis(self, final_content_core_props, props):
        node_content_core_synopsis = Node(
            **{LABEL: CONTENT_CORE_SYNOPSIS, PROPERTIES: {CONTENT_CORE_ID: props[CONTENT_CORE_ID]}})
        node_content_core_synopsis = self.graph.find_node(node_content_core_synopsis)
        if len(node_content_core_synopsis) > 0:
            final_content_core_props[CONTENT_CORE_SYNOPSIS] = node_content_core_synopsis[0].properties[
                CONTENT_CORE_SYNOPSIS]
            final_content_core_props[CONTENT_CORE_SYNOPSIS_EN] = node_content_core_synopsis[0].properties[
                CONTENT_CORE_SYNOPSIS_EN]

    def add_content_core_properties(self, final_content_core_props, props):
        node_content_core = Node(
            **{LABEL: CONTENT_CORE, PROPERTIES: {CONTENT_CORE_ID: props[CONTENT_CORE_ID]}})
        node_content_core = self.graph.find_node(node_content_core)
        final_content_core_props[CONTENT_CORE_ID] = node_content_core[0].properties[CONTENT_CORE_ID]
        final_content_core_props[CONTENT_CORE_TITLE] = node_content_core[0].properties[CONTENT_CORE_TITLE]
        final_content_core_props[CONTENT_CORE_EPISODE] = node_content_core[0].properties[CONTENT_CORE_EPISODE]

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
        content_node = self.child_network_generator(HOMEPAGE, HOMEPAGE, HAS_HOMEPAGE, payload=payload)
        print("Generating content to content core network")
        self.child_network_generator_2(content_node, CONTENT_CORE, CONTENT_CORE, HAS_CONTENT_CORE, payload=payload)
        return True

    def specified_homepage_network_data(self):
        dict_ids = self.graph.custom_query(F'''
        g.V().out('{HAS_HOMEPAGE}').valueMap('{HOMEPAGE_ID}').dedup()
        ''', payload={
            'HAS_HOMEPAGE': HAS_HOMEPAGE,
            'HOMEPAGE_ID': HOMEPAGE_ID
        })
        list_dict_ids = list(chain.from_iterable(dict_ids))
        list_homepage_ids = list(map(lambda x: x[HOMEPAGE_ID], list_dict_ids))
        list_homepage_ids = [item[0] for item in list_homepage_ids]

        homepage_network = []
        for i, ids in enumerate(list_homepage_ids):
            query_network = self.graph.custom_query(f'''
                    g.V().has('{HOMEPAGE_ID}',{ids}).in('{HAS_HOMEPAGE}').valueMap().by(unfold()).toList()
                    ''', payload={
                'HOMEPAGE_ID': HOMEPAGE_ID,
                'ids': ids,
                'HAS_HOMEPAGE': HAS_HOMEPAGE
            })
            homepage_network.append(query_network)
        return homepage_network, list_homepage_ids

    def add_similarity_property(self, list_dict_content_similarities, list_homepage_id):
        content_similarity_property = {}
        for (homepage_id, dict_content_similarities) in zip(list_homepage_id, list_dict_content_similarities):
            for key, value in dict_content_similarities.items():
                output_type = {homepage_id: value}
                content_similarity_property.setdefault(key, [])
                content_similarity_property[key].append(output_type)

        for content_id, sim_property in content_similarity_property.items():
            node_to_update = Node(**{LABEL: CONTENT, PROPERTIES: {CONTENT_ID: content_id}})
            query_content_node = self.graph.find_node(node_to_update)
            dict_similarity_score = dict(sum(map(list, map(dict.items, sim_property)), []))
            new_node = self.graph.update_node_property(query_content_node[0],
                                                       {CC_SIMILARITY_SCORE: dict_similarity_score})
        return new_node

    def get_all_content(self):
        query = self.graph.custom_query(f'''
        g.V().hasLabel('{CONTENT}').valueMap().by(unfold()).toList()
        ''', payload={
            'CONTENT': CONTENT
        })
        return query

    def add_all_content_similarity_property(self, all_content_dict_cos_sim):
        for key, value in all_content_dict_cos_sim.items():
            query = self.graph.custom_query(f'''
            g.V().hasLabel('{CONTENT}').has('{CONTENT_ID}', {key})
            .property('{ALL_SIMILARITY_SCORE}', '{value}').valueMap()
            ''', payload={
                'CONTENT': CONTENT,
                'CONTENT_ID': CONTENT_ID,
                'key': key,
                'ALL_SIMILARITY_SCORE': ALL_SIMILARITY_SCORE,
                'value': value
            })
        return query

    def add_content_similarity_homepage_wise(self):
        # Calculate Content-Similarity in Homepage_id Wise
        list_homepage_network, list_homepage_ids = self.specified_homepage_network_data()
        list_dataframe_homepage = cluster_data_to_df(list_homepage_network)
        list_new_df_homepage = generate_new_features(list_dataframe_homepage)
        list_tfidf_df = generate_tfidf_matrix(list_new_df_homepage)
        list_dict_content_similarities = calculate_cosine_similarity(list_tfidf_df)
        output_content_similarity_homepageid_wise = self.add_similarity_property(list_dict_content_similarities,
                                                                                 list_homepage_ids)

        return output_content_similarity_homepageid_wise

    def add_content_similarity_all_content(self):
        all_content_cluster = self.get_all_content()
        all_content_df = cluster_data_to_single_df(all_content_cluster)
        all_content_new_df = combine_features(all_content_df)
        all_content_tfidf = create_tfidf_df(all_content_new_df)
        all_content_dict_cos_sim = calculate_single_cosine_similarity(all_content_tfidf)
        output_all_content_similarity = self.add_all_content_similarity_property(all_content_dict_cos_sim)
        return output_all_content_similarity
