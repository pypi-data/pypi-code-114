from rtamt.operation.iastl.discrete_time.online.ast_visitor import IAStlDiscreteTimeOnlineAstVisitor
from rtamt.operation.abstract_discrete_time_online_evaluator import discrete_time_online_evaluator_factory

def IAStlDiscreteTimeOnlineEvaluator(semantics):
    iastlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(IAStlDiscreteTimeOnlineAstVisitor)(semantics)
    return iastlDiscreteTimeOnlineEvaluator
