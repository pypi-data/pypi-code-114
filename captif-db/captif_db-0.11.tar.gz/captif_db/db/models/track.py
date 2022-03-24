"""
The track models are used to describe the state of the track for a specific project.

"""

from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship

from .base import Table, Base


__all__ = [
    "Basecourse",
    "Subbase",
    "Subgrade",
    "Surface",
    "Damage",
    "Repair",
]


class Basecourse(Table, Base):
    """
    Basecourse details for a specific section of the track.

    :param id: index (required)
    :param project_id: project ID (required)
    :param section_id: track section ID (required)
    :param lap_count: lap count at construction of the layer. Allows for additional layers to be constructed at some intermediate lap count (required)
    :param material: material description (required)
    :param thickness_mm: layer thickness (mm) (required)
    :param quality: construction quality description

    :relationships: - section_obj
                    - station_obj

    """

    __tablename__ = "basecourse"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    section_id = Column(String(1), nullable=False)
    lap_count = Column(Integer, nullable=False, comment="lap count at construction")
    material = Column(String(50), nullable=False)
    thickness_mm = Column(Integer, nullable=False)
    quality = Column(String(10))

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="basecourse_obj", lazy=True)
    station_obj = relationship(
        "Station", lazy=True, secondary="section", viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return (
            f"Basecourse({self.section_id}, {self.material}, {self.thickness_mm}mm, "
            f"lap_count={self.lap_count})"
        )


class Subbase(Table, Base):
    """
    Subbase details for a specific section of the track.

    :param id: index (required)
    :param project_id: project ID (required)
    :param section_id: track section ID (required)
    :param lap_count: lap count at construction of the layer. Allows for additional layers to be constructed at some intermediate lap count (required)
    :param material: material description (required)
    :param thickness_mm: layer thickness (mm) (required)
    :param quality: construction quality description

    :relationships: - section_obj
                    - station_obj

    """

    __tablename__ = "subbase"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    section_id = Column(String(1), nullable=False)
    lap_count = Column(Integer, nullable=False, comment="lap count at construction")
    material = Column(String(50), nullable=False)
    thickness_mm = Column(Integer, nullable=False)
    quality = Column(String(10))

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="subbase_obj", lazy=True)
    station_obj = relationship(
        "Station", lazy=True, secondary="section", viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return (
            f"Subbase({self.section_id}, {self.material}, {self.thickness_mm}mm, "
            f"lap_count={self.lap_count})"
        )


class Subgrade(Table, Base):
    """
    Subgrade details for a specific section of the track.

    :param id: index (required)
    :param project_id: project ID (required)
    :param section_id: track section ID (required)
    :param lap_count: lap count at construction of the layer. Allows for additional layers to be constructed at some intermediate lap count (required)
    :param material: material description (required)
    :param thickness_mm: layer thickness (mm) (required)
    :param cbr: target CBR value
    :param target_moisture: target moisture content (GWC, %)

    :relationships: - section_obj
                    - station_obj

    """

    __tablename__ = "subgrade"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    section_id = Column(String(1), nullable=False)
    lap_count = Column(Integer, nullable=False, comment="lap count at construction")
    material = Column(String(50), nullable=False)
    thickness_mm = Column(Integer, nullable=False)
    cbr = Column(Integer)
    target_moisture = Column(Integer)

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="subgrade_obj", lazy=True)
    station_obj = relationship(
        "Station", lazy=True, secondary="section", viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return (
            f"Subgrade({self.section_id}, {self.material}, {self.thickness_mm}mm, "
            f"lap_count={self.lap_count})"
        )


class Surface(Table, Base):
    """
    Surface details for a specific section of the track.

    :param id: index (required)
    :param project_id: project ID (required)
    :param section_id: track section ID (required)
    :param lap_count: lap count at construction of the layer. Allows for additional layers to be constructed at some intermediate lap count (required)
    :param material: material description (required)
    :param thickness_mm: layer thickness (mm)
    :param notes: notes

    :relationships: - section_obj
                    - station_obj

    """

    __tablename__ = "surface"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    section_id = Column(String(1), nullable=False)
    lap_count = Column(Integer, nullable=False, comment="lap count at construction")
    date = Column(
        Date,
        nullable=False,
        comment="needed to sort surfaces when multiple constructed at the same lap count",
    )
    material = Column(String(50), nullable=False)
    thickness_mm = Column(Integer, comment="not necessary for chipseals")
    notes = Column(String(200), nullable=True)

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="surface_obj", lazy=True)
    station_obj = relationship(
        "Station", lazy=True, secondary="section", viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return (
            f"Surface({self.section_id}, {self.material}, lap_count={self.lap_count})"
        )


class Damage(Table, Base):
    """
    Details of damage. Entries should be limited to major failures that could
    affect the results of deflection and surface profile readings (e.g. blowouts,
    potholes, heaving requiring repair).

    :param id: index (required)
    :param project_id: project ID (required)
    :param station_no: track station number (required)
    :param lap_count: lap count when damage observed (required)
    :param damage_type: description of damage (required)
    :param notes: notes

    :relationships: - station_obj

    """

    __tablename__ = "damage"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    station_no = Column(Integer, nullable=False)
    lap_count = Column(
        Integer,
        nullable=False,
        comment="lap count (test interval) when damage observed",
    )
    damage_type = Column(String(20), nullable=False, comment="blowout, pothole, etc")
    notes = Column(String(200))

    # Relationships:
    station_obj = relationship(
        "Station", back_populates="damage_obj", lazy=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "station_no"], ["station.project_id", "station.station_no"],
        ),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return (
            f"Damage({self.station_no}, {self.damage_type}, lap_count={self.lap_count})"
        )


class Repair(Table, Base):
    """
    Details of repairs. Generally in response to damage, but may extend beyond the damaged area.

    :param id: index (required)
    :param project_id: project ID (required)
    :param station_no: track station number (required)
    :param lap_count: lap count when repair made (required)
    :param material: material used for repair (e.g. AC10) (required)
    :param thickness_mm: repair thickness (mm)
    :param width: width description (i.e. "wheel track", "full width") (required)
    :param notes: notes

    :relationships: - station_obj

    """

    __tablename__ = "repair"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, comment="index")
    project_id = Column(Integer, nullable=False)
    station_no = Column(Integer, nullable=False)
    lap_count = Column(
        Integer,
        nullable=False,
        comment="lap count (test interval) when repair performed",
    )
    date = Column(Date, nullable=False, comment="repair date")
    material = Column(String(20), nullable=False, comment="e.g AC10")
    thickness_mm = Column(Integer, comment="depth of repair")
    width = Column(String(20), nullable=False, comment="wheel track, full width")
    notes = Column(String(200))

    # Relationships:
    station_obj = relationship(
        "Station", back_populates="repair_obj", lazy=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "station_no"], ["station.project_id", "station.station_no"],
        ),
        ForeignKeyConstraint(["width"], ["repair_width_reference.width"],),
        {"info": {"er_tags": ["track"]}},
    )

    def __repr__(self):
        return f"Repair({self.station_no}, {self.material}, lap_count={self.lap_count})"
