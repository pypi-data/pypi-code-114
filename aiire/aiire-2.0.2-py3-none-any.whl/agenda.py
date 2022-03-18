"""This module provides aiire.agenda functionality."""
from typing import Generator, Type
from . import grammar


class Agenda(object):
    """
    Agenda is the base class for AIIRE agendas.

    AIIRE agenda is an in-memory storage for the constituents
    recognized while parsing. Constituents on the agenda are
    ready to be bound with new constituents as their left neighbors.

    When a constituent is being put on the agenda, it is checked
    for being identical with a constituent already stored there;
    if yes, it gets merged; otherwise, it gets bound with all
    possible left neighbors.

    @ivar by_end: a mapping from the end positions to the
        constituents which end at these positions and are, therefore,
        left neighbors of those which start there.

    @ivar by_identity: a mapping from the constituents identity
        tuples to the constituents having them

    @ivar grammar: a Grammar instance used by the Agenda to bind
        constituents

    @ivar cov_by_class: a coverage by class mapping, i.e., a mapping
        from constituent classes to their coverages, where coverages
        are stored as binary (0/1) arrays (lists) holding zeros for
        positions no covered by constituents of the given class, and
        ones for those covered.
    """

    def __init__(self, grammar: 'grammar.Grammar'):
        """Create an Agenda."""
        self.by_end = {}
        self.by_identity = {}
        self.grammar = grammar
        self.cov_by_class = {}

    def put(
        self, c: 'grammar.Grammar.Constituent'
    ) -> Generator['grammar.Grammar.Constituent', None, None]:
        """
        Put a Constituent on the Agenda.

        When a constituent is being put on the agenda, it is checked
        for being identical with a constituent already stored there;
        if yes, it gets merged; otherwise, it gets bound with all
        possible left neighbors.

        If the binding succeeds, and the resulting parent constituent
        is valid for the agenda, then it is also put on the agenda.

        If no parent constituents could be put on the agenda, which
        means that the constituent being put could not be bound with
        any left neighbors, then it is only stored on the agenda, if
        it is not right only. Storing such a constituent would mean
        that it should wait for being bound with some further
        constituents as left neighbor, but as it is right only, this
        is impossible.

        @param c: the Constituent being put
        @yield: the old constituent with the same identity which
            had been already stored on the agenda before putting if
            available, otherwise the produced parent constituents
            during binding, and the `c' constituent itself, if it
            is not right_only, or if parents could be produced and
            put.
        """
        identity = c.identity
        by_identity = self.by_identity
        old = by_identity.get(identity)
        if old is not None:
            old.merge(c)
            yield old
        else:
            found = False
            by_end = self.by_end
            grammar = self.grammar
            for leftneib in by_end.get(c.start, []):
                for newc in grammar.bind(leftneib, c):
                    if newc.is_valid_for_agenda(self):
                        for cic in self.put(newc):
                            found = True
                            yield cic
            if not found and c.right_only:
                return
            by_identity[identity] = c
            by_end.setdefault(c.end, set()).add(c)
            c.register_coverage(self.cov_by_class)
            yield c

    def has_constituent_class(
            self,
            start: int,
            end: int,
            cls: Type['grammar.Grammar.Constituent']):
        """
        Check whether the agenda has `cls' constituents at `start'..`end'.

        @param start: the start of the span
        @param end: the end of the span
        @param cls: the constituent class for which the check is performed
        """
        cov = self.cov_by_class.get(cls, [])
        if start and start < len(cov) and cov[start] and cov[start - 1]:
            # print(f'Has {cls.__name__}[{start}..{end}]')
            return True
        # print(f'No {cls.__name__}[{start}..{end}]: {cov}')
        return False
