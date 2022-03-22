# standard imports
import json
import os

# local imports
from cic.contract.base import Data, data_dir
from cic.contract.helpers import select_contract


class Token(Data):
    """Encapsulates the token data used by the extension to deploy and/or register token and token related applications on chain.

    Token details (name, symbol etc) will be used to initialize the token settings when start is called. If load is called instead, any token detail parameters passed to the constructor will be overwritten by data stored in the settings.

    :param path: Settings directory path
    :type path: str
    :param name: Token name
    :type name: str
    :param symbol: Token symbol
    :type symbol: str
    :param precision: Token value precision (number of decimals)
    :type precision: int
    :param supply: Token supply (in smallest precision units)
    :type supply: int
    :param code: Bytecode for token chain application
    :type code: str (hex)
    """

    def __init__(
        self,
        path=".",
        name="Foo Token",
        symbol="FOO",
        precision=6,
        supply=0,
        code=None,
        extra_args=[],
        extra_args_types=[],
        interactive=False,
    ):
        super(Token, self).__init__()
        self.name = name
        self.symbol = symbol.upper()
        self.supply = supply
        self.precision = precision
        self.code = code
        self.extra_args = extra_args
        self.extra_args_types = extra_args_types
        self.path = path
        self.token_path = os.path.join(self.path, "token.json")

        if interactive:
            contract = select_contract()
            self.code = contract["bin_path"]
            self.extra_args = contract["extra_args"]
            self.extra_args_types = contract["extra_args_types"]

            self.name = input(f"Enter Token Name ({self.name}): ") or self.name
            self.symbol = input(f"Enter Token Symbol ({self.symbol}): ") or self.symbol
            self.symbol = self.symbol.upper()
            self.precision = input(f"Enter Token Precision ({self.precision}): ") or self.precision
            self.supply = input(f"Enter Token Supply ({self.supply}): ") or self.supply

    def load(self):
        """Load token data from settings."""
        super(Token, self).load()

        with open(self.token_path, "r", encoding="utf-8") as f:
            o = json.load(f)

        self.name = o["name"]
        self.symbol = o["symbol"].upper()
        self.precision = o["precision"]
        self.code = o["code"]
        self.supply = o["supply"]
        extras = []
        extra_types = []
        token_extras: list = o["extra"]
        if token_extras:
            for idx, token_extra in enumerate(token_extras):
                arg = token_extra.get("arg")
                arg_type = token_extra.get("arg_type")
                if arg and arg_type:
                    extras.append(arg)
                    extra_types.append(arg_type)
                elif (arg and not arg_type) or (not arg and arg_type):
                    raise ValueError(
                        f"Extra contract args must have a 'arg' and 'arg_type', Please check {self.token_path}:extra[{idx}] "
                    )
        self.extra_args = extras
        self.extra_args_types = extra_types
        self.inited = True

    def start(self):
        """Initialize token settings from arguments passed to the constructor and/or template."""
        super(Token, self).load()

        token_template_file_path = os.path.join(
            data_dir, f"token_template_v{self.version()}.json"
        )
        with open(token_template_file_path, encoding="utf-8") as f:
            o = json.load(f)
        o["name"] = self.name
        o["symbol"] = self.symbol.upper()
        o["precision"] = self.precision
        o["code"] = self.code
        o["supply"] = self.supply
        extra = []
        for idx, extra_arg in enumerate(self.extra_args):
            extra.append({"arg": extra_arg, "arg_type": self.extra_args_types[idx]})
        if len(extra) != 0:
            o["extra"] = extra

        with open(self.token_path, "w", encoding="utf-8") as f:
            json.dump(o, f, sort_keys=True, indent="\t")

    def __str__(self):
        s = f"name = {self.name}\n"
        s += f"symbol = {self.symbol.upper()}\n"
        s += f"precision = {self.precision}\n"
        s += f"supply = {self.supply}\n"
        for idx, extra in enumerate(self.extra_args):
            s += f"extra_args[{idx}]({self.extra_args_types[idx]}) = {extra}\n"
        return s
