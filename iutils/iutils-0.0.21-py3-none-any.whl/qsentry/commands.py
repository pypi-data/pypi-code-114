import jmespath
import pprint

from .api import SentryApi


def multiselect_hash_string(attributes):
    """Construct and return a jmespath multiselect hash."""
    return "{" + ", ".join([f"{attr}: {attr}" for attr in attributes]) + "}"


class Command:
    def __init__(self, **kwargs):
        self.host_url = kwargs["host_url"]
        self.org_slug = kwargs["org"]
        self.auth_token = kwargs["auth_token"]
        self.print_count = kwargs["count"]
        self.count = 0


class MembersCommand(Command):
    def run(self, **kwargs):
        if kwargs["team"]:
            self.handle_the_team_option(kwargs["team"], kwargs["role"])
        elif kwargs["search_by"]:
            self.handle_the_search_by_option(search_by_term=kwargs["search_by"])
        elif kwargs["list_all"]:
            self.handle_the_list_all_option(attrs=kwargs["list_all"])

    def handle_the_list_all_option(self, attrs):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_members_api():
            for member in jmespath.search(
                f"[].{ multiselect_hash_string(attrs) }", page
            ):
                print(", ".join(member.values()))
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")

    def handle_the_search_by_option(self, search_by_term):
        key, value = search_by_term.split("=")
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_members_api():
            for member in page:
                if member.get(key) == value:
                    pprint.pprint(member)

    def handle_the_team_option(self, team_slug, role):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).teams_members_api(team_slug):
            for member in jmespath.search(
                f"[?role == '{role}' && flags.\"sso:linked\"].{ multiselect_hash_string(['id', 'name', 'email']) }",
                page,
            ):
                print(f"{member['id']}, {member['name']}, {member['email']}")
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")


class OrgsCommand(Command):
    def run(self, **kwargs):
        if kwargs["list_members"]:
            for page in SentryApi(
                self.host_url, self.org_slug, self.auth_token
            ).org_members_api():
                for member in page:
                    print(f"{member['id']}, {member['email']}, {member['role']}")
                    self.count += 1
            if self.print_count:
                print(f"Count: {self.count}")


class TeamsCommand(Command):
    def run(self, **kwargs):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_teams_api():
            for team in page:
                print(f"{team['slug']}")
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")
