"""
Reference model objects represent constants and are used to restrict fields if other models.

"""

from sqlalchemy import Column, Integer, String

from .base import Table, Base


__all__ = [
    "StationReference",
    "RepairWidthReference",
    "TrackConditionReference",
    "TrackMoistureReference",
    "TriggerMethodReference",
    "StrainCoilPositionReference",
    "StrainCoilPairDirectionReference",
]


class StationReference(Table, Base):
    """Used to restrict the possible station values in the Station model.

    :param station_no: reference station number (required)

    """

    __tablename__ = "station_reference"
    __index_column__ = "station_no"
    station_no = Column(Integer, primary_key=True, autoincrement=False)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class RepairWidthReference(Table, Base):
    """
    Used to restrict the possible repair reference width descriptions.

    :param width: width description (required)

    """

    __tablename__ = "repair_width_reference"
    __index_column__ = "width"
    width = Column(String(20), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class TrackConditionReference(Table, Base):
    """
    Used to restrict the possible track condition descriptions.

    :param track_condition: track condition description (required)

    """

    __tablename__ = "track_condition_reference"
    __index_column__ = "track_condition"
    track_condition = Column(String(50), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class TrackMoistureReference(Table, Base):
    """
    Used to restrict the possible track moisture descriptions.

    :param track_moisture: track moisture description (required)

    """

    __tablename__ = "track_moisture_reference"
    __index_column__ = "track_moisture"
    track_moisture = Column(String(50), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class TriggerMethodReference(Table, Base):
    """
    Used to restrict the possible measurement trigger methods.

    :param trigger_method:  (required)

    """

    __tablename__ = "trigger_method_reference"
    __index_column__ = "trigger_method"
    trigger_method = Column(String(20), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class StrainCoilPositionReference(Table, Base):
    """
    Used to restrict the possible strain coil position descriptions.

    :param coil_position: coil position description (required)

    """

    __tablename__ = "strain_coil_position_reference"
    __index_column__ = "coil_position"
    coil_position = Column(String(20), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}


class StrainCoilPairDirectionReference(Table, Base):
    """
    Used to restrict the possible strain coil pair direction descriptions.

    :param coil_pair_direction: coil pair direction description (required)

    """

    __tablename__ = "strain_coil_pair_direction_reference"
    __index_column__ = "coil_pair_direction"
    coil_pair_direction = Column(String(20), primary_key=True)

    __table_args__ = {"info": {"er_tags": ["reference"]}}
