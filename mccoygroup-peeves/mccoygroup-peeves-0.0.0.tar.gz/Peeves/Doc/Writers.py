"""
Implements a set of writer classes that document python objects
"""
import abc, os, sys, types, inspect, re, importlib
from .ExamplesParser import TestExamplesFormatter, ExamplesParser

__all__ = [
    "DocWriter",
    "ModuleWriter",
    "ClassWriter",
    "FunctionWriter",
    "ObjectWriter",
    "IndexWriter"
]

class MarkdownFormatter:

    def format_item(self, item, item_level = 0):
        return "{}- {}".format('  ' * (item_level + 1), item)
    def format_link(self, alt, link):
        return '[{}]({})'.format(alt, link)
    def format_obj_link(self, spec):
        return self.format_link(spec.split('.')[-1], spec.replace('.', '/') + ".md")
    def format_inline_code(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+1)
        return fence + arg + fence
    def format_code_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+3)
        return fence + "python\n" + arg + "\n" + fence

    def format_quote_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """

        return ">" + arg.replace("\n", "\n>")

    link_bar_template='<div class="container alert alert-secondary bg-light">\n{links}\n</div>'
    link_row_template='  <div class="row">\n{cols}\n</div>'
    link_item_template='   <div class="col" markdown="1">\n{item}   \n</div>'
    def format_grid_box(self, link_grid):
        return self.link_bar_template.format(links="\n".join(
            self.link_row_template.format(
                cols="\n".join(self.link_item_template.format(item=item) for item in row)
            )
            for row in link_grid if len(row) > 0
        ))

class DocWriter(metaclass=abc.ABCMeta):
    """
    A general writer class that writes a file based off a template and filling in object template specs
    """

    template = "No template ;_;"
    template_root = "templates"
    template_name = ""
    default_template_base = os.path.dirname(__file__)
    examples_header = "## Examples"
    default_examples_root = "examples"
    default_tests_root = "tests"
    _template_cache = {}
    def __init__(self,
                 obj,
                 out_file,
                 tree=None,

                 name=None,
                 parent=None,
                 spec=None, # extra parameters that can be used to get special behavior

                 template_directory=None,
                 examples_directory=None,
                 parent_tests=None,

                 template=None,
                 root=None,
                 ignore_paths=None,
                 examples=None,
                 tests=None,
                 formatter=None,
                 include_line_numbers=True,
                 include_link_bars=True,

                 extra_fields=None
                 ):
        """
        :param obj: object to write
        :type obj:
        :param out_file: file to write to
        :type out_file: str | None
        :param tree: tree of written docs for looking stuff up
        :type tree:
        :param name: name to be used in the docs
        :type name:
        :param parent: parent object for docs purposes
        :type parent:
        :param spec: extra parameters that are usually inherited from the parent writer
        :type spec: dict | None
        :param template: template string to use when generating files
        :type template: str | None
        :param root: root directory to build off of
        :type root: str | None
        :param ignore_paths: paths to never write
        :type ignore_paths: Iterable[str]
        :param examples: path to examples to load
        :type examples: str | None
        :param tests: path to tests to load
        :type tests: str | None
        :param formatter: object that can format the stuff that Markdown supports
        :type formatter:
        """
        self.obj = obj
        self._id = None
        self._name = name
        self._parent = parent
        self._pobj = None
        self._chobj = None
        if extra_fields is None:
            extra_fields = {}
        self.extra_fields = extra_fields

        self.tree = tree

        if out_file is None:
            out_file = sys.stdout
        elif isinstance(out_file, str) and os.path.isdir(out_file):
            if root is None:
                root = out_file
            out_file = os.path.join(root, *self.identifier.split("."))+".md"
        self.ignore_paths = ignore_paths if ignore_paths is not None else set()

        self.spec = {} if spec is None else spec
        self.extra_fields = dict(self.extra_fields, **self.spec)
        for k in ['id']:#, 'tests_root', 'examples_root']:
            try:
                del self.extra_fields[k]
            except KeyError:
                pass

        self.target = out_file
        if root is None:
            root = os.path.dirname(self.target)
        self.root = root

        self.fallback_template_root = 'repo_templates' if 'gh_repo' in self.extra_fields else 'templates'
        self.default_template_dir = os.path.join(self.default_template_base, self.fallback_template_root)
        self._templ_directory = (
                                    template_directory if isinstance(template_directory, str)
                                                          and os.path.isdir(template_directory) else None
        )
        self._exmpl_directory = examples_directory if isinstance(examples_directory, str) and os.path.isdir(examples_directory) else None

        self.template = self.find_template(template)
        self.examples_root = self.default_examples_root if examples is None else examples
        self.tests_root = self.default_tests_root if tests is None else tests
        self._tests = None
        self.include_line_numbers = include_line_numbers
        self.parent_tests = parent_tests

        self.include_link_bars = include_link_bars
        self.formatter = MarkdownFormatter() if formatter is None else formatter

    @property
    def name(self):
        """
        Returns the name (not full identifier) of the object
        being documented

        :return:
        :rtype:
        """
        return self.get_name()
    def get_name(self):
        """
        Returns the name the object will have in its documentation page

        :return:
        :rtype:
        """
        if self._name is not None:
            name = self._name
        else:
            try:
                name = self.obj.__name__
            except AttributeError:
                name = "<{} Instance>".format(type(self.obj).__name__)

        return name

    class outStream:
        def __init__(self, file, mode = 'w+', **kw):
            self.file = file
            self.file_handle = None
            self.mode = mode
            self.kw = kw
        def __enter__(self):
            if self.file_handle is None:
                if isinstance(self.file, str):
                    try:
                        os.makedirs(os.path.dirname(self.file))
                    except OSError:
                        pass
                    self.file_handle = open(self.file, self.mode, **self.kw)
                else:
                    self.file_handle = self.file
            return self.file_handle
        def __exit__(self, exc_type, exc_val, exc_tb):
            if isinstance(self.file, str):
                self.file_handle.close()
            self.file_handle = None
        def write(self, s):
            with self as out:
                out.write(s)
            return self.file
    @property
    def out(self):
        return self.outStream(self.target)
    def write_string(self, txt):
        return self.out.write(txt)

    def template_params(self, **kwargs):
        base_parms = self.extra_fields.copy()
        base_parms.update(self.get_template_params(**kwargs))
        if hasattr(self.obj, "__doc_fields__"):
            base_parms.update(self.obj.__doc_fields__)
        return base_parms

    @abc.abstractmethod
    def get_template_params(self, **kwargs):
        """
        Returns the parameters that should be inserted into the template

        :return:
        :rtype:
        """
        raise NotImplementedError("abstract base class")

    def _clean_doc(self, doc):
        """
        Originally did a bunch of work. Now just an alias for `inspect.cleandoc`

        :param doc: a docstring
        :type doc: str
        :return: a cleaned docstring
        :rtype: str
        """
        return inspect.cleandoc(doc)

    def format(self, template=None):
        """
        Formats the documentation Markdown from the supplied template

        :param template:
        :type template:
        :return:
        :rtype:
        """
        if template is None:
            template = self.template
        params = self.template_params()
        out_file = self.target
        if isinstance(out_file, str):
            pkg, file_url = self.package_path
            params['package_name'] = pkg
            params['file_url'] = file_url
            params['package_url'] = os.path.dirname(file_url)

            if self.root is not None:
                root_split = []
                root = self.root
                while root and (root != "/" and root != os.path.pathsep):
                    root, base = os.path.split(root)
                    root_split.append(base)
                out_split = []
                out = out_file
                while out and (out != "/" and out != os.path.pathsep):
                    out, base = os.path.split(out)
                    out_split.append(base)
                out_split = list(reversed(out_split))
                root_depth = len(root_split)
                out_url = "/".join(out_split[root_depth:])
                # print(os.path.split(out_file), root_depth)
            else:
                out_url = "/".join(os.path.split(out_file)[-len(os.path.split(file_url))])
            params['file'] = out_file
            params['url'] = out_url

        try:
            form_text = template.format(**params)
        except KeyError as e:
            raise ValueError("{} ({}): template needs key {}".format(
                type(self).__name__,
                self.obj,
                e.args[0]
            ))
        except IndexError as e:
            raise ValueError("{} ({}): template index {} out of range...".format(
                type(self).__name__,
                self.obj,
                e.args[0]
            ))
        return form_text

    blacklist_packages= {"builtins", 'numpy', 'scipy', 'matplotlib'}
    def check_should_write(self):
        """
        Determines whether the object really actually should be
        documented (quite permissive)
        :return:
        :rtype:
        """
        return self.identifier.split(".", 1)[0] not in self.blacklist_packages
    def write(self, template=None):
        """
        Writes the actual docs file

        :param template:
        :type template:
        :return:
        :rtype:
        """
        if self.check_should_write():
            if self.target not in self.ignore_paths:
                return self.write_string(self.format(template=template))

    def get_package_and_url(self):
        """
        Returns package name and corresponding URL for the object
        being documented

        :return:
        :rtype:
        """
        pkg_split = self.identifier.split(".", 1)
        if len(pkg_split) == 1:
            pkg = pkg_split[0]
            rest = ""
        elif len(pkg_split) == 0:
            pkg = ""
            rest = "Not.A.Real.Package"
        else:
            pkg, rest = pkg_split
        if len(rest) == 0:
            file_url = "__init__.py"
        else:
            file_url = rest.replace(".", "/") + "/__init__.py"
        if 'url_base' in self.extra_fields:
            file_url = self.extra_fields['url_base'] + "/" + file_url
        return pkg, file_url
    @property
    def package_path(self):
        return self.get_package_and_url()

    @classmethod
    def load_template(cls, file):
        """
        Loads the documentation template
        for the object being documented

        :param file:
        :type file:
        :return:
        :rtype:
        """
        with open(file) as f:
            return f.read()
    @classmethod
    def get_identifier(cls, o):

        try:
            pkg = o.__module__
        except AttributeError:
            pkg = ""

        try:
            n = o.__qualname__
        except AttributeError:
            try:
                n = o.__name__
            except AttributeError:
                n = type(o).__name__

        qn = pkg + ('.' if pkg != "" else "") + n

        return qn
    @property
    def identifier(self):
        if self._id is None:
            self._id = self.get_identifier(self.obj)
        return self._id
    def get_lineno(self):
        try:
            lineno = 1+inspect.findsource(self.obj)[1] if self.include_line_numbers else ""
        except:
            lineno = ""
        return lineno

    def resource_dir(self, spec_key, base_root):
        """
        Returns the directory for a given resource (e.g. examples or tests)
        by trying a number of different possible locations

        :param spec_key:
        :type spec_key:
        :param base_root:
        :type base_root:
        :return:
        :rtype:
        """
        if spec_key in self.spec:
            return os.path.abspath(self.spec[spec_key])
        elif os.path.isdir(os.path.abspath(base_root)):
            return base_root
        else:
            # try to inherit from the parent
            if (
                    self.tree is not None
                    and self._parent is not None
                    and self._parent in self.tree
            ):
                spec = self.tree[self._parent]
            else:
                spec = {}
            if spec_key in spec:
                return os.path.abspath(spec[spec_key])
            else:
                return os.path.join(self.root, base_root)

    def _find_template_by_name(self, name):
        test_dirs = []
        tdir = self.template_dir
        template = os.path.join(tdir, *self.identifier.split(".")) + ".md"
        if not os.path.exists(template):
            test_dirs.append(os.path.join(tdir, *self.identifier.split(".")))
            template = os.path.join(tdir, name)
        if not os.path.exists(template):
            test_dirs.append(tdir)
            def_dir = os.path.join(self.root, self.template_root)
            if not os.path.isdir(def_dir):
                def_dir = self.default_template_dir
            template = os.path.join(def_dir, name)
            if not os.path.isfile(template):
                test_dirs.append(def_dir)
                template = os.path.join(self.default_template_dir, name)
            # if os.path.isfile(template):
            #     print("no template found in {} for {}, using default".format(tdir, self.template_name))
        if os.path.exists(template):
            if template in self._template_cache:
                template = self._template_cache[template]
            else:
                tkey = template
                with open(template) as tf:
                    template = tf.read()
                self._template_cache[tkey] = template
        else:
            test_dirs.append(self.default_template_dir)
            print("no template found in {} for {}".format(test_dirs, name))
            template = self.template
        return template
    def find_template(self, template):
        """
        Finds the appropriate template for the object by looking
        in a variety of different locations

        :param template:
        :type template:
        :return:
        :rtype:
        """
        if template is None:
            template = self._find_template_by_name(self.template_name)
        elif (
            len(template.splitlines()) == 1 and
            len(os.path.split(template)) == 2
        ):
            template = self._find_template_by_name(template)

        return template

    @property
    def template_dir(self):
        if self._templ_directory is not None:
            return self._templ_directory
        elif os.path.isdir(os.path.join(self.root, self.template_root)):
            return os.path.join(self.root, self.template_root)
        else:
            return self.default_template_dir

    @property
    def examples_dir(self):
        """
        Returns the directory in which to look for examples
        :return:
        :rtype:
        """
        spec_key='examples_root'
        if self._exmpl_directory is None:
            return self.resource_dir(spec_key, self.examples_root)
        else:
            return self._exmpl_directory

    @property
    def examples_path(self):
        """
        Provides the default examples path for the object
        :return:
        :rtype:
        """
        splits = self.identifier.split(".")
        return os.path.join(*splits)+".md"
    def load_examples(self):
        """
        Loads examples for the stored object if provided
        :return:
        :rtype:
        """
        if hasattr(self.obj, '__examples__'):
            examples = os.path.join(self.examples_dir, self.obj.__examples__)
            if os.path.isfile(examples):
                with open(examples) as f:
                    return f.read()
            else:
                return self.obj.__examples__
        elif self.root is not None:
            examples = os.path.join(self.examples_dir, self.examples_path)
            if os.path.isfile(examples):
                with open(examples) as f:
                    return f.read()

    @property
    def tests_dir(self):
        """
        Returns the directory in which to look for tests
        :return:
        :rtype:
        """
        spec_key='tests_root'
        return self.resource_dir(spec_key, self.tests_root)
    @property
    def tests_path(self):
        """
        Provides the default tests path for the object
        :return:
        :rtype:
        """
        return os.path.join(*self.identifier.split(".")) + "Tests.py"
    def load_tests(self):
        """
        Loads tests for the stored object if provided
        :return:
        :rtype:
        """

        # print(">>>>", self.tests_dir, self.tests_path)
        test_str = None
        if hasattr(self.obj, '__tests__'):
            tests = os.path.join(self.tests_dir, self.obj.__tests__)
            if os.path.isfile(tests):
                with open(tests) as f:
                    test_str = f.read()
            else:
                test_str = self.obj.__tests__
        elif self.root is not None:
            tests = os.path.join(self.tests_dir, self.tests_path)
            if os.path.isfile(tests):
                with open(tests) as f:
                    test_str = f.read()
            else:
                tests = os.path.join(self.tests_dir, os.path.basename(self.tests_path))
                # print("....", tests)
                if os.path.isfile(tests):
                    with open(tests) as f:
                        test_str = f.read()

        return ExamplesParser(test_str) if test_str is not None else test_str
    @property
    def tests(self):
        if self._tests is None:
            self._tests = self.load_tests()
        return self._tests
    def get_test_markdown(self):
        tests = self.tests
        if tests is None and self.parent_tests is not None:
            tests = self.parent_tests.filter_by_name(self.name.split(".")[-1])

        formatted = TestExamplesFormatter(tests,
                                          template=self.find_template('tests.md'),
                                          example_template=self.find_template('test_example.md'),
                                          ).format() if tests is not None else ""
        # print(self.name, len(formatted))
        return formatted

    @property
    def parent(self):
        """
        Returns the parent object for docs purposes

        :return:
        :rtype:
        """
        if self._pobj is None:
            self._pobj = self.resolve_parent()
        return self._pobj

    def resolve_parent(self, check_tree=True):
        """
        Resolves the "parent" of obj.
        By default, just the module in which it is contained.
        Allows for easy skipping of pieces of the object tree,
        though, since a parent can be directly added to the set of
        written object which is distinct from the module it would
        usually resolve to.
        Also can be subclassed to provide more fine grained behavior.

        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        if check_tree:
            oid = self.identifier
            if self.tree is not None and oid in self.tree:
                return self.tree[oid]['parent']

        if self._parent is not None:
            if isinstance(self._parent, str):
                return self.resolve_object(self._parent)
            else:
                return self._parent
        elif 'parent' in self.spec:
            parent = self.spec['parent']
            if isinstance(parent, str):
                return self.resolve_object(parent)
            else:
                return parent

        if isinstance(self.obj, types.ModuleType):
            # not totally sure this will work...
            modspec = self.obj.__name__.rsplit(".", 1)[0]
        else:
            modspec = self.obj.__module__

        if modspec == "":
            return None

        return self.resolve_object(modspec)

    @property
    def children(self):
        """
        Returns the child objects for docs purposes

        :return:
        :rtype:
        """
        if self._chobj is None:
            self._chobj = self.resolve_children()
        return self._chobj

    def resolve_children(self, check_tree=True):
        """
        Resolves the "children" of obj.
        First tries to use any info supplied by the docs tree
        or a passed object spec, then that failing looks for an
        `__all__` attribute

        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        childs=None
        if check_tree:
            oid = self.identifier
            if self.tree is not None and oid in self.tree:
                childs = self.tree[oid]['children']
        if childs is None:
            if 'children' in self.spec:
                childs = self.spec['children']
            elif hasattr(self.obj, '__all__'):
                childs = self.obj.__all__
            else:
                childs=[]

        oid = self.identifier
        return [self.resolve_object(oid+"."+x) if isinstance(x, str) else x for x in childs]

    @staticmethod
    def resolve_object(o):
        """
        Resolves to an arbitrary object by name

        :param o:
        :type o:
        :return:
        :rtype:
        """

        if o in sys.modules:
            # first we try to do a direct look up
            o = sys.modules[o]
        elif o.rsplit(".", 1)[0] in sys.modules:
            # if direct lookup failed, but the parent module has been loaded
            # try direct lookup on that
            try:
                mod, attr = o.rsplit(".", 1)
                o = getattr(sys.modules[mod], attr)
            except AttributeError:
                o = importlib.import_module(o)
        else:
            # otherwise fall back on standard import machinery
            try:
                o = importlib.import_module(o)
            except ModuleNotFoundError:  # tried to load a member but couldn't...
                # we try to resolve this by doing an iterated getattr
                p_split = o.split(".")
                mod_spec = ".".join(p_split[:-1])
                if mod_spec == "":
                    raise ValueError("can't resolve '{}'".format(o))
                try:
                    mood = importlib.import_module(mod_spec)
                    from functools import reduce
                    v = reduce(lambda m, a: getattr(m, a), p_split[1:], mood)
                except ModuleNotFoundError:
                    pass
                else:
                    o = v

        return o

    @property
    def doc_spec(self):
        """
        Provides info that gets added to the `written` dict and which allows
        for a doc tree to be built out.

        :return:
        :rtype:
        """

        base_spec = {
            'id': self.identifier,
            'parent': self.parent,
            'children': self.children
        }
        base_spec.update(self.spec)
        return base_spec

    param_template = """  - `{name}`: `{type}`\n    >{description}"""
    def parse_doc(self, doc):
        """

        :param doc:
        :type doc: str
        :return:
        :rtype:
        """
        from collections import deque

        # parses a docstring based on reStructured text type specs but Markdown description
        splits = doc.strip().splitlines()

        params = deque()
        param_map = {}
        i = len(splits)-1
        for i in range(len(splits)-1, -1, -1):
            line = splits[i].strip()
            if line.startswith(":"):
                if line.startswith(":param"):
                    bits = line.split(":", 2)[1:]
                    name = bits[0][5:].strip()
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"Any", "description":"No description..."}
                    desc = bits[1].strip() if len(bits) == 2 else ""
                    if len(desc) > 0:
                        param_map[name]["description"] = desc
                elif line.startswith(":type"):
                    bits = line.split(":", 2)[1:]
                    name = bits[0][4:].strip()
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"Any", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["type"] = t
                elif line.startswith(":return"):
                    bits = line.split(":", 2)[1:]
                    name = ":returns"
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"_", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["description"] = t
                elif line.startswith(":rtype"):
                    bits = line.split(":", 2)[1:]
                    name = ":returns"
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"_", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["type"] = t
            else:
                i = i+1
                break

        param = []
        for p in params:
            param.append(self.param_template.format(**param_map[p]).strip())

        desc = splits[:i]

        return "\n".join(param), "\n".join(desc)

class ModuleWriter(DocWriter):
    """A writer targeted to a module object. Just needs to write the Module metadata."""

    template_name = 'module.md'
    def __init__(self, obj, out_file, **kwargs):
        if isinstance(obj, str):
            obj = importlib.import_module(obj)
        super().__init__(obj, out_file, **kwargs)

    def get_template_params(self):
        """
        Provides module specific parameters
        :return:
        :rtype:
        """
        import types

        mod = self.obj # type: types.ModuleType
        name = mod.__name__
        ident = self.identifier
        ident_depth = len(ident.split("."))
        # get identifiers
        idents = [ DocWriter.get_identifier(getattr(mod, a)) for a in self.get_members(mod) ]
        # flattend them
        idents = [ i for i in idents if ident in i ]
        # split by qualified names
        idents = [".".join(a.split(".")[ident_depth-1:]) for a in idents]
        # format links
        links = [ self.formatter.format_obj_link(l) for l in idents ]
        if self.include_link_bars:
            num_cols = 3
            splits = []
            sub = []
            for x in links:
                sub.append(x)
                if len(sub) == num_cols:
                    splits.append(sub)
                    sub = []
            splits.append(sub)
            mems = self.formatter.format_grid_box(splits)
        else:
            mems = "\n".join([ self.formatter.format_item(l) for l in links ])
        # print([idents, mems])
        descr = mod.__doc__ if mod.__doc__ is not None else ''

        ex = self.load_examples()
        tests = self.get_test_markdown()
        return {
            'id' : ident,
            'description' : descr.strip(),
            'name': name,
            'members' : mems,
            'examples' : self.examples_header+"\n"+ex if ex is not None else "",
            'tests': tests
        }

    @classmethod
    def get_members(cls, mod):
        return (mod.__all__ if hasattr(mod, '__all__') else [])

class ClassWriter(DocWriter):
    """A writer targeted to a class"""

    template_name = 'class.md'
    def load_methods(self, function_writer=None):
        """
        Loads the methods supported by the class

        :param function_writer:
        :type function_writer:
        :return:
        :rtype:
        """
        import types

        if function_writer is None:
            function_writer = MethodWriter

        cls = self.obj
        keys = cls.__all__ if hasattr(cls, '__all__') else list(cls.__dict__.keys())

        props = []
        methods = []

        extra_fields = self.extra_fields.copy()
        pkg, file_url = self.package_path
        extra_fields['package_name'] = pkg
        extra_fields['file_url'] = file_url
        extra_fields['package_url'] = os.path.dirname(file_url)
        for k in keys:
            o = getattr(cls, k)
            if isinstance(o, (types.FunctionType, types.MethodType, classmethod, staticmethod, property)):
                if not k.startswith("_") or (k.startswith("__") and k.endswith("__")):
                    methods.append(
                        function_writer(o,
                                        tree=self.tree, parent=self.identifier, name=k,
                                        out_file=None, root=self.root,
                                        template_directory=self.template_dir,
                                        examples_directory=self.examples_dir,
                                        extra_fields=extra_fields
                                        ).format().strip()
                    )
            else:
                if not k.startswith("_"):
                    props.append(self.format_prop(k, o).strip())

        return props, methods

    def get_package_and_url(self):
        pkg, rest = self.identifier.split(".", 1)
        rest, bleh = rest.rsplit(".", 1)
        file_url = rest.replace(".", "/") + ".py"
        if 'url_base' in self.extra_fields:
            file_url = self.extra_fields['url_base'] + "/" + file_url
        # lineno = inspect.findsource(self.obj)[1]
        return pkg, file_url #+ "#L" + str(lineno) # for GitHub links

    def format_prop(self, k, o):
        return '{}: {}'.format(k, type(o).__name__)

    def get_template_params(self, function_writer = None):
        """

        :param function_writer:
        :type function_writer:
        :return:
        :rtype:
        """

        cls = self.obj # type: type
        ex = self.load_examples()
        tests = self.get_test_markdown()
        name = cls.__name__
        ident = self.identifier
        props, methods = self.load_methods(function_writer=function_writer)
        param, descr = self.parse_doc(cls.__doc__ if cls.__doc__ is not None else '')
        descr = self._clean_doc(descr)
        param = self._clean_doc(param)
        if len(param) > 0:
            param = "\n" + param
        props = "\n".join(props)
        if len(props) > 0:
            props = self.formatter.format_code_block(props)+"\n"
        lineno = self.get_lineno()

        return {
            'id': ident,
            'name': name,
            'lineno': lineno,
            'description' : descr,
            'parameters' : param,
            'props' : props,
            'methods' : "\n\n".join(methods),
            'examples' : ex if ex is not None else "",
            'tests': tests
        }

class FunctionWriter(DocWriter):
    """
    Writer to dump functions to file
    """

    template_name = 'function.md'
    def get_signature(self):
        return str(inspect.signature(self.obj))
    def get_template_params(self, **kwargs):
        f = self.obj # type: types.FunctionType
        ident = self.identifier
        signature = self.get_signature()
        mem_obj_pat = re.compile(" object at \w+>")
        signature = re.sub(mem_obj_pat, " instance>", signature)
        name = self.get_name()
        param, descr = self.parse_doc(f.__doc__ if f.__doc__ is not None else '')
        descr = descr.strip()
        param = param.strip()
        if len(param) > 0:
            param = "\n" + param
        ex = self.load_examples()
        tests = self.get_test_markdown()
        lineno = self.get_lineno()
        return {
            'id': ident,
            'name' : name,
            'lineno' : lineno,
            'signature' : signature,
            'parameters' : param,
            'description' : descr,
            'examples' : ex if ex is not None else "",
            'tests': tests
        }

    def get_package_and_url(self):
        pkg, rest = self.identifier.split(".", 1)
        rest, bleh = rest.rsplit(".", 1)
        file_url = rest.replace(".", "/") + ".py"
        if 'url_base' in self.extra_fields:
            file_url = self.extra_fields['url_base'] + "/" + file_url
        # lineno = inspect.findsource(self.obj)[1]
        return pkg, file_url #+ "#L" + str(lineno) # for GitHub links

class MethodWriter(FunctionWriter):
    """
    Writes class methods to file
    (distinct from functions since not expected to exist solo)
    """

    template_name = 'method.md'
    def get_template_params(self, **kwargs):
        params = super().get_template_params(**kwargs)
        meth = self.obj # type: types.MethodType
        decorator = ""
        if isinstance(meth, classmethod):
            decorator = 'classmethod'
        elif isinstance(meth, property):
            decorator = 'property'
        elif isinstance(meth, staticmethod):
            decorator = 'staticmethod'
        if len(decorator) > 0:
            decorator = "@" + decorator + "\n"
        params['decorator'] = decorator
        return params
    def get_signature(self):
        try:
            signature = str(inspect.signature(self.obj))
        except TypeError:  # dies on properties
            signature = "(self)"
        return signature
    @property
    def identifier(self):
        if isinstance(self.obj, property):
            return self.get_identifier(self.resolve_parent(check_tree=False)) + "." + self.get_name()
        else:
            return self.get_identifier(self.obj)

class ObjectWriter(DocWriter):
    """
    Writes general objects to file.
    Basically a fallback to support singletons and things
    of that nature.
    """

    template_name = 'object.md'
    @property
    def identifier(self):
        try:
            qualname = self.obj.__qualname__
        except AttributeError:
            qualname = self.get_identifier(type(self.obj)) + "." + self.get_name()
        qn = qualname.split(".")
        qualname = ".".join(qn[:-2] + qn[-1:]) # want to drop the class name
        # print(qualname)
        return qualname

    def check_should_write(self):
        """
        Determines whether the object really actually should be
        documented (quite permissive)
        :return:
        :rtype:
        """
        return (
                hasattr(self.obj, "__doc__")
                and hasattr(self.obj, "__name__")
                and super().check_should_write()
        )

    def get_template_params(self):

        try:
            descr = self.obj.__doc__
        except AttributeError:
            descr = "instance of "+type(self.obj).__name__

        if descr is None:
            descr = ''

        ex = self.load_examples()
        lineno = self.get_lineno()
        return {
            'id': self.identifier,
            'lineno': lineno,
            'name': self.get_name(),
            'description' : descr.strip(),
            'examples' : ex if ex is not None else ""
        }

class IndexWriter(DocWriter):
    """
    Writes an index file with all of the
    written documentation files.
    Needs some work to provide more useful info by default.
    """

    template_name = 'index.md'
    def __init__(self, *args, description=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = description if description is not None else "# Documentation"

    def get_identifier(cls, o):
        return 'index'

    def get_file_paths(self):
        rl = len(os.path.split(self.root))
        fs = [ "/".join(os.path.split(f)[rl-1:]) for f in self.obj ]
        return fs

    def get_template_params(self):
        files = [
            self.formatter.format_item(
                self.formatter.format_link(os.path.splitext(f.split("/")[-1])[0], f)
            ) for f in self.get_file_paths()
        ]
        return {
            'index_files' : "\n".join(files),
            'description' : self.description
        }