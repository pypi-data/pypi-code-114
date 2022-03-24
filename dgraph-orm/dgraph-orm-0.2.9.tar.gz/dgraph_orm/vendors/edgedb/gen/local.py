from __future__ import annotations
import typing as T
from enum import Enum
from datetime import datetime, date, timedelta
from uuid import UUID
from decimal import Decimal
from edgedb import RelativeDuration, AsyncIOClient, create_async_client
from pydantic import BaseModel, Field
from dgraph_orm.vendors.edgedb import (
    Node,
    Resolver,
    NodeException,
    ResolverException,
    UpdateOperation,
    Batch,
)

client = create_async_client(
    tls_security="insecure",
    host="localhost",
    password="mQj9wCxh3W25H5ds7XJqoUhj",
    port=10701,
)


class AnimalType(str, Enum):
    lion = "lion"
    tiger = "tiger"


class Category(str, Enum):
    Hip_Hop = "Hip_Hop"
    Pop = "Pop"
    EDM = "EDM"
    DJ = "DJ"
    Rock = "Rock"
    Country = "Country"
    Reggae = "Reggae"
    Jazz = "Jazz"
    Tribute = "Tribute"
    Comedy = "Comedy"


class BandConfigurationOption(str, Enum):
    solo = "solo"
    duo = "duo"
    trio = "trio"
    full_band = "full_band"


class Billing(str, Enum):
    Opener = "Opener"
    Headliner = "Headliner"
    Co_Headliner = "Co_Headliner"


class BookingFlow(str, Enum):
    venue = "venue"
    private = "private"
    upb = "upb"


class BookingStatus(str, Enum):
    created = "created"
    contracting = "contracting"
    negotiating = "negotiating"
    advancing = "advancing"
    performance = "performance"
    canceled = "canceled"
    declined = "declined"
    rescheduling = "rescheduling"


class IndoorsOrOutdoors(str, Enum):
    Indoors = "Indoors"
    Outdoors = "Outdoors"


class UserRole(str, Enum):
    buyer = "buyer"
    seller = "seller"
    admin = "admin"


class UserType(str, Enum):
    owner = "owner"
    employee = "employee"
    read_only = "read_only"
    Artist = "Artist"
    Agent = "Agent"
    Manager = "Manager"
    Other_Seller = "Other_Seller"
    Bar = "Bar"
    Brewery = "Brewery"
    Restaurant = "Restaurant"
    Nightclub = "Nightclub"
    Vineyard_Winery = "Vineyard_Winery"
    Theater = "Theater"
    Country_Club = "Country_Club"
    Hotel_Resort = "Hotel_Resort"
    University_Program_Board = "University_Program_Board"
    Fraternity_Sorority = "Fraternity_Sorority"
    Wedding = "Wedding"
    Corporate_Event = "Corporate_Event"
    Municipality = "Municipality"
    Other_Buyer = "Other_Buyer"


class VenueType(str, Enum):
    Bar = "Bar"
    Brewery = "Brewery"
    Restaurant = "Restaurant"
    Nightclub = "Nightclub"
    Municipality = "Municipality"
    Vineyard_Winery = "Vineyard_Winery"
    Theater = "Theater"
    Country_Club = "Country_Club"
    Other_Venue = "Other_Venue"
    Hotel = "Hotel"


class AnimalInsert(BaseModel):
    public_id: str
    slug: str
    animal_type: AnimalType
    name: str
    age: T.Optional[int] = None
    created_at: T.Optional[datetime] = None
    description: T.Optional[str] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "public_id": "std::str",
        "slug": "std::str",
        "animal_type": "std::str",
        "name": "std::str",
        "age": "std::int16",
        "created_at": "std::datetime",
        "description": "std::str",
    }


class Animal(Node[AnimalInsert]):
    id: UUID = Field(..., allow_mutation=False)
    public_id: str = Field(..., allow_mutation=True)
    slug: str = Field(..., allow_mutation=True)
    animal_type: AnimalType = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    age: T.Optional[int] = Field(None, allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    description: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "public_id": "std::str",
        "slug": "std::str",
        "animal_type": "std::str",
        "name": "std::str",
        "age": "std::int16",
        "created_at": "std::datetime",
        "description": "std::str",
    }

    async def update(
        self,
        given_resolver: AnimalResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
    ) -> None:
        set_links_d = {}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Animal"
        client = client
        updatable_fields: T.Set[str] = {
            "age",
            "animal_type",
            "created_at",
            "description",
            "name",
            "public_id",
            "slug",
        }
        exclusive_fields: T.Set[str] = {"id", "public_id", "slug"}


