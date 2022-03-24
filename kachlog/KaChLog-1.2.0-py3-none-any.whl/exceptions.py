class ChangelogDoesNotExistError(Exception):
    pass


class VersionDoesNotExistError(Exception):
    pass


class InvalidSemanticVersion(Exception):
    def __init__(self, version: str):
        super().__init__(
            f"{version} is not following semantic versioning. Check https://semver.org for more information."
        )
