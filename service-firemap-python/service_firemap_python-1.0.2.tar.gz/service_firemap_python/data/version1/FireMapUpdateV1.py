# -*- coding: utf-8 -*-
import datetime
from dataclasses import dataclass


@dataclass
class FireMapUpdateV1:
    type: str  # Type of the update
    time: datetime.datetime  # Time when update was reported
    drone_id: str  # Drone ID that reported the update
    long: float  # Center longitude
    lat: float  # Center latitude
    people: int  # Number of people in the area
