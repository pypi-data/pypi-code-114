from typing import Any, Iterator, Optional

from automagically.response import AutomagicallyResponse, PageResponse
from requests import Response


class AutomagicallyServiceAPI:
    def __init__(self, automagically_client, relative_url: str):
        self.relative_url = relative_url
        self.client = automagically_client

    def list(self) -> Response:
        return self.client.do_service_request("GET", self.relative_url)

    def send(self, data: dict) -> Response:
        return self.client.do_service_request("POST", self.relative_url, data)

    def retrieve(self, data_object_id: str) -> Response:
        return self.client.do_service_request(
            "GET", f"{self.relative_url}{data_object_id}"
        )

    def iterate_over_pages(
        self, page_size: Optional[int] = None
    ) -> Iterator[PageResponse]:
        page = self.get_page_from_response(
            self.client.do_service_request(
                "GET", self.relative_url, params={"page_size": page_size}
            )
        )

        while True:
            yield page

            if not page.next:
                break

            page = self.get_page_from_response(
                self.client.do_service_request(method="GET", url_for_request=page.next)
            )

    def iterate_over_records(self) -> Iterator[dict]:
        for page in self.iterate_over_pages():
            for record in page.results:
                yield record

    def get_page_from_response(self, response: AutomagicallyResponse) -> PageResponse:
        return PageResponse(
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
            url=response.url,
            method=response.method,
        )
