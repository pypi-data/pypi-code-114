# -*- coding: utf-8 -*-

import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class FireMapTileV1:
    id: str  # Rounder center lng_lat

    zoom: int  # Zoom level
    flng: float  # From longitude
    flat: float  # From latitude
    tlng: float  # To longitude
    tlat: float  # To latitude

    clear: Optional[datetime.datetime] = None  # Date and time when clear was detected
    cdrone: Optional[str] = None  # Drone ID that detected clear
    smoke: Optional[datetime.datetime] = None  # Date and time when smoke was detected
    sdrone: Optional[str] = None  # Drone ID that detected smoke
    fire: Optional[datetime.datetime] = None  # Date and time when fire was detected
    fdrone: Optional[str] = None  # Drone ID that detected fire

    people: Optional[datetime.datetime] = None  # Date and time when people was detected
    pdrone: Optional[str] = None  # Drone id that detected people
    people_count: Optional[int] = None  # Number of people in the area

    @staticmethod
    def from_json(tile: dict) -> 'FireMapTileV1':
        from_date = lambda date: None if not date else datetime.datetime.fromisoformat(date)

        return FireMapTileV1(
            id=tile.get('id'),

            zoom=tile.get('zoom'),
            flng=tile.get('flng'),
            flat=tile.get('flat'),
            tlng=tile.get('tlng'),
            tlat=tile.get('tlat'),

            clear=from_date(tile.get('clear')),
            cdrone=tile.get('cdrone'),
            smoke=from_date(tile.get('smoke')),
            sdrone=tile.get('sdrone'),
            fire=from_date(tile.get('fire')),
            fdrone=tile.get('fdrone'),

            people=from_date(tile.get('people')),
            pdrone=tile.get('pdrone'),
            people_count=tile.get('people_count'),
        )
