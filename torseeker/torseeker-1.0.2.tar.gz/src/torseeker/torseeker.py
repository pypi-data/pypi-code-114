#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# TorSeeker
#
# A tool used to query information about Tor relays by using a two
# letter country code or via Tor IP addresses.
#
# ASCII Art REF:
# https://patorjk.com/software/taag/#p=display&f=Slant&t=TorSeeker
#

import json
import re
import requests
import argparse


# Package information
__package__     = "torseeker"
__version__     = "1.0.2"
__license__     = "MIT"
__author__      = "eldiablo"
__email__       = "avsarria@gmail.com"
__url__         = "http://github.com/rwprimitives/tor-seeker"
__bug_tracker__ = "https://github.com/rwprimitives/tor-seeker/issues"
__date__        = "03/23/2022"
__copyright__   = "Copyright (c) 2022 rwprimitives"
__description__ = "A tool used to query information about Tor relays " \
                  "by using a two letter country code or via Tor IP "  \
                  "addresses."


class TorNode:
    """
    The TorNode class defines a Tor relay.

    This class provides the ability to parse raw JSON data containing information
    about a Tor relay. The `parse_new_data()` function consumes raw JSON data and
    populates the following members which are accessible via this class:

    * **first_seen** - The date and time when the Tor relay was first seen online\n
    * **last_seen** - The date and time the Tor relay was last seen online
    * **last_restarted** - The date and time the Tor relay was restarted
    * **country** - The two letter country code the Tor relay resides
    * **country_name** - The country name the Tor relay resides
    * **nickname** - A name assigned to the Tor relay
    * **ipv4** - The IP address version 4
    * **ipv4_port** - The port number of the IPv4 address
    * **ipv6** - The IP address version 6
    * **ipv6_port** - The port number of the IPv6 address
    * **raw_data** - The raw JSON data about the Tor relay

    """

    def __init__(self):
        """Constructor method.
        """

        self.raw_data = ""
        self.first_seen = ""
        self.last_seen = ""
        self.last_restarted = ""
        self.country = ""
        self.country_name = ""
        self.nickname = ""
        self.ipv4 = ""
        self.ipv4_port = ""
        self.ipv6 = ""
        self.ipv6_port = ""

    def parse_raw_data(self, raw_data):
        """Parse raw JSON data about a given Tor relay.

        :param raw_data: a dictionary containing information about a Tor relay
        :type: dict
        """

        self.raw_data = raw_data
        self.first_seen = raw_data["first_seen"]
        self.last_seen = raw_data["last_seen"]
        self.last_restarted = raw_data["last_restarted"]
        self.country = raw_data["country"]
        self.country_name = raw_data["country_name"]
        self.nickname = raw_data["nickname"]

        # The IP addresses are combined, so we must separate them
        or_addresses = raw_data["or_addresses"]

        # IPv4 is always available, so we know it's first
        self.ipv4 = or_addresses[0].split(":")[0]
        self.ipv4_port = or_addresses[0].split(":")[1]
        self.ipv6 = ""
        self.ipv6_port = ""

        # If IPv6 is available, then it's the second item in the list
        if len(or_addresses) == 2:
            s = or_addresses[1]
            self.ipv6 = s[s.find("[") + 1:s.find("]")]
            self.ipv6_port = s[s.rfind(":") + 1:]

    def __str__(self):
        data = f"{self.ipv4 : <15} | "
        data += f"Port: {self.ipv4_port}, "
        data += f"Nickname: {self.nickname}, "
        data += f"Country: {self.country_name}, "
        data += f"First seen: {self.first_seen}, "
        data += f"Last seen: {self.last_seen}, "
        data += f"Last restarted: {self.last_restarted}"

        # If IPv6 is available, then print it
        if len(self.ipv6):
            return f"{data}, IPv6: {self.ipv6}, IPv6 Port: {self.ipv6_port}"
        else:
            return data


