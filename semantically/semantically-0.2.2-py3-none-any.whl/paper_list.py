"""This module handles the custom list implementation for semanticallys paper results."""
from collections import UserList
from typing import Iterable, List, Union

from typing_extensions import Self

from .datastructures import DetailedPaper, Paper


class PaperList(UserList):
    """Custom List class for holing lists of papers. This custom list implementation enables
    filter methods to be implemented. Furthermore strict type checking is implemented, so that
    these lists only hold paper data."""

    def __add__(self: Self, other: Iterable) -> Self:
        ret = self.copy()
        ret.extend(other)
        return ret

    def extend(self, other: Iterable) -> None:
        for paper in other:
            self.append(paper)

    def append(self, item) -> None:
        if not isinstance(item, Paper) or not isinstance(item, DetailedPaper):
            raise TypeError("Only paper types are allowed in the list.")
        return super().append(item)

    def filter_citations_greater(self, min_citations: int) -> Self:
        """Remove all papers from list, which have less citations than min_citations

        Args:
            min_citations (int): minimum amount of citations
        """
        self.data[:] = [
            paper for paper in self.data if paper.citationCount > min_citations
        ]
        return self

    def filter_reference_greater(self, min_references: int) -> Self:
        """Remove all papers from list, which have less references than min_citations

        Args:
            min_references (int): minimum amount of references
        """
        self.data[:] = [
            paper for paper in self.data if paper.referenceCount > min_references
        ]
        return self

    def filter_category(self, category: Union[str, List[str]]) -> Self:
        """Remove all papers, which do not fit in a specified category

        Args:
            category (Union[str, List[str]]): either a list of categories or a single category
        """
        self.data[:] = [
            paper
            for paper in self.data
            if self._check_study_fields(category, paper.fieldsOfStudy)
        ]
        return self

    def filter_has_abstract(self) -> Self:
        """Remove all papers without an abstract"""
        self.data[:] = [paper for paper in self.data if paper.abstract]
        return self

    def filter_has_url(self) -> Self:
        """Remove all papers without an url"""
        self.data[:] = [paper for paper in self.data if paper.url]
        return self

    def filter_published_after(self, year: int) -> Self:
        """Remove all papers published before a given year

        Args:
            year (int): earliest year of publishment
        """
        self.data[:] = [paper for paper in self.data if paper.year >= year]
        return self

    def filter_published_before(self, year: int) -> Self:
        """Remove all papers published after a given year

        Args:
            year (int): latest year of publishment
        """
        self.data[:] = [paper for paper in self.data if paper.year <= year]
        return self

    @staticmethod
    def _check_study_fields(specified_category, given_category) -> bool:
        for category in given_category:
            if category in specified_category:
                return True
        return False