class AnimalResolver(Resolver[Animal]):
    _node = Animal


Animal.GraphORM.resolver_type = AnimalResolver


class ArtistInsert(BaseModel):
    firebase_id: str
    slug: str
    connect_account_id: str
    created_at: datetime
    last_updated: datetime
    name: str
    published: bool
    category: T.Optional[Category] = None
    bio: T.Optional[str] = None
    admin_details: T.Optional[str] = None
    band_configuration: T.Optional[str] = None
    contact_information: T.Optional[str] = None
    cover_image: T.Optional[str] = None
    last_backend_updated: T.Optional[datetime] = None
    last_redis_refreshed: T.Optional[datetime] = None
    last_triggered_at: T.Optional[datetime] = None
    media: T.Optional[str] = None
    migration_version: T.Optional[int] = None
    profile_image: T.Optional[str] = None
    social_media: T.Optional[str] = None
    spotify_id: T.Optional[str] = None
    subgenres: T.Optional[T.List[str]] = None
    venue_take_percentages: T.Optional[str] = None
    version: T.Optional[int] = None
    bookings: T.Optional[BookingResolver] = None
    sellers: T.Optional[UserResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": "std::str",
        "slug": "std::str",
        "connect_account_id": "std::str",
        "created_at": "std::datetime",
        "last_updated": "std::datetime",
        "name": "std::str",
        "published": "std::bool",
        "category": "std::str",
        "bio": "std::str",
        "admin_details": "std::str",
        "band_configuration": "std::str",
        "contact_information": "std::str",
        "cover_image": "std::str",
        "last_backend_updated": "std::datetime",
        "last_redis_refreshed": "std::datetime",
        "last_triggered_at": "std::datetime",
        "media": "std::str",
        "migration_version": "std::int16",
        "profile_image": "std::str",
        "social_media": "std::str",
        "spotify_id": "std::str",
        "subgenres": "array<std::str>",
        "venue_take_percentages": "std::str",
        "version": "std::int16",
    }


class Artist(Node[ArtistInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    connect_account_id: str = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    published: bool = Field(..., allow_mutation=True)
    category: T.Optional[Category] = Field(None, allow_mutation=True)
    bio: T.Optional[str] = Field(None, allow_mutation=True)
    admin_details: T.Optional[str] = Field(None, allow_mutation=True)
    band_configuration: T.Optional[str] = Field(None, allow_mutation=True)
    contact_information: T.Optional[str] = Field(None, allow_mutation=True)
    cover_image: T.Optional[str] = Field(None, allow_mutation=True)
    last_backend_updated: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_redis_refreshed: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    media: T.Optional[str] = Field(None, allow_mutation=True)
    migration_version: T.Optional[int] = Field(None, allow_mutation=True)
    profile_image: T.Optional[str] = Field(None, allow_mutation=True)
    social_media: T.Optional[str] = Field(None, allow_mutation=True)
    spotify_id: T.Optional[str] = Field(None, allow_mutation=True)
    subgenres: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    venue_take_percentages: T.Optional[str] = Field(None, allow_mutation=True)
    version: T.Optional[int] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
        "slug": "std::str",
        "connect_account_id": "std::str",
        "created_at": "std::datetime",
        "last_updated": "std::datetime",
        "name": "std::str",
        "published": "std::bool",
        "category": "std::str",
        "bio": "std::str",
        "admin_details": "std::str",
        "band_configuration": "std::str",
        "contact_information": "std::str",
        "cover_image": "std::str",
        "last_backend_updated": "std::datetime",
        "last_redis_refreshed": "std::datetime",
        "last_triggered_at": "std::datetime",
        "media": "std::str",
        "migration_version": "std::int16",
        "profile_image": "std::str",
        "social_media": "std::str",
        "spotify_id": "std::str",
        "subgenres": "array<std::str>",
        "venue_take_percentages": "std::str",
        "version": "std::int16",
    }

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def sellers(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[User]]:
        return await self.resolve(
            edge_name="sellers",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: ArtistResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        bookings: T.Optional[BookingResolver] = None,
        sellers: T.Optional[UserResolver] = None,
    ) -> None:
        set_links_d = {"bookings": bookings, "sellers": sellers}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Artist"
        client = client
        updatable_fields: T.Set[str] = {
            "admin_details",
            "band_configuration",
            "bio",
            "bookings",
            "category",
            "connect_account_id",
            "contact_information",
            "cover_image",
            "created_at",
            "last_backend_updated",
            "last_redis_refreshed",
            "last_triggered_at",
            "last_updated",
            "media",
            "migration_version",
            "name",
            "profile_image",
            "published",
            "sellers",
            "slug",
            "social_media",
            "spotify_id",
            "subgenres",
            "venue_take_percentages",
            "version",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "slug"}


class ArtistResolver(Resolver[Artist]):
    _node = Artist

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> ArtistResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self

    def sellers(self, _: T.Optional[UserResolver] = None, /) -> ArtistResolver:
        if "sellers" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `sellers` has already been provided."
            )
        self._nested_resolvers["sellers"] = _ or UserResolver()
        return self


