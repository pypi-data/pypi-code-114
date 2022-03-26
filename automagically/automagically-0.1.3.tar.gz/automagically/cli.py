"""Console script for automagically."""

import fire


def help():
    print("Automagically")
    print("=" * len("automagically"))
    print("Python SDK für Automagically")


def version():
    print("Version: 0.1.3")


def main():
    fire.Fire({"help": help, "version": version})


if __name__ == "__main__":
    main()  # pragma: no cover
