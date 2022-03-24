"""
In addition to providing some high level information about a project, these models act as
parent models for other models. They are primarily used to retrieve instances of other
models that relate to a particular project, section or station.

"""

from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Date, DateTime
from sqlalchemy.orm import relationship

from captif_db.helpers.models import objects_to_frame

from .base import Table, Base


__all__ = [
    "Project",
    "Section",
    "Station",
    "LapCount",
    "Interval",
]


class Project(Table, Base):
    """
    Project details.

    :param id: project ID (required)
    :param start_date: start date (begin construction) (required)
    :param end_date: end date (completion of loading)
    :param name: name (required)
    :param name_short: abbreviated name
    :param owner: owner/sponsor
    :param description: description

    :relationships: - section_obj
                    - station_obj
                    - lap_count_obj
                    - interval_obj

    """

    __tablename__ = "project"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True, autoincrement=False)
    start_date = Column(Date, nullable=False, comment="date track construction began")
    end_date = Column(Date, comment="date track removal began")
    name = Column(
        String(200), nullable=False, comment="as used in reporting (capitalised)"
    )
    name_short = Column(String(50))
    owner = Column(String(200), comment="project sponsor, partner (generally external)")
    description = Column(String(500), comment="experiment details")

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="project_obj", lazy="subquery", viewonly=True
    )
    station_obj = relationship(
        "Station",
        back_populates="project_obj",
        lazy="subquery",
        secondary="section",
        viewonly=True,
    )
    lap_count_obj = relationship(
        "LapCount", back_populates="project_obj", lazy=True, viewonly=True
    )
    interval_obj = relationship(
        "Interval", back_populates="project_obj", lazy=True, viewonly=True
    )

    __table_args__ = {
        "info": {
            "er_tags": [
                "track",
                "readings",
                "interval",
                "continuous",
                "static_strain",
                "pore_pressure",
                "moisture",
                "temperature",
                "suction",
                "deflection_beam",
                "surface_profiler",
                "texture_profiler",
            ]
        }
    }

    def __repr__(self):
        return f"Project(id={self.id}, start_date={self.start_date:%Y-%m-%d}, name={self.name})"

    def lap_count_df(self):
        return objects_to_frame(self.lap_count_obj)[
            ["datetime", "lap_count"]
        ].sort_values("datetime")


class Section(Table, Base):
    """
    Project section details.

    The test sections contain consistent pavement and surface designs across their
    length. They represent a single trial within the experiment matrix.

    :param project_id: project ID (required)
    :param section_id: section ID (required)

    :relationships: - project_obj
                    - station_obj
                    - basecourse_obj
                    - subbase_obj
                    - subgrade_obj
                    - surface_obj
                    - damage_obj
                    - repair_obj
                    - transmitter_strain_coil_obj
                    - receiver_strain_coil_obj
                    - strain_coil_pair_obj
                    - suction_sensor_position_obj
                    - pore_pressure_sensor_position_obj
                    - temperature_sensor_position_obj
                    - tdr_sensor_position_obj

    """

    __tablename__ = "section"
    __index_column__ = ["project_id", "section_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True, autoincrement=False)
    section_id = Column(String(1), primary_key=True, comment="use A, B, C, etc")

    # Relationships:
    project_obj = relationship("Project", back_populates="section_obj", lazy=True)
    station_obj = relationship(
        "Station", back_populates="section_obj", lazy=True, viewonly=True
    )

    basecourse_obj = relationship(
        "Basecourse", back_populates="section_obj", lazy=True, viewonly=True
    )
    subbase_obj = relationship(
        "Subbase", back_populates="section_obj", lazy=True, viewonly=True
    )
    subgrade_obj = relationship(
        "Subgrade", back_populates="section_obj", lazy=True, viewonly=True
    )
    surface_obj = relationship(
        "Surface", back_populates="section_obj", lazy=True, viewonly=True
    )
    damage_obj = relationship("Damage", lazy=True, secondary="station", viewonly=True)
    repair_obj = relationship("Repair", lazy=True, secondary="station", viewonly=True)

    transmitter_strain_coil_obj = relationship(
        "TransmitterStrainCoil", back_populates="section_obj", lazy=True, viewonly=True
    )
    receiver_strain_coil_obj = relationship(
        "ReceiverStrainCoil", back_populates="section_obj", lazy=True, viewonly=True
    )
    strain_coil_pair_obj = relationship(
        "StrainCoilPair", back_populates="section_obj", lazy=True, viewonly=True
    )
    suction_sensor_position_obj = relationship(
        "SuctionSensorPosition", back_populates="section_obj", lazy=True, viewonly=True
    )
    pore_pressure_sensor_position_obj = relationship(
        "PorePressureSensorPosition",
        back_populates="section_obj",
        lazy=True,
        viewonly=True,
    )
    temperature_sensor_position_obj = relationship(
        "TemperatureSensorPosition",
        back_populates="section_obj",
        lazy=True,
        viewonly=True,
    )
    tdr_sensor_position_obj = relationship(
        "TdrSensorPosition", back_populates="section_obj", lazy=True, viewonly=True
    )

    # dynamic_strain_reading_obj = relationship("DynamicStrainReading", lazy=True, viewonly=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        {
            "info": {
                "er_tags": [
                    "track",
                    "readings",
                    "interval",
                    "continuous",
                    "static_strain",
                    "pore_pressure",
                    "moisture",
                    "temperature",
                    "suction",
                    "deflection_beam",
                    "surface_profiler",
                    "texture_profiler",
                ]
            }
        },
    )

    def __repr__(self):
        return f"Section(project_id={self.project_id}, section_id={self.section_id})"


