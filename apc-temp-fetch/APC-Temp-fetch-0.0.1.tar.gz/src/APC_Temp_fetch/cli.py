# output format: host[\t]temperature_in_°C
# NOTE: this program does not submit results to mqtt (separation of responsibilities)

import argparse
import logging
import sys
import time
from . import KINDS
from .base import ATF_LOGGER

class UnknownFetcher(Exception):
    pass
def run_one(kind: str, host: str, user: str, password: str, timeout) -> None:
    x = None
    try:
        x = KINDS[kind]
    except KeyError:
        raise UnknownFetcher('unknown fetcher: ' + kind)
    rqa = {}
    if timeout:
        rqa['timeout'] = timeout
    val = x.extract(x(host, rqa).fetch(user, password))
    if val:
        print(f"{host}\t{val}")

def main_one() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("kind", help="APC interface kind (one of: old frmnc cs141)")
    parser.add_argument("host", help="connect to the host (APC) via HTTP")
    parser.add_argument("user", help="with the given user")
    parser.add_argument("password", help="with the given pass")
    parser.add_argument("--timeout", help="set a timeout (in seconds) for each request execution (per request)", type=float)
    args = parser.parse_args()
    del parser
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    ch.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    ATF_LOGGER.addHandler(ch)
    ATF_LOGGER.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    try:
        run_one(args.kind, args.host, args.user, args.password, args.timeout)
    except Exception as e:
        ATF_LOGGER.exception(args.host)

def main_list() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("apclist", help="file containing list of 'kind host user password [timeout]'")
    args = parser.parse_args()
    del parser
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    ch.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    ATF_LOGGER.addHandler(ch)
    ATF_LOGGER.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    with open(args.apclist, 'r') as apclist:
        for line in apclist:
            parts = line.split()
            if not parts or parts[0] == '#':
                pass
            elif len(parts) < 4:
                ATF_LOGGER.error(F'got invalid apclist line: {line}')
            else:
                kind, host, user, password = parts[:4]
                try:
                    timeout = float(parts[4]) if len(parts) > 4 else None
                    run_one(kind, host, user, password, timeout)
                except Exception as e:
                    ATF_LOGGER.exception(host)
