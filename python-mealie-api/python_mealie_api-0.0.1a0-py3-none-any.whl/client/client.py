from typing import Any, Callable, Mapping, TypeVar

from pydantic import ValidationError

from ..exception import ClientException
from ..model import (
    MealPlanResponse,
    RecipeResponse,
    Response,
    StatisticsResponse,
    Status,
    TokenResponse,
    UserResponse,
)
from .http_client import HttpClient
from .token_repository import TokenRepository

T = TypeVar("T")


class Api:
    def __init__(
        self,
        http_client: HttpClient,
        base_url: str,
        token_repository: TokenRepository,
    ) -> None:
        self._http_client = http_client
        self._token_repository = token_repository
        self._base_url = base_url
        self._headers = {"accept": "application/json"}

    def _url(self, suffix: str) -> str:
        return f"{self._base_url}{suffix}"

    async def _get_authorization_header(self) -> Mapping[str, str]:
        access_token = await self._token_repository.get_token()
        return {"Authorization": f"Bearer {access_token}"}

    def _parse(
        self, response: Response, parser: Callable[[Mapping[str, Any] | None], T]
    ) -> T:
        if response.status == Status.FAILURE:
            raise ClientException("Bad response")

        try:
            return parser(response.data)
        except ValidationError as error:
            raise ClientException("Could not parse response") from error

    async def get_token(
        self, username: str, password: str, long_token: bool = False
    ) -> TokenResponse:
        url = (
            self._url("/api/auth/token/long")
            if long_token
            else self._url("/api/auth/token")
        )
        headers = self._headers
        response = await self._http_client.post(
            url=url,
            headers=headers,
            data={"username": username, "password": password},
        )

        token_reponse = self._parse(response=response, parser=TokenResponse.parse_obj)

        await self._token_repository.set_token(token=token_reponse.access_token)
        return token_reponse

    async def get_refresh_token(self) -> TokenResponse:
        url = self._url("/api/auth/refresh")
        headers = self._headers | await self._get_authorization_header()
        response = await self._http_client.get(url=url, headers=headers)

        token_reponse = self._parse(response=response, parser=TokenResponse.parse_obj)

        await self._token_repository.set_token(token=token_reponse.access_token)
        return token_reponse

    async def get_meal_plan_this_week(self) -> MealPlanResponse | None:
        url = self._url("/api/meal-plans/this-week")
        headers = self._headers | await self._get_authorization_header()

        meal_plan_response = await self._http_client.get(url=url, headers=headers)

        if meal_plan_response.data:
            return self._parse(
                response=meal_plan_response, parser=MealPlanResponse.parse_obj
            )
        else:
            return None

    async def get_user(self) -> UserResponse:
        url = self._url("/api/users/self")
        headers = self._headers | await self._get_authorization_header()
        user_response = await self._http_client.get(url=url, headers=headers)

        return self._parse(response=user_response, parser=UserResponse.parse_obj)

    async def get_statistics(self) -> StatisticsResponse:
        url = self._url("/api/debug/statistics")
        headers = self._headers | await self._get_authorization_header()
        statistics_response = await self._http_client.get(url=url, headers=headers)

        return self._parse(
            response=statistics_response, parser=StatisticsResponse.parse_obj
        )

    async def get_recipe_today(self) -> RecipeResponse | None:
        url = self._url("/api/meal-plans/today")
        headers = self._headers | await self._get_authorization_header()
        recipe_response = await self._http_client.get(url=url, headers=headers)

        if recipe_response.data:
            return self._parse(
                response=recipe_response, parser=RecipeResponse.parse_obj
            )
        else:
            return None
