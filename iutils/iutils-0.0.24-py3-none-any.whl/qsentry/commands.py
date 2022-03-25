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
    def list_command(self, **kwargs):
        if kwargs["team"]:
            self.handle_the_team_option(kwargs["team"], kwargs["role"])
        elif kwargs["all"]:
            if kwargs["attrs"]:
                self.handle_the_list_all_option(attrs=kwargs["attrs"])
            else:
                self.handle_the_list_all_option(attrs=["id", "email"])

    def search_by(self, search_by_term):
        key, value = search_by_term.split("=")
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_members_api():
            for member in page:
                if member.get(key) == value:
                    pprint.pprint(member)
                    return None

    def handle_the_list_all_option(self, attrs):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_members_api():
            for member in jmespath.search(
                f"[].{ multiselect_hash_string(attrs) }", page
            ):
                print(", ".join([str(val) for val in member.values()]))
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")

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
    def list_projects(self, attrs):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_projects_api():
            for member in jmespath.search(
                f"[].{ multiselect_hash_string(attrs) }", page
            ):
                print(", ".join([str(val) for val in member.values()]))
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")

    def list_users(self, attrs):
        for page in SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).org_users_api():
            for member in jmespath.search(
                f"[].{ multiselect_hash_string(attrs) }", page
            ):
                print(", ".join([str(val) for val in member.values()]))
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")

        print(
            "Warning: this command may not list all users for the org_users "
            "api does not paginate. Use the members command instead for full "
            "list of members."
        )


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
