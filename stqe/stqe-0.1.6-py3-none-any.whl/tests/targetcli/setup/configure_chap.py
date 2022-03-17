#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from stqe.host.persistent_vars import read_var, write_var
from stqe.host.atomic_run import atomic_run, parse_ret
from libsan.host.lio import TargetCLI
from random import randint
from os import environ


def remove_nones(kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}


def rand_string(length):
    """
    Creates random string of length passed as parameter.
    :param length: integer representing length of the string
    :return:
    None: if length is not integer
    string: with random characters
    """
    ret = ""
    if not isinstance(length, int):
        return None
    for i in range(length):
        while True:
            num = randint(48, 122)
            # 48-57 -> numbers, 65 - 90 -> uppercase letters, 97 - 122 -> lowercase letters
            if 48 <= num <= 57 or 65 <= num <= 90 or 97 <= num <= 122:
                ret += chr(num)
                break
    return ret


def configure_chap():
    errors = []
    target_iqn = read_var("TARGET_IQN")
    tgp = read_var("TGP")
    # supported fmf arguments
    args = {"random": False, "userid": None, "password": None,
            "mutual_userid": None, "mutual_password": None, "chap_ways": 1}
    # Getting arguments from fmf
    for arg in args:
        try:
            if arg == "chap_ways":
                args[arg] = int(environ["fmf_%s" % arg])
                continue
            args[arg] = environ["fmf_%s" % arg]
        except KeyError:
            pass

    if args["random"]:  # if random is true, generate userid and password randomly
        if args["chap_ways"] == 2:
            args["mutual_userid"] = rand_string(randint(1, 255))
            args["mutual_password"] = rand_string(randint(1, 255))
        args["userid"] = rand_string(randint(1, 255))
        args["password"] = rand_string(randint(1, 255))
    for i in ["random", "chap_ways"]:  # removing these args from dict because this dict is used as kwargs in atomic run
        args.__delitem__(i)

    target = TargetCLI()

    target.path = "/iscsi"

    atomic_run("Enabling discovery_auth and setting userid and password",
               enable=1,
               group="discovery_auth",
               command=target.set,
               errors=errors,
               **remove_nones(args)
               )

    target.path = "/iscsi/" + target_iqn + "/" + tgp

    atomic_run("Enabling authentication and generate node acls",
               group="attribute",
               authentication=1,
               generate_node_acls=1,
               command=target.set,
               errors=errors
               )

    atomic_run("Setting userid and password in auth group",
               group="auth",
               command=target.set,
               errors=errors,
               **remove_nones(args)
               )

    if args["mutual_userid"] is not None and args["mutual_password"] is not None:
        atomic_run("Writing var CHAP_MUTUAL_USERID",
                   command=write_var,
                   var={"CHAP_MUTUAL_USERID": args["mutual_userid"]},
                   errors=errors)

        atomic_run("Writing var CHAP_MUTUAL_PASSWORD",
                   command=write_var,
                   var={"CHAP_MUTUAL_PASSWORD": args["mutual_password"]},
                   errors=errors)

    atomic_run("Writing var CHAP_USERID",
               command=write_var,
               var={"CHAP_USERID": args["userid"]},
               errors=errors)

    atomic_run("Writing var CHAP_PASSWORD",
               command=write_var,
               var={"CHAP_PASSWORD": args["password"]},
               errors=errors)

    return errors


if __name__ == "__main__":
    errs = configure_chap()
    exit(parse_ret(errs))
