#!/usr/bin/python3
"""
    ptprssi - Path-relative Stylesheet Import Vulnerability Testing Tool

    Copyright (c) 2020 HACKER Consulting s.r.o.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = "0.0.1"

import argparse
import sys
import urllib

from bs4 import BeautifulSoup, Comment
import requests

import ptlibs.ptjsonlib as ptjsonlib
import ptlibs.ptmisclib as ptmisclib


class ptprssi:
    def __init__(self, args):
        self.use_json      = args.json
        self.ptjsonlib     = ptjsonlib.ptjsonlib(self.use_json)
        self.json_no       = self.ptjsonlib.add_json(SCRIPTNAME)
        self.url           = self.parse_url(args.url)
        self.proxy         = {"https": args.proxy, "http": args.proxy}
        self.headers       = ptmisclib.get_request_headers(args)
        self.redirects     = args.redirects
        self.is_vulnerable = False

    def run(self):
        initial_response = self.get_response(payload="")
        if not self.redirects and initial_response.is_redirect:
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"Redirect: {initial_response.url} -> {initial_response.headers.get('location')}", "TITLE", self.use_json, colortext=True))
            ptmisclib.end_error(f"Not following redirects: [redirects disabled]", self.json_no, self.ptjsonlib, self.use_json)
        if initial_response.history and self.redirects:
            url_history = [h.url for h in initial_response.history]
            #ptmisclib.ptprint(ptmisclib.out_ifnot(f"Testing: {self.url}", "TITLE", self.use_json, colortext=True))
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"Redirect: {'-> '.join(url_history)} -> {initial_response.url}", "TITLE", self.use_json, colortext=True))
            self.url = initial_response.url
        ptmisclib.ptprint(ptmisclib.out_ifnot(f"Testing: {self.url}", "TITLE", self.use_json, colortext=True))

        for payload in ["", "foo/foo/foo/foo/foo"]:
            self.data = {}
            self.test_site_with_payload(payload)

        self.ptjsonlib.set_status(self.json_no, "ok")
        self.ptjsonlib.set_vulnerable(self.json_no, self.is_vulnerable)
        ptmisclib.ptprint(ptmisclib.out_if(self.ptjsonlib.get_all_json(), "", self.use_json))

    def test_site_with_payload(self, payload):
        test_type = "relative" if not payload else "absolute"
        css_comments = None
        if payload and not self.url.endswith("/"):
            payload = "/"+payload
        response = self.get_response(payload)
        ptmisclib.ptprint(ptmisclib.out_ifnot(f"Response: {response.url}", "INFO", self.use_json))
        soup = BeautifulSoup(response.text, "lxml")
        page_css = [css.get('href') for css in soup.find_all('link', type="text/css")]
        page_comments = soup.find(text=lambda text: isinstance(text, Comment))
        if page_comments:
            comment_soup = BeautifulSoup(page_comments, 'lxml')
            css_comments = [css.get('href') for css in comment_soup.find_all('link', type="text/css")]
        if payload:
            vulnerable_css = [css for css in page_css if "foo" in css]
            if css_comments:
                vulnerable_css += [css for css in css_comments if "foo" in css]
        else:
            vulnerable_css = [css for css in page_css if not css.startswith("/") and not css.startswith("http")]
            if css_comments:
                vulnerable_css += [css for css in css_comments if not css.startswith("/")]

        ptmisclib.ptprint(ptmisclib.out_ifnot(f"Vulnerable {test_type} CSS paths [{response.status_code}]:", "INFO", self.use_json))
        self.data.update({test_type: {"url": self.url+payload, "status_code": response.status_code, "vuln_css": vulnerable_css}})
        self.ptjsonlib.add_data(self.json_no, self.data)
        if vulnerable_css:
            self.is_vulnerable = True
            for i in vulnerable_css:
                ptmisclib.ptprint(ptmisclib.out_ifnot(f"    {i}", "", self.use_json))
        else:
                ptmisclib.ptprint(ptmisclib.out_ifnot(f"    None", "", self.use_json))

    def parse_url(self, url):
        o = urllib.parse.urlparse(url)
        if not o.scheme or o.scheme not in ["http", "https"]:
            ptmisclib.end_error("Missing or wrong scheme", self.json_no, self.ptjsonlib, self.use_json)
        """
        if not o.path.endswith("/"):
            o = o._replace(path=o.path+"/")
        """
        parsed_url = urllib.parse.urlunparse((o.scheme, o.netloc, o.path, "", "", ""))
        return parsed_url

    def get_response(self, payload):
        try:
            response = requests.get(self.url + payload, headers=self.headers, proxies=self.proxy, verify=False, allow_redirects=self.redirects)
            return response
        except Exception as e:
            ptmisclib.end_error(f"Cannot connect to website: {self.url}", self.json_no, self.ptjsonlib, self.use_json)


def get_help():
    return [
        {"description": ["PRSSI Testing Tool"]},
        {"usage": ["ptprssi <options>"]},
        {"usage_example": [
            "ptprssi -u https://www.example.com/",
            "ptprssi -u https://www.example.com/ -r"
        ]},
        {"options": [
            ["-u",  "--url",                    "<url>",            "Connect to URL"],
            ["-r",  "--redirects",              "",                 "Follow redirects"],
            ["-p",  "--proxy",                  "<proxy>",          "Set proxy (e.g. http://127.0.0.1:8080)"],
            ["-H",  "--headers",                "<header:value>",   "Set custom header(s)"],
            ["-ua",  "--user-agent",            "<ua>",             "Set User-Agent header"],
            ["-c",  "--cookie",                 "<cookie>",         "Set cookie"],
            ["-j",  "--json",                   "",                 "Output in JSON format"],
            ["-v",  "--version",                "",                 "Show script version and exit"],
            ["-h",  "--help",                   "",                 "Show this help message and exit"]
        ]
        }]


def parse_args():
    parser = argparse.ArgumentParser(add_help=False, usage="ptprssi <options>")
    parser.add_argument("-u",  "--url",        type=str, required=True)
    parser.add_argument("-r",  "--redirects",  action="store_true")
    parser.add_argument("-p",  "--proxy",      type=str)
    parser.add_argument("-H",  "--headers",    type=ptmisclib.pairs)
    parser.add_argument("-ua", "--user-agent", type=str, default="Penterep Tools")
    parser.add_argument("-c",  "--cookie",     type=str)
    parser.add_argument("-j",  "--json",       action="store_true")
    parser.add_argument("-v",  "--version",    action="version", version=f"{SCRIPTNAME} {__version__}")

    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        ptmisclib.help_print(get_help(), SCRIPTNAME, __version__)
        sys.exit(0)
    args = parser.parse_args()
    ptmisclib.print_banner(SCRIPTNAME, __version__, args.json)
    return args


def main():
    global SCRIPTNAME
    SCRIPTNAME = "ptprssi"
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    args = parse_args()
    script = ptprssi(args)
    script.run()


if __name__ == "__main__":
    main()
