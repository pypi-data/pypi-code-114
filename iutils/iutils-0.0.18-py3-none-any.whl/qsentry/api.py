import requests
import jmespath


class SentryApi:
    def __init__(self, host_url, auth_token):
        self.host_url = host_url
        self.auth_header = {"Authorization": f"Bearer {auth_token}"}

    def filter_by_role_name(
        self, org_slug, team_slug, role_name, attributes=["id", "email"]
    ):
        """Filter by a role name.

        Given a role name, return a list of members represented by member attributes listed in the
        attributes argument.
        """

        r = requests.get(
            f"{self.host_url}/api/0/teams/{org_slug}/{team_slug}/members/",
            headers=self.auth_header,
        )
        if r.status_code == requests.codes.ok:
            # construct a jmespath multiselect hash
            multiselect_hash = ""
            for attr in attributes:
                multiselect_hash += f"{attr}: {attr}, "
            multiselect_hash = multiselect_hash[0:-2]  # remove the trailing ", "

            members = jmespath.search(
                f"[?role == '{role_name}' && flags.\"sso:linked\"].{{{multiselect_hash}}}",
                r.json(),
            )
            return members
        else:
            r.raise_for_status()
