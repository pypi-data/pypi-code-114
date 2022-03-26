"""Console script for automagically."""

import fire


def help():
    print("Automagically")
    print("=" * len("automagically"))
    print("Python SDK für Automagically")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
