from rtamt.operation.iastl.dense_time.offline.ast_visitor import IAStlDenseTimeOfflineAstVisitor
from rtamt.operation.abstract_dense_time_offline_evaluator import dense_time_offline_evaluator_factory

def IAStlDenseTimeOfflineEvaluator():
    iastlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(IAStlDenseTimeOfflineAstVisitor)()
    return iastlDenseTimeOfflineEvaluator