class TorSeeker:
    """
    The TorSeeker class provides two methods for querying information about Tor
    relays: two letter country code, one or multiple Tor IP addresses.
    Once a query is performed, Tor relays are stored in separate lists based on
    the type of relay, ie: Guard, Middle or Exit.

    Logging is available to display error messages encountered during the process.
    However, logging is disabled by default. Use the function set_logging() to
    enable logging if desired.

    :param country: optional two letter country code
    :type: str
    """

    # URL used for querying information about tor nodes
    TOR_QUERY_URL = "https://onionoo.torproject.org/details?"

    # List of all country codes
    COUNTRY_CODES = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG",
                     "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB",
                     "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW",
                     "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM",
                     "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM",
                     "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ",
                     "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE",
                     "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF",
                     "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP",
                     "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN",
                     "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL",
                     "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR",
                     "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT",
                     "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ",
                     "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS",
                     "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI",
                     "NE", "NG", "NU", "NF", "MK", "MP", "NO", "OM", "PK", "PW",
                     "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR",
                     "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF",
                     "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL",
                     "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES",
                     "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ",
                     "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC",
                     "TV", "UG", "UA", "AE", "GB", "UM", "US", "UY", "UZ", "VU",
                     "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]

    # Regex for validating an IPv4 address
    IPV4_REGEX = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    def __init__(self, country=None):
        """Constructor method.

        :param country: optional two letter country code
        :type: str
        """

        self.country = country
        self.country_name = ""
        self.json_data = ""
        self.all_relays = []
        self.guard_relays = []
        self.middle_relays = []
        self.exit_relays = []
        self._is_logging = False
        self.ipv4_re = re.compile(self.IPV4_REGEX)

    def _loge(self, message):
        if self._is_logging:
            print(f"ERROR: {message}")

    def _is_ipv4(self, ipv4):
        if self.ipv4_re.match(ipv4):
            return True
        return False

    def _http_request(self, url, params, timeout=10):
        content = ""

        if timeout > 0:
            try:
                response = requests.get(url, params=params, timeout=timeout)
                if response.status_code == 200:
                    content = response.text
                else:
                    self._loge("Failed to perform query.")

            except requests.exceptions.HTTPError:
                self._loge("Invalid response")
            except requests.exceptions.ConnectionError:
                self._loge("Failed to establish connection")
            except requests.exceptions.TooManyRedirects:
                self._loge("Tor query URL is no longer valid")
            except requests.exceptions.Timeout:
                self._loge("Request timed out")
            except requests.exceptions.RequestException:
                self._loge("An unforseen error has occurred")

        return content

    def _query(self, params):
        status = 0
        json_data = ""

        raw_data = self._http_request(TorSeeker.TOR_QUERY_URL, params)

        if raw_data:
            try:
                json_data = json.loads(raw_data)
                status = self._parse_relays(json_data)
            except json.JSONDecodeError:
                self._loge("The JSON data acquired is invalid")

        return status

    def _add_relay(self, raw_relay):
        tor_node = TorNode()
        tor_node.parse_raw_data(raw_relay)

        self.all_relays.append(tor_node)

        # Get the probability values for the relay
        guard_prob = raw_relay["guard_probability"]
        middle_prob = raw_relay["middle_probability"]
        exit_prob = raw_relay["exit_probability"]

        # A Guard relay must be stable and fast (at least 2MByte/s).
        # If a relay does not meet those requirements, then it's demoted
        # to be a middle relay. A Middle relay can be promoted to be a
        # Guard relay if it meets the desired critera for Guard relays
        if guard_prob > middle_prob:
            self.guard_relays.append(tor_node)

        if middle_prob > guard_prob:
            self.middle_relays.append(tor_node)

        # Exit relays will never be Guard or Middle relays,
        # so only need to check if the probability is greater than zero
        if exit_prob > 0:
            self.exit_relays.append(tor_node)

    def _parse_relays(self, json_data):
        status = 0

        if json_data is None or json_data == "":
            self._loge("No tor relays are available")
        else:
            for raw_relay in json_data["relays"]:

                # skip relays that are not operational
                if not raw_relay["running"]:
                    continue

                # Get the name of the country for any relay. This is
                # only used when querying for relays of a specific country.
                # When querying for tor IP addresses, this is not reliable
                # as it will be updated based on the last IP address queried
                self.country_name = raw_relay["country_name"]

                self._add_relay(raw_relay)

            status = 1

        return status

    def set_logging(self, state):
        """Enable logging to stdout.

        :param state: True enables logging, False disables logging
        :type: bool
        """
        self._is_logging = state

    def query_relays_by_country(self, country=None):
        """Query for Tor relays based a two letter country code.
        This function performs input validation and verifies the
        two letter country code is valid. If 0 is returned, then
        the country code specified is invalid or there are no Tor
        relays located in that country.

        :param country: a two letter country code. This is optional if a country
                        code was defined via the constructor of this class
        :type: str

        :returns: 1 on successful query, 0 otherwise
        :rtype: int
        """

        status = 0
        ret = 0

        if country is None:
            country = self.country

        if country is None or not isinstance(country, str) or len(country) != 2 or \
           country.upper() not in self.COUNTRY_CODES:
            self._loge("Must enter a valid country code")
        else:
            params = f"search=country:{country}"
            ret = self._query(params)

            if ret:
                status = 1
            else:
                self._loge(f"Failed to seek tor data for country code '{country}'")

        return status

    def query_relays_by_ip(self, ip_addresses=None):
        """Query for Tor relays based on one or multiple Tor IP addresses.
        This functions performs input validation to verify that the IP
        addresses provided are valid IPv4 format. If 0 is returned, then
        the IP addresses specified are invalid or there are no Tor relays
        associated with those IP addresses.

        :param ip_addresses: a list of Tor IP addresses
        :type: list

        :returns: 1 on successful query, 0 otherwise
        :rtype: int
        """

        status = 0
        ret = 0

        if ip_addresses is None or not isinstance(ip_addresses, list) or len(ip_addresses) == 0:
            self._loge("Must enter one or multiple IP addresses inside a list")
        else:
            for ip in ip_addresses:
                if self._is_ipv4(ip):
                    params = f"search={ip}"
                    ret = self._query(params)

                    if ret:
                        status = 1
                    else:
                        self._loge(f"Failed to seek tor data for IP {ip}")
                        status = 0
                        break
                else:
                    self._loge(f"Invalid IP address '{ip}'")

        return status

    def get_all_relays(self):
        """Returns a list of TorNode objects for all Tor relay types.

        :returns: a list storing TorNode objects as elements,
                  None otherwise
        :rtype: list
        """

        return self.all_relays

    def get_guard_relays(self):
        """Returns a list of TorNode objects for Tor Guard relay types.

        :returns: a list storing TorNode objects as elements,
                  None otherwise
        :rtype: list
        """

        return self.guard_relays

    def get_middle_relays(self):
        """Returns a list of TorNode objects for Tor Middle relay types.

        :returns: a list storing TorNode objects as elements,
                  None otherwise
        :rtype: list
        """

        return self.middle_relays

    def get_exit_relays(self):
        """Returns a list of TorNode objects for Tor Exit relay types.

        :returns: a list storing TorNode objects as elements
        :rtype: list
        """

        return self.exit_relays


