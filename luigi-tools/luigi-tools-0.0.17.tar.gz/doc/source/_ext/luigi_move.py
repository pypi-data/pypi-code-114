from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective


class luigi_moved(nodes.Admonition, nodes.Element):
    pass


def visit_todo_node(self, node):
    self.visit_admonition(node)


def depart_todo_node(self, node):
    self.depart_admonition(node)


class MovedDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "luigi_version": directives.unchanged,
        "previous_luigi_version": directives.unchanged,
        "deprecation_version": directives.unchanged,
    }

    def run(self):
        targetid = "luigi_moved-%d" % self.env.new_serialno("luigi_moved")
        targetnode = nodes.target("", "", ids=[targetid])

        msg = "This feature was moved to the :mod:`luigi` package"
        if ("luigi_version" in self.options) == ("previous_luigi_version" in self.options):
            raise ValueError(
                "Either the 'luigi_version' or the 'previous_luigi_version' argument of the "
                f"'{self.name}' directive must be not None but not both of them"
            )
        if "luigi_version" in self.options:
            msg += f" and is available since version {self.options['luigi_version']}."
        else:
            msg += (
                " and will be available after the version "
                f"{self.options['previous_luigi_version']}."
            )
        body = [msg]

        if "deprecation_version" in self.options:
            body.append(f"It will be deprecated in version {self.options['deprecation_version']}.")
        else:
            body.append(f"It will be deprecated in a future version.")

        if self.content:
            body.append("")
            body.extend(self.content.data)
        todo_node = luigi_moved(body)
        todo_node += nodes.title(_("Moved to luigi"), _("Moved to luigi"))
        self.state.nested_parse(StringList(body), self.content_offset, todo_node)

        return [targetnode, todo_node]


def setup(app):
    app.add_node(
        luigi_moved,
        html=(visit_todo_node, depart_todo_node),
        latex=(visit_todo_node, depart_todo_node),
        text=(visit_todo_node, depart_todo_node),
    )
    app.add_directive("moved_to_luigi", MovedDirective)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
