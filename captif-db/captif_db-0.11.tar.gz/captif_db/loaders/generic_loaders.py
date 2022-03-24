import toml
import pandas as pd
from functools import lru_cache

from captif_db.db.models import Interval
from captif_db.logging import create_logger
from captif_db.helpers.parse_datetime import to_datetime
from captif_db.helpers.file_operations import find_file, abs_directory

from .helpers import max_station
from .schema import (
    project_config_schema,
    interval_schema,
    deflection_beam_session_schema,
    surface_profiler_schema,
    texture_profiler_schema,
    dynamic_strain_schema,
)


logger = create_logger(__name__)


class Loader:
    def __init__(self, path):
        project_info = self.load_project_info(path)

        if project_info is None:
            logger.error("could not load project.toml from file tree")
            return None

        self.project_id = project_info["project"]["id"]
        self.raw_readings = self.load_raw(path)

    def load_raw(self, path):
        return None

    def validate(self, df):
        return df

    @staticmethod
    @lru_cache(maxsize=1)
    def load_project_info(path):
        try:
            project_toml_path = find_file(path, "project.toml")
            project_toml = toml.load(project_toml_path)

        except TypeError:
            return None

        return project_config_schema.validate(project_toml)

    @staticmethod
    def combine_date_time(df):
        df["datetime"] = df["date"].apply(to_datetime) + df["time"].apply(to_datetime)
        return df.drop(columns=["date", "time"])


class ContinuousLoader(Loader):
    reading_model = None
    sensor_position_model = None

    raw_file_fields = []
    reading_fields = []

    def load_raw(self, path):
        df = pd.read_csv(path, skiprows=1, sep="\t", names=self.raw_file_fields)
        df = self.combine_date_time(df)

        df.drop_duplicates(["sensor_position_id", "datetime"], inplace=True)

        df["project_id"] = self.project_id  # Append project_id column
        df = df.where(pd.notnull(df), None)  # Convert NaN to None

        return self.validate(df)

    def upload(self, db_session):
        # Append the section_id based on project_id and sensor_position_id:
        raw_readings = self.append_section_id(self.raw_readings, db_session)

        for (section_id, sensor_position_id), readings in raw_readings.groupby(
            ["section_id", "sensor_position_id"]
        ):
            sensor_position_key = {
                "project_id": self.project_id,
                "section_id": section_id,
                "sensor_position_id": sensor_position_id,
            }

            new_readings, next_reading_id = self.new_readings(
                db_session, readings, **sensor_position_key
            )

            if self.sensor_position_invalid(db_session, **sensor_position_key):
                logger.info(
                    f"sensor_position_id={sensor_position_id} not found. Skipping "
                    f"{len(new_readings)} affected rows."
                )
                continue

            logger.info(
                f"adding {len(new_readings)} rows for sensor_position_id={sensor_position_id}"
            )

            for _, row in new_readings.iterrows():
                db_session.add(
                    self.reading_model(
                        **sensor_position_key,
                        reading_id=next_reading_id,
                        datetime=row["datetime"].to_pydatetime(),
                        **{ff: row[ff] for ff in self.reading_fields},
                    )
                )
                next_reading_id += 1

        db_session.commit()

    @classmethod
    def latest_reading_details(cls, db_session, **kwargs):
        reading = (
            db_session.query(cls.reading_model)
            .filter_by(**kwargs)
            .order_by(cls.reading_model.datetime.desc())
            .first()
        )
        if reading is None:
            return None, 1
        return reading.datetime, reading.reading_id + 1

    @classmethod
    def new_readings(cls, db_session, readings, **kwargs):
        last_reading_datetime, next_reading_id = cls.latest_reading_details(
            db_session,
            **kwargs,
        )

        if last_reading_datetime:
            return (
                readings.loc[readings["datetime"] > last_reading_datetime],
                next_reading_id,
            )

        return readings, next_reading_id

    @classmethod
    def sensor_position_invalid(cls, db_session, **kwargs):
        sensor_position = (
            db_session.query(cls.sensor_position_model).filter_by(**kwargs).first()
        )
        return sensor_position is None

    @classmethod
    def append_section_id(cls, df, db_session):
        sensor_positions = cls.sensor_position_model.read_table(db_session)

        section_mapper = pd.DataFrame.from_records(
            sensor_positions.index, columns=sensor_positions.index.names
        ).set_index(["project_id", "sensor_position_id"])

        return df.join(section_mapper, on=["project_id", "sensor_position_id"])


