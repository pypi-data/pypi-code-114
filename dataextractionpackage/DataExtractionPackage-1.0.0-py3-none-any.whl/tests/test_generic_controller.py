import unittest

from src.__main__ import MainClass


class GenericControllerTest(unittest.TestCase):

    # Initiate Asset Controller Class
    def setUp(self):
        main = MainClass("./src/tests/test_controller_config.yml")
        self.asset_controller = main.setup_asset_controller()
        self.attribute_controller = main.setup_attribute_controller()
        self.attribute_type_controller = main.setup_attribute_type_controller()
        self.domain_controller = main.setup_domain_controller()
        self.community_controller = main.setup_communitiy_controller()
        self.relation_controller = main.setup_relation_controller()
        self.relation_type_controller = main.setup_relation_types_controller()
        self.responsibilities_controller = main.setup_responsibilities_controller()
        self.users_controller = main.setup_users_controller()
        self.create_lists()

    def create_lists(self):
        self.assets_list = self.asset_controller.get_objects()
        self.attributes_list = self.attribute_controller.get_objects()
        self.attribute_types_list = self.attribute_type_controller.get_objects()
        self.communities_list = self.community_controller.get_objects()
        self.domains_list = self.domain_controller.get_objects()
        self.relations_list = self.relation_controller.get_objects()
        self.relation_types_list = self.relation_type_controller.get_objects()
        self.responsibilities_list = self.responsibilities_controller.get_objects()
        self.users_list = self.users_controller.get_objects()

    def testGetObjects(self):
        assert self.attributes_list.status_code == 200
        assert self.attribute_types_list.status_code == 200
        assert self.assets_list.status_code == 200
        assert self.communities_list.status_code == 200
        assert self.domains_list.status_code == 200
        assert self.relations_list.status_code == 200
        assert self.relation_types_list.status_code == 200
        assert self.responsibilities_list.status_code == 200
        assert self.users_list.status_code == 200

    def testExtractAssets(self):
        test_users = self.users_controller.extract_objects(self.users_list)

        test_assets = self.asset_controller.extract_objects(self.assets_list)
        test_attributes = self.attribute_controller.extract_objects(self.attributes_list)
        test_attribute_types = self.attribute_type_controller.extract_objects(self.attribute_types_list)
        test_communities = self.community_controller.extract_objects(self.communities_list)
        test_domains = self.domain_controller.extract_objects(self.domains_list)
        test_relations = self.relation_controller.extract_objects(self.relations_list)
        test_relations_types = self.relation_type_controller.extract_objects(self.relation_types_list)
        test_responsibilities = self.responsibilities_controller.extract_objects(self.responsibilities_list)

        assert test_assets
        assert test_attributes
        assert test_attribute_types
        assert test_communities
        assert test_domains
        assert test_relations
        assert test_relations_types
        assert test_responsibilities
        assert test_users

    def test_get_assets_as_pandas_db(self):
        test_asset_dataframe = self.asset_controller.get_pandas_db()
        test_attributes_dataframe = self.attribute_controller.get_pandas_db()
        test_attribute_types_dataframe = self.attribute_type_controller.get_pandas_db()
        test_communities_dataframe = self.community_controller.get_pandas_db()
        test_domain_dataframe = self.domain_controller.get_pandas_db()
        test_relation_dataframe = self.relation_controller.get_pandas_db()
        test_relation_type_dataframe = self.relation_type_controller.get_pandas_db()
        test_responsibilities_dataframe = self.responsibilities_controller.get_pandas_db()
        test_users_dataframe = self.users_controller.get_pandas_db()

        assert not test_asset_dataframe.columns.empty
        assert not test_asset_dataframe.empty

        assert not test_attributes_dataframe.columns.empty
        assert not test_attributes_dataframe.empty

        assert not test_attribute_types_dataframe.columns.empty
        assert not test_attribute_types_dataframe.empty

        assert not test_communities_dataframe.columns.empty
        assert not test_communities_dataframe.empty

        assert not test_domain_dataframe.columns.empty
        assert not test_domain_dataframe.empty

        assert not test_relation_dataframe.columns.empty
        assert not test_relation_dataframe.empty

        assert not test_relation_type_dataframe.columns.empty
        assert not test_relation_type_dataframe.empty

        assert not test_responsibilities_dataframe.columns.empty
        assert not test_responsibilities_dataframe.empty

        assert not test_users_dataframe.columns.empty
        assert not test_users_dataframe.empty
