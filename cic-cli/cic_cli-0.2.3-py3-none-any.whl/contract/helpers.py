# standard imports
import os
import logging
import sys
import json
import requests
import importlib
import tempfile
import hashlib

# local imports
from cic.writers import OutputWriter

log = logging.getLogger(__name__)


CONTRACTS = [
    {
        "url": "https://gitlab.com/cicnet/eth-erc20/-/raw/master/python/giftable_erc20_token/data/GiftableToken",
        "name": "Giftable Token",
    },
    {
        "url": "https://gitlab.com/cicnet/erc20-demurrage-token/-/raw/master/python/erc20_demurrage_token/data/DemurrageTokenSingleNocap",
        "name": "Demurrage Token Single No Cap",
    }
]

# Download File from Url
def download_file(url: str, filename=None) -> (str, bytes):
    directory = tempfile.gettempdir()
    filename = filename if filename else url.split("/")[-1]
    log.debug(f"Downloading {filename}")
    r = requests.get(url, allow_redirects=True)
    content_hash = hashlib.md5(r.content).hexdigest()
    path = os.path.join(directory, content_hash)
    with open(path, "wb") as f:
        f.write(r.content)
    log.debug(f"{filename} downloaded to {path}")
    return path

def get_contract_args(data: list):
    for item in data:
        if item["type"] == "constructor":
            return item["inputs"]
    raise Exception("No constructor found in contract")

def select_contract():
    print("Contracts:")
    print("\t C - Custom (path/url to contract)")
    for idx, contract in enumerate(CONTRACTS):
        print(f"\t {idx} - {contract['name']}")

    val = input("Select contract (C,0,1..): ")
    if val.isdigit() and int(val) < len(CONTRACTS):
        contract = CONTRACTS[int(val)]
        bin_path = os.path.abspath(download_file(contract["url"] + ".bin"))
        json_path = download_file(contract["url"] + ".json")

    elif val == "C":
        possible_bin_location = input("Enter a path or url to a contract.bin: ")
        if possible_bin_location.startswith('http'):
            # possible_bin_location is url
            bin_path = download_file(possible_bin_location)
        else:
            # possible_bin_location is path
            if os.path.exists(possible_bin_location):
                bin_path = os.path.abspath(possible_bin_location)
            else:
                raise Exception(f"File {possible_bin_location} does not exist")

            possible_json_path = val.replace(".bin", ".json")
            if os.path.exists(possible_json_path):
                json_path = possible_json_path
    else:
        print("Invalid selection")
        sys.exit(1)
    contract_extra_args = []
    contract_extra_args_types = []

    if os.path.exists(json_path):
        with open(json_path, encoding="utf-8") as f:
            json_data = json.load(f)
        for contract_arg in get_contract_args(json_data):
            arg_name = contract_arg.get("name")
            arg_type = contract_arg.get("type")
            if arg_name not in ["_decimals", "_name", "_symbol"]:
                val = input(f"Enter value for {arg_name} ({arg_type}): ")
                contract_extra_args.append(val)
                if arg_type == "uint128":
                    contract_extra_args_types.append("uint256")
                else:
                    contract_extra_args_types.append(arg_type)

    return {
        "bin_path": bin_path,
        "json_path": json_path,
        "extra_args": contract_extra_args,
        "extra_args_types": contract_extra_args_types,
    }


Writers = {
    "meta": OutputWriter,
    "attachment": OutputWriter,
    "proof": OutputWriter,
    "ext": OutputWriter,
}

def init_writers_from_config(config) -> Writers:
    writers: Writers = {
        "meta": None,
        "attachment": None,
        "proof": None,
        "ext": None,
    }
    for key in writers:
        writer_config_name = f"CIC_CORE_{key.upper()}_WRITER"
        (module_name, attribute_name) = config.get(writer_config_name).rsplit(".", maxsplit=1)
        mod = importlib.import_module(module_name)
        writer = getattr(mod, attribute_name)
        writers[key] = writer

    return writers
