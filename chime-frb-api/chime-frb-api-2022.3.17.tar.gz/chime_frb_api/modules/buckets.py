"""CHIME/FRB Bucket API v2."""

from typing import Any, Dict, List, Optional

from chime_frb_api.core import API


class Buckets(API):
    """CHIME/FRB Backend Bucket API."""

    def __init__(
        self,
        debug: bool = False,
        base_url: str = "http://localhost:8000",
        authentication: bool = False,
    ):
        """Initialize the Buckets API.

        Args:
            debug (bool, optional): Whether to enable debug mode. Defaults to False.
            base_url (_type_, optional): The base URL of the API.
                Defaults to "http://localhost:8000".
            authentication (bool, optional): Whether to enable authentication.
                Defaults to False.
        """
        API.__init__(
            self,
            debug=debug,
            default_base_urls=["http://frb-vsop.chime:8004", "http://localhost:8004"],
            base_url=base_url,
            authentication=authentication,
        )

    def deposit(self, works: List[Dict[str, Any]]) -> bool:
        """Deposit works into the buckets backend.

        Args:
            works (List[Dict[str, Any]]): The payload from the Work Object.

        Returns:
            bool: Whether the works were deposited successfully.

        Examples:
        >>> from chime_frb_api.buckets import Buckets
        >>> from chime_frb_api.tasks import Work
        >>> work = Work(pipeline="sample")
        >>> status = buckets.deposit([work.payload])
        """
        return self.post(url="/work", json=works)

    def withdraw(
        self,
        pipeline: str,
        event: Optional[List[int]] = None,
        site: Optional[str] = None,
        priority: Optional[int] = None,
        user: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Withdraw `queued` work from the buckets backend.

        Args:
            pipeline (str): The pipeline to withdraw from. Required.
            event (Optional[List[int]], optional): The event to withdraw from.
            site (Optional[str], optional): The site to withdraw from.
            priority (Optional[int], optional): The priority to withdraw from.
            user (Optional[str], optional): The user to withdraw from.

        Returns:
            Dict[str, Any]: The work withdrawn.
        """
        query: Dict[str, Any] = {"pipeline": pipeline}
        if site:
            query["site"] = site
        if priority:
            query["priority"] = priority
        if user:
            query["user"] = user
        if event:
            query["event"] = {"$in": event}
        print(query)
        response: Dict[str, Any] = self.post(url="/work/withdraw", json=query)
        return response

    def update(self, works: List[Dict[str, Any]]) -> bool:
        """Update works in the buckets backend.

        Args:
            works (List[Dict[str, Any]]): The payload from the Work Object.

        Returns:
            bool: Whether the works were updated successfully.
        """
        response: bool = self.put(url="/work", json=works)
        return response

    def delete_ids(self, ids: List[str]) -> bool:
        """Delete works from the buckets backend with the given ids.

        Args:
            ids (List[str]): The IDs of the works to delete.

        Returns:
            bool: Whether the works were deleted successfully.
        """
        return self.delete(url="/work", params={"ids": ids})

    def delete_many(
        self,
        pipeline: str,
        status: Optional[str] = None,
        events: List[Optional[int]] = None,
    ) -> bool:
        """Delete works belonging to a pipeline from the buckets backend.

        If a status is provided, only works with that status will be deleted.
        If an event number is provided, only works with that event will be deleted.

        Args:
            pipeline (str): The pipeline to delete works from.
            status (Optional[List[str]]): The status to delete works with.
            e.g. ["queued"].
            event (Optional[int]): The event to delete works with.

        Returns:
            bool: Whether the works were deleted successfully.
        """
        query: Dict[str, Any] = {"pipeline": pipeline}
        if status:
            query["status"] = status
        if events:
            query["event"] = {"$in": events}
        projection = {"id": True}
        result = self.view(query, projection)
        ids: List[str] = []
        if result:
            for work in result:
                ids.append(work["id"])
        return self.delete_ids(ids)

    def status(self, pipeline: Optional[str] = None) -> Dict[str, Any]:
        """View the status of the buckets backend.

        If overall is True, the status of all pipelines will be returned.

        Args:
            pipeline (Optional[str], optional): The pipeline to return the status of.

        Returns:
            List[Dict[str, Any]]: The status of the buckets backend.
        """
        if pipeline:
            return self.get(url=f"/status/details/{pipeline}")
        else:
            return self.get(url="/status")

    def pipelines(self) -> List[str]:
        """View the current pipelines in the buckets backend.

        Returns:
            List[str]: The current pipelines.
        """
        return self.get("/status/pipelines")

    def view(
        self,
        query: Dict[str, Any],
        projection: Dict[str, bool],
        skip: int = 0,
        limit: Optional[int] = 100,
    ) -> List[Dict[str, Any]]:
        """View works in the buckets backend.

        Args:
            query (Dict[str, Any]): The query to filter the works with.
            projection (Dict[str, bool]): The projection to use to map the output.
            skip (int, optional): The number of works to skip. Defaults to 0.
            limit (Optional[int], optional): The number of works to limit to.
                Defaults to 100.

        Returns:
            List[Dict[str, Any]]: The works matching the query.
        """
        payload = {
            "query": query,
            "projection": projection,
            "skip": skip,
            "limit": limit,
        }
        response: List[Dict[str, Any]] = self.post("/view", json=payload)
        return response

    def audit(self) -> Dict[str, Any]:
        """Audit work buckets backend.

        The audit process retries failed work, expires any work past the
        expiration time and checks for any stale work older than 31.0 days.

        Returns:
            Dict[str, Any]: The audit results.
        """
        return {
            "failed": self.get("/audit/failed"),
            "expired": self.get("/audit/expired"),
            "stale": self.get("/audit/stale/31.0"),
        }
