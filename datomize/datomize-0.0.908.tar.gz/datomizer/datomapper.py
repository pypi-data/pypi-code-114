from datomizer import Datomizer
from datomizer.helpers.datasource import datasource_helper
from datomizer.helpers import common_helper
from datomizer.helpers.business_unit_project import business_unit_project_helper as bu_proj_helper
from datomizer.helpers.autodiscovery import autodiscovery_helper
from datomizer.helpers.wrapper.schema_wrapper import SchemaWrapper
from datomizer.utils import step_types, general


class DatoMapper(object):
    datomizer: Datomizer
    business_unit_id = 0
    project_id = 0
    datasource_id = 0
    flow_id = 0
    schema: SchemaWrapper = None

    def __init__(self, datomizer: Datomizer):
        """Create DatoMapper object for extracting the structure of the input data.
        Args:
            datomizer: the Datomizer authentication object."""
        datomizer.next_step_validation()
        self.datomizer = datomizer
        self.business_unit_id, self.project_id = bu_proj_helper.get_default_business_unit_project(self.datomizer)

    @classmethod
    def restore(cls, datomizer: Datomizer, flow_id):
        dato_mapper = cls(datomizer)
        dato_mapper.flow_id = flow_id
        dato_mapper.wait()
        return dato_mapper

    def get_flow(self) -> dict:
        self.restore_validation()
        return common_helper.get_flow(self.datomizer, self.business_unit_id, self.project_id, self.flow_id)

    def create_datasource_from_path(self, path) -> None:
        self.set_datasource_validation()
        self.datasource_id = datasource_helper.create_origin_private_datasource_from_path(self.datomizer, path)

    def create_datasource_from_df(self, df, name="temp_df") -> None:
        self.set_datasource_validation()
        self.datasource_id = datasource_helper.create_origin_private_datasource_from_df(self.datomizer, df, name)

    def create_datasource(self, path, df, name):
        if path is not None:
            self.create_datasource_from_path(path)
        elif df is not None:
            self.create_datasource_from_df(df, name)

    def discover(self, path=None, df=None, df_name=None, sample_percent: int = 1, title: str = "sdk_flow", wait=True) -> None:
        """Extract the structure of the input data.
        Args:
            path: full path for the input data
            df: a dataframe containing the input data
            df_name: the name of the input data
            sample_percent: the sampling ratio; 1 (100%) by default.
            title: the name of the created task in Datomize; "sdk_flow" by default.
            wait: use wait=False for asynchronous programming; True by default (awaits for the results)."""
        self.create_datasource(path, df, df_name if df_name else title)

        self.pre_run_validation()
        self.flow_id = autodiscovery_helper.discover(self.datomizer,
                                                     self.business_unit_id, self.project_id, self.datasource_id,
                                                     sample_percent, title)
        if wait:
            self.wait()

    def wait(self) -> None:
        """Wait until the discovery method returns."""
        self.restore_validation()
        status = common_helper.wait_for_step_type(datomizer=self.datomizer,
                                                  business_unit_id=self.business_unit_id,
                                                  project_id=self.project_id,
                                                  flow_id=self.flow_id,
                                                  step_type=step_types.COLUMN_DISCOVERY)
        if status == general.ERROR:
            raise Exception("Auto Discovery Failed")
        self.datasource_id = self.get_flow()[general.ORIGIN_DATASOURCE_ID]
        self.get_schema_discovery()

    def get_schema_discovery(self) -> None:
        """Get a data mapping object for the input data.
        Returns:
            Datomize mapping dictionary"""
        self.restore_validation()
        if self.schema:
            return
        self.schema = SchemaWrapper(autodiscovery_helper
                                    .get_schema_discovery(self.datomizer,
                                                          self.business_unit_id, self.project_id, self.flow_id))

    def base_validation(self):
        if not (self.business_unit_id > 0 and self.project_id > 0):
            raise Exception("missing base properties")

    def set_datasource_validation(self):
        self.base_validation()
        if self.datasource_id > 0:
            raise Exception("datasource id cannot be mutated")

    def pre_run_validation(self):
        self.base_validation()
        if not (self.datasource_id > 0):
            raise Exception("datasource id required for this step")

    def restore_validation(self):
        self.base_validation()
        if not (self.flow_id > 0):
            raise Exception("flow id required for this step")

    def next_step_validation(self):
        self.restore_validation()
        if not self.schema:
            raise Exception("DatoMapper not ready")
