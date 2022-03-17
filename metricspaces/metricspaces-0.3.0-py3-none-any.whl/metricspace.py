class MetricSpace:
    """
    A class to store a metric space.
    The standard usage is to specify a collection of points and a distance
    function.  Either the points or the distance function can be omitted.
    If only the points are provided, the distance function will default to the
    `dist` method on the point objects.
    If only the distance function is provided, then it is not possible to
    iterate over the points.  This would be the case for infinite metric spaces.
    """

    def __init__(self, points = (),
                 dist = None,
                 cache = None,
                 turnoffcache=False,
                 pointclass = lambda x:x):
        """
        Initialize a new `MetricSpace` object.

        The `points` and the `dist` function are optional.
        If `dist` is not provided, then the distance is computed by calling
        the `dist` method on the point.

        It is possible to seed the cache at the time of construction.
        If `cache` is not provided, a new empty cache will be initialized.

        If `turnoffcache` is True, then distances will not be cached.
        """
        self.turnoffcache = turnoffcache
        self.cache = cache if cache is not None else {}
        self.points = []
        for p in points:
            self.add(pointclass(p))
        self.distfn = dist if dist is not None else MetricSpace.pointdist

    def add(self, point):
        """
        Add `point` to the metric space.
        """
        # Note: we use a dictionary here to preserve insertion order for
        # things like distance matrices and MDS.
        # Sid: We changed the dict to a list to support changing the order
        # of points to a random or greedy ordering
        self.points.append(point)

    def fromstrings(self, strings, parser):
        """
        Take a collection of strings as input and parse each as a point.

        The string is read only up to the first semicolon (if present).
        """
        for s in strings:
            self.add(parser(s.split(';')[0]))

    def __iter__(self):
        """
        Return an iterator over the points that have been explicitly added to
        the metric space.

        The iteration order is fixed to be the order of first insertion.
        This is accomplished through Python's natural ordering for dict keys.

        It is possible to use a metric space object only as a cache-enabled
        wrapper around a metric function.  The iterator will not iterate over
        all points in the cache, only those that were added in the initializer
        or through the `add` method.
        """
        return iter(self.points)

    def __len__(self):
        """
        Return the number of points stored in the metric space.

        As with `__iter__`, only those points explicitly added in `__init__` or
        `add` will be counted.
        """
        return len(self.points)

    def __getitem__(self, index):
        """
        Return points of the metric space accessed by index.

        If the index is a slice object then a subspace of the slcied points is
        returned. Otherwise the single point is returned.
        """
        if isinstance(index, slice):
            return self.subspace(self.points[index])
        else:
            return self.points[index]

    def subspace(self, points):
        """
        Return a subspace of the metric space

        It takes a subset of points of the metric space as input and returns
        a new MetricSpace object created with those points and the superspace's
        parameters
        """
        return MetricSpace(points,
                            dist=self.distfn,
                            cache=self.cache,
                            turnoffcache=self.turnoffcache)

    def pointdist(a, b):
        """
        Return the distance from `a` to `b` as measured using the metric
        supplied by the input points.
        """
        return a.dist(b)

    def dist(self, a, b):
        """
        Return the distance from`a` to `b`.

        The metric used will depend on the `distfn`.
        """
        if self.turnoffcache:
            return self.distfn(a,b)
        else:
            key = frozenset((a,b))
            if key not in self.cache:
                self.cache[key] = self.distfn(a,b)
            return self.cache[key]

    def distsq(self, a, b):
        """
        Return the squared distance from `a` to `b`.
        """
        return self.dist(a, b) ** 2.

    def comparedist(self, x, a, b, delta = 0, alpha = 1):
        """
        Return True iff `x` is closer to `a` than to `b`.

        Technically, it returns `d(x,a) < alpha * d(x,b) - delta`, where delta is
        optional and defaults to zero.
        """
        return self.dist(x,a) < alpha * self.dist(x,b) - delta

    def distlt(self, a, b, delta = 0):
        """
        Return True iff `d(a,b) < delta`.
        """
        return self.dist(a,b) < delta
