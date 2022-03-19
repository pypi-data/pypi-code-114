from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective


class config(nodes.General, nodes.Element):
    pass


class FiguratorDirective(SphinxDirective):

    # this enables content in the directive
    has_content = True

    def run(self):
        target_id = 'figurator-%d' % self.env.new_serialno('figurator')
        target_node = nodes.target('', '', ids=[target_id])

        config_node = config('\n'.join(self.content))
        config_node += nodes.title(_('Config'), _('Config'))
        self.state.nested_parse(self.content, self.content_offset, config_node)

        if not hasattr(self.env, 'figurator_all_configs'):
            self.env.figurator_all_configs = []

        self.env.figurator_all_configs.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'config': config_node.deepcopy(),
            'target': target_node,
        })

        return [target_node, config_node]


def purge_configs(app, env, docname):
    if not hasattr(env, 'figurator_all_configs'):
        return

    env.figurator_all_configs = [c for c in env.figurator_all_configs if c['docname'] != docname]


def merge_configs(app, env, docnames, other):
    if not hasattr(env, 'figurator_all_configs'):
        env.figurator_all_configs = []

    if hasattr(other, 'figurator_all_configs'):
        env.figurator_all_configs.extend(other.figurator_all_configs)


def import_and_get_config()


def process_config_nodes(app, doctree, fromdocname):
    # Replace all config nodes
    env = app.builder.env

    if not hasattr(env, 'figurator_all_configs'):
        env.figurator_all_configs = []

    for node in doctree.traverse(config):
        content = []

        for config_info in env.figurator_all_configs:
            para = nodes.paragraph()
            
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = todo_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, todo_info['docname'])
            newnode['refuri'] += '#' + todo_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the todolist
            content.append(todo_info['todo'])
            content.append(para)

        node.replace_self(content)


def setup(app):
    app.add_node(config)

    app.add_directive('figurator', FiguratorDirective)
    app.connect('env-purge-doc', purge_configs)
    app.connect('env-merge-info', merge_configs)
    app.connect('doctree-resolved', process_config_nodes)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
