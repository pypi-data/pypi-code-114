from __future__ import annotations

# standard import
import logging

from chainlib.cli.config import Config

# local imports
from cic.contract.contract import deploy_contract, generate_contract, load_contract

log = logging.getLogger(__name__)


def process_args(argparser):
    argparser.add_argument(
        "--skip-gen", action="store_true", default=False, help="Skip Generation"
    )
    argparser.add_argument(
        "--skip-deploy",
        action="store_true",
        help="Skip Deployment",
    )
    argparser.add_argument(
        "--target",
        default="eth",
        help="Contract Target (eth)",
    )
    argparser.add_argument(
        "path",
        type=str,
        help="Path to generate/use contract deployment info",
    )
    argparser.add_argument(
        "-p",
        type=str,
        help="RPC Provider (http://localhost:8545)",
    )
    argparser.add_argument(
        "-y",
        type=str,
        help="Wallet Keystore",
    )


def validate_args(_args):
    pass


ExtraArgs = {"skip_gen": str, "skip_deploy": str, "target": str, "path": str, "p": str}


def execute(config: Config, eargs: ExtraArgs):
    directory = eargs.path
    target = eargs.target
    skip_gen = eargs.skip_gen
    skip_deploy = eargs.skip_deploy
    wallet_keystore = eargs.y
    if wallet_keystore:
        config.add(wallet_keystore, "WALLET_KEY_FILE", exists_ok=True)

    if not skip_gen:
        contract = generate_contract(directory, [target], config, interactive=True)
    else:
        contract = load_contract(directory)

    print(contract)

    print(f"Meta: {config.get('META_URL')}")
    print(f"ChainSpec: {config.get('CHAIN_SPEC', contract.network.chain_spec(target))}")
    print(f"RPC: {config.get('RPC_PROVIDER')}\n")

    if not skip_deploy:
        ready_to_deploy = input("Are you ready to Deploy? (y/n): ")
        if ready_to_deploy == "y":
            deploy_contract(
                config=config,
                contract_directory=directory,
                target=target,
            )
            print("Deployed")
        else:
            print("Skipping deployment")


if __name__ == "__main__":
    # execute()
    print("Not Implemented")
