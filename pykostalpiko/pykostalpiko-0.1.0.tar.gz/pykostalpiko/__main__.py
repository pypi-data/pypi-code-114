import sys

from pykostalpiko.dxs import entries
from pykostalpiko.dxs.entries import Entries
from pykostalpiko.inverter import Inverter


def main() -> None:
    inv = Inverter(ip=sys.argv[1])

    values = inv.fetch(*Entries.__members__.values())

    print(values)


if __name__ == "__main__":
    main()
