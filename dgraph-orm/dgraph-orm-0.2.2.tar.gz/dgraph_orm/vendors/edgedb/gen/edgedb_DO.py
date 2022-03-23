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
    tls_security="insecure", host="143.244.174.160", password="beatgig8859"
)


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


class ArtistInsert(BaseModel):
    slug: str
    beatgig_id: str
    created_at: datetime
    name: str
    connect_account_id: str
    last_updated: datetime
    published: bool
    media: T.Optional[str] = None
    admin_details: T.Optional[str] = None
    band_configuration: T.Optional[str] = None
    bio: T.Optional[str] = None
    category: T.Optional[Category] = None
    contact_information: T.Optional[str] = None
    cover_image: T.Optional[str] = None
    last_backend_updated: T.Optional[datetime] = None
    last_redis_refreshed: T.Optional[datetime] = None
    last_triggered_at: T.Optional[datetime] = None
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
        "slug": "std::str",
        "beatgig_id": "std::str",
        "created_at": "std::datetime",
        "name": "std::str",
        "connect_account_id": "std::str",
        "last_updated": "std::datetime",
        "published": "std::bool",
        "media": "std::str",
        "admin_details": "std::str",
        "band_configuration": "std::str",
        "bio": "std::str",
        "category": "std::str",
        "contact_information": "std::str",
        "cover_image": "std::str",
        "last_backend_updated": "std::datetime",
        "last_redis_refreshed": "std::datetime",
        "last_triggered_at": "std::datetime",
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
    slug: str = Field(..., allow_mutation=True)
    beatgig_id: str = Field(..., allow_mutation=False)
    created_at: datetime = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    connect_account_id: str = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    published: bool = Field(..., allow_mutation=True)
    media: T.Optional[str] = Field(None, allow_mutation=True)
    admin_details: T.Optional[str] = Field(None, allow_mutation=True)
    band_configuration: T.Optional[str] = Field(None, allow_mutation=True)
    bio: T.Optional[str] = Field(None, allow_mutation=True)
    category: T.Optional[Category] = Field(None, allow_mutation=True)
    contact_information: T.Optional[str] = Field(None, allow_mutation=True)
    cover_image: T.Optional[str] = Field(None, allow_mutation=True)
    last_backend_updated: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_redis_refreshed: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    migration_version: T.Optional[int] = Field(None, allow_mutation=True)
    profile_image: T.Optional[str] = Field(None, allow_mutation=True)
    social_media: T.Optional[str] = Field(None, allow_mutation=True)
    spotify_id: T.Optional[str] = Field(None, allow_mutation=True)
    subgenres: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    venue_take_percentages: T.Optional[str] = Field(None, allow_mutation=True)
    version: T.Optional[int] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "slug": "std::str",
        "beatgig_id": "std::str",
        "created_at": "std::datetime",
        "name": "std::str",
        "connect_account_id": "std::str",
        "last_updated": "std::datetime",
        "published": "std::bool",
        "media": "std::str",
        "admin_details": "std::str",
        "band_configuration": "std::str",
        "bio": "std::str",
        "category": "std::str",
        "contact_information": "std::str",
        "cover_image": "std::str",
        "last_backend_updated": "std::datetime",
        "last_redis_refreshed": "std::datetime",
        "last_triggered_at": "std::datetime",
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
            "bio",
            "media",
            "band_configuration",
            "created_at",
            "category",
            "slug",
            "contact_information",
            "cover_image",
            "last_backend_updated",
            "spotify_id",
            "last_triggered_at",
            "subgenres",
            "name",
            "venue_take_percentages",
            "migration_version",
            "published",
            "admin_details",
            "connect_account_id",
            "social_media",
            "last_redis_refreshed",
            "version",
            "last_updated",
            "profile_image",
        }
        exclusive_fields: T.Set[str] = {"id", "slug", "beatgig_id"}


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


class BookingInsert(BaseModel):
    beatgig_id: str
    created_at: datetime
    performance_length_mins: int
    start_time: datetime
    negotiation_steps: str
    artist: ArtistResolver
    buyer: UserResolver
    account_exec: T.Optional[UserResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "beatgig_id": "std::str",
        "created_at": "std::datetime",
        "performance_length_mins": "std::int16",
        "start_time": "std::datetime",
        "negotiation_steps": "std::str",
    }


