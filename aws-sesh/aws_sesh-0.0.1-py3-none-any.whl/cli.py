import os
import glob
import json
import argparse

from sesh.credentials import generate_default_credentials, write_session_credentials

HOME = os.path.expanduser("~/.aws")

def sesh():

    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="default")
    parser.add_argument("--token", type=str, default=None)
    args = parser.parse_args()

    # Generate default credentials
    generate_default_credentials()

    if args.token is not None:
        session_credentials_path = os.path.join(
            HOME, f"profiles/{args.profile}/credentials.json"
        )
        with open(os.path.join(HOME, f"profiles/{args.profile}/device.txt"), "r") as f:
            device = f.read()
        cmd = f"aws sts get-session-token --profile {args.profile} --serial-number {device} --token-code {args.token} > {session_credentials_path}"
        os.system(cmd)
        write_session_credentials(session_credentials_path)
