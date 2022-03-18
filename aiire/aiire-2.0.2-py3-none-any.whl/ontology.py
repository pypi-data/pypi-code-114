"""
This module provides the ontology functionality.

It defines the `Ontology' class, as well as `Ontology.Concept'.
These classes are intended to be subclassed in applications.
"""

import typing
import csv


class Ontology(object):
    """
    `Ontology' is the base class of ontologies.

    An Ontology instance contain concepts (Concept instances).
    It can retrieve concepts by their unique names or ids.

    @ivar by_name: a mapping from names to concepts
    """

    def __init__(self):
        """Construct an Ontology instance."""
        self.by_name = {}

    @classmethod
    def from_concept(
        cls, concept: 'Ontology.Concept',
        ontology_concept_relation_name: str = 'have concept'
    ) -> 'Ontology':
        """
        Construct an Ontology instance from a `concept'.

        This `concept' is supposed to be a _concept_ of ontology,
        which, in turn, contains concepts.

        @param concept: a concept of ontology, which contains its
            concepts as objects of relation named
            `ontology_concept_relation_name'

        @param ontology_concept_relation_name: the name of the
            relation between `concept' and the concepts of the
            ontology being constructed

        @return: an Ontology instance which contains all concepts
            that are objects of the concept's relation named
            `ontology_concept_relation_name'
        """
        return OntologyFromConcept(concept)

    def create_or_get(self, name: str) -> 'Ontology.Concept':
        """
        Create a new concept or retrieve it by name.

        If the ontology has a concept with such name, then
        this concept is returned.
        Otherwise, a new concept is created, stored in the
        ontology, and returned.

        @param name: the name of the concept
        @return: the concept (retrieved or created)
        """
        if name in self.by_name:
            return self.by_name[name]
        conc = self.Concept(name, self)
        self.by_name[name] = conc
        return conc

    def create_group(
        self,
        items: typing.Iterable['Concept'],
        conc_name: str = 'group',
        rel_name: str = 'include',
        inh_name: str = 'inheritance'
    ):
        """
        Create a concept of a group of concepts from given items.

        @param items: a collection of items to be added to the group
        @param conc_name: the group concept name in the ontology
        @param rel_name: the ontology name of the relation between
            group concept and its items
        @param inh_name: inheritance relation name in the ontology
        """
        groupcls = self.create_or_get(conc_name)
        include = self.create_or_get(rel_name)
        group = self.Concept(conc_name, self)
        inheritance = self.create_or_get(inh_name)
        group.add_attr(inheritance, groupcls)
        for item in items:
            group.add_attr(include, item)
        return group

    def __iter__(self):
        """Iterate Ontology concepts."""
        return iter(self.by_name.values())

    def save_db_csv(
        self,
        expressions_file: typing.IO,
        concepts_file: typing.IO,
        relations_file: typing.IO
    ):
        """
        Save the ontology to AIIRE ontology database CSV files.

        These CSV files are intended to be uploaded to the database
        by 'COPY' command and must fit with the structure of the
        tables.

        The IO handles provided as parameters must be open for
        writing. They can be physical file handles or in-memory.

        @param expressions_file: an open IO handle for the
            `expressions' table
        @param concepts_file: an open IO handle for the
            `concepts' table
        @param relations_file: an open IO handle for the
            `relations' table
        """
        expressions_writer = csv.writer(expressions_file)
        concepts_writer = csv.writer(concepts_file)
        relations_writer = csv.writer(relations_file)

        # Generate the identifiers
        expr_id = 1
        relation_id = 1

        # Write the data
        for conc in self:
            if hasattr(conc, 'descr'):
                conc_name = conc.descr
                expr_name = conc.name
            else:
                expr_name = conc_name = conc.name
            expressions_writer.writerow(
                [expr_id, expr_name, expr_name]
            )
            concepts_writer.writerow([conc.id, expr_id, conc_name])
            for relation in conc.attrs:
                for relation_object in conc.attrs[relation]:
                    relations_writer.writerow(
                        [
                            relation_id, conc.id,
                            relation.id, relation_object.id
                        ]
                    )
                    relation_id += 1
            expr_id += 1

    class Concept(object):
        """
        `Concept' is the base class for concepts.

        Concepts have attributes, i.e. are subjects of relations to
        other concepts.
        Concept always belongs to a certain ontology.

        @ivar name: the name of the concept
        @ivar ontology: the ontology to which the concept belongs
        @ivar attrs: concept's attributes relation->object mapping
        @ivar id: an integer identifier of the concept
        """

        _last_id = 0

        def __init__(self, name: str, ontology: 'Ontology'):
            """
            Construct a Concept instance.

            @param name: the name of the concept
            @param ontology: the ontology of the concept
            """
            self.name = name
            self.ontology = ontology
            self.attrs = {}
            self.id = self._last_id + 1
            self.__class__._last_id = self.id

        def add_attr(
            self,
            reltype: 'Ontology.Concept',
            obj: 'Ontology.Concept'
        ):
            """
            Add a new attribute to the concept.

            @param reltype: relation type concept
            @param obj: relation object concept
            """
            self.attrs.setdefault(reltype, []).append(obj)

        def getattr(self, attrname) -> typing.Iterable[
            'Ontology.Concept'
        ]:
            """
            Get attribute by relation name.

            @param attrname: the name of the relation
            @return: objects of this relation
            """
            return self.attrs[self.ontology.create_or_get(attrname)]

        def __str__(self) -> str:
            """
            Make a string representation of the concept.

            @return representation
            """
            return f'{self.name}:\n    ' + (
                '\n    '.join(
                    f'{attr.name}: '
                    '{", ".join(c.name for c in self.attrs[attr])}'
                    for attr in self.attrs
                )
            )


class OntologyFromConcept(Ontology):
    """Ontology that is actually a concept which acts as ontology."""

    def __init__(
        self, concept: Ontology.Concept,
        ontology_concept_relation_name: str = 'have concept'
    ):
        """
        Construct an OntologyFromConcept from `concept'.

        This `concept' is supposed to be a _concept_ of ontology,
        which, in turn, contains concepts.

        @param concept: a concept of ontology, which contains its
            concepts as objects of relation named
            `ontology_concept_relation_name'

        @param ontology_concept_relation_name: the name of the
            relation between `concept' and the concepts of the
            ontology being constructed
        """
        # The concept and the name of the relation to ontology
        # concepts are just stored in the OntologyFromConcept
        # instance.
        self.concept = concept
        self.concept_relation_name = ontology_concept_relation_name

        # For perfomance, store also the underlying concept ontology
        self.underlying_ontology = concept.ontology

        # Also for performance, store the concept of the concept
        # relation in the underlying_ontology
        self.concept_relation = concept.ontology.create_or_get(
            ontology_concept_relation_name
        )

    @property
    def by_name(self) -> typing.Dict[str, Ontology.Concept]:
        """Get the underlying ontology `by_name' mapping."""
        return self.underlying_ontology.by_name

    def create_or_get(self, name: str) -> Ontology.Concept:
        """
        Create a new concept or retrieve it by name.

        If the ontology has a concept with such name, then
        this concept is returned.
        Otherwise, a new concept is created, stored in the
        ontology, and returned.

        @param name: the name of the concept
        @return: the concept (retrieved or created)
        """
        concept = self.underlying_ontology.create_or_get(name)
        self.concept.add_attr(self.concept_relation, concept)
        return concept
