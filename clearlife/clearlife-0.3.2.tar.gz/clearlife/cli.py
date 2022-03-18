#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

    You might be tempted to import things from __main__ later, but that will cause
    problems: the code will get executed twice:

    - When you run `python -m clearlife` python will execute
      ``__main__.py`` as a script. That means there won't be any
      ``clearlife.__main__`` in ``sys.modules``.
    - When you import __main__ it will get executed again (as a module) because
      there's no ``clearlife.__main__`` in ``sys.modules``.

Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from uuid import uuid4
from aries_cloudagent.wallet.util import b58_to_bytes, b64_to_bytes, bytes_to_b64
from os import path, environ
import argparse
import threading
import logging
import logging.config
import json
from aries_cloudagent.wallet.crypto import sign_message
import requests

from clearlife.utility import relpath
from clearlife import msg
from clearlife.base import exhandler, bparser
from clearlife.crypto import anon_crypt_message, anon_decrypt_message, generate_keys, verify_signature

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


shutdown = threading.Event()
"""threading.Event: for signaling shutdown has been triggered for the script.
"""

DEFAULT_HOST = "localhost"
"""str: server name to use by default for binding.
"""
DEFAULT_PORT = 25433
"""int: default port number to bind `clearlifed` to.
"""

SERVER_KEY_NAME = "CLEARLIFE_{}_SERVER"
APP_SEED_NAME = "CLEARLIFE_{}_SEED"
DERIVED_KEY_NAME = "CLEARLIFE_{}_DERIVED"


def examples():
    """Prints examples of using the script to the console using colored output.
    """
    script = "ClearLIFE Key Client"
    explain = ("This script is a derived key client for getting derived keys from "
               "the ClearLIFE daemon on ClearNODE home servers.")
    contents = [(("Register a random public key for the ClearSHARE server app "
                  "with clearlifed for end-to-end encryption."),
                 "clearlife register --name clearshare",
                 "The resulting key pair is stored in environment variable CLEARLIFE_CLEARSHARE_SEED "
                 "which can be used to generate the keypair dynamically any time."),
                (("Get the 5th derived key within the `host` context for clearshare."),
                 "clearlife derive --name clearshare --context host --keyid 5",
                 "The response from the clearlifed API will be a derived key seed that can "
                 "be used to derived other keys. It will be stored in the CLEARLIFE_CLEARSHARE_DERIVED "
                 "environment variable. Each time is executed, the environment variable will be "
                 "overwritten.")
                ]
    required = ("")
    output = ("")
    details = ("")
    outputfmt = ("")

    msg.example(script, explain, contents, required, output, outputfmt, details)


script_options = {
    "command": {"help": "Which action to perform with clearlifed", 
                "choices": ["register", "derive", "appkeys"]},
    "--host": {"help": "Specify the host name to bind the API to.", "default": DEFAULT_HOST},
    "--port": {"help": "Specify the port to bind the API to.", "type": int, "default": DEFAULT_PORT},
    "--name": {"help": "Name of the application executing `command`."},
    "--context": {"help": "Key context to use when deriving keys."},
    "--keyid": {"help": "Integer derived key index to use when deriving keys."},
    "--seed": {"help": "Random seed generated for this session for end-to-end "
                       "encryption of the API requests."},
    "--spk": {"help": "Specify the base58 encoded server public key to use."}
}
"""dict: default command-line arguments and their
    :meth:`argparse.ArgumentParser.add_argument` keyword arguments.
"""


def _parser_options():
    """Parses the options and arguments from the command line."""
    pdescr = "ClearLIFE Key Client"
    parser = argparse.ArgumentParser(parents=[bparser], description=pdescr)
    for arg, options in script_options.items():
        parser.add_argument(arg, **options)

    args = exhandler(examples, parser)
    if args is None:
        return

    return args


def _get_url(args, urlpath):
    """Gets the formated HTTP URL to send requests to.

    Args:
        path (str): name of the endpoint to get a URL for.
    """
    return f"http://{args['host']}:{args['port']}/{urlpath}"


def _get_json(r):
    """Safely attempts to deserialize the JSON from a request object,
    returning an empty `dict` if that fails.
    """
    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {}


def get_default_args(name):
    """Gets the default command-line args dict for use in programmatic
    execution instead of command-line execution.
    """
    return {
        "host": DEFAULT_HOST,
        "port": DEFAULT_PORT,
        "name": name
    }
    