class IntervalLoader(Loader):
    session_model = None
    reading_model = None
    trace_model = None

    reading_fields = []

    def __init__(self, directory):
        """
        directory: str or Path
            Path of directory containing the raw data files. Filenames will be ignored.
        """

        self.path = abs_directory(directory)

        self.project_info = self.load_project_info(self.path)
        if self.project_info is None:
            raise ValueError("could not load project.toml from file tree")

        self.project_id = self.project_info["project"]["id"]
        self.interval_info = self.load_interval_info(self.path)
        self.session_info = self.load_session_info(self.path)

        self.load_raw()

        self.interval_obj = None
        self.session_obj = None
        self.session_exists = False

    @staticmethod
    @lru_cache(maxsize=1)
    def load_interval_info(path):
        info = interval_schema.validate(toml.load(find_file(path, "interval.toml")))
        info["project_id"] = IntervalLoader.load_project_info(path)["project"]["id"]
        return info

    @staticmethod
    def session_schema(session_type):
        if session_type == "deflection_beam_session":
            return deflection_beam_session_schema
        if session_type == "surface_profiler_session":
            return surface_profiler_schema
        if session_type == "texture_profiler_session":
            return texture_profiler_schema
        if session_type == "dynamic_strain_session":
            return dynamic_strain_schema
        return None

    @staticmethod
    @lru_cache(maxsize=1)
    def load_session_info(path):
        path = find_file(path, "session.toml")

        if path is None:
            return None

        session_type = path.stem
        schema = IntervalLoader.session_schema(session_type)
        if schema is None:
            return None

        info = schema.validate(toml.load(path))
        interval = IntervalLoader.load_interval_info(path)

        info["session"]["project_id"] = interval["project_id"]
        info["session"]["interval_id"] = interval["interval_id"]

        return info

    def load_raw(self):
        pass

    def upload(self, db_session):
        self.upload_interval(db_session)
        self.upload_session(db_session)
        if not self.session_exists:
            self.upload_readings(db_session)

    def upload_interval(self, db_session):
        self.interval_obj = Interval(**self.interval_info)
        query = db_session.query(Interval.project_id, Interval.interval_id).filter_by(
            project_id=self.interval_info["project_id"],
            interval_id=self.interval_info["interval_id"],
        )
        if query.scalar() is None:
            db_session.add(self.interval_obj)
            db_session.commit()
        else:
            self.interval_obj = query.one()

    def upload_session(self, db_session):
        self.session_obj = self.session_model(**self.session_info["session"])
        query = db_session.query(self.session_model).filter_by(
            project_id=self.session_info["session"]["project_id"],
            interval_id=self.session_info["session"]["interval_id"],
            session_id=self.session_info["session"]["session_id"],
        )
        if query.scalar() is None:
            db_session.add(self.session_obj)
            db_session.commit()
        else:
            self.session_obj = query.one()
            self.session_exists = True

    def upload_readings(self, db_session):
        for reading, traces in self.build_readings(db_session):
            db_session.add(reading)
            db_session.add_all(traces)
            db_session.flush()
        db_session.commit()

    def build_readings(self, db_session):
        for session_reading_no, row in self.raw_readings.iterrows():
            if row["station_no"] is not None:
                if row["station_no"] > max_station(db_session, self.project_id):
                    continue

            reading = self.reading_model(
                session_obj=self.session_obj,
                station_no=row["station_no"],
                datetime=row["datetime"].to_pydatetime(),
                session_reading_no=session_reading_no,
                **{ff: row[ff] for ff in row.index if ff in self.reading_fields},
            )

            traces = self.build_reading_traces(reading, row["trace"])

            yield reading, traces

    def build_reading_traces(self, reading_obj, trace_points):
        return (self.trace_model(reading_obj=reading_obj, **pp) for pp in trace_points)


class StationIntervalLoader(IntervalLoader):
    pass


class DynamicIntervalLoader(IntervalLoader):
    def build_readings(self, db_session):
        for _, row in self.raw_readings.iterrows():
            reading = self.reading_model(
                session_obj=self.session_obj,
                section_id=row["section_id"],
                sensor_position_id=row["sensor_position_id"],
                datetime=row["datetime"].to_pydatetime(),
                **{ff: row[ff] for ff in row.index if ff in self.reading_fields},
            )

            traces = self.build_reading_traces(reading, row["trace"])

            yield reading, traces

    @classmethod
    def append_section_id(cls, df, db_session):
        sensor_positions = cls.sensor_position_model.read_table(db_session)

        section_mapper = pd.DataFrame.from_records(
            sensor_positions.index, columns=sensor_positions.index.names
        ).set_index(["project_id", "sensor_position_id"])

        return df.join(section_mapper, on=["project_id", "sensor_position_id"])

    def upload(self, db_session):
        self.raw_readings = self.append_section_id(self.raw_readings, db_session)
        return super().upload(db_session)
