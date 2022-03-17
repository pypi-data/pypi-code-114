import sys


def main():
    if len(sys.argv) > 1:
        x = sys.argv[1]
    else:
        x = 88
    return f"hello, {x}"


if __name__ == "__main__":
    print(main())
