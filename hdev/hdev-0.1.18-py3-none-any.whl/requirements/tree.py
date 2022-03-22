from packaging.version import Version


class DependencyTree:
    @classmethod
    def create(cls, requirements, node_filter=None):
        """Create a dependency tree from a dict of requirement sets.

        :param requirements: Dict of dependency types to lists of Package
            objects
        :param node_filter: Function returning true for nodes to keep
        :return: A DependencyTree instance
        """
        return cls(
            dependencies=cls.flatten_requirements(requirements),
            node_filter=node_filter,
        )

    def __init__(
        self, dependencies, depth=0, node_filter=None, package=None, parent=None
    ):  # pylint: disable=too-many-arguments
        """Initialise a DependencyTree object.

        :param dependencies: A list of package objects this node depends on
        :param depth: The distance from the root node
        :param node_filter: Function returning true for nodes to keep
        :param package: The package at this node
        :param parent: The parent in the tree
        """
        self.depth = depth
        self.package = package
        self.parent = parent

        # Don't do any work we don't have to if we aren't going to be kept
        # by the filter. This prevents generating all the children
        # unnecessarily and can speed things up a lot
        if node_filter and not node_filter(self):
            return

        children = (
            DependencyTree(
                package=package,
                dependencies=package.requirements,
                parent=self,
                depth=depth + 1,
                node_filter=node_filter,
            )
            for package in dependencies
        )

        if node_filter:
            # Filter out children we don't want
            self.children = [node for node in children if node_filter(node)]
        else:
            self.children = list(children)

    def visit(self, visitor):
        visitor(self)

        for child in self.children:
            child.visit(visitor)

    def dump(self, render=str):
        def visitor(node):
            print("    " * node.depth + render(node))

        self.visit(visitor)

    def flat(self):
        nodes = []
        self.visit(lambda node: nodes.append(node) if node.package else None)
        return nodes

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.package)})"

    @classmethod
    def flatten_requirements(cls, typed_requirements):
        """Convert a dict of dep_type: [deps] into flat dependencies.

        This will also tag the dependencies with the requirements_types they have
        so we can keep track of whether they are say "dev" or "tests" requirements.
        """
        flat = {}

        for req_type, reqs in typed_requirements.items():
            for req in reqs:
                req = flat.setdefault(req.canonical_name, req)
                req.requirement_types.add(req_type)

        return flat.values()

    @classmethod
    def standard_node_filter(
        cls, maximum_python_version=None, ignore_libs=None, no_dependencies=None
    ):
        """Get a predicate function which indicates if a node should be kept.

        This implements some standard filtering behaviors to keep the graph under
        control.

        :param maximum_python_version: Filter out nodes which meet or exceed
            this version
        :param ignore_libs: Filter out packages with these names
        :param no_dependencies: Filter out the dependencies of packages with
            these names
        :return: A function which accepts a single DependencyTree node and
            returns True of False
        """
        maximum_python_version = (
            Version(maximum_python_version) if maximum_python_version else None
        )

        def should_keep_node(node):
            if node.package:
                # Don't list anything in a set of things we don't care about
                if ignore_libs and node.package.canonical_name in ignore_libs:
                    return False

                # Don't list anything that meets our required version of python
                if maximum_python_version and (
                    python_versions := node.package.python_versions
                ):
                    if any(ver >= maximum_python_version for ver in python_versions):
                        return False

            # Don't list dependencies for these packages (but do list the
            # packages themselves). This applies beyond the bottom level,
            # because if we ask for the dependencies of something directly as
            # the root we don't want to filter those out
            if (
                no_dependencies
                and node.depth > 0
                and node.parent
                and node.parent.package
                and node.parent.package.canonical_name in no_dependencies
            ):
                return False
            return True

        return should_keep_node
