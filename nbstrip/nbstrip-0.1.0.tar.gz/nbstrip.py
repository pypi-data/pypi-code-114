import json
import os.path
from argparse import ArgumentParser


def strip_recursively(data, metadata=True, outputs=True, execution=True):
    failures = set()
    kwargs = dict(metadata=metadata, outputs=outputs, execution=execution)
    if isinstance(data, list):
        for elem in data:
            failures.update(strip_recursively(elem, **kwargs))
        return failures
    elif not isinstance(data, dict):
        return failures
    for key in data:
        if key == "metadata" and metadata:
            if data[key] != dict():
                failures.add("metadata")
                data[key] = dict()
        elif key == "outputs" and outputs:
            if data[key] != list():
                failures.add("outputs")
                data[key] = list()
        elif key == "execution_count" and execution:
            if data[key] is not None:
                failures.add("execution_count")
                data[key] = None
        else:
            failures.update(strip_recursively(data[key], **kwargs))
    return failures


def main() -> int:
    parser = ArgumentParser("Notebook stripper")
    parser.add_argument("inputs", nargs="*")
    parser.add_argument("-m", "--metadata", "-m", type=bool, default=True)
    parser.add_argument("-o", "--outputs", type=bool, default=True)
    parser.add_argument("-e", "--execution-count", type=bool, default=True)
    parser.add_argument("-i", "--inplace", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-c", "--check", action="store_true")
    parser.add_argument("--only-cell-metadata", action="store_true")

    args = parser.parse_args()
    failures = 0
    for input in args.inputs:
        with open(input, "r") as ff:
            data = json.load(ff)
        if args.only_cell_metadata:
            check = data["cells"]
        else:
            check = data
        passing = strip_recursively(
            check, args.metadata, args.outputs, args.execution_count
        )
        failures += int(len(passing) > 0)
        if args.verbose:
            if len(passing) > 0:
                print(f"{input}: FAIL {passing}")
            else:
                print(f"{input}: PASS")
        if args.check:
            continue
        if args.inplace:
            output = input
        else:
            split_name = os.path.splitext(input)
            output = "".join([split_name[0], ".stripped", split_name[1]])
        with open(output, "w") as ff:
            json.dump(data, ff, indent=1)
    if args.verbose:
        print(f"{failures} of {len(args.inputs)} reformatted")
    raise SystemExit(int(failures > 0))


if __name__ == "__main__":
    main()
