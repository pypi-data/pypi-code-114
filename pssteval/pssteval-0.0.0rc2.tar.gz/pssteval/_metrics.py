from io import StringIO
from typing import NamedTuple


class ErrorSummary(NamedTuple):
    tp: int
    tn: int
    fp: int
    fn: int

    def precision(self):
        return self.tp / (self.tp + self.fp)


    def recall(self):
        return self.tp / (self.tp + self.fn)


    def f1(self):
        return 2 * self.tp / ((2 * self.tp) + self.fp + self.fn)


    def specificity(self):
        return self.tn / (self.tn + self.fp)


    def accuracy(self):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fp + self.fn)


    def negative_precision(self):
        return self.tn / (self.tn + self.fn)


    def true_negative_rate(self):
        return self.tp / (self.tp + self.fn)


    def false_positive_rate(self):
        return self.fp / (self.fp + self.tn)


    def false_negative_rate(self):
        return self.fn / (self.fn + self.tp)

    def __str__(self):
        sb = StringIO()
        sb.write(f"              True   False   Total\n")
        sb.write(f"Pred True    {str(self.tp):>5s} {str(self.fp):>7s} {str(self.tp + self.fp):>7s}\n")
        sb.write(f"Pred False   {str(self.fn):>5s} {str(self.tn):>7s} {str(self.fn + self.tn):>7s}\n")
        sb.write(f"Totals       {str(self.tp + self.fn):>5s} {str(self.fp + self.tn):>7s} {str(sum(self)):>7s}\n")
        sb.write(f"\n")
        sb.write(f"F1 score:    {self.f1():.3f}\n")
        sb.write(f"Precision:   {self.precision():.3f}\n")
        sb.write(f"Recall:      {self.recall():.3f}\n")
        sb.write(f"Accuracy:    {self.accuracy():.3f}\n")
        return sb.getvalue()

    @classmethod
    def build(cls, y_true, y_pred):
        y_true = list(y_true)
        y_pred = list(y_pred)
        if len(y_true) != len(y_pred):
            raise ValueError("Lengths don't match.")
        tp = sum(truth is True and pred is True for truth, pred in zip(y_true, y_pred))
        tn = sum(truth is False and pred is False for truth, pred in zip(y_true, y_pred))
        fp = sum(truth is False and pred is True for truth, pred in zip(y_true, y_pred))
        fn = sum(truth is True and pred is False for truth, pred in zip(y_true, y_pred))
        return cls(tp, tn, fp, fn)
