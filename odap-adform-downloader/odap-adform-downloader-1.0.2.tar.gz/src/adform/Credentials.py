import tempfile
from dataclasses import dataclass
from typing import List

# _METADATA = ['banners-adgroups','browsers','campaigns','clickdetails-paidkeywords', 'clients','costs','deals',
#              'devices','events','geolocations','iabcategories','inventorysources','languages','medias',
#              'operatingsystems','parties','placements-activities','screensizes','tags','trackingpoints','zip-codes']


@dataclass
class Credentials:
    """
    Dataclass, which keeps credentials for AdForm Api Calls
    """

    # nutny posledni radek, abychom dostali data
    SCOPES = [
        "https://api.adform.com/scope/buyer.masterdata",
        "https://api.adform.com/scope/eapi",
        "https://api.adform.com/scope/buyer.rtb.lineitem",
    ]
    TABLES_and_META = ["Click", "Event", "Impression", "Trackingpoint", "meta"]

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        setup_id: str,
        scopes: List[str] = None,
        tables: List[str] = None,
        start_day=None,
        end_day=None,
        landing_file: str = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.setup_id = setup_id

        self.tables = tables if tables is not None else self.TABLES_and_META
        self.end_day = end_day
        self.start_day = start_day

        self.landing_file = landing_file if landing_file is not None else tempfile.gettempdir()

        self.scopes = scopes if scopes is not None else self.SCOPES
