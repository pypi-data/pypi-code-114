import argparse
import re
import secrets
import sys

import xerox
from colorama import Fore, Style

from witaker.clipboardserver import (
    app,
    name,
    version,
    DEFAULT_SERVER_PORT,
    start_flask_webserver,
    get_auth_marker,
    get_auth_marker_color,
    AuthorizedClipboardUtil,
)

def program_version(n, v):
    return f"{n} {v}"

def program_version_color(n, v):
    return f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{n} {Fore.YELLOW}{v}{Style.RESET_ALL}"


def add_program_arguments(parser):
    parser.add_argument('-v', '--version', help='output version information and exit', action='store_true')
    parser.add_argument('-p', '--port', help=f"set web server port, default is {DEFAULT_SERVER_PORT}", default=DEFAULT_SERVER_PORT)
    parser.add_argument('-a', '--auth-key', help='specify auth-key to use instead of generating a random key')

def if_version_print_version_and_exit(args):
    if args.version:
        print(program_version_color(name, version))
        sys.exit(0)

def get_port_or_default_port(args):
    port = DEFAULT_SERVER_PORT
    if args.port:        
        MIN_PORT = 1024
        MAX_PORT = 65535
        bad_port_warning = f"{Style.BRIGHT}{Fore.RED} * Warning{Style.RESET_ALL} : port must be number between {MIN_PORT} and {MAX_PORT}, using default port: {DEFAULT_SERVER_PORT}"
        if re.match(r"^\d+$", str(args.port)):
            port_number = int(args.port)
            if port_number >= MIN_PORT and port_number <= MAX_PORT:
                port = port_number
            else:
                print(bad_port_warning)
        else:
            print(bad_port_warning)
    return port

def get_auth_key_or_generate_auth_key(args):
    if args.auth_key:
        base_64_pattern = r"^[\d\w\+\/]+={0,2}$"
        if re.match(base_64_pattern, args.auth_key):
            return args.auth_key
        else:
            bad_auth_key_error = f"{Style.BRIGHT}{Fore.RED} * Error{Style.RESET_ALL} : auth-key may only contain [A-Z] [a-z] [0-9] + / ="
            print(bad_auth_key_error)
            sys.exit(1)
    else:   
        return secrets.token_hex()

def clipboard_server_cli_main():
    cli_argument_parser = argparse.ArgumentParser(prog='witaker-clipboard-server', description='start Witaker Clipboard Server local web service', allow_abbrev=True, add_help=True)
    add_program_arguments(cli_argument_parser)
    args = cli_argument_parser.parse_args()

    if_version_print_version_and_exit(args)

    port = get_port_or_default_port(args)

    

    secret_auth_key = get_auth_key_or_generate_auth_key(args)
    
    print(f" * Initializing {program_version_color(name, version)}  -  {get_auth_marker_color(port, secret_auth_key)}")

    clipboard_util = AuthorizedClipboardUtil(secret_auth_key)
    clipboard_util.copy_text_to_clipboard(secret_auth_key, get_auth_marker(port, secret_auth_key))
    app.config["clipboard_util"] = clipboard_util

    start_flask_webserver(port)
    return 0