Artist.GraphORM.resolver_type = ArtistResolver


class MetaBookingInsert(BaseModel):
    firebase_id: str
    start_time: datetime
    is_published: bool
    performance_length_mins: int
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
    }


class MetaBooking(Node[MetaBookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    start_time: datetime = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    performance_length_mins: int = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
    }

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: MetaBookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {"venue": venue}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "MetaBooking"
        client = client
        updatable_fields: T.Set[str] = {
            "indoors_or_outdoors",
            "is_published",
            "performance_length_mins",
            "public_event_description",
            "start_time",
            "venue",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class MetaBookingResolver(Resolver[MetaBooking]):
    _node = MetaBooking

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> MetaBookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


MetaBooking.GraphORM.resolver_type = MetaBookingResolver


class BookingInsert(BaseModel):
    firebase_id: str
    start_time: datetime
    is_published: bool
    performance_length_mins: int
    created_at: datetime
    booking_flow: BookingFlow
    location: str
    negotiation_steps: str
    status: BookingStatus
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    admin_cancellation_message: T.Optional[str] = None
    band_configuration: T.Optional[BandConfigurationOption] = None
    billing: T.Optional[Billing] = None
    booking_dispute: T.Optional[str] = None
    buyer_has_reviewed: T.Optional[bool] = None
    capacity: T.Optional[int] = None
    charge: T.Optional[str] = None
    comments: T.Optional[str] = None
    customer_balance_transaction_id: T.Optional[str] = None
    deposit: T.Optional[str] = None
    has_extra_charge: T.Optional[bool] = None
    has_extra_payout: T.Optional[bool] = None
    last_triggered_at: T.Optional[datetime] = None
    last_updated: T.Optional[datetime] = None
    old_start_time: T.Optional[datetime] = None
    payout: T.Optional[str] = None
    production_and_venue_specs: T.Optional[str] = None
    refunded_in_credits: T.Optional[bool] = None
    reschedule_message: T.Optional[str] = None
    resolved_booking_dispute: T.Optional[str] = None
    seller_has_reviewed: T.Optional[bool] = None
    should_auto_publish: T.Optional[bool] = None
    week_out_notification: T.Optional[bool] = None
    week_out_notification_at: T.Optional[datetime] = None
    artist: ArtistResolver
    buyer: UserResolver
    account_exec: T.Optional[UserResolver] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "created_at": "std::datetime",
        "booking_flow": "std::str",
        "location": "std::str",
        "negotiation_steps": "std::str",
        "status": "std::str",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
        "admin_cancellation_message": "std::str",
        "band_configuration": "std::str",
        "billing": "std::str",
        "booking_dispute": "std::str",
        "buyer_has_reviewed": "std::bool",
        "capacity": "std::int16",
        "charge": "std::str",
        "comments": "std::str",
        "customer_balance_transaction_id": "std::str",
        "deposit": "std::str",
        "has_extra_charge": "std::bool",
        "has_extra_payout": "std::bool",
        "last_triggered_at": "std::datetime",
        "last_updated": "std::datetime",
        "old_start_time": "std::datetime",
        "payout": "std::str",
        "production_and_venue_specs": "std::str",
        "refunded_in_credits": "std::bool",
        "reschedule_message": "std::str",
        "resolved_booking_dispute": "std::str",
        "seller_has_reviewed": "std::bool",
        "should_auto_publish": "std::bool",
        "week_out_notification": "std::bool",
        "week_out_notification_at": "std::datetime",
    }


class Booking(Node[BookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    start_time: datetime = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    performance_length_mins: int = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    booking_flow: BookingFlow = Field(..., allow_mutation=True)
    location: str = Field(..., allow_mutation=True)
    negotiation_steps: str = Field(..., allow_mutation=True)
    status: BookingStatus = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)
    admin_cancellation_message: T.Optional[str] = Field(None, allow_mutation=True)
    band_configuration: T.Optional[BandConfigurationOption] = Field(
        None, allow_mutation=True
    )
    billing: T.Optional[Billing] = Field(None, allow_mutation=True)
    booking_dispute: T.Optional[str] = Field(None, allow_mutation=True)
    buyer_has_reviewed: T.Optional[bool] = Field(None, allow_mutation=True)
    capacity: T.Optional[int] = Field(None, allow_mutation=True)
    charge: T.Optional[str] = Field(None, allow_mutation=True)
    comments: T.Optional[str] = Field(None, allow_mutation=True)
    customer_balance_transaction_id: T.Optional[str] = Field(None, allow_mutation=True)
    deposit: T.Optional[str] = Field(None, allow_mutation=True)
    has_extra_charge: T.Optional[bool] = Field(None, allow_mutation=True)
    has_extra_payout: T.Optional[bool] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_updated: T.Optional[datetime] = Field(None, allow_mutation=True)
    old_start_time: T.Optional[datetime] = Field(None, allow_mutation=True)
    payout: T.Optional[str] = Field(None, allow_mutation=True)
    production_and_venue_specs: T.Optional[str] = Field(None, allow_mutation=True)
    refunded_in_credits: T.Optional[bool] = Field(None, allow_mutation=True)
    reschedule_message: T.Optional[str] = Field(None, allow_mutation=True)
    resolved_booking_dispute: T.Optional[str] = Field(None, allow_mutation=True)
    seller_has_reviewed: T.Optional[bool] = Field(None, allow_mutation=True)
    should_auto_publish: T.Optional[bool] = Field(None, allow_mutation=True)
    week_out_notification: T.Optional[bool] = Field(None, allow_mutation=True)
    week_out_notification_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "created_at": "std::datetime",
        "booking_flow": "std::str",
        "location": "std::str",
        "negotiation_steps": "std::str",
        "status": "std::str",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
        "admin_cancellation_message": "std::str",
        "band_configuration": "std::str",
        "billing": "std::str",
        "booking_dispute": "std::str",
        "buyer_has_reviewed": "std::bool",
        "capacity": "std::int16",
        "charge": "std::str",
        "comments": "std::str",
        "customer_balance_transaction_id": "std::str",
        "deposit": "std::str",
        "has_extra_charge": "std::bool",
        "has_extra_payout": "std::bool",
        "last_triggered_at": "std::datetime",
        "last_updated": "std::datetime",
        "old_start_time": "std::datetime",
        "payout": "std::str",
        "production_and_venue_specs": "std::str",
        "refunded_in_credits": "std::bool",
        "reschedule_message": "std::str",
        "resolved_booking_dispute": "std::str",
        "seller_has_reviewed": "std::bool",
        "should_auto_publish": "std::bool",
        "week_out_notification": "std::bool",
        "week_out_notification_at": "std::datetime",
    }

    async def artist(
        self,
        resolver: ArtistResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> Artist:
        return await self.resolve(
            edge_name="artist",
            edge_resolver=resolver or ArtistResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def buyer(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> User:
        return await self.resolve(
            edge_name="buyer",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[User]:
        return await self.resolve(
            edge_name="account_exec",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: BookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        artist: T.Optional[ArtistResolver] = None,
        buyer: T.Optional[UserResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {
            "artist": artist,
            "buyer": buyer,
            "account_exec": account_exec,
            "venue": venue,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Booking"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec",
            "admin_cancellation_message",
            "artist",
            "band_configuration",
            "billing",
            "booking_dispute",
            "booking_flow",
            "buyer",
            "buyer_has_reviewed",
            "capacity",
            "charge",
            "comments",
            "created_at",
            "customer_balance_transaction_id",
            "deposit",
            "has_extra_charge",
            "has_extra_payout",
            "indoors_or_outdoors",
            "is_published",
            "last_triggered_at",
            "last_updated",
            "location",
            "negotiation_steps",
            "old_start_time",
            "payout",
            "performance_length_mins",
            "production_and_venue_specs",
            "public_event_description",
            "refunded_in_credits",
            "reschedule_message",
            "resolved_booking_dispute",
            "seller_has_reviewed",
            "should_auto_publish",
            "start_time",
            "status",
            "venue",
            "week_out_notification",
            "week_out_notification_at",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class BookingResolver(Resolver[Booking]):
    _node = Booking

    def artist(self, _: T.Optional[ArtistResolver] = None, /) -> BookingResolver:
        if "artist" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `artist` has already been provided."
            )
        self._nested_resolvers["artist"] = _ or ArtistResolver()
        return self

    def buyer(self, _: T.Optional[UserResolver] = None, /) -> BookingResolver:
        if "buyer" in self._nested_resolvers:
            raise ResolverException("A resolver for `buyer` has already been provided.")
        self._nested_resolvers["buyer"] = _ or UserResolver()
        return self

    def account_exec(self, _: T.Optional[UserResolver] = None, /) -> BookingResolver:
        if "account_exec" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec` has already been provided."
            )
        self._nested_resolvers["account_exec"] = _ or UserResolver()
        return self

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> BookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


Booking.GraphORM.resolver_type = BookingResolver


class UserInsert(BaseModel):
    phone_number: str
    slug: str
    firebase_id: str
    email: str
    approved: bool
    created_at: datetime
    last_updated: datetime
    metadata: str
    name: str
    user_role: UserRole
    user_type: UserType
    admin_permissions: T.Optional[T.List[str]] = None
    admin_type: T.Optional[UserType] = None
    approval: T.Optional[str] = None
    default_state_abbr: T.Optional[str] = None
    last_triggered_at: T.Optional[datetime] = None
    profile_image: T.Optional[str] = None
    referred_by_id: T.Optional[str] = None
    artists: T.Optional[ArtistResolver] = None
    account_exec_bookings: T.Optional[BookingResolver] = None
    bookings: T.Optional[BookingResolver] = None
    venues: T.Optional[VenueResolver] = None
    venues_assigned_to: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "phone_number": "std::str",
        "slug": "std::str",
        "firebase_id": "std::str",
        "email": "std::str",
        "approved": "std::bool",
        "created_at": "std::datetime",
        "last_updated": "std::datetime",
        "metadata": "std::str",
        "name": "std::str",
        "user_role": "std::str",
        "user_type": "std::str",
        "admin_permissions": "array<std::str>",
        "admin_type": "std::str",
        "approval": "std::str",
        "default_state_abbr": "std::str",
        "last_triggered_at": "std::datetime",
        "profile_image": "std::str",
        "referred_by_id": "std::str",
    }


class User(Node[UserInsert]):
    id: UUID = Field(..., allow_mutation=False)
    phone_number: str = Field(..., allow_mutation=True)
    slug: str = Field(..., allow_mutation=True)
    firebase_id: str = Field(..., allow_mutation=False)
    email: str = Field(..., allow_mutation=True)
    approved: bool = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    metadata: str = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    user_role: UserRole = Field(..., allow_mutation=True)
    user_type: UserType = Field(..., allow_mutation=True)
    admin_permissions: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    admin_type: T.Optional[UserType] = Field(None, allow_mutation=True)
    approval: T.Optional[str] = Field(None, allow_mutation=True)
    default_state_abbr: T.Optional[str] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    profile_image: T.Optional[str] = Field(None, allow_mutation=True)
    referred_by_id: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "phone_number": "std::str",
        "slug": "std::str",
        "firebase_id": "std::str",
        "email": "std::str",
        "approved": "std::bool",
        "created_at": "std::datetime",
        "last_updated": "std::datetime",
        "metadata": "std::str",
        "name": "std::str",
        "user_role": "std::str",
        "user_type": "std::str",
        "admin_permissions": "array<std::str>",
        "admin_type": "std::str",
        "approval": "std::str",
        "default_state_abbr": "std::str",
        "last_triggered_at": "std::datetime",
        "profile_image": "std::str",
        "referred_by_id": "std::str",
    }

    async def artists(
        self,
        resolver: ArtistResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Artist]]:
        return await self.resolve(
            edge_name="artists",
            edge_resolver=resolver or ArtistResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec_bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="account_exec_bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venues(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Venue]]:
        return await self.resolve(
            edge_name="venues",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venues_assigned_to(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Venue]]:
        return await self.resolve(
            edge_name="venues_assigned_to",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: UserResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        artists: T.Optional[ArtistResolver] = None,
        account_exec_bookings: T.Optional[BookingResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
        venues: T.Optional[VenueResolver] = None,
        venues_assigned_to: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {
            "artists": artists,
            "account_exec_bookings": account_exec_bookings,
            "bookings": bookings,
            "venues": venues,
            "venues_assigned_to": venues_assigned_to,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "User"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec_bookings",
            "admin_permissions",
            "admin_type",
            "approval",
            "approved",
            "artists",
            "bookings",
            "created_at",
            "default_state_abbr",
            "email",
            "last_triggered_at",
            "last_updated",
            "metadata",
            "name",
            "phone_number",
            "profile_image",
            "referred_by_id",
            "slug",
            "user_role",
            "user_type",
            "venues",
            "venues_assigned_to",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "phone_number", "slug"}


class UserResolver(Resolver[User]):
    _node = User

    def artists(self, _: T.Optional[ArtistResolver] = None, /) -> UserResolver:
        if "artists" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `artists` has already been provided."
            )
        self._nested_resolvers["artists"] = _ or ArtistResolver()
        return self

    def account_exec_bookings(
        self, _: T.Optional[BookingResolver] = None, /
    ) -> UserResolver:
        if "account_exec_bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec_bookings` has already been provided."
            )
        self._nested_resolvers["account_exec_bookings"] = _ or BookingResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> UserResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self

    def venues(self, _: T.Optional[VenueResolver] = None, /) -> UserResolver:
        if "venues" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `venues` has already been provided."
            )
        self._nested_resolvers["venues"] = _ or VenueResolver()
        return self

    def venues_assigned_to(
        self, _: T.Optional[VenueResolver] = None, /
    ) -> UserResolver:
        if "venues_assigned_to" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `venues_assigned_to` has already been provided."
            )
        self._nested_resolvers["venues_assigned_to"] = _ or VenueResolver()
        return self


User.GraphORM.resolver_type = UserResolver


class VenueInsert(BaseModel):
    firebase_id: str
    slug: str
    created_at: datetime
    customer_id: str
    last_updated: datetime
    location: str
    name: str
    num_stages: int
    place_id: str
    venue_type: VenueType
    budget: T.Optional[str] = None
    capacity: T.Optional[int] = None
    colors: T.Optional[str] = None
    display_images: T.Optional[str] = None
    genres_booked: T.Optional[T.List[str]] = None
    images: T.Optional[str] = None
    logo: T.Optional[str] = None
    phone_number: T.Optional[str] = None
    production_and_venue_specs: T.Optional[str] = None
    social_media: T.Optional[str] = None
    website: T.Optional[str] = None
    created_by: UserResolver
    account_exec: T.Optional[UserResolver] = None
    owners: T.Optional[UserResolver] = None
    bookings: T.Optional[BookingResolver] = None
    external_bookings: T.Optional[ExternalBookingResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": "std::str",
        "slug": "std::str",
        "created_at": "std::datetime",
        "customer_id": "std::str",
        "last_updated": "std::datetime",
        "location": "std::str",
        "name": "std::str",
        "num_stages": "std::int16",
        "place_id": "std::str",
        "venue_type": "std::str",
        "budget": "std::str",
        "capacity": "std::int16",
        "colors": "std::str",
        "display_images": "std::str",
        "genres_booked": "array<std::str>",
        "images": "std::str",
        "logo": "std::str",
        "phone_number": "std::str",
        "production_and_venue_specs": "std::str",
        "social_media": "std::str",
        "website": "std::str",
    }


class Venue(Node[VenueInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    customer_id: str = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    location: str = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    num_stages: int = Field(..., allow_mutation=True)
    place_id: str = Field(..., allow_mutation=True)
    venue_type: VenueType = Field(..., allow_mutation=True)
    budget: T.Optional[str] = Field(None, allow_mutation=True)
    capacity: T.Optional[int] = Field(None, allow_mutation=True)
    colors: T.Optional[str] = Field(None, allow_mutation=True)
    display_images: T.Optional[str] = Field(None, allow_mutation=True)
    genres_booked: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    images: T.Optional[str] = Field(None, allow_mutation=True)
    logo: T.Optional[str] = Field(None, allow_mutation=True)
    phone_number: T.Optional[str] = Field(None, allow_mutation=True)
    production_and_venue_specs: T.Optional[str] = Field(None, allow_mutation=True)
    social_media: T.Optional[str] = Field(None, allow_mutation=True)
    website: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
        "slug": "std::str",
        "created_at": "std::datetime",
        "customer_id": "std::str",
        "last_updated": "std::datetime",
        "location": "std::str",
        "name": "std::str",
        "num_stages": "std::int16",
        "place_id": "std::str",
        "venue_type": "std::str",
        "budget": "std::str",
        "capacity": "std::int16",
        "colors": "std::str",
        "display_images": "std::str",
        "genres_booked": "array<std::str>",
        "images": "std::str",
        "logo": "std::str",
        "phone_number": "std::str",
        "production_and_venue_specs": "std::str",
        "social_media": "std::str",
        "website": "std::str",
    }

    async def created_by(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> User:
        return await self.resolve(
            edge_name="created_by",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[User]:
        return await self.resolve(
            edge_name="account_exec",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def owners(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[User]]:
        return await self.resolve(
            edge_name="owners",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def external_bookings(
        self,
        resolver: ExternalBookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[ExternalBooking]]:
        return await self.resolve(
            edge_name="external_bookings",
            edge_resolver=resolver or ExternalBookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: VenueResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        created_by: T.Optional[UserResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
        owners: T.Optional[UserResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
        external_bookings: T.Optional[ExternalBookingResolver] = None,
    ) -> None:
        set_links_d = {
            "created_by": created_by,
            "account_exec": account_exec,
            "owners": owners,
            "bookings": bookings,
            "external_bookings": external_bookings,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Venue"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec",
            "bookings",
            "budget",
            "capacity",
            "colors",
            "created_at",
            "created_by",
            "customer_id",
            "display_images",
            "external_bookings",
            "genres_booked",
            "images",
            "last_updated",
            "location",
            "logo",
            "name",
            "num_stages",
            "owners",
            "phone_number",
            "place_id",
            "production_and_venue_specs",
            "slug",
            "social_media",
            "venue_type",
            "website",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "slug"}


class VenueResolver(Resolver[Venue]):
    _node = Venue

    def created_by(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "created_by" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `created_by` has already been provided."
            )
        self._nested_resolvers["created_by"] = _ or UserResolver()
        return self

    def account_exec(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "account_exec" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec` has already been provided."
            )
        self._nested_resolvers["account_exec"] = _ or UserResolver()
        return self

    def owners(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "owners" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `owners` has already been provided."
            )
        self._nested_resolvers["owners"] = _ or UserResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> VenueResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self

    def external_bookings(
        self, _: T.Optional[ExternalBookingResolver] = None, /
    ) -> VenueResolver:
        if "external_bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `external_bookings` has already been provided."
            )
        self._nested_resolvers["external_bookings"] = _ or ExternalBookingResolver()
        return self


Venue.GraphORM.resolver_type = VenueResolver


class ExternalBookingInsert(BaseModel):
    firebase_id: str
    start_time: datetime
    is_published: bool
    performance_length_mins: int
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    artist_name: T.Optional[str] = None
    cover_image: T.Optional[str] = None
    last_triggered_at: T.Optional[datetime] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
        "artist_name": "std::str",
        "cover_image": "std::str",
        "last_triggered_at": "std::datetime",
    }


class ExternalBooking(Node[ExternalBookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    start_time: datetime = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    performance_length_mins: int = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)
    artist_name: T.Optional[str] = Field(None, allow_mutation=True)
    cover_image: T.Optional[str] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
        "start_time": "std::datetime",
        "is_published": "std::bool",
        "performance_length_mins": "std::int16",
        "indoors_or_outdoors": "std::str",
        "public_event_description": "std::str",
        "artist_name": "std::str",
        "cover_image": "std::str",
        "last_triggered_at": "std::datetime",
    }

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: ExternalBookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {"venue": venue}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "ExternalBooking"
        client = client
        updatable_fields: T.Set[str] = {
            "artist_name",
            "cover_image",
            "indoors_or_outdoors",
            "is_published",
            "last_triggered_at",
            "performance_length_mins",
            "public_event_description",
            "start_time",
            "venue",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class ExternalBookingResolver(Resolver[ExternalBooking]):
    _node = ExternalBooking

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> ExternalBookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


ExternalBooking.GraphORM.resolver_type = ExternalBookingResolver


class FirebaseObjectInsert(BaseModel):
    firebase_id: str

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {"firebase_id": "std::str"}


class FirebaseObject(Node[FirebaseObjectInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "firebase_id": "std::str",
    }

    async def update(
        self,
        given_resolver: FirebaseObjectResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
    ) -> None:
        set_links_d = {}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "FirebaseObject"
        client = client
        updatable_fields: T.Set[str] = {}
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class FirebaseObjectResolver(Resolver[FirebaseObject]):
    _node = FirebaseObject


FirebaseObject.GraphORM.resolver_type = FirebaseObjectResolver


class MovieInsert(BaseModel):
    title: str
    year: T.Optional[int] = None
    actors: T.Optional[PersonResolver] = None
    director: T.Optional[PersonResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "title": "std::str",
        "year": "std::int64",
    }


class Movie(Node[MovieInsert]):
    id: UUID = Field(..., allow_mutation=False)
    title: str = Field(..., allow_mutation=True)
    year: T.Optional[int] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "title": "std::str",
        "year": "std::int64",
    }

    async def actors(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="actors",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def director(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Person]:
        return await self.resolve(
            edge_name="director",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: MovieResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        actors: T.Optional[PersonResolver] = None,
        director: T.Optional[PersonResolver] = None,
    ) -> None:
        set_links_d = {"actors": actors, "director": director}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Movie"
        client = client
        updatable_fields: T.Set[str] = {"actors", "director", "title", "year"}
        exclusive_fields: T.Set[str] = {"id"}


class MovieResolver(Resolver[Movie]):
    _node = Movie

    def actors(self, _: T.Optional[PersonResolver] = None, /) -> MovieResolver:
        if "actors" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `actors` has already been provided."
            )
        self._nested_resolvers["actors"] = _ or PersonResolver()
        return self

    def director(self, _: T.Optional[PersonResolver] = None, /) -> MovieResolver:
        if "director" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `director` has already been provided."
            )
        self._nested_resolvers["director"] = _ or PersonResolver()
        return self


Movie.GraphORM.resolver_type = MovieResolver


class PersonInsert(BaseModel):
    slug: str
    inserted_at: T.Optional[datetime] = None
    first_name: str
    created_at: T.Optional[datetime] = None
    last_name: T.Optional[str] = None
    full_name: T.Optional[str] = None
    ordered_tags: T.Optional[T.List[str]] = None
    tags: T.Optional[T.Set[str]] = None
    best_friend: T.Optional[PersonResolver] = None
    people_i_follow: T.Optional[PersonResolver] = None
    my_followers: T.Optional[PersonResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": "std::str",
        "inserted_at": "std::datetime",
        "first_name": "std::str",
        "created_at": "std::datetime",
        "last_name": "std::str",
        "full_name": "std::str",
        "ordered_tags": "array<std::str>",
        "tags": "std::str",
    }


class Person(Node[PersonInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    inserted_at: datetime = Field(..., allow_mutation=False)
    first_name: str = Field(..., allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_name: T.Optional[str] = Field(None, allow_mutation=True)
    full_name: T.Optional[str] = Field(None, allow_mutation=True)
    ordered_tags: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    tags: T.Optional[T.Set[str]] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "slug": "std::str",
        "inserted_at": "std::datetime",
        "first_name": "std::str",
        "created_at": "std::datetime",
        "last_name": "std::str",
        "full_name": "std::str",
        "ordered_tags": "array<std::str>",
        "tags": "std::str",
    }

    async def best_friend(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Person]:
        return await self.resolve(
            edge_name="best_friend",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def people_i_follow(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="people_i_follow",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def my_followers(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="my_followers",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: PersonResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        best_friend: T.Optional[PersonResolver] = None,
        people_i_follow: T.Optional[PersonResolver] = None,
        my_followers: T.Optional[PersonResolver] = None,
    ) -> None:
        set_links_d = {
            "best_friend": best_friend,
            "people_i_follow": people_i_follow,
            "my_followers": my_followers,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Person"
        client = client
        updatable_fields: T.Set[str] = {
            "best_friend",
            "created_at",
            "first_name",
            "full_name",
            "last_name",
            "my_followers",
            "ordered_tags",
            "people_i_follow",
            "slug",
            "tags",
        }
        exclusive_fields: T.Set[str] = {"id", "slug"}


class PersonResolver(Resolver[Person]):
    _node = Person

    def best_friend(self, _: T.Optional[PersonResolver] = None, /) -> PersonResolver:
        if "best_friend" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `best_friend` has already been provided."
            )
        self._nested_resolvers["best_friend"] = _ or PersonResolver()
        return self

    def people_i_follow(
        self, _: T.Optional[PersonResolver] = None, /
    ) -> PersonResolver:
        if "people_i_follow" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `people_i_follow` has already been provided."
            )
        self._nested_resolvers["people_i_follow"] = _ or PersonResolver()
        return self

    def my_followers(self, _: T.Optional[PersonResolver] = None, /) -> PersonResolver:
        if "my_followers" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `my_followers` has already been provided."
            )
        self._nested_resolvers["my_followers"] = _ or PersonResolver()
        return self


Person.GraphORM.resolver_type = PersonResolver

AnimalInsert.update_forward_refs()
ArtistInsert.update_forward_refs()
MetaBookingInsert.update_forward_refs()
BookingInsert.update_forward_refs()
UserInsert.update_forward_refs()
VenueInsert.update_forward_refs()
ExternalBookingInsert.update_forward_refs()
FirebaseObjectInsert.update_forward_refs()
MovieInsert.update_forward_refs()
PersonInsert.update_forward_refs()
