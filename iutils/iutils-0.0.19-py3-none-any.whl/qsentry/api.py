import requests
import jmespath

from urllib.parse import urljoin


class SentryApi:
    def __init__(self, host_url, auth_token):
        self.host_url = host_url
        self.auth_header = {"Authorization": f"Bearer {auth_token}"}

    def page_iterator(self, url):
        """Return an iterator that goes through the paginated results.

        See https://docs.sentry.io/api/pagination/ for Sentry's pagination API.
        """

        while True:
            res = requests.get(url, headers=self.auth_header)
            if res.status_code == requests.codes.ok:
                yield res
                if res.links and res.links["next"]["results"] == "true":
                    url = res.links["next"]["url"]
                else:
                    break
            else:
                res.raise_for_status()

    def filter_by_role_name(
        self, org_slug, team_slug, role_name, attributes=["id", "email"]
    ):
        """Filter by a role name.

        Given a role name, return a list of members represented by member attributes listed in the
        attributes argument.
        """

        # construct a jmespath multiselect hash
        multiselect_hash = ""
        for attr in attributes:
            multiselect_hash += f"{attr}: {attr}, "
        multiselect_hash = multiselect_hash[0:-2]  # remove the trailing ", "

        members = []
        for page in self.page_iterator(
            urljoin(self.host_url, f"/api/0/teams/{org_slug}/{team_slug}/members/")
        ):
            members += jmespath.search(
                f"[?role == '{role_name}' && flags.\"sso:linked\"].{{{multiselect_hash}}}",
                page.json(),
            )
        return members

    def get_all_teams(self, org_slug):
        """Return all teams of the given organization."""

        teams = []
        for page in self.page_iterator(
            urljoin(self.host_url, f"/api/0/organizations/{org_slug}/teams/")
        ):
            teams += jmespath.search(
                "[].{slug: slug, member_count: memberCount}",
                page.json(),
            )
        return teams
