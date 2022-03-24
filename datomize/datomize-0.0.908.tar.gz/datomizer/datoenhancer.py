from datomizer import DatoMapper
from datomizer.helpers import common_helper
from datomizer.helpers.train import enhance_ml_helper, train_helper
from datomizer.utils import general, step_types
from datomizer.helpers.wrapper import schema_wrapper


class DatoEnhancer(object):
    dato_mapper: DatoMapper
    train_id = 0
    model_id = 0
    target_table = ""
    target_column = ""

    def __init__(self, dato_mapper: DatoMapper):
        dato_mapper.next_step_validation()
        self.dato_mapper = dato_mapper

    @classmethod
    def restore(cls, dato_mapper: DatoMapper, train_id):
        dato_enhancer = cls(dato_mapper)
        dato_enhancer.train_id = train_id
        dato_enhancer.wait()
        return dato_enhancer

    def enhance(self, target_table="", target_column="", metric_list=[], algorithm_list=[], wait=True) -> None:
        if self.train_id > 0:
            return

        metric_list = [metric.value for metric in metric_list]
        algorithm_list = [algorithm.value for algorithm in algorithm_list]

        self.target_table = self.dato_mapper.schema.table(target_table)[schema_wrapper.NAME]
        self.target_column = self.dato_mapper.schema.column(target_table, target_column)[schema_wrapper.NAME]

        self.train_id = enhance_ml_helper.enhance_ml_evaluate(self.dato_mapper,
                                                              target_table=self.target_table,
                                                              target_column=self.target_column,
                                                              metric_list=metric_list, algorithm_list=algorithm_list)
        if wait:
            self.wait()

    def wait(self) -> None:
        """Wait until the train method returns."""
        self.restore_validation()
        status = common_helper.wait_for_step_type(datomizer=self.dato_mapper.datomizer,
                                                  business_unit_id=self.dato_mapper.business_unit_id,
                                                  project_id=self.dato_mapper.project_id,
                                                  flow_id=self.dato_mapper.flow_id,
                                                  step_type=step_types.ML_SPLIT_AND_EVALUATE,
                                                  train_id=self.train_id)
        if status == general.ERROR:
            raise Exception("Trainer Failed")
        train = train_helper.get_train_iteration(self.dato_mapper, self.train_id)
        print(train)
        self.model_id = train[general.MODELS][0][general.ID]

    def get_generated_data(self) -> None:
        self.restore_validation()
        print(common_helper.get_generated_zip(datomizer=self.dato_mapper.datomizer,
                                              business_unit_id=self.dato_mapper.business_unit_id,
                                              project_id=self.dato_mapper.project_id,
                                              flow_id=self.dato_mapper.flow_id,
                                              train_id=self.train_id))

    def restore_validation(self):
        if not (self.train_id > 0):
            raise Exception("flow id required for this step")
