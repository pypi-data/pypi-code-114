import jmespath

from .api import SentryApi


def multiselect_hash_string(attributes):
    """Construct and return a jmespath multiselect hash."""
    return "{" + ", ".join([f"{attr}: {attr}" for attr in attributes]) + "}"


class Command:
    def __init__(self, **kwargs):
        self.host_url = kwargs["host_url"]
        self.org_slug = kwargs["org"]
        self.auth_token = kwargs["auth_token"]
        self.count = kwargs["count"]


class MembersCommand(Command):
    def run(self, **kwargs):
        count = 0
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).teams_members_api(kwargs["team"]):
            for member in jmespath.search(
                f"[?role == '{kwargs['role']}' && flags.\"sso:linked\"].{ multiselect_hash_string(['id', 'name', 'email']) }",
                page,
            ):
                print(f"{member['id']}, {member['name']}, {member['email']}")
                count += 1
        if self.count:
            print(f"Count: {count}")


class OrgsCommand(Command):
    def run(self, **kwargs):
        count = 0
        if kwargs["list_members"]:
            for page in SentryApi(
                self.host_url, self.org_slug, self.auth_token
            ).org_members_api():
                for member in page:
                    print(f"{member['id']}, {member['email']}, {member['role']}")
                    count += 1
            if self.count:
                print(f"Count: {count}")


class TeamsCommand(Command):
    def run(self, **kwargs):
        count = 0
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_teams_api():
            for team in page:
                print(f"{team['slug']}")
        if self.count:
            print(f"Count: {count}")
