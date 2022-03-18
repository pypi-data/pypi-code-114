"""
AIIRE grammar module provides basic AIIRE grammar functionality.

Grammar is the base class for grammars, and it has nested constituent
classes.
Both Grammar and constituent classes are intended to be subclassed
for each language.
"""

from typing import Iterator, Type, Dict
from . import agenda, ontology


class Grammar(object):
    """
    Grammar is the base class of grammars.

    It provides nested constituent classes and constituent binding
    functionality.

    @cvar ontology: an Ontology instance where the grammar gets and
        creates concepts for its constituents; multiple Grammar
        instances can share the same Ontology

    @ivar by_children: the grammar's mapping from child constituent
        class pairs to parent constituent classes; in terms of
        production rules (or rewriting rules), it is a mapping from
        the right parts of the rules to their left parts
        E.g., if the Grammar has Constituent classes like this:

        >>> # CNF rule: A -> B C
        >>>
        >>> class A(Constituent):
        >>>     pass
        >>>
        >>> class B(Constituent):
        >>>     pass
        >>>
        >>> class C(Constituent):
        >>>     pass
        >>>
        >>> A.left = [B]
        >>> A.right = [C]
        >>>
        >>> # To add A -> B1 C, A -> B2 C:
        >>>
        >>> class B1(B):
        >>>     pass
        >>>
        >>> class B2(B):
        >>>     pass
        >>>
        >>> # This also adds:
        >>> # A -> B C1, A -> B C2, A -> B1 C1, A -> B1 C2,
        >>> # A -> B2 C1, and A -> B2 C2
        >>>
        >>> class C1(C):
        >>>     pass
        >>>
        >>> class C2(C):
        >>>     pass
    """

    ontology = NotImplemented

    @classmethod
    def iter_constituents(
        cls,
        complex_only: bool = False
    ) -> Iterator[Type['Grammar.Constituent']]:
        """
        Iterate through the Grammar constituent classes.

        Yields nested classes of `cls' Grammar class, wchich are
        subclasses of Grammar.Consituent

        @param complex_only: if set, yields only complex constituent
            classes, i.e., those that have children

        @yield: constituent classes
        """
        for value in cls.__dict__.values():
            if isinstance(value, type) and issubclass(value, cls.Constituent):
                if complex_only:
                    if(
                        not hasattr(value, 'left') or
                        not hasattr(value, 'right')
                    ):
                        continue
                yield value

    def __init__(self):
        """
        Create the Grammar instance.

        Build the `by_children' mapping by the immediate
        <x.left, x.right> pairs for each x constituent, and also by
        all available substitutions both of `x.left' and `x.right'
        with subclasses thereof.
        """
        self.by_children = {}
        # Maps left constituents to <(left, right) -> parent> rules
        rules_by_left = {}
        # Maps right constituents to <(left, right) -> parent> rules
        rules_by_right = {}

        # Immediate <(left, right) -> parent> rules
        for parent in self.iter_constituents(complex_only=True):
            # Store rules for each (left, right) pair for each parent
            # constituent class
            for left in parent.left:
                for right in parent.right:
                    rule = (left, right, parent)
                    self.by_children[(left, right)] = {parent}
                    rules_by_left.setdefault(left, []).append(rule)
                    rules_by_right.setdefault(right, []).append(rule)

        # Extend known rules with left child subclasses for each rule
        for child in self.iter_constituents():
            for left in rules_by_left:
                if issubclass(child, left):
                    for rleft, rright, parent in rules_by_left[left]:
                        self.by_children.setdefault(
                            (child, rright), set()
                        ).add(parent)
                        rules_by_right.setdefault(
                            rright, []
                        ).append((child, rright, parent))

        # Now add right child subclasses for each rule
        for child in self.iter_constituents():
            for right in rules_by_right:
                if issubclass(child, right):
                    for rleft, rright, parent in rules_by_right[right]:
                        self.by_children.setdefault(
                            (rleft, child), set()).add(parent)

    def bind(
        self, c1: 'Grammar.Constituent', c2: 'Grammar.Constituent'
    ) -> Iterator['Grammar.Constituent']:
        """
        Bind (`c1', `c2') constituent pair into a single constituent.

        @param c1: left constituent
        @param c2: right constituent
        @yield: possible parent constituents
        """
        l, r = c1.__class__, c2.__class__
        if (l, r) in self.by_children:
            for cls in self.by_children[(l, r)]:
                res = cls(c1.start, c2.end, children=(c1, c2))
                yield res

    class Constituent(object):
        """
        Constituent is the base class for all constituents.

        @cvar left: left child constituent classes
            (only non-Atoms have this attribute)
        @cvar right: right child constituent classes
            (only non-Atoms have this attribute)
        @cvar right_only: if set, the Constituent is treated as able
            to be bound only from the right side and, therefore,
            unable to be bound as a left child. It allows to get
            rid of incorrect constituent versions when they prove
            to be unbindable from the right, not to put them on the
            agenda and not to try to bind them with furthercoming
            constituents.
        """

        right_only = False

        def __str__(self) -> str:
            """Represent the Constituent as a string."""
            return (
                f'{self.__class__.__name__} [{self.start}..{self.end}] (' +
                ' or '.join(
                    '<%s %s>' %
                    (c1, c2)
                    for c1, c2 in self.childvars
                ) + ')'
            )

        def get_text(self) -> str:
            """
            Get the text of the constituent.

            Basically, the constituent text is a combination
            of its left child text with its right child text.
            E.g., if `a' is a constituent, `b' is its left child,
            and `c' is its right child, and the text of `b' is 'foo',
            whereas the text of `c' is 'bar', then the text of `a' is
            'foobar'.

            Due to the properties of structural ambiguity packing,
            all variants of children produce the same text, thus,
            the first child structure variant can be taken.

            If no child variants are available, return None.

            Atoms don't have children and hust have their text as
            an attribute, so they have this method overriden.
            """
            if not self.childvars:
                return
            return ''.join(c.get_text() for c in self.childvars[0])

        def repr_text(self):
            """Create a python representation of the text."""
            return repr(self.get_text())

        def __init__(
            self,
            start: int, end: int,
            text: str = None,
            children: tuple['Grammar.Constituent'] = None
        ):
            """
            Create the constituent.

            @param start: the Constituent start position in the text
                is the number of its first character
            @param end: the Constituent end position in the text is
                the number of the character after its last character
            @param text: the Constituent text (from start till end)
                to be stored as an attribute (only applicable to
                Atoms)
            @param children: the first variant of children structure
                (only applicable to non-Atoms built from these
                children)
            """
            self.start = start
            self.end = end
            self.text = text
            self.childvars = []
            if children is not None:
                self.childvars.append(children)

        @property
        def identity(self):
            """
            Get the Constituent identity as a (class, start, end) tuple.

            Identity is necessary to determine identic constituents
            built from different children combinations and to merge
            them into a single Constituent instance with ambiguous
            children structure (packing).

            Constituents of the same class which have the same
            (start, end) spans are considered identical.
            """
            return (self.__class__, self.start, self.end)

        def merge(self, c: 'Grammar.Constituent'):
            """
            Merge the Constituent with another Constituent.

            The Constituent child constituent variants are extended
            with those of `c'.

            @param c: the Constituent to be merged with
            """
            self.childvars.extend(c.childvars)

        def get_list_items(self) -> Iterator['Grammar.Constituent']:
            """
            Get the items of a constituent list.

            Basically, the Constituent is not a list and, therefore,
            it is yielded as is.
            ListConstituent overrides this and iterates through its
            children and descendents to get the items.
            """
            yield self

        def is_valid_for_agenda(
            self, agenda: 'agenda.Agenda'
        ) -> bool:
            """
            Check whether the Constituent is valid for the agenda.

            Basically, all Constituents are considered valid.
            ListConstituent is only valid for the agenda if it does
            not intersect with a larger ListConstituent of the same
            class which is already stored on the agenda; cf.
            ListConstituent.is_valid_for_agenda method.
            """
            return True

        def eval_conc(self) -> 'ontology.Ontology.Concept':
            """
            Evaluate the Constituent meaning as a Concept.

            This method should be overriden in subclasses.
            """
            raise NotImplementedError(
                '%s.eval_conc()' %
                self.__class__.__name__
            )

        def register_coverage(
            self, by_cov: Dict[Type['Grammar.Constituent'], list[int]]
        ):
            """
            Register the Constituent coverage in the `by_cov'.

            Coverage should be registered to prevent an agenda from
            accepting list constituent versions when larger list
            constituent version of the same class is already built.
            Basically, Constituent needs not registering its
            coverage, but ListConstituent overrides this method.
            """
            return

    class AtomicConstituent(Constituent):
        """
        AtomicConstituent is a Constituent treated as atomic.

        AtomicConstituent is the base class for those constituents
        which may or may not have children, but should be treated as
        atomic in representation and concept evaluation procedures.
        """

        def __str__(self) -> str:
            """Get string representation without children."""
            return (
                f'{self.__class__.__name__} '
                f'[{self.start}..{self.end}] ({self.repr_text()})'
            )

        def get_list_items(self) -> Iterator['Grammar.Constituent']:
            """Get the Constituent only instead of list items."""
            yield self

    class ListConstituent(Constituent):
        """
        ListConstituent is a Constituent treated as an unfixed size list.

        Typically, list constituent class is a subclass of its
        possible left child class, i.e., the list is formed by
        self embedding, and no structural ambiguity should be
        allowed like (a, b, c) <- (a, b) c | a, (b, c)

        List constituents denote enumerations, sequences, groups,
        etc.

        List representations are more convenient for list
        constituents than basic tree representations, because they
        are shorter and look natural, so they are overriden.

        If a list constituent is already on the agenda, then its
        smaller parts are not considered valid for this agenda to
        form separate constituent versions.
        This prevents the agenda from building redundant versions,
        e.g., when (a, b, c, d, e) list is already on the agenda,
        versions like (b, c, d, e), (c, d, e), (d, e), (e) are not
        allowed; thisa also means excluding (b, c, d), (c, d), (d),
        and (b, c), (c) on the previous steps.

        The list nature of ListConstituent classes and the upper
        mentioned restriction on structural ambiguity allows to
        evaluate their concepts by just creating a group concept
        with the constituent items concepts as elements.
        """

        def __str__(self) -> str:
            """Create a string representation."""
            return (
                f'{self.__class__.__name__} [{self.start}..{self.end}] (' +
                ' or '.join(
                    '<\n    %s\n    %s>' % (
                        '\n    '.join(map(str, c1.get_list_items())),
                        '\n    '.join(map(str, c2.get_list_items()))
                    )
                    for c1, c2 in self.childvars
                ) +
                ')'
            )

        def get_list_items(self) -> Iterator['Grammar.Constituent']:
            """
            Get the ListConstituent items.

            As ListConstituent classes have structural ambiguity
            restricted to have only one children variant, the items
            are only taken from the first children variant.

            @yield: list items of the Constituent children
            """
            for c in self.childvars[0]:
                yield from c.get_list_items()

        def is_valid_for_agenda(self, agenda: 'agenda.Agenda') -> bool:
            """
            Check whether the Constituent is valid for the agenda.

            If the Constituent class already covers the constituent
            (start, end) span on the agenda, then the Constituent is
            considered invalid; otherwise, it is valid.
            """
            return not agenda.has_constituent_class(
                self.start, self.end, self.__class__
            )

        def eval_conc(self) -> 'ontology.Ontology.Concept':
            """
            Evaluate ListConstituent concept.

            Create a concept of a group of concepts of the
            ListConstituent items.
            If there are no items, or if the items have no concepts,
            then None is returned.

            @return: a concept of a group of concepts of the
                ListConstituent items
            """
            items = [item for item in self.get_list_items()]
            if not items:
                return
            items = [item.eval_conc() for item in items]
            items = [item for item in items if item is not None]
            if not items:
                return
            ontology = items[0].ontology
            return ontology.create_group(items)

        def register_coverage(
            self, by_cov: Dict[Type['Grammar.Constituent'], list[int]]
        ):
            """
            Register the ListConstituent coverage in `by_cov'.

            @param by_cov: a mapping from list constituent classes
                to binary (0/1) arrays containing, for each class,
                zeros for positions not covered by the class, and
                ones for positions covered by the class
            """
            cov = by_cov.setdefault(self.__class__, [])
            # The coverage list can be shorter than the constituent
            # span; in this case, it is padded with zeros here.
            cov.extend([0] * (self.end - len(cov)))

            # Ones are written to the coverage list on the whole span
            # of the constituent.
            cov[self.start:self.end] = [1] * (self.end - self.start)
            # print(f'{self.__class__.__name__} coverage: {l}')

    class InlineListConstituent(ListConstituent):
        """InlineListConstituent is a one-line ListConstituent."""

        def __str__(self):
            """Create a string representation."""
            return (
                f'{self.__class__.__name__} [{self.start}..{self.end}] (' +
                ' or '.join(
                    '<%s, %s>' % (
                        ', '.join(map(str, c1.get_list_items())),
                        ', '.join(map(str, c2.get_list_items()))
                    )
                    for c1, c2 in self.childvars
                ) +
                ')'
            )

    class Atom(AtomicConstituent):
        """
        Atom is an AtomicConstituent which has no children.

        Atoms store their texts instead of combining children's texts.
        Atoms change their classes according with their texts on
        initialization.

        @ivar text: the Atom's text stored as an attribute
        """

        def get_text(self) -> str:
            """Get the Atom's text."""
            return self.text

        def __init__(self, *args, **kwargs):
            """
            Create an Atom.

            The Atom class is changed to the one which
            self.get_cls_by_text() will return.
            If it returns None, the class remains unchanged.
            """
            super().__init__(*args, **kwargs)
            newcls = self.get_cls_by_text()
            if newcls is not None:
                self.__class__ = newcls

        def get_cls_by_text() -> Type['Grammar.Atom']:
            """
            Get a new class for the Atom according with its text.

            Should be overriden in subclasses depending on language,
            grammar, and the logic behind atom class determination.
            """
            raise NotImplementedError

    class LeftConc(Constituent):
        """LeftConc is a Constituent meaning the same as its left child."""

        def eval_conc(self) -> 'ontology.Ontology.Concept':
            """Evaluate the Constituent concept."""
            return self.childvars[0][0].eval_conc()  # TODO: ambiguity

    class RightConc(Constituent):
        """RightConc is a Constituent meaning the same as its right child."""

        def eval_conc(self) -> 'ontology.Ontology.Concept':
            """Evaluate the Constituent concept."""
            return self.childvars[0][1].eval_conc()

    class RightIdentityConstituent(RightConc):
        """
        RightIdentityConstituent is a RightConc identical with its right child.

        These constituents are omitted when traversing the
        constituent tree for retrieving list items.

        They are also considered always valid for the agenda, even
        if they are list constituents.
        """

        def get_list_items(self) -> Iterator['Grammar.Constituent']:
            """Iterate through the items of the constituent."""
            yield self.childvars[0][1]

        def is_valid_for_agenda(self, agenda: 'agenda.Agenda') -> bool:
            """Check whether the constituent is valid for the agenda."""
            return True