def _register_app(args):
    """Registers an application with `clearlifed` for getting derived keys.
    """
    pk = environ.get(SERVER_KEY_NAME)
    if pk is None:
        r0 = requests.get(_get_url(args, "register"), params={"name": args["name"]})
        raw = _get_json(r0)
        log.debug(f"Obtained {raw} as API result for /register GET.")
        if r0.status_code >= 200 and r0.status_code < 300:
            pk = raw["verkey"]
            environ[SERVER_KEY_NAME] = pk
            log.info(f"Successfully retrieved the unique public key for the app: {pk}.")
        else:
            log.error(f"While GETting the unique encryption public key for the app.")

    if pk is None:
        return

    if args.get("seed") is None:
        keys = generate_keys(uuid4().hex)
        source = {
            "name": args["name"],
            "key": keys["public"]
        }
        args["seed"] = keys["seed"]

    _msg = json.dumps(source).encode()
    log.debug(f"Encrypting the local application keys for {pk}.")
    body = bytes_to_b64(anon_crypt_message(_msg, b58_to_bytes(pk)))
    payload = {
        "name": args["name"],
        "body": body
    }
    log.debug(f"POSTing OTP keys encrypted as {body} for {keys['public']}.")

    r1 = requests.post(_get_url(args, "register"), json=payload)
    raw = _get_json(r1)
    log.debug(f"Obtained {raw} as API result for /register POST.")
    if r1.status_code >= 200 and r1.status_code < 300:
        log.info(f"Successfully registered the applications OTP with clearlifed.")
        # Check the signature of the server against the public key.
        if not verify_signature(raw["signature"], pk, raw["message"]):
            log.warn("The response from the server has an invalid signature")

        msg.okay(f"Registration of public key {keys['public']} successful.")

        return keys


def _get_app_keys(args):
    """Gets the app keys represented by the seed in environment variables.
    """
    return generate_keys(args["seed"])


def _derive_key(args):
    """Derives a set of cryptographic keys from `clearlifed` API.
    """
    keys = _get_app_keys(args)
    _msg = f"{args['context']}:{args['keyid']}".encode()
    payload = {
        "name": args["name"],
        "context": args["context"],
        "keyId": args["keyid"],
        "signature": sign_message(_msg, bytes.fromhex(keys["secret"])).hex()
    }

    r = requests.post(_get_url(args, "derive"), json=payload)
    raw = _get_json(r)
    log.debug(f"Obtained {raw} as response for derive request.")
    if r.status_code >= 200 and r.status_code < 300 and "payload" in raw:
        log.debug(f"Decrypting payload using {keys['public']}.")
        decrypt = anon_decrypt_message(b64_to_bytes(raw["payload"]), b58_to_bytes(keys["public"]), bytes.fromhex(keys["secret"]))
        body = json.loads(decrypt)
        sig = raw["signature"]
        if not verify_signature(sig, environ[SERVER_KEY_NAME], decrypt):
            msg.err(f"The signature in the derived key payload is invalid for {environ[SERVER_KEY_NAME]}.")
            exit(1)

        msg.okay(f"Obtained {body['did']} as derived DID.")

        return body
    else:
        log.error(f"While requesting derived keys from API: {raw}.")


def _request_app_keys(args):
    """Performs an API request to `clearlifed` API to get the
    application keys.
    """
    keys = _get_app_keys(args)
    _msg = f"{args['name']}:appkeys".encode()
    payload = {
        "name": args["name"],
        "signature": sign_message(_msg, bytes.fromhex(keys["secret"])).hex()
    }

    r = requests.post(_get_url(args, "appkeys"), json=payload)
    raw = _get_json(r)
    log.debug(f"Obtained {raw} as response for app keys request.")
    if r.status_code >= 200 and r.status_code < 300 and raw is not None and raw["success"]:
        log.debug(f"Decrypting payload using {keys['public']}.")
        decrypt = anon_decrypt_message(b64_to_bytes(raw["payload"]), b58_to_bytes(keys["public"]), bytes.fromhex(keys["secret"]))
        body = json.loads(decrypt)
        sig = raw["signature"]
        if not verify_signature(sig, environ[SERVER_KEY_NAME], decrypt):
            msg.err(f"The signature in the derived key payload is invalid for {environ[SERVER_KEY_NAME]}.")
            exit(1)

        msg.okay(f"Obtained {body['did']} as app's DID.")
        return body
    else:
        log.error(f"While requesting app keys from API: {raw}")


CMD_REGISTER = "register"
"""str: command for registering an application with clearlifed.
"""
CMD_DERIVE = "derive"
"""str: command for deriving a cryptographic key from clearlifed.
"""
CMD_APPKEYS = "appkeys"
TARGETS = {
  CMD_REGISTER: _register_app,
  CMD_DERIVE: _derive_key,
  CMD_APPKEYS: _request_app_keys
}
"""dict: keys are one of the available commands; values
are functions for executing that command.
"""

def _sub_app_name(args):
    """Substitutes the name of the application into the constants used
    for setting environment variables with query results.
    """
    global SERVER_KEY_NAME, APP_SEED_NAME, DERIVED_KEY_NAME
    SERVER_KEY_NAME = SERVER_KEY_NAME.format(args["name"].upper())
    APP_SEED_NAME = APP_SEED_NAME.format(args["name"].upper())
    DERIVED_KEY_NAME = DERIVED_KEY_NAME.format(args["name"].upper())


def run(**args):
    """Starts the local KERI DHT node and API server.
    """    
    x = TARGETS.get(args["command"])
    if x is not None:
        _sub_app_name(args)

        if args.get("spk") is not None:
            environ[SERVER_KEY_NAME] = args["spk"]
            
        return x(args)


def main(args=None):
    args = _parser_options() if args is None else args
    return run(**args)


if __name__ == '__main__':  # pragma: no cover
    main()


