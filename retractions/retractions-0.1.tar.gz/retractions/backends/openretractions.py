import datetime as dt
import json
import typing as tp
from dataclasses import dataclass
from urllib.request import Request

from ..doi import DOI
from .base import Backend, Update, UpdateType

Jso = tp.Optional[tp.Union[tp.Dict[str, "Jso"], tp.List["Jso"], int, float, str]]

OPENRETRACTIONS_URL_FMT = "http://openretractions.com/api/doi/{}/data.json"


@dataclass
class ORUpdate:
    timestamp: dt.datetime
    doi: DOI
    type: str

    @classmethod
    def from_jso(cls, jso: tp.Dict[str, Jso]):
        return cls(
            dt.datetime.fromtimestamp(jso["timestamp"] / 1000),
            DOI.parse(jso["identifier"]["doi"]),
            str(jso["type"]),
        )


@dataclass
class OREntry:
    """
    Note that this documentation is wrong, just copied from the site.

    {
        "retracted": false,  // whether or not the paper has been retracted
        // the UNIXtime when the original paper was published
        "timestamp": 1361836800000,
        "update": {
            "timestamp": 1491464002919, // the UNIXtime when the update was recorded
            "doi": "10.1002/job.1858", // the DOI of the update
            "type": "correction" // the publisher's description of the update
        },
        "doi": "10.1002/job.1787", // the DOI of the original paper
        "journal": "Journal of Organizational Behavior",
        "publisher": "Wiley-Blackwell",
        "title": "Erratum: Cognitive and affective identification:
            Exploring the links between different forms of social "
            "identification and personality with work attitudes and behavior"
    }
    """

    retracted: bool
    timestamp: dt.datetime
    updates: tp.List[ORUpdate]
    doi: DOI
    journal: str
    publisher: tp.Optional[str]
    title: str

    @classmethod
    def from_jso(cls, jso: tp.Dict[str, Jso]):
        return cls(
            bool(jso["retracted"]),
            dt.datetime.fromtimestamp(jso["timestamp"] / 1000),
            [ORUpdate.from_jso(u) for u in jso["updates"]],
            DOI.parse(jso["identifier"]["doi"]),
            jso.get("journal"),
            jso["publisher"],
            jso["title"],
        )


def make_url(doi: tp.Union[str, DOI]):
    if isinstance(doi, str):
        doi = DOI.parse(doi)
    return OPENRETRACTIONS_URL_FMT.format(doi.to_minimal())


def parse_content(s: str):
    jso = json.loads(s)
    return OREntry.from_jso(jso)


class OpenRetractions(Backend):
    def make_request(self, doi: DOI) -> Request:
        if isinstance(doi, str):
            doi = DOI.parse(doi)
        url = OPENRETRACTIONS_URL_FMT.format(doi.to_minimal())
        return Request(url)

    def parse_content(self, content: bytes) -> tp.Optional[Update]:
        jso = json.loads(content.decode("utf-8"))
        or_entry = OREntry.from_jso(jso)
        if or_entry.retracted:
            return Update(or_entry.doi, UpdateType.RETRACTION)
        elif not or_entry.updates:
            return None

        last_update = or_entry.updates[-1]
        return Update(
            or_entry.doi,
            UpdateType(last_update.type),
            last_update.timestamp,
            last_update.doi,
        )
