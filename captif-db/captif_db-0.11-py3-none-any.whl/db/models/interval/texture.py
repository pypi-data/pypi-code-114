"""
The texture profile models are used to describe the texture profiler instruments and
associated measurements.
"""

from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from ..base import Table, Base


__all__ = [
    "TextureProfilerType",
    "TextureProfiler",
    "TextureProfilerVersion",
    "TextureProfilerSession",
    "TextureProfilerReading",
    "TextureProfilerTrace",
]


class TextureProfilerType(Table, Base):
    """
    Texture profiler type.

    :param texture_profiler_type: type of texture profiler (e.g. stationary laser
        profiler) (required)

    :relationships: - texture_profiler_obj (viewonly)

    """

    __tablename__ = "texture_profiler_type"
    __index_column__ = "texture_profiler_type"

    texture_profiler_type = Column(String(50), primary_key=True)

    # Relationships:
    texture_profiler_obj = relationship(
        "TextureProfiler",
        back_populates="texture_profiler_type_obj",
        lazy=True,
        viewonly=True,
    )

    __table_args__ = (
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )


class TextureProfiler(Table, Base):
    """
    Texture profiler instrument details.

    :param name: texture profiler instrument name (e.g. CAPTIF SLP) (required)
    :param texture_profiler_type: type of texture profiler (required)

    :relationships: - texture_profiler_type_obj
                    - texture_profiler_version_obj (viewonly)

    """

    __tablename__ = "texture_profiler"
    __index_column__ = "name"

    name = Column(String(50), primary_key=True)
    texture_profiler_type = Column(String(50), nullable=False)

    # Relationships:
    texture_profiler_type_obj = relationship(
        "TextureProfilerType", back_populates="texture_profiler_obj", lazy=True
    )
    texture_profiler_version_obj = relationship(
        "TextureProfilerVersion",
        back_populates="texture_profiler_obj",
        lazy=True,
        viewonly=True,
    )
    session_obj = relationship(
        "TextureProfilerSession",
        lazy=True,
        secondary="texture_profiler_version",
        viewonly=True,
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["texture_profiler_type"],
            ["texture_profiler_type.texture_profiler_type"],
        ),
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )


class TextureProfilerVersion(Table, Base):
    """
    Texture profiler instrument version details.

    Used to track changes to the instrument following identification of faults or general
    improvements.

    :param texture_profiler_name: texture profiler instrument name (required)
    :param version_no: version number (required)
    :param version_details: details of changes from the previous version (required)
    :param version_notes: additional notes

    :relationships: - texture_profiler_obj

    """

    __tablename__ = "texture_profiler_version"
    __index_column__ = ["texture_profiler_name", "version_no"]

    texture_profiler_name = Column(String(50), primary_key=True)
    version_no = Column(Integer, primary_key=True)
    version_details = Column(String(100), nullable=False)
    version_notes = Column(String(200))

    # Relationships:
    texture_profiler_obj = relationship(
        "TextureProfiler", back_populates="texture_profiler_version_obj", lazy=True
    )
    session_obj = relationship(
        "TextureProfilerSession",
        back_populates="texture_profiler_version_obj",
        lazy=True,
        viewonly=True,
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["texture_profiler_name"],
            ["texture_profiler.name"],
            onupdate="CASCADE",
        ),
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )


