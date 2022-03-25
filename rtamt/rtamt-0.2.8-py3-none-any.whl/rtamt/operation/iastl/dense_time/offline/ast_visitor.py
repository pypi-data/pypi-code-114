from rtamt.enumerations.options import Semantics
from rtamt.enumerations.comp_op import StlComparisonOperator
from rtamt.operation.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor, subtraction_operation


class IAStlDenseTimeOfflineAstVisitor(StlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        sample_left = self.visit(node.children[0], *args, **kwargs)
        sample_right = self.visit(node.children[1], *args, **kwargs)

        sample_return = []
        input_list = subtraction_operation(sample_left, sample_right)

        prev = float("nan")
        for i, in_sample in enumerate(input_list):
            if node.operator.value == StlComparisonOperator.EQ.value:
                out_val = - abs(in_sample[1])
            elif node.operator.value == StlComparisonOperator.NEQ.value:
                out_val = abs(in_sample[1])
            elif node.operator.value == StlComparisonOperator.LEQ.value or node.operator.value == StlComparisonOperator.LESS.value:
                out_val = - in_sample[1]
            elif node.operator.value == StlComparisonOperator.GEQ.value or node.operator.value == StlComparisonOperator.GREATER.value:
                out_val = in_sample[1]
            else:
                out_val = float('nan')

            if out_val != prev or i == len(input_list) - 1:
                sample_return.append([in_sample[0], out_val])
            prev = out_val

        return sample_return


        in_sample_1 = self.visit(node.children[0], args)
        in_sample_2 = self.visit(node.children[1], args)

        monitor = self.node_monitor_dict[node.name]
        out_sample = monitor.update(in_sample_1, in_sample_2)
        sat_samples = monitor.sat(in_sample_1, in_sample_2)
        out = []

        if self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
            for i, sample in enumerate(sat_samples):
                val = float("inf") if sample == True else -float("inf")
                out.append([out_sample[i][0], val])
        elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
            for i, sample in enumerate(sat_samples):
                val = float("inf") if sample == True else - float("inf")
                out.append([out_sample[i][0], val])
        elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        else:
            out = out_sample



        sample = StlDenseTimeOfflineAstVisitor.visitPredicate(self, node, *args, **kwargs)
        if self.ast.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
            for i, sample in enumerate(samples):
                val = float("inf") if sample == True else -float("inf")
                out.append([out_sample[i][0], val])
        elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
            for i, sample in enumerate(sat_samples):
                val = float("inf") if sample == True else - float("inf")
                out.append([out_sample[i][0], val])
        elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
            for i, sample in enumerate(sat_samples):
                out.append([out_sample[i][0], 0.0])
        else:
            out = out_sample

        return sample
