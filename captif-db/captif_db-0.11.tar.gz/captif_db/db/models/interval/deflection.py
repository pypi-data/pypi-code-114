"""
The deflection beam models are used to describe the deflection beam instruments and
associated measurements.

"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKeyConstraint,
    Float,
    DateTime,
    Numeric,
)
from sqlalchemy.orm import relationship

from ..base import Table, Base


__all__ = [
    "DeflectionBeamType",
    "DeflectionBeam",
    "DeflectionBeamVersion",
    "DeflectionBeamSession",
    "DeflectionBeamReading",
    "DeflectionBeamTrace",
]


class DeflectionBeamType(Table, Base):
    """
    Deflection beam type.

    :param deflection_beam_type: type of deflection beam (e.g. electronic benkelman beam)
        (required)

    :relationships: - deflection_beam_obj (viewonly)

    """

    __tablename__ = "deflection_beam_type"
    __index_column__ = "deflection_beam_type"

    # Fields:
    deflection_beam_type = Column(String(50), primary_key=True)

    # Relationships:
    deflection_beam_obj = relationship(
        "DeflectionBeam", back_populates="deflection_beam_type_obj", lazy=True, viewonly=True)

    __table_args__ = (
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )


class DeflectionBeam(Table, Base):
    """
    Deflection beam instrument details.

    :param name: deflection beam instrument name (e.g. CAPTIF electronic benkelman beam)
        (required)
    :param deflection_beam_type: type of deflection beam (required)

    :relationships: - deflection_beam_type_obj
                    - deflection_beam_version_obj (viewonly)
                    - session_obj (viewonly)

    """

    __tablename__ = "deflection_beam"
    __index_column__ = "name"

    name = Column(String(50), primary_key=True)
    deflection_beam_type = Column(String(50), nullable=False)

    # Relationships:
    deflection_beam_type_obj = relationship(
        "DeflectionBeamType", back_populates="deflection_beam_obj", lazy=True)
    deflection_beam_version_obj = relationship(
        "DeflectionBeamVersion", back_populates="deflection_beam_obj", lazy=True, viewonly=True)
    session_obj = relationship(
        "DeflectionBeamSession", lazy=True, secondary="deflection_beam_version", viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["deflection_beam_type"], ["deflection_beam_type.deflection_beam_type"],
        ),
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )


class DeflectionBeamVersion(Table, Base):
    """
    Deflection beam instrument version details.

    Used to track changes to the instrument following identification of faults or general
    improvements.

    :param deflection_beam_name: deflection beam instrument name (required)
    :param version_no: version number (required)
    :param version_details: details of changes from the previous version (required)
    :param version_notes: additional notes
    :param deflection_beam_correction_multiplier: correction factor that should be
        applied to raw deflection readings (default: 1.0)

    :relationships: - deflection_beam_obj
                    - session_obj (viewonly)

    """

    __tablename__ = "deflection_beam_version"
    __index_column__ = ["deflection_beam_name", "version_no"]

    deflection_beam_name = Column(String(50), primary_key=True)
    version_no = Column(Integer, primary_key=True)
    version_details = Column(String(100), nullable=False)
    version_notes = Column(String(200))
    deflection_correction_multiplier = Column(Float, nullable=False, default=1.0)

    # Relationships:
    deflection_beam_obj = relationship(
        "DeflectionBeam", back_populates="deflection_beam_version_obj", lazy=True)
    session_obj = relationship(
        "DeflectionBeamSession", back_populates="deflection_beam_version_obj", lazy=True,
        viewonly=True,
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["deflection_beam_name"], ["deflection_beam.name"], onupdate="CASCADE",
        ),
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )


class DeflectionBeamSession(Table, Base):
    """
    Deflection beam testing session.

    :param project_id: project ID (required)
    :param interval_id: interval ID (required)
    :param session_id: measurement session ID (required)
    :param track_condition: track condition during measurements (i.e. "before
        repair/surfacing (if any)" or "after repair/surfacing") (required)
    :param load_kn: vehicle load during measurements (required)
    :param datetime: datetime of start of measurement session (required)
    :param deflection_beam_name: deflection beam name (required)
    :param deflection_beam_version_no: version number (required)
    :param file: measurement file reference
    :param notes: general notes, purpose of measurement session

    :relationships: - track_condition_obj
                    - interval_obj
                    - deflection_beam_obj (viewonly)
                    - deflection_beam_version_obj
                    - reading_obj (viewonly)

    """

    __tablename__ = "deflection_beam_session"
    __index_column__ = ["project_id", "interval_id", "session_id"]

    project_id = Column(Integer, primary_key=True)
    interval_id = Column(Integer, primary_key=True)
    session_id = Column(Integer, primary_key=True)
    track_condition = Column(String(50), nullable=False)
    load_kn = Column(Integer, nullable=False)
    datetime = Column(
        DateTime,
        nullable=False,
        comment="datetime of start of measurement session (used to determine lap_count)",
    )
    deflection_beam_name = Column(String(50), nullable=False)
    deflection_beam_version_no = Column(Integer, nullable=False)
    file = Column(String(100))
    notes = Column(String(200))

    # Relationships:
    track_condition_obj = relationship("TrackConditionReference", lazy=True)
    interval_obj = relationship(
        "Interval", back_populates="deflection_beam_session_obj", lazy=True)
    deflection_beam_obj = relationship(
        "DeflectionBeam", lazy=True, secondary="deflection_beam_version", uselist=False,
        viewonly=True,
    )
    deflection_beam_version_obj = relationship(
        "DeflectionBeamVersion", back_populates="session_obj", lazy=True)
    reading_obj = relationship(
        "DeflectionBeamReading", back_populates="session_obj", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "interval_id"],
            ["interval.project_id", "interval.interval_id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        ForeignKeyConstraint(
            ["track_condition"], ["track_condition_reference.track_condition"],
        ),
        ForeignKeyConstraint(
            ["deflection_beam_name", "deflection_beam_version_no"],
            [
                "deflection_beam_version.deflection_beam_name",
                "deflection_beam_version.version_no",
            ],
            onupdate="CASCADE",
        ),
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )


class DeflectionBeamReading(Table, Base):
    """
    Deflection beam reading.

    :param id: index
    :param project_id: project ID (required)
    :param interval_id: interval ID (required)
    :param session_id: measurement session ID (required)
    :param session_reading_no: session reading number (required)
    :param station_no: station number
    :param datetime: datetime of reading (required)
    :param raw_max_deflection_mm: raw maximum deflection (mm) during reading (required)

    :relationships: - station_obj (viewonly)
                    - session_obj
                    - trace_obj (viewonly)

    """

    __tablename__ = "deflection_beam_reading"
    __index_column__ = "id"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    interval_id = Column(Integer, nullable=False)
    session_id = Column(Integer, nullable=False)
    session_reading_no = Column(Integer, nullable=False)
    station_no = Column(Integer, nullable=False)
    datetime = Column(DateTime, nullable=False)
    raw_max_deflection_mm = Column(Numeric(6, 4), nullable=False)

    # Relationships:
    station_obj = relationship(
        "Station", back_populates="deflection_beam_reading_obj", lazy=True, viewonly=True)
    session_obj = relationship(
        "DeflectionBeamSession", back_populates="reading_obj", lazy=True)
    trace_obj = relationship(
        "DeflectionBeamTrace", back_populates="reading_obj", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "interval_id", "session_id"],
            [
                "deflection_beam_session.project_id",
                "deflection_beam_session.interval_id",
                "deflection_beam_session.session_id",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        ForeignKeyConstraint(
            ["project_id", "station_no"], ["station.project_id", "station.station_no"],
        ),
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )


class DeflectionBeamTrace(Table, Base):
    """
    Deflection beam reading trace value.

    :param reading_id: deflection beam reading ID (required)
    :param distance_m: position of vehicle (m) (required)
    :param raw_deflection_mm: raw deflection (mm) at specified vehicle position (required)

    :relationships: - reading_obj

    """

    __tablename__ = "deflection_beam_trace"
    __index_column__ = ["reading_id", "distance_m"]

    reading_id = Column(Integer, primary_key=True)
    distance_m = Column(Numeric(6, 4), primary_key=True)
    raw_deflection_mm = Column(Numeric(6, 4), nullable=False)

    # Relationships:
    reading_obj = relationship(
        "DeflectionBeamReading", back_populates="trace_obj", lazy=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["reading_id"], ["deflection_beam_reading.id"], ondelete="CASCADE"
        ),
        {"info": {"er_tags": ["readings", "interval", "deflection_beam"]}},
    )
