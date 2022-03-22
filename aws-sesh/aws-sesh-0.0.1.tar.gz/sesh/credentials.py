import os
import glob
import json

HOME = os.path.expanduser("~/.aws")

def generate_default_credentials():
    profiles = sorted([os.path.basename(p) for p in glob.glob(f"{HOME}/profiles/*")])
    profiles.insert(0, profiles.pop(profiles.index("default")))
    with open(os.path.join(HOME, "credentials"), "w") as cf:
        for profile in profiles:
            profile_keys = os.path.join(HOME, f"profiles/{profile}/accessKeys.csv")
            if os.path.exists(profile_keys):
                with open(profile_keys, "r") as pf:
                    key_id, secret_key = pf.readlines()[-1].rstrip("\n").split(",")
                cf.write(f"[{profile}]\n")
                cf.write(f"aws_access_key_id = {key_id}\n")
                cf.write(f"aws_secret_access_key = {secret_key}\n")


def write_session_credentials(session_credentials_path):

    with open(session_credentials_path, "r") as f:
        sts = json.load(f)
    access_key_id = sts["Credentials"]["AccessKeyId"]
    secret_access_key = sts["Credentials"]["SecretAccessKey"]
    session_token = sts["Credentials"]["SessionToken"]

    # Credentials
    credentials = ["[default]"]
    credentials.append(f"aws_access_key_id = {access_key_id}")
    credentials.append(f"aws_secret_access_key = {secret_access_key}")
    credentials.append(f"aws_session_token = {session_token}")

    # Update credentials
    with open(os.path.join(HOME, "credentials"), "w") as f:
        for item in credentials:
            f.write(f"{item}\n")
