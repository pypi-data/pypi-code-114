import io

from datomizer import DatoTrainer
from datomizer.helpers import common_helper
from datomizer.helpers.generator import generator_helper
from datomizer.helpers.datasource import datasource_helper
from datomizer.utils import general, step_types
from datomizer.helpers.wrapper import schema_wrapper


class DatoGenerator(object):
    dato_trainer: DatoTrainer
    synth_id = 0
    datasource_id = 0

    def __init__(self, dato_trainer: DatoTrainer):
        """Create DatoGenerator object for generating data using the trained generative model.
        Args:
            dato_trainer: the DatoTrainer object trained on the input data."""
        dato_trainer.next_step_validation()
        self.dato_trainer = dato_trainer

    @classmethod
    def restore(cls, dato_trainer: DatoTrainer, synth_id):
        dato_generator = cls(dato_trainer)
        dato_generator.synth_id = synth_id
        dato_generator.wait()
        return dato_generator

    def get_flow(self) -> dict:
        self.restore_validation()
        return common_helper.get_flow(datomizer=self.dato_trainer.dato_mapper.datomizer,
                                      business_unit_id=self.dato_trainer.dato_mapper.business_unit_id,
                                      project_id=self.dato_trainer.dato_mapper.project_id,
                                      flow_id=self.synth_id,
                                      is_synth=True)

    def create_datasource(self) -> None:
        if self.datasource_id > 0:
            return
        self.datasource_id = datasource_helper.create_target_private_datasource(self.dato_trainer.dato_mapper.datomizer)

    def generate(self, wait=True) -> None:
        """Generate output data.
        Args:
            wait: use wait=False for asynchronous programming; True by default (awaits for the results)."""
        self.create_datasource()
        if self.synth_id > 0:
            return
        self.synth_id = generator_helper.generate(self.dato_trainer, self.datasource_id)
        if wait:
            self.wait()

    def wait(self) -> None:
        """Wait until the generate method returns."""
        self.restore_validation()
        status = common_helper.wait_for_step_type(datomizer=self.dato_trainer.dato_mapper.datomizer,
                                                  business_unit_id=self.dato_trainer.dato_mapper.business_unit_id,
                                                  project_id=self.dato_trainer.dato_mapper.project_id,
                                                  flow_id=self.synth_id,
                                                  is_synth=True,
                                                  step_type=step_types.GENERATE)
        if status == general.ERROR:
            raise Exception("Synth Failed")
        self.datasource_id = self.get_flow()[general.TARGET_DATASOURCE_ID]

    def get_generated_data(self) -> None:
        self.restore_validation()
        print(common_helper.get_generated_zip(datomizer=self.dato_trainer.dato_mapper.datomizer,
                                              business_unit_id=self.dato_trainer.dato_mapper.business_unit_id,
                                              project_id=self.dato_trainer.dato_mapper.project_id,
                                              flow_id=self.synth_id))

    def get_generated_data_csv(self, table_name: str = None) -> io.StringIO:
        """Get the generated data in a csv format.
                Args:
                    table_name: the name of the generated data
                Returns:
                    StringIO object containing the generated data"""
        self.restore_validation()

        table_name = self.dato_trainer.dato_mapper.schema.table(table_name)[schema_wrapper.NAME]

        return common_helper.get_generated_csv(datomizer=self.dato_trainer.dato_mapper.datomizer,
                                               business_unit_id=self.dato_trainer.dato_mapper.business_unit_id,
                                               project_id=self.dato_trainer.dato_mapper.project_id,
                                               flow_id=self.synth_id,
                                               table_name=table_name)

    def restore_validation(self):
        if not (self.synth_id > 0):
            raise Exception("synth id required for this step")
