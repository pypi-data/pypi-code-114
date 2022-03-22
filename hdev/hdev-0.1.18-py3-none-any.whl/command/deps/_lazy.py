"""Lazy loaded command content for Deps."""
import json
import sys
from subprocess import Popen

from hdev.jinja_env import get_jinja_env
from hdev.model.project import Project
from hdev.requirements import OUR_LIBS
from hdev.requirements.graph import DependencyGraph
from hdev.requirements.package import Package
from hdev.requirements.tree import DependencyTree
from hdev.shell import Color

IGNORE_LIBS = {"setuptools", "six"}


class LazyDeps:  # pylint: disable=too-few-public-methods
    """Lazy loaded command content for Deps."""

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """

        target_package = None
        project = None

        if args.package:
            target_package = Package(args.package)
            requirements = {"install": target_package.requirements}

        else:
            project = args.project
            requirements = project.requirements()

        if args.json:
            data = self._serialize(
                target_package=target_package,
                project=project,
                requirements=requirements,
            )

            if args.debug:
                print(json.dumps(data, indent=4, sort_keys=True))
            else:
                print(json.dumps(data))

        else:
            print(
                get_jinja_env()
                .get_template("dep_command.txt.jinja2")
                .render(
                    target_package=target_package,
                    project=project,
                    requirements=requirements,
                    verbose=args.verbose,
                    color=Color,
                    our_libs=OUR_LIBS,
                )
                .strip()
            )

        if args.graph:
            self._create_graph(args, requirements)

    @classmethod
    def _serialize(cls, target_package, project, requirements):
        data = {}

        if target_package:
            data["name"] = target_package.canonical_name
            data["meta"] = {"is_package": True, "info": target_package.info}

        else:
            assert project
            data["name"] = project.root_dir.stem
            data["meta"] = {
                "is_app": project.type == Project.Type.APPLICATION,
                "is_lib": project.type == Project.Type.LIBRARY,
            }

        data["requirements"] = [
            req.as_dict() for req in DependencyTree.flatten_requirements(requirements)
        ]

        return data

    @classmethod
    def _create_graph(cls, args, requirements):
        node_filter = None
        if not args.verbose:
            node_filter = DependencyTree.standard_node_filter(
                maximum_python_version=args.python_version_max or args.python_version,
                ignore_libs=IGNORE_LIBS,
                no_dependencies=OUR_LIBS,
            )

        dot = DependencyGraph.create_dot(
            tree=DependencyTree.create(requirements, node_filter=node_filter),
            target_python_version=args.python_version,
        )

        if args.debug:
            print("Graphviz dot ----------------------------")
            print(dot)
            print("End of graphviz dot ----------------------------")

        output_file = args.output_file
        if not args.output_file:
            if args.package:
                graph_name = args.package
            else:
                graph_name = args.project.root_dir.absolute().name

            output_file = f"{graph_name}_deps.png"

        DependencyGraph.create_png(dot=dot, output_file=output_file)
        if args.show:
            # Using Popen rather than check_output etc. means we don't attach
            # to stderr etc. and end up waiting for the sub-process to finish

            # pylint: disable=consider-using-with
            Popen(["open" if sys.platform == "darwin" else "xdg-open", output_file])

        print(f"Created: {output_file}")
