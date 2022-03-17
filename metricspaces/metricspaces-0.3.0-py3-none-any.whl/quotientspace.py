from metricspaces import MetricSpace

class QuotientSpace(MetricSpace):
    """
    A class to store quotients of metric spaces with a single equivalence class.

    WARNING: This is still work in progress.
    Maybe, don't use it yet.
    """

    def __init__(self, X:MetricSpace, proj):
        """
        Initialize a new QuotientSpace object.
        """
        super().__init__(points=X.points, dist=X.dist, cache=X.cache, turnoffcache=X.turnoffcache)
        self.projfn = proj

    def proj(self, a):
        return self.projfn(a)

    def dist(self, a, b):
        return min(super().dist(a, b), super().dist(a, self.proj(a))+super().dist(b, self.proj(b)))