class TextureProfilerSession(Table, Base):
    """
    Texture profile testing session.

    :param project_id: project ID (required)
    :param interval_id: interval ID (required)
    :param session_id: measurement session ID (required)
    :param track_condition: track condition during measurements (i.e. "before
        repair/surfacing (if any)" or "after repair/surfacing") (required)
    :param datetime: datetime of start of measurement session (required)
    :param texture_profiler_name: surface profiler name (required)
    :param texture_profiler_version_no: version number (required)
    :param file: measurement file reference
    :param notes: general notes, purpose of measurement session

    :relationships: - track_condition_obj
                    - interval_obj
                    - texture_profiler_obj (viewonly)
                    - texture_profiler_version_obj
                    - reading_obj (viewonly)

    """

    __tablename__ = "texture_profiler_session"
    __index_column__ = ["project_id", "interval_id", "session_id"]

    project_id = Column(Integer, primary_key=True)
    interval_id = Column(Integer, primary_key=True)
    session_id = Column(Integer, primary_key=True)
    track_condition = Column(String(50), nullable=False)
    datetime = Column(
        DateTime,
        nullable=False,
        comment="datetime of start of measurement session (used to determine lap_count)",
    )
    texture_profiler_name = Column(String(50), nullable=False)
    texture_profiler_version_no = Column(Integer, nullable=False)
    file = Column(String(100))
    notes = Column(String(200))

    # Relationships:
    track_condition_obj = relationship("TrackConditionReference", lazy=True)
    interval_obj = relationship(
        "Interval", back_populates="texture_profiler_session_obj", lazy=True
    )
    texture_profiler_obj = relationship(
        "TextureProfiler",
        lazy=True,
        secondary="texture_profiler_version",
        uselist=False,
        viewonly=True,
    )
    texture_profiler_version_obj = relationship(
        "TextureProfilerVersion", back_populates="session_obj", lazy=True
    )
    reading_obj = relationship(
        "TextureProfilerReading", back_populates="session_obj", lazy=True, viewonly=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "interval_id"],
            ["interval.project_id", "interval.interval_id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        ForeignKeyConstraint(
            ["track_condition"],
            ["track_condition_reference.track_condition"],
        ),
        ForeignKeyConstraint(
            ["texture_profiler_name", "texture_profiler_version_no"],
            [
                "texture_profiler_version.texture_profiler_name",
                "texture_profiler_version.version_no",
            ],
            onupdate="CASCADE",
        ),
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )


class TextureProfilerReading(Table, Base):
    """
    Texture profiler reading.

    :param id: index
    :param project_id: project ID (required)
    :param interval_id: interval ID (required)
    :param session_id: measurement session ID (required)
    :param session_reading_no: session reading number (required)
    :param station_no: station number
    :param datetime: datetime of reading (required)
    :param mpd: mean profile depth (mm), only reported in enough valid segments
    :param stdev: standard deviation of MSD values (mm), only reported in enough valid
           segments
    :param proportion_valid_segments: proportion of segments that are valid (between
           0 and 1. Only valid segments can be used to calculate MPD and the standard
           deviation, and at least 50% of the segments must be valid.

    :relationships: - station_obj (viewonly)
                    - session_obj
                    - trace_obj (viewonly)

    """

    __tablename__ = "texture_profiler_reading"
    __index_column__ = "id"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    interval_id = Column(Integer, nullable=False)
    session_id = Column(Integer, nullable=False)
    session_reading_no = Column(Integer, nullable=False)
    station_no = Column(Integer, nullable=False)
    datetime = Column(DateTime, nullable=False)
    mpd = Column(Numeric(5, 3), nullable=False)
    stdev = Column(Numeric(5, 3), nullable=False)
    valid_segments = Column(Integer, nullable=False)
    proportion_valid_segments = Column(Numeric(4, 3), nullable=False)
    is_valid = Column(Boolean, nullable=False)

    # Relationships:
    station_obj = relationship(
        "Station",
        back_populates="texture_profiler_reading_obj",
        lazy=True,
        viewonly=True,
    )
    session_obj = relationship(
        "TextureProfilerSession", back_populates="reading_obj", lazy=True
    )
    trace_obj = relationship(
        "TextureProfilerTrace", back_populates="reading_obj", lazy=True, viewonly=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "interval_id", "session_id"],
            [
                "texture_profiler_session.project_id",
                "texture_profiler_session.interval_id",
                "texture_profiler_session.session_id",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        ForeignKeyConstraint(
            ["project_id", "station_no"],
            ["station.project_id", "station.station_no"],
        ),
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )


class TextureProfilerTrace(Table, Base):
    """
    Texture profiler reading trace value.

    :param reading_id: texture profiler reading ID (required)
    :param distance_mm: position of the profiler (mm) (required)
    :param relative_height_mm: height of the surface relative to the datum (mm) (required)

    :relationships: - reading_obj

    """

    __tablename__ = "texture_profiler_trace"
    __index_column__ = ["reading_id", "distance_mm"]

    reading_id = Column(Integer, primary_key=True)
    distance_mm = Column(Numeric(7, 3), primary_key=True)
    relative_height_mm = Column(Numeric(6, 3), nullable=False)

    # Relationships:
    reading_obj = relationship(
        "TextureProfilerReading", back_populates="trace_obj", lazy=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["reading_id"], ["texture_profiler_reading.id"], ondelete="CASCADE"
        ),
        {"info": {"er_tags": ["readings", "interval", "texture_profiler"]}},
    )
