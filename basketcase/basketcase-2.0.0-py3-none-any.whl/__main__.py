import argparse
from . import basketcase

def main():
    parser = argparse.ArgumentParser(description='Fetch resources from Instagram.')
    parser.add_argument('-l', '--login', action='store_true', help='Attempt to authenticate (interactively)')
    parser.add_argument('input_file', type=argparse.FileType('r'), help='A list of URLs separated by newline characters')
    args = parser.parse_args()

    urls = set()

    for line in args.input_file:
        line = line.rstrip()

        if line:
            urls.add(line)

    bc = basketcase.BasketCase()

    if args.login:
        bc.login()

    bc.fetch(urls)

if __name__ == '__main__':
    main()

