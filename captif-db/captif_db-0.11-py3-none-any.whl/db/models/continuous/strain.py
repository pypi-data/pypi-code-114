"""
The strain models are used to describe the strain coils, coil positions and associated
measurements.
"""

from typing import Optional
from numpy import diff
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


from captif_db.helpers.models import objects_to_frame

from ..base import Table, Base


__all__ = [
    "ReceiverStrainCoil",
    "TransmitterStrainCoil",
    "StrainCoilPair",
    "StrainReading",
]


class TransmitterStrainCoil(Table, Base):
    """
    Transmitter strain coil details.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param coil_no: coil number (required)
    :param coil_position: coil position ("centre", "transverse", "longitudinal" or
        "reference") (required)
    :param coil_depth_mm: coil depth (mm) below top of pavement (required)
    :param ram_position_cm: lateral position of coil

    :relationships: - section_obj (viewonly)

    """

    __tablename__ = "transmitter_strain_coil"
    __index_column__ = ["project_id", "section_id", "coil_no"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    coil_no = Column(Integer, primary_key=True)
    coil_position = Column(String(20), nullable=False)
    coil_depth_mm = Column(Integer, nullable=True)
    ram_position_cm = Column(Integer, nullable=True)

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="transmitter_strain_coil_obj", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        ForeignKeyConstraint(
            ["coil_position"], ["strain_coil_position_reference.coil_position"],
        ),
        {"info": {"er_tags": ["readings", "interval", "continuous", "static_strain"]}},
    )


class ReceiverStrainCoil(Table, Base):
    """
    Receiver strain coil details.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param coil_no: coil number (required)
    :param coil_position: coil position ("centre", "transverse", "longitudinal" or
        "reference") (required)
    :param coil_depth_mm: coil depth (mm) below top of pavement (required)
    :param ram_position_cm: lateral position of coil

    :relationships: - section_obj (viewonly)

    """

    __tablename__ = "receiver_strain_coil"
    __index_column__ = ["project_id", "section_id", "coil_no"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    coil_no = Column(Integer, primary_key=True)
    coil_position = Column(String(20), nullable=False)
    coil_depth_mm = Column(Integer, nullable=True)
    ram_position_cm = Column(Integer, nullable=True)

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="receiver_strain_coil_obj", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        ForeignKeyConstraint(
            ["coil_position"], ["strain_coil_position_reference.coil_position"],
        ),
        {"info": {"er_tags": ["readings", "interval", "continuous", "static_strain"]}},
    )


