from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Numeric, DateTime
from sqlalchemy.orm import relationship

from ..base import Table, Base


__all__ = [
    "TemperatureSensor",
    "TemperatureSensorPosition",
    "TemperatureReading",
]


class TemperatureSensor(Table, Base):
    """
    Temperature sensor details.

    :param id: index (required)
    :param manufacturer: sensor manufacturer
    :param model_no: sensor model number
    :param serial_no: sensor serial number

    :relationships: - temperature_sensor_position_obj (viewonly)

    """

    __tablename__ = "temperature_sensor"
    __index_column__ = ["id"]

    # Fields:
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(100), nullable=True)
    model_no = Column(String(100), nullable=True)
    serial_no = Column(String(100), nullable=True)

    # Relationships:
    temperature_sensor_position_obj = relationship(
        "TemperatureSensorPosition", back_populates="temperature_sensor_obj", lazy=True,
        viewonly=True
    )

    __table_args__ = ({"info": {"er_tags": ["readings", "continuous", "temperature"]}},)


class TemperatureSensorPosition(Table, Base):
    """
    Temperature sensor position.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param sensor_position_id: sensor position ID (required)
    :param sensor_id: sensor ID (required)
    :param station_no: station number
    :param relative_depth_mm: sensor depth relative to the position_description
    :param ram_position_cm: lateral position of sensor
    :param position_description: details of sensors position (e.g. subbase layer)
    :param lap_count: lap count when sensor was installed
    :param notes: notes

    :relationships: - section_obj
                    - temperature_sensor_obj
                    - reading_obj (viewonly)

    """

    __tablename__ = "temperature_sensor_position"
    __index_column__ = ["project_id", "section_id", "sensor_position_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    sensor_position_id = Column(String(20), primary_key=True)

    station_no = Column(Numeric(3, 1), nullable=True)
    sensor_id = Column(Integer, nullable=False)
    relative_depth_mm = Column(Integer, nullable=True)
    ram_position_cm = Column(Integer, nullable=True)
    position_description = Column(String(100), nullable=True)
    lap_count = Column(
        Integer, nullable=False, default=0, comment="lap count at installation"
    )
    notes = Column(String(200), nullable=True)

    # Relationships:
    section_obj = relationship(
        "Section", back_populates="temperature_sensor_position_obj", lazy=True)
    temperature_sensor_obj = relationship(
        "TemperatureSensor", back_populates="temperature_sensor_position_obj", lazy=True)
    reading_obj = relationship(
        "TemperatureReading", back_populates="temperature_sensor_position_obj", lazy=True,
        viewonly=True
    )

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id"], ["section.project_id", "section.section_id"],
        ),
        ForeignKeyConstraint(["sensor_id"], ["temperature_sensor.id"]),
        {"info": {"er_tags": ["readings", "continuous", "temperature"]}},
    )


class TemperatureReading(Table, Base):
    """
    Temperature reading.

    :param project_id: project ID (required)
    :param section_id: section ID (required)
    :param sensor_position_id: sensor position ID (required)
    :param reading_id: reading ID (required)
    :param datetime: datetime fo the reading (required)
    :param raw_signal_volts: uncalibrated reading (volts)
    :param temperature: calibrated reading (degC)

    :relationships: - temperature_sensor_position_obj

    """

    __tablename__ = "temperature_reading"
    __index_column__ = ["project_id", "section_id", "sensor_position_id", "reading_id"]

    # Fields:
    project_id = Column(Integer, primary_key=True)
    section_id = Column(String(1), primary_key=True)
    sensor_position_id = Column(String(20), primary_key=True)
    reading_id = Column(Integer, primary_key=True, autoincrement=True)

    datetime = Column(DateTime, nullable=False)
    raw_signal_volts = Column(Numeric(6, 4), nullable=True)
    temperature = Column(Numeric(4, 1), nullable=True)

    # Relationships:
    temperature_sensor_position_obj = relationship(
        "TemperatureSensorPosition", back_populates="reading_obj", lazy=True)

    # Foreign keys:
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id", "section_id", "sensor_position_id"],
            [
                "temperature_sensor_position.project_id",
                "temperature_sensor_position.section_id",
                "temperature_sensor_position.sensor_position_id",
            ],
        ),
        {"info": {"er_tags": ["readings", "continuous", "temperature"]}},
    )