def print_relay_info(relays, relay_type=None):
    """Prints to stdout the information about the Tor relays.

    :param relays: a list of TorNode objects
    :type: list

    :param relay_type: a optional string identifying the type of Tor relays stored
                       in the list to print to stdout
    :type: str
    """

    if relay_type is not None and relay_type != "":
        title = f"{relay_type} [{len(relays)}]"
        print(title)
        print("-" * len(title))

    if relays:
        for relay in relays:
            print(relay)
    else:
        print("None")

    print("\n")


def get_banner():
    return("""\
  ______           _____           __
 /_  __/___  _____/ ___/___  ___  / /_____  _____
  / / / __ \/ ___/\__ \/ _ \/ _ \/ //_/ _ \/ ___/
 / / / /_/ / /   ___/ /  __/  __/ ,< /  __/ /
/_/  \____/_/   /____/\___/\___/_/|_|\___/_/
    """)


def get_version_info():
    info = get_banner()
    info += "\n"
    info += f"{__package__} v{__version__} \n"
    info += f"{__copyright__} \n"
    info += f"{__license__} \n"
    info += f"Written by {__author__}"
    return info


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__description__)

    parser.add_argument("-d", "--details",
                        help="show additional information",
                        dest="details",
                        action="store_true",
                        required=False)
    parser.add_argument("-v",
                        action="version",
                        version=get_version_info())

    # set -c and --ip arguments as mutual exclusion
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--country",
                       help="two letter country code of interest",
                       dest="country",
                       type=str,
                       metavar='',
                       required=False)
    group.add_argument("--ip",
                       help="one or more tor IP addresses spaced separated",
                       dest="ip_addresses",
                       type=str,
                       metavar='',
                       nargs='+',
                       required=False)
    return parser.parse_args()


def main():
    ret = -1

    args = parse_args()

    print(f"TorSeeker v{__version__} by {__author__}")
    print()

    tor_seeker = TorSeeker()
    tor_seeker.set_logging(True)

    if args.country:
        ret = tor_seeker.query_relays_by_country(args.country)

        if ret and len(tor_seeker.country_name):
            print(f"Country: {tor_seeker.country_name}")

    elif args.ip_addresses:
        ret = tor_seeker.query_relays_by_ip(args.ip_addresses)

    if ret > 0:
        print(f"Total relays: {len(tor_seeker.get_all_relays())}")
        print(f"Guard relays: {len(tor_seeker.get_guard_relays())}")
        print(f"Middle relays: {len(tor_seeker.get_middle_relays())}")
        print(f"Exit relays: {len(tor_seeker.get_exit_relays())}")
        print("\n")

        if args.details:
            print_relay_info(tor_seeker.get_guard_relays(), "GUARD RELAYS")
            print_relay_info(tor_seeker.get_middle_relays(), "MIDDLE RELAYS")
            print_relay_info(tor_seeker.get_exit_relays(), "EXIT RELAYS")
    else:
        print()


if __name__ == "__main__":
    main()