class StrainCoilPair(Table, Base):
    """
    Strain coil pair details.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param sensor_position_id: coil pair position ID (required)
    :param station_no: station number
    :param transmitter_coil_no: transmitter coil number (required)
    :param receiver_coil_no: receiver coil number (required)
    :param coil_pair_depth_mm: depth of the upper-most coil in the pair (mm) (required)
    :param coil_pair_direction: strain measurement direction ('vertical', 'longitudinal', 'transverse' or 'reference') (required)
    :param coil_pair_plane: strain measurement plane ('vertical', 'horizontal' or 'reference') (required)
    :param vertical_stack_position: vertical pair position ('centre', 'longitudinal' or 'transverse'). None for all horizontal and reference pairs (required)

    :relationships: - section_obj
                    - transmitter_strain_coil_obj (viewonly)
                    - receiver_strain_coil_obj (viewonly)
                    - strain_reading_obj (viewonly)
                    - dynamic_strain_reading_obj (viewonly)

    """

    __tablename__ = "strain_coil_pair"
    __index_column__ = ["project_id", "section_id", "sensor_position_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    sensor_position_id = Column(String(10), primary_key=True)

    station_no = Column(Numeric(3, 1), nullable=True)
    transmitter_coil_no = Column(Integer, nullable=False)
    receiver_coil_no = Column(Integer, nullable=False)

    coil_pair_depth_mm = Column(
        Integer, nullable=True, comment="depth of upper-most coil"
    )
    coil_pair_direction = Column(
        String(20),
        nullable=False,
        comment="strain measurement direction ('vertical', 'longitudinal', 'transverse' or 'reference')",
    )
    coil_pair_plane = Column(
        String(20),
        nullable=False,
        comment="strain measurement plane ('vertical', 'horizontal' or 'reference')",
    )
    vertical_stack_position = Column(
        String(20),
        nullable=True,
        comment="vertical pair position ('centre', 'longitudinal' or 'transverse'). None for horizontal and reference pairs",
    )

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="strain_coil_pair_obj", lazy=True)
    transmitter_strain_coil_obj = relationship(
        "TransmitterStrainCoil", lazy=True, viewonly=True)
    receiver_strain_coil_obj = relationship(
        "ReceiverStrainCoil", lazy=True, viewonly=True)
    strain_reading_obj = relationship(
        "StrainReading", back_populates="strain_coil_pair_obj", lazy=True, viewonly=True)
    dynamic_strain_reading_obj = relationship(
        "DynamicStrainReading", back_populates="strain_coil_pair_obj", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"]
        ),
        ForeignKeyConstraint(
            ["project_id", "section_id", "transmitter_coil_no"],
            [
                "transmitter_strain_coil.project_id",
                "transmitter_strain_coil.section_id",
                "transmitter_strain_coil.coil_no",
            ],
        ),
        ForeignKeyConstraint(
            ["project_id", "section_id", "receiver_coil_no"],
            [
                "receiver_strain_coil.project_id",
                "receiver_strain_coil.section_id",
                "receiver_strain_coil.coil_no",
            ],
        ),
        {"info": {"er_tags": ["readings", "interval", "continuous", "static_strain"]}},
    )

    @hybrid_property
    def coil_pair_direction_check(self) -> Optional[str]:
        """
        Determines the coil pair direction based on the individual coil positions and
        depths. Returns None for invalid coil combinations. The result should match the
        instance "coil_pair_direction" value.
        """
        positions, depths = self.coil_positions_depths()

        if positions.count("reference") == 2:
            return "reference"

        if positions[0] == positions[1]:
            if abs(diff(depths)[0]) == 75:  # Must have 75 mm spacing.
                return "vertical"

        if abs(diff(depths)) == 0:  # If coils are in the same horizontal plane.
            if set(positions) == set(("centre", "longitudinal")):
                return "longitudinal"
            if set(positions) == set(("centre", "transverse")):
                return "transverse"

        return None  # All other combinations are invalid

    @hybrid_property
    def coil_pair_plane_check(self) -> Optional[str]:
        """
        Return the coil pair plane (i.e. "vertical" or "horizontal"). Returns None for
        reference coil pairs.
        """
        positions, depths = self.coil_positions_depths()
        try:
            if (abs(diff(depths)[0]) == 75) and len(set(positions)) == 1:
                return "vertical"
            if (diff(depths)[0] == 0) and (positions.count("centre") == 1):
                return "horizontal"
        except TypeError:
            pass
        return None

    @hybrid_property
    def vertical_stack_position_check(self) -> Optional[str]:
        """
        Return the position of the "vertical" coil pairs (e.g. "centre", "longitudinal"
        or "transverse"). Returns None for all other coil pair directions.
        """
        return (
            self.receiver_strain_coil_obj.coil_position
            if self.coil_pair_direction == "vertical"
            else None
        )

    @hybrid_property
    def coil_pair_depth_mm_check(self) -> Optional[str]:
        """
        Return the coil pair depth (mm). The depth is taken as the depth of the top most
        coil. Returns None for reference coil pairs.
        """
        try:
            return int(min(self.coil_positions_depths()[1]))
        except TypeError:
            return None

    def coil_positions_depths(self):
        return (
            (
                self.receiver_strain_coil_obj.coil_position,
                self.transmitter_strain_coil_obj.coil_position,
            ),
            (
                self.receiver_strain_coil_obj.coil_depth_mm,
                self.transmitter_strain_coil_obj.coil_depth_mm,
            ),
        )

    def static_strain_reading_df(self):
        return objects_to_frame(self.static_strain_reading_obj).sort_values("datetime")


class StrainReading(Table, Base):
    """
    Static strain reading.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param sensor_position_id: coil pair position ID (required)
    :param reading_id: reading ID (required)
    :param datetime: datetime fo the reading (required)
    :param coil_spacing_mm: distance between the coils (mm) (required)

    :relationships: - strain_coil_pair_obj

    """

    __tablename__ = "strain_reading"
    __index_column__ = ["project_id", "section_id", "sensor_position_id", "reading_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    sensor_position_id = Column(String(20), primary_key=True)
    reading_id = Column(Integer, primary_key=True, autoincrement=True)

    datetime = Column(DateTime, nullable=False)
    coil_spacing_mm = Column(Numeric(5, 3), nullable=False)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id", "sensor_position_id"],
            [
                "strain_coil_pair.project_id",
                "strain_coil_pair.section_id",
                "strain_coil_pair.sensor_position_id",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        {"info": {"er_tags": ["readings", "continuous", "static_strain"]}},
    )

    # Relationships:
    strain_coil_pair_obj = relationship(
        "StrainCoilPair", back_populates="strain_reading_obj", lazy=True)
