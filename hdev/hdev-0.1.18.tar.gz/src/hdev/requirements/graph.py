from subprocess import check_output
from tempfile import NamedTemporaryFile

from packaging.version import Version

from hdev.jinja_env import get_jinja_env
from hdev.requirements import OUR_LIBS


class DependencyGraph:
    @classmethod
    def create_png(cls, dot, output_file, algo="dot"):
        """Create a graph from the specified tree data.

        :param dot: A graphviz format graph string
        :param output_file: Target file to create PNG
        :param algo: One of: `dot`, `neato`, `fdp`, `sfdp`, `circo`, `twopi`
        """
        with NamedTemporaryFile() as dot_file:
            dot_file.write(dot.encode("utf-8"))
            dot_file.flush()

            check_output([algo, "-Tpng", "-o", output_file, dot_file.name])

    @classmethod
    def create_dot(cls, tree, target_python_version):
        """Create a graphviz dot format string for the given requirements dict.

        :param tree: DependencyTree to graph
        :param target_python_version: Highlight packages which don't meet this
        :return: A graphviz format digraph string
        """
        nodes = tree.flat()

        # Get all of the unique parent child relationships
        unique_dependencies = set()
        for node in nodes:
            unique_dependencies.update(
                (node.package.canonical_name, child.package.canonical_name)
                for child in node.children
            )

        # Create a color map for
        color_map = cls._make_color_map(target_python_version)

        return (
            get_jinja_env()
            .get_template("dep_graph.dot.jinja2")
            .render(
                packages=[node.package for node in nodes],
                unique_dependencies=unique_dependencies,
                color_for=lambda package: cls._color_for(package, color_map),
            )
            .strip()
        )

    @classmethod
    def _make_color_map(cls, target_python_version):
        color_map = {target_python_version: "green"}
        major, minor = Version(target_python_version).release
        for color in ["greenyellow", "yellow", "orange"]:
            minor -= 1
            if minor < 0:
                break

            color_map[f"{major}.{minor}"] = color

        return color_map

    @classmethod
    def _color_for(cls, package, color_map):
        if package.canonical_name in OUR_LIBS:
            return "darkslategray1"

        versions = [str(ver) for ver in package.python_versions]

        for key, color in color_map.items():
            if key in versions:
                return color

        return "red"