class Booking(Node[BookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    beatgig_id: str = Field(..., allow_mutation=False)
    created_at: datetime = Field(..., allow_mutation=True)
    performance_length_mins: int = Field(..., allow_mutation=True)
    start_time: datetime = Field(..., allow_mutation=True)
    negotiation_steps: str = Field(..., allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "beatgig_id": "std::str",
        "created_at": "std::datetime",
        "performance_length_mins": "std::int16",
        "start_time": "std::datetime",
        "negotiation_steps": "std::str",
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

    async def update(
        self,
        given_resolver: BookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        artist: T.Optional[ArtistResolver] = None,
        buyer: T.Optional[UserResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
    ) -> None:
        set_links_d = {"artist": artist, "buyer": buyer, "account_exec": account_exec}
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
            "negotiation_steps",
            "performance_length_mins",
            "created_at",
            "start_time",
        }
        exclusive_fields: T.Set[str] = {"id", "beatgig_id"}


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


Booking.GraphORM.resolver_type = BookingResolver


class UserInsert(BaseModel):
    phone_number: str
    slug: str
    beatgig_id: str
    firebase_id: str
    email: str
    created_at: datetime
    name: str
    approved: bool
    last_updated: datetime
    metadata: str
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
    bookings: T.Optional[BookingResolver] = None
    account_exec_bookings: T.Optional[BookingResolver] = None
    venues: T.Optional[VenueResolver] = None
    venues_assigned_to: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "phone_number": "std::str",
        "slug": "std::str",
        "beatgig_id": "std::str",
        "firebase_id": "std::str",
        "email": "std::str",
        "created_at": "std::datetime",
        "name": "std::str",
        "approved": "std::bool",
        "last_updated": "std::datetime",
        "metadata": "std::str",
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
    beatgig_id: str = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    email: str = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    approved: bool = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    metadata: str = Field(..., allow_mutation=True)
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
        "beatgig_id": "std::str",
        "firebase_id": "std::str",
        "email": "std::str",
        "created_at": "std::datetime",
        "name": "std::str",
        "approved": "std::bool",
        "last_updated": "std::datetime",
        "metadata": "std::str",
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
        bookings: T.Optional[BookingResolver] = None,
        account_exec_bookings: T.Optional[BookingResolver] = None,
        venues: T.Optional[VenueResolver] = None,
        venues_assigned_to: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {
            "artists": artists,
            "bookings": bookings,
            "account_exec_bookings": account_exec_bookings,
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
            "approval",
            "metadata",
            "email",
            "user_type",
            "phone_number",
            "admin_permissions",
            "default_state_abbr",
            "last_triggered_at",
            "user_role",
            "referred_by_id",
            "name",
            "slug",
            "created_at",
            "admin_type",
            "last_updated",
            "profile_image",
            "approved",
        }
        exclusive_fields: T.Set[str] = {
            "firebase_id",
            "phone_number",
            "id",
            "slug",
            "beatgig_id",
        }


class UserResolver(Resolver[User]):
    _node = User

    def artists(self, _: T.Optional[ArtistResolver] = None, /) -> UserResolver:
        if "artists" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `artists` has already been provided."
            )
        self._nested_resolvers["artists"] = _ or ArtistResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> UserResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
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
        updatable_fields: T.Set[str] = {"title", "year"}
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
    last_name: T.Optional[str] = None
    full_name: T.Optional[str] = None
    tags: T.Optional[T.Set[str]] = None
    ordered_tags: T.Optional[T.List[str]] = None
    created_at: T.Optional[datetime] = None
    my_followers: T.Optional[PersonResolver] = None
    best_friend: T.Optional[PersonResolver] = None
    people_i_follow: T.Optional[PersonResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": "std::str",
        "inserted_at": "std::datetime",
        "first_name": "std::str",
        "last_name": "std::str",
        "full_name": "std::str",
        "tags": "std::str",
        "ordered_tags": "array<std::str>",
        "created_at": "std::datetime",
    }


class Person(Node[PersonInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    inserted_at: datetime = Field(..., allow_mutation=False)
    first_name: str = Field(..., allow_mutation=True)
    last_name: T.Optional[str] = Field(None, allow_mutation=True)
    full_name: T.Optional[str] = Field(None, allow_mutation=True)
    tags: T.Optional[T.Set[str]] = Field(None, allow_mutation=True)
    ordered_tags: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "slug": "std::str",
        "inserted_at": "std::datetime",
        "first_name": "std::str",
        "last_name": "std::str",
        "full_name": "std::str",
        "tags": "std::str",
        "ordered_tags": "array<std::str>",
        "created_at": "std::datetime",
    }

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

    async def update(
        self,
        given_resolver: PersonResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        my_followers: T.Optional[PersonResolver] = None,
        best_friend: T.Optional[PersonResolver] = None,
        people_i_follow: T.Optional[PersonResolver] = None,
    ) -> None:
        set_links_d = {
            "my_followers": my_followers,
            "best_friend": best_friend,
            "people_i_follow": people_i_follow,
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
            "first_name",
            "tags",
            "full_name",
            "last_name",
            "slug",
            "created_at",
            "ordered_tags",
        }
        exclusive_fields: T.Set[str] = {"id", "slug"}


class PersonResolver(Resolver[Person]):
    _node = Person

    def my_followers(self, _: T.Optional[PersonResolver] = None, /) -> PersonResolver:
        if "my_followers" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `my_followers` has already been provided."
            )
        self._nested_resolvers["my_followers"] = _ or PersonResolver()
        return self

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


Person.GraphORM.resolver_type = PersonResolver


class VenueInsert(BaseModel):
    slug: str
    beatgig_id: str
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
    bookings: T.Optional[BookingResolver] = None
    account_exec: T.Optional[UserResolver] = None
    owners: T.Optional[UserResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": "std::str",
        "beatgig_id": "std::str",
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
    slug: str = Field(..., allow_mutation=True)
    beatgig_id: str = Field(..., allow_mutation=False)
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
        "slug": "std::str",
        "beatgig_id": "std::str",
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

    async def update(
        self,
        given_resolver: VenueResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        created_by: T.Optional[UserResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
        owners: T.Optional[UserResolver] = None,
    ) -> None:
        set_links_d = {
            "created_by": created_by,
            "bookings": bookings,
            "account_exec": account_exec,
            "owners": owners,
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
            "budget",
            "created_at",
            "logo",
            "slug",
            "place_id",
            "location",
            "phone_number",
            "production_and_venue_specs",
            "display_images",
            "name",
            "capacity",
            "colors",
            "images",
            "genres_booked",
            "customer_id",
            "website",
            "social_media",
            "venue_type",
            "last_updated",
            "num_stages",
        }
        exclusive_fields: T.Set[str] = {"id", "slug", "beatgig_id"}


class VenueResolver(Resolver[Venue]):
    _node = Venue

    def created_by(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "created_by" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `created_by` has already been provided."
            )
        self._nested_resolvers["created_by"] = _ or UserResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> VenueResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
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


Venue.GraphORM.resolver_type = VenueResolver


class AnimalInsert(BaseModel):
    public_id: str
    slug: str
    name: str
    animal_type: AnimalType
    description: T.Optional[str] = None
    age: T.Optional[int] = None
    created_at: T.Optional[datetime] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "public_id": "std::str",
        "slug": "std::str",
        "name": "std::str",
        "animal_type": "std::str",
        "description": "std::str",
        "age": "std::int16",
        "created_at": "std::datetime",
    }


class Animal(Node[AnimalInsert]):
    id: UUID = Field(..., allow_mutation=False)
    public_id: str = Field(..., allow_mutation=True)
    slug: str = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    animal_type: AnimalType = Field(..., allow_mutation=True)
    description: T.Optional[str] = Field(None, allow_mutation=True)
    age: T.Optional[int] = Field(None, allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": "std::uuid",
        "public_id": "std::str",
        "slug": "std::str",
        "name": "std::str",
        "animal_type": "std::str",
        "description": "std::str",
        "age": "std::int16",
        "created_at": "std::datetime",
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
            "description",
            "animal_type",
            "name",
            "slug",
            "created_at",
            "age",
            "public_id",
        }
        exclusive_fields: T.Set[str] = {"id", "public_id", "slug"}


class AnimalResolver(Resolver[Animal]):
    _node = Animal


Animal.GraphORM.resolver_type = AnimalResolver

ArtistInsert.update_forward_refs()
BookingInsert.update_forward_refs()
UserInsert.update_forward_refs()
MovieInsert.update_forward_refs()
PersonInsert.update_forward_refs()
VenueInsert.update_forward_refs()
AnimalInsert.update_forward_refs()
