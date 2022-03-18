from sherlockpipe.ml.ml_model_builder import MLModelBuilder
from sherlockpipe.ml.ml_training_set_preparer import MlTrainingSetPreparer


cpus = 1
first_negative_sector = 1
training_data_dir = "/mnt/DATA-2/training_data/"
cache_dir = "/home/martin/"
#ml_training_set_preparer = MlTrainingSetPreparer(training_data_dir, cache_dir)
#ml_training_set_preparer.prepare_positive_training_dataset(cpus)
# #ml_training_set_preparer.prepare_false_positive_training_dataset(cpus)
# ml_training_set_preparer.prepare_negative_training_dataset(first_negative_sector, cpus)
#MLSingleTransitsClassifier().load_candidate_single_transits(traid ning_data_dir, "tp")
MlTrainingSetPreparer.prepare_cadence_set_dir(training_data_dir, "short")
MLModelBuilder().get_model()
#MLModelBuilder()get_single_transit_model()
#TODO prepare_negative_training_dataset(negative_dir)
