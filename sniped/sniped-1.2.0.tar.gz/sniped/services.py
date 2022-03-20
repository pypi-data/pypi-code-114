"""Listing of all available services and endpoings."""

import enum


class Service(enum.Enum):
    CARBON = "carbon"
    SNAPPIFY = "snappify"


ENDPOINTS = {
    Service.CARBON: "https://carbonara-42.herokuapp.com/api/cook",
    Service.SNAPPIFY: "https://api.snappify.io/snap/simple",
}
