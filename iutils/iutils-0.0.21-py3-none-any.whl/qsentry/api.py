import requests

from urllib.parse import urljoin


class SentryApi:
    def __init__(self, host_url, org_slug, auth_token):
        self.host_url = host_url
        self.org_slug = org_slug
        self.auth_header = {"Authorization": f"Bearer {auth_token}"}

    def page_iterator(self, url):
        """Return an iterator that goes through the paginated results.

        See https://docs.sentry.io/api/pagination/ for Sentry's pagination API.
        """
        while True:
            res = requests.get(url, headers=self.auth_header)
            if res.status_code == requests.codes.ok:
                yield res.json()
                if res.links and res.links["next"]["results"] == "true":
                    url = res.links["next"]["url"]
                else:
                    break
            else:
                res.raise_for_status()

    def org_members_api(self):
        url = urljoin(self.host_url, f"/api/0/organizations/{self.org_slug}/members/")
        return self.page_iterator(url)

    def org_teams_api(self):
        url = urljoin(self.host_url, f"/api/0/organizations/{self.org_slug}/teams/")
        return self.page_iterator(url)

    def teams_members_api(self, team_slug):
        url = urljoin(
            self.host_url, f"/api/0/teams/{self.org_slug}/{team_slug}/members/"
        )
        return self.page_iterator(url)