class Station(Table, Base):
    """
    Project station details.

    Interval readings are taken on discrete station marks. The stations are also used as
    a positioning reference for the in-track sensors and well as damage and repair areas.

    The table defines the valid station numbers for the project and the section ID that
    contains each station.

    :param project_id: project ID (required)
    :param station_no: station number (required)
    :param section_id: section ID (required)

    :relationships: - project_obj
                    - section_obj
                    - basecourse_obj
                    - subbase_obj
                    - subgrade_obj
                    - surface_obj
                    - repair_obj
                    - deflection_beam_reading_obj

    """

    __tablename__ = "station"
    __index_column__ = ["project_id", "station_no"]

    # Fields:
    project_id = Column(Integer, primary_key=True, autoincrement=False)
    station_no = Column(Integer, primary_key=True, autoincrement=False)
    section_id = Column(String(1), nullable=False)

    # Relationships:
    project_obj = relationship(
        "Project",
        back_populates="station_obj",
        lazy=True,
        secondary="section",
        viewonly=True,
    )
    section_obj = relationship("Section", back_populates="station_obj", lazy=True)

    basecourse_obj = relationship(
        "Basecourse",
        back_populates="station_obj",
        lazy=True,
        secondary="section",
        viewonly=True,
    )
    subbase_obj = relationship(
        "Subbase",
        back_populates="station_obj",
        lazy=True,
        secondary="section",
        viewonly=True,
    )
    subgrade_obj = relationship(
        "Subgrade",
        back_populates="station_obj",
        lazy=True,
        secondary="section",
        viewonly=True,
    )
    surface_obj = relationship(
        "Surface",
        back_populates="station_obj",
        lazy=True,
        secondary="section",
        viewonly=True,
    )
    damage_obj = relationship(
        "Damage", back_populates="station_obj", lazy=True, viewonly=True
    )
    repair_obj = relationship(
        "Repair", back_populates="station_obj", lazy=True, viewonly=True
    )

    deflection_beam_reading_obj = relationship(
        "DeflectionBeamReading", back_populates="station_obj", lazy=True, viewonly=True
    )
    surface_profiler_reading_obj = relationship(
        "SurfaceProfilerReading", back_populates="station_obj", lazy=True, viewonly=True
    )
    texture_profiler_reading_obj = relationship(
        "TextureProfilerReading", back_populates="station_obj", lazy=True, viewonly=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"],
            ["section.project_id", "section.section_id"],
        ),
        ForeignKeyConstraint(
            ["station_no"],
            ["station_reference.station_no"],
        ),
        {
            "info": {
                "er_tags": [
                    "track",
                    "readings",
                    "interval",
                    "deflection_beam",
                    "surface_profiler",
                    "texture_profiler",
                ]
            }
        },
    )

    def __repr__(self):
        return f"Station({self.station_no}, section_id={self.section_id})"


class LapCount(Table, Base):
    """
    Project lap count reading.

    :param id: index (required)
    :param project_id: project ID (required)
    :param datetime: datetime of the lap count reading (required)
    :param lap_count: lap count (required)
    :param position_cm: vehicle lateral position
    :param speed_kph: vehicle speed (km/h)

    :relationships: - project_obj

    """

    __tablename__ = "lap_count"
    __index_column__ = "id"

    # Fields:
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False)
    datetime = Column(DateTime, nullable=False)
    lap_count = Column(Integer, nullable=False)
    position_cm = Column(Integer, nullable=True, comment="rig wander position")
    speed_kph = Column(Integer, nullable=True, comment="rig speed (km/h)")

    # Relationships:
    project_obj = relationship("Project", back_populates="lap_count_obj", lazy=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        {"info": {"er_tags": ["readings", "continuous"]}},
    )

    def __repr__(self):
        return f"LapCount({self.lap_count}, {self.datetime})"


class Interval(Table, Base):
    """
    Project test interval.

    :param project_id: project ID (required)
    :param interval_id: interval ID (required)
    :param datetime: datetime of the start of the test interval (required)
    :param lap_count_nominal: nominal lap count

    :relationships: - project_obj
                    - deflection_beam_session_obj

    """

    __tablename__ = "interval"
    __index_column__ = ["project_id", "interval_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    interval_id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    lap_count_nominal = Column(Integer, nullable=True)

    # Relationships:
    project_obj = relationship("Project", back_populates="interval_obj", lazy=True)
    deflection_beam_session_obj = relationship(
        "DeflectionBeamSession", back_populates="interval_obj", lazy=True, viewonly=True
    )
    surface_profiler_session_obj = relationship(
        "SurfaceProfilerSession",
        back_populates="interval_obj",
        lazy=True,
        viewonly=True,
    )
    texture_profiler_session_obj = relationship(
        "TextureProfilerSession",
        back_populates="interval_obj",
        lazy=True,
        viewonly=True,
    )
    dynamic_strain_session_obj = relationship(
        "DynamicStrainSession", back_populates="interval_obj", lazy=True, viewonly=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        {
            "info": {
                "er_tags": [
                    "readings",
                    "interval",
                    "deflection_beam",
                    "surface_profiler",
                    "texture_profiler",
                ]
            }
        },
    )

    def __repr__(self):
        return (
            f"Interval({self.interval_id}, {self.datetime}, {self.lap_count_nominal})"
        )
