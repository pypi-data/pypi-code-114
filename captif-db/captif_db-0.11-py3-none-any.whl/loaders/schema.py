from typing import List
from schema import Schema, Optional
from datetime import date, datetime
from pydantic import BaseModel, root_validator


project_info_schema = Schema(
    {
        "id": int,
        "name": str,
        "name_short": str,
        "start_date": date,
        Optional("end_date"): date,
        Optional("owner"): str,
        Optional("description"): str,
    }
)

section_info_schema = Schema(
    {
        "section_id": str,
        "start_station": int,
        "end_station": int,
    }
)

basecourse_schema = Schema(
    {
        "lap_count": int,
        "material": str,
        "thickness_mm": int,
        Optional("quality"): str,
    }
)

subbase_schema = Schema(
    {
        "lap_count": int,
        "material": str,
        "thickness_mm": int,
        Optional("quality"): str,
    }
)

subgrade_schema = Schema(
    {
        "lap_count": int,
        "material": str,
        "thickness_mm": int,
        Optional("cbr"): int,
        Optional("target_moisture"): int,
    }
)

surface_schema = Schema(
    {
        "lap_count": int,
        Optional("date"): date,
        "material": str,
        Optional("thickness_mm"): int,
        Optional("notes"): str,
    }
)

section_schema = Schema(
    {
        "info": section_info_schema,
        Optional("basecourse", default=[]): [basecourse_schema],
        Optional("subbase", default=[]): [subbase_schema],
        Optional("subgrade", default=[]): [subgrade_schema],
        Optional("surface", default=[]): [surface_schema],
    }
)


project_config_schema = Schema(
    {
        "project": project_info_schema,
        "section": [section_schema],
    }
)


interval_schema = Schema(
    {
        "interval_id": int,
        "datetime": datetime,
        "lap_count_nominal": int,
    }
)


deflection_beam_session_schema = Schema(
    {
        "filename": str,
        "session": {
            "session_id": int,
            "track_condition": str,
            "load_kn": int,
            "deflection_beam_name": str,
            "deflection_beam_version_no": int,
            Optional("notes"): str,
            Optional("file"): str,
        },
    }
)


surface_profiler_schema = Schema(
    {
        "filename": {
            "reading_filename": str,
            "profile_trace_filename": str,
        },
        "session": {
            "session_id": int,
            "track_condition": str,
            "surface_profiler_name": str,
            "surface_profiler_version_no": int,
            Optional("notes"): str,
            Optional("file"): str,
        },
        Optional("control"): {
            "station_no": int,
        },
    }
)


texture_profiler_schema = Schema(
    {
        "session": {
            "session_id": int,
            "track_condition": str,
            "texture_profiler_name": str,
            "texture_profiler_version_no": int,
            Optional("notes"): str,
        },
    }
)


dynamic_strain_schema = Schema(
    {
        "session": {
            "session_id": int,
            "track_condition": str,
            "track_moisture": str,
            "trigger_method": str,
            "load_kn": int,
        },
    }
)


def fields(schema):
    fields = []
    for ff in schema.schema.keys():
        if isinstance(ff, str):
            fields.append(ff)
        elif isinstance(ff.schema, str):
            fields.append(ff.schema)
    return fields


class TextureProfilerLoaderInputData(BaseModel):
    folder: str
    filename: str
    station_no: int
    datetime: datetime
    mpd: float
    stdev: float
    valid_segments: int
    proportion_valid_segments: float
    is_valid: bool
    trace: List[dict]

    @root_validator
    def convert_field_names(cls, values):
        values["station_no"] = values.pop("file_number")
        values["mpd"] = values.pop("mean")
        return values
