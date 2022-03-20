from pathlib import Path


def ensure_path(*, path: Path):
    """
    Ensure a path exists.

    :param path: The path to ensure.

    :return None
    """

    path.mkdir(parents=True, exist_ok=True)
