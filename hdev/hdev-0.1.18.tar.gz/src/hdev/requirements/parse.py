from pathlib import Path


def parse(
    lines,
    base_dir=None,
    ref_factory=lambda operation, file_name: (operation, file_name),
    dep_factory=str,
):
    """Parse a requirements file.

    :param lines: An iterable of strings
    :param base_dir: The directory from which this file was read (for relative
        file references)
    :param ref_factory: The function to call to generate file references
    :param dep_factory: The function to call to generate plain dependencies
    :return: A generator of parsed results
    :rtype: The return types of the factory methods

    :raises TypeError: If relative file references are found and no `base_dir`
        is provided
    """
    base_dir = Path(base_dir) if base_dir is not None else None

    for line in lines:
        line = line.strip()

        # Skip blank and entirely comment lines
        if line.startswith("#") or not line:
            continue

        # Strip trailing comments
        if "#" in line:
            line = line[: line.index("#")].strip()

        # Lines with pip operations like `-r`, `-c` or `-e`
        if line.startswith("-"):
            yield from _parse_pip_command_line(line, base_dir, ref_factory)
        else:
            yield dep_factory(line)


def _parse_pip_command_line(line, base_dir, ref_factory):
    operation = line[:2]

    if operation == "-e":
        # No need to handle editable things yet
        return

    file_name = line[2:].strip()
    if file_name.startswith("/"):
        # Absolute file references
        file_name = Path(file_name)

    else:
        # Relative file references
        if not base_dir:
            raise TypeError("base_dir must be specified to handle relative references")

        # Make relative files relative to us
        file_name = base_dir / file_name

    ref = ref_factory(operation, file_name.absolute())
    if ref:
        yield ref
