from datomizer import DatoMapper
from datomizer.helpers import common_helper
from datomizer.helpers.train import train_helper
from datomizer.utils import general, step_types


class DatoTrainer(object):
    dato_mapper: DatoMapper
    train_id = 0
    model_id = 0
    evaluate = True

    def __init__(self, dato_mapper: DatoMapper):
        """Create DatoTrainer object for training a generative model for the mapped input data.
        Args:
            dato_mapper: the Datomapper object for the input data."""
        dato_mapper.next_step_validation()
        self.dato_mapper = dato_mapper

    @classmethod
    def restore(cls, dato_mapper: DatoMapper, train_id):
        dato_trainer = cls(dato_mapper)
        dato_trainer.train_id = train_id
        dato_trainer.wait()
        return dato_trainer

    def train(self, should_evaluate=True, wait=True) -> None:
        """Train a generative model.
        Args:
            should_evaluate: evaluate the generated data; Evaluation is performed (True) by default.
            wait: use wait=False for asynchronous programming; True by default (awaits for the results)."""
        if self.train_id > 0:
            return
        self.train_id = train_helper.train(self.dato_mapper, should_evaluate)
        self.evaluate = should_evaluate
        if wait:
            self.wait()

    def wait(self) -> None:
        """Wait until the train method returns."""
        self.restore_validation()
        status = common_helper.wait_for_step_type(datomizer=self.dato_mapper.datomizer,
                                                  business_unit_id=self.dato_mapper.business_unit_id,
                                                  project_id=self.dato_mapper.project_id,
                                                  flow_id=self.dato_mapper.flow_id,
                                                  step_type=step_types.EVALUATE if self.evaluate else step_types.TRAIN,
                                                  train_id=self.train_id)
        if status == general.ERROR:
            raise Exception("Trainer Failed")
        self.model_id = train_helper.get_train_iteration(self.dato_mapper, self.train_id)[general.MODELS][0][general.ID]

    def get_generated_data(self) -> None:
        self.next_step_validation()
        if not self.evaluate:
            return

        print(common_helper.get_generated_zip(datomizer=self.dato_mapper.datomizer,
                                              business_unit_id=self.dato_mapper.business_unit_id,
                                              project_id=self.dato_mapper.project_id,
                                              flow_id=self.dato_mapper.flow_id,
                                              train_id=self.train_id))

    def restore_validation(self):
        if not (self.train_id > 0):
            raise Exception("flow id required for this step")

    def next_step_validation(self):
        self.restore_validation()
        if not (self.model_id > 0):
            raise Exception("DatoTrainer not ready")
