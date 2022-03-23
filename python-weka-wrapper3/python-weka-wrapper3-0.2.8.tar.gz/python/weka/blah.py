import weka.core.jvm as jvm
from weka.core.converters import load_any_file
from weka.classifiers import Classifier, SingleClassifierEnhancer, FilteredClassifier, MultiSearch, AttributeSelectedClassifier, Evaluation
from weka.core.classes import MathParameter, from_commandline, Random, get_classname
from weka.filters import Filter
from weka.attribute_selection import ASEvaluation, ASSearch

jvm.start(packages=True)

data_modelos_1_2 = load_any_file("/home/fracpete/development/datasets/uci/vote.arff")
data_modelos_1_2.class_is_last()

base = Classifier(classname="weka.classifiers.trees.ADTree",
                  options=["-B", "10", "-E", "-3", "-S", "1"])

CostS_cls = SingleClassifierEnhancer(classname="weka.classifiers.meta.CostSensitiveClassifier",
                                     options=["-cost-matrix", "[0.0 1.0; 1.0 0.0]", "-S", "1"])
CostS_cls.classifier = base
smote = Filter(classname="weka.filters.supervised.instance.SMOTE",
               options=["-C", "0", "-K", "3", "-P", "250.0", "-S", "1"])
fc = FilteredClassifier(options=["-S", "1"])
fc.filter = smote
fc.classifier = CostS_cls
bagging_cls = SingleClassifierEnhancer(classname="weka.classifiers.meta.Bagging",
                                       options=["-P", "100", "-S", "1", "-num-slots", "1", "-I", "100"])
bagging_cls.classifier = fc
multisearch_cls = MultiSearch(options=["-S", "1"])
multisearch_cls.evaluation = "FM"
multisearch_cls.search = ["-sample-size", "100", "-initial-folds", "2", "-subsequent-folds", "10",
                          "-initial-test-set", ".", "-subsequent-test-set", ".", "-num-slots", "1"]
mparam = MathParameter()
mparam.prop = "numIterations"
mparam.minimum = 5.0
mparam.maximum = 50.0
mparam.step = 1.0
mparam.base = 10.0
mparam.expression = "I"
multisearch_cls.parameters = [mparam]
multisearch_cls.classifier = bagging_cls

AttS_cls = AttributeSelectedClassifier()
AttS_cls.search = from_commandline('weka.attributeSelection.GreedyStepwise -B -T -1.7976931348623157E308 -N -1 -num-slots 1', classname=get_classname(ASSearch))
AttS_cls.evaluation = from_commandline('weka.attributeSelection.CfsSubsetEval -P 1 -E 1', classname=get_classname(ASEvaluation))
AttS_cls.classifier = multisearch_cls

# original
# train, test = data_modelos_1_2.train_test_split(70.0, Random(1))
# AttS_cls.build_classifier(train)
# evl = Evaluation(test)
# evl.crossvalidate_model(AttS_cls, test, 10, Random(1))
# print(evl.summary())

# cross-validation
print("\ncross-validation\n")
evl = Evaluation(data_modelos_1_2)
evl.crossvalidate_model(AttS_cls, data_modelos_1_2, 10, Random(1))
print(evl.summary())

# train/test split
print("\ntrain/test split\n")
train, test = data_modelos_1_2.train_test_split(70.0, Random(1))
AttS_cls.build_classifier(train)
evl = Evaluation(test)
evl.test_model(AttS_cls, test)
print(evl.summary())

jvm.stop()
