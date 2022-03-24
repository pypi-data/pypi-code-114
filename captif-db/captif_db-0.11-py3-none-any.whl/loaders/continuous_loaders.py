from captif_db.logging import create_logger
from captif_db.db.models import (
    StrainReading,
    StrainCoilPair,
    TdrReading,
    TdrSensorPosition,
    PorePressureReading,
    PorePressureSensorPosition,
    SuctionReading,
    SuctionSensorPosition,
    TemperatureReading,
    TemperatureSensorPosition,
)

from .generic_loaders import ContinuousLoader


__all__ = [
    "ContinuousStrainLoader",
    "ContinuousTdrLoader",
    "ContinuousPorePressureLoader",
    "ContinuousSoilSuctionLoader",
    "ContinuousTemperatureLoader",
]

logger = create_logger(__name__)


class ContinuousStrainLoader(ContinuousLoader):
    reading_model = StrainReading
    sensor_position_model = StrainCoilPair

    raw_file_fields = [
        "date",
        "time",
        "lap_count",
        "sensor_position_id",
        "coil_spacing_mm",
    ]
    reading_fields = ["coil_spacing_mm"]

    def validate(self, df):
        is_valid = df["coil_spacing_mm"] > 0
        return df.loc[is_valid]


class ContinuousTdrLoader(ContinuousLoader):
    """
    Loader object for continuous TDR readings.

    """

    reading_model = TdrReading
    sensor_position_model = TdrSensorPosition

    raw_file_fields = [
        "date",
        "time",
        "lap_count",
        "sensor_position_id",
        "moisture_gwc",
        "raw_signal_microseconds",
    ]
    reading_fields = ["moisture_gwc", "raw_signal_microseconds"]

    def validate(self, df):
        is_valid = df["raw_signal_microseconds"].isna() | (
            df["raw_signal_microseconds"] < 1000
        )
        return df.loc[is_valid]


class ContinuousPorePressureLoader(ContinuousLoader):
    """
    Loader object for continuous pore pressure readings.

    """

    reading_model = PorePressureReading
    sensor_position_model = PorePressureSensorPosition

    raw_file_fields = [
        "date",
        "time",
        "lap_count",
        "sensor_position_id",
        "pore_pressure_kpa",
    ]
    reading_fields = ["pore_pressure_kpa"]


class ContinuousSoilSuctionLoader(ContinuousLoader):
    """
    Loader object for continuous soil suction readings.

    """

    reading_model = SuctionReading
    sensor_position_model = SuctionSensorPosition

    raw_file_fields = [
        "date",
        "time",
        "lap_count",
        "sensor_position_id",
        "raw_signal_volts",
    ]
    reading_fields = ["raw_signal_volts"]


class ContinuousTemperatureLoader(ContinuousLoader):
    """
    Loader object for continuous temperature readings.

    """

    reading_model = TemperatureReading
    sensor_position_model = TemperatureSensorPosition

    raw_file_fields = ["date", "time", "lap_count", "sensor_position_id", "temperature"]
    reading_fields = ["temperature"]
