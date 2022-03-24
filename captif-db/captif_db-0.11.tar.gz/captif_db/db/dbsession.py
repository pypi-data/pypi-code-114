from sqlalchemy import event
from captif_db_config import DbSession as BaseDbSession

from .models.base import Base
from .models.reference import (
    StationReference,
    RepairWidthReference,
    StrainCoilPairDirectionReference,
    StrainCoilPositionReference,
    TrackConditionReference,
    TrackMoistureReference,
    TriggerMethodReference,
)
from .constants import (
    DATABASE,
    REPAIR_WIDTH_VALUES,
    STRAIN_COIL_PAIR_DIRECTION_VALUES,
    STRAIN_COIL_POSITION_VALUES,
    TRACK_CONDITION_VALUES,
    TRACK_MOISTURE_VALUES,
    TRIGGER_METHOD_VALUES,
)


class DbSession(BaseDbSession):
    database = DATABASE
    base = Base


"""
Insert default rows into reference tables upon creation
"""


@event.listens_for(StationReference.__table__, "after_create")
def _insert_station_values(target, connection, **kwargs):
    session = DbSession.factory()
    for station_no in range(60):
        session.add(StationReference(station_no=station_no))
    session.commit()
    session.close()


@event.listens_for(RepairWidthReference.__table__, "after_create")
def _insert_repair_width_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in REPAIR_WIDTH_VALUES:
        session.add(RepairWidthReference(width=vv))
    session.commit()
    session.close()


@event.listens_for(TrackConditionReference.__table__, "after_create")
def _insert_track_condition_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in TRACK_CONDITION_VALUES:
        session.add(TrackConditionReference(track_condition=vv))
    session.commit()
    session.close()


@event.listens_for(TrackMoistureReference.__table__, "after_create")
def _insert_track_moisture_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in TRACK_MOISTURE_VALUES:
        session.add(TrackMoistureReference(track_moisture=vv))
    session.commit()
    session.close()


@event.listens_for(TriggerMethodReference.__table__, "after_create")
def _insert_trigger_method_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in TRIGGER_METHOD_VALUES:
        session.add(TriggerMethodReference(trigger_method=vv))
    session.commit()
    session.close()


@event.listens_for(StrainCoilPositionReference.__table__, "after_create")
def _insert_strain_coil_position_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in STRAIN_COIL_POSITION_VALUES:
        session.add(StrainCoilPositionReference(coil_position=vv))
    session.commit()
    session.close()


@event.listens_for(StrainCoilPairDirectionReference.__table__, "after_create")
def _insert_strain_coil_pair_direction_values(target, connection, **kwargs):
    session = DbSession.factory()
    for vv in STRAIN_COIL_PAIR_DIRECTION_VALUES:
        session.add(StrainCoilPairDirectionReference(coil_pair_direction=vv))
    session.commit()
    session.close()
