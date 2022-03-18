"""
Provides a class that will walk through a set of objects & their children, as loaded into memory, and will generate Markdown for each.
The actual object Markdown is written by the things in the `Writers` module.
"""

import os, types, collections
from .Writers import *

__all__ = [ "DocWalker" ]

class DocTree(dict):
    """
    Simple tree that stores the structure of the documentation
    """

class MethodDispatch(collections.OrderedDict):
    """
    Provides simple utility to dispatch methods based on types
    """

    def __init__(self, *args, default=None, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)
    class DispatchTests:
        def __init__(self, *tests):
            self.tests = tests
        def __hash__(self):
            return self.tests.__hash__()
        def __call__(self, obj):
            return all(self.test(t, obj) for t in self.tests)
        @classmethod
        def test(cls, k, obj):
            """
            Does the actual dispatch testing

            :param k:
            :type k:
            :param obj:
            :type obj:
            :return:
            :rtype:
            """
            if (
                    isinstance(k, type) or
                    isinstance(k, tuple) and all(isinstance(kk, type) for kk in k)
            ):
                return isinstance(obj, k)
            elif isinstance(k, str):
                return hasattr(obj, k)
            elif isinstance(k, tuple) and all(isinstance(kk, str) for kk in k):
                return any(hasattr(obj, kk) for kk in k)
            elif isinstance(k, tuple):
                return any(kk(obj) for kk in k)
            else:
                return k(obj)
    def method_dispatch(self, obj, *args, **kwargs):
        """
        A general-ish purpose type or duck-type method dispatcher.

        :param obj:
        :type obj:
        :param table:
        :type table:
        :return:
        :rtype:
        """

        for k, v in self.items():
            if isinstance(k, self.DispatchTests):
                matches = k(obj)
            else:
                matches = self.DispatchTests.test(k, obj)
            if matches:
                return v(obj, *args, **kwargs)

        if self.default is None:
            raise TypeError("object {} can't dispatch from table {}".format(
                obj, self
            ))
        else:
            return self.default(obj, *args, **kwargs)
    def __call__(self, obj, *args, **kwargs):
        return self.method_dispatch(obj, *args, **kwargs)
    def __setitem__(self, key, value):
        """
        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        #TODO: make dispatch keys automatically feed into
        if isinstance(key, tuple):
            # make sure we're not just doing alternatives
            if not (
                    all(isinstance(k, str) for k in key) or
                    all(isinstance(k, type) for k in key) or
                    all(callable(k) for k in key)
            ):
                # then we do, basically, an 'and' operand
                key = self.DispatchTests(*key)

        super().__setitem__(key, value)

class DocSpec(dict):
    """
    A specification for an object to document.
    Supports the fields given by `spec_fields`.
    """
    spec_fields = (
        'id', # name for resolving the object
        'parent', # parent object name for writing,
        'children',
        'examples_root',
        'tests_root'
    )

    def __repr__(self):
        return '{}({})'.format(
            type(self).__name__,
            super().__repr__()
        )

class DocWalker:
    """
    A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
    and a Markdown index file.

    Takes a set of objects & writers and walks through the objects, generating files on the way
    """

    default_writers = collections.OrderedDict((
        ((str, types.ModuleType), ModuleWriter),
        ((type,), ClassWriter),
        ((types.FunctionType,), FunctionWriter)
    ))
    default_docs_ext='Documentation'
    def __init__(self,
                 objects,
                 tree=None,
                 out=None,
                 docs_ext=None,
                 writers=None,
                 ignore_paths=None,
                 description=None,
                 verbose=True,
                 extra_fields=None,
                 template_directory=None,
                 examples_directory=None,
                 strip_undocumented=False
                 ):
        """
        :param objects: the objects to write out
        :type objects: Iterable[Any]
        :param out: the directory in which to write the files (`None` means `sys.stdout`)
        :type out: None | str
        :param out: the directory in which to write the files (`None` means `sys.stdout`)
        :type out: None | str
        :param: writers
        :type: DispatchTable
        :param ignore_paths: a set of paths not to write (passed to the objects)
        :type ignore_paths: None | Iterable[str]
        """

        if extra_fields is None:
            extra_fields = {}
        self.extra_fields = extra_fields

        self.template_directory = template_directory
        self.examples_directory = examples_directory

        self.objects = objects

        # obtain default writer set
        if writers is None:
            writers = {}
        if not isinstance(writers, MethodDispatch):
            if hasattr(writers, 'items'):
                writers = MethodDispatch(writers.items(), default=ObjectWriter)
            else:
                writers = MethodDispatch(writers, default=ObjectWriter)
        for k, v in self._initial_writers.items():
            if k not in writers:
                writers[k] = v
        self.writers = writers

        # obtain default tree
        if tree is None:
            tree = DocTree()
        self.tree = tree

        self.ignore_paths = ignore_paths

        if out is None:
            if docs_ext is None:
                docs_ext = self.default_docs_ext
            out = os.path.join(os.getcwd(), docs_ext)
        self.out_dir = out
        try:
            os.makedirs(self.out_dir)
        except OSError:
            pass

        self.description = description
        self.verbose = verbose
        self.strip_undocumented = strip_undocumented

    @property
    def _initial_writers(self):
        """
        Adds a minor hook onto the default_writes dict and returns it
        :return:
        :rtype:
        """

        writers = self.default_writers.copy()
        writers[DocSpec] = self.resolve_spec
        return writers

    def resolve_spec(self, spec, *args,
                     template_directory=None,
                     examples_directory=None,
                     extra_fields=None,
                     **kwargs
                     ):
        """
        Resolves an object spec.

        :param spec: object spec
        :type spec: DocSpec
        :return:
        :rtype:
        """

        # for the moment we only reolve using the `id` parameter
        oid = spec['id']
        o = DocWriter.resolve_object(oid)
        # but we attach all of the other info

        template_directory = self.template_directory if template_directory is None else template_directory
        examples_directory = self.examples_directory if examples_directory is None else examples_directory
        extra_fields = self.extra_fields if extra_fields is None else extra_fields

        return self.writers(o, *args,
                            spec=spec,
                            template_directory=template_directory,
                            examples_directory=examples_directory,
                            extra_fields=extra_fields,
                            **kwargs
                            )

    def write_object(self, o, parent=None):
        """
        Writes a single object to file.
        Provides type dispatching to a writer, basically.

        :param o: the object we want to write
        :type o:
        :param parent: the writer that was called right before this
        :type parent: DocWriter
        :return: the written file
        :rtype: None | str
        """

        if (
                isinstance(o, (dict, collections.OrderedDict))
                and all(k in o for k in ['id'])
        ):
            o = DocSpec(o.items())

        if parent is not None:
            pid = parent.identifier
            ptests = parent.tests
        else:
            pid = None
            ptests = None

        writer = self.writers(o,
                              self.out_dir,
                              parent=pid,
                              parent_tests=ptests,
                              tree=self.tree,
                              ignore_paths=self.ignore_paths,
                              template_directory=self.template_directory,
                              examples_directory=self.examples_directory,
                              extra_fields=self.extra_fields
                              )

        oid = writer.identifier
        if oid not in self.tree:
            res = writer.write()
            if res is not None: # basically means stop writing
                spec = writer.doc_spec
                spec.update(file=res)
                self.tree[oid] = spec

                for child in writer.children:
                    self.write_object(child, parent=writer)
            return res

    def write_docs(self):
        """
        Walks through the objects supplied and writes them & their children to file
        :return: written files
        :rtype: list[str]
        """

        if self.verbose:
            print("Generating documentation to {}".format(self.out_dir))
        files = [ self.write_object(o) for o in self.objects ]
        files = [ f for f in files if f is not None ]
        w = IndexWriter(files, os.path.join(self.out_dir, 'index.md'),
                        description=self.description,
                        root=self.out_dir,
                        template_directory=self.template_directory,
                        examples_directory=self.examples_directory,
                        extra_fields=self.extra_fields
                        )
        return w.write()



