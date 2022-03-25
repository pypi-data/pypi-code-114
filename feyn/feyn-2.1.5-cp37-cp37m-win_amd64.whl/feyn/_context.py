import os
from typing import List, Tuple

import feyn
import _qepler

from lark import Lark, Tree, Token

DIR, _ = os.path.split(__file__)
QUERY_GRAMMAR = os.path.join(DIR, "qlang/query_grammar.lark")


class Context:
    PARSER = Lark.open(QUERY_GRAMMAR, start="expr", parser="lalr")
    SPECIAL_OPCODES = {
        "register_any": 0,
        "interact1": 1,
        "interact2": 2,
        "wildcard": 3,
        "exclude": 4,
        # 50-80 are also reserved
    }

    def __init__(self):
        self.registers = []

    def translate_ast(self, ast) -> int:
        """Translate a node in a lark AST to an opcode."""
        if isinstance(ast, Token):
            term_name = ast.value.strip("\"'")
            if term_name not in self.registers:
                raise ValueError(f"Input '{term_name}' in query but not in input_names.")
            return self.lookup_by_fname(term_name, 0)

        dat = ast.data
        special_code = Context.SPECIAL_OPCODES.get(dat)
        if special_code is not None:
            return special_code
        if dat == "expr":
            return self.lookup_by_fname("add", 2)
        if dat == "term":
            return self.lookup_by_fname("multiply", 2)

        if dat == "gaussian":
            dat += str(len(ast.children))

        return self.lookup_by_fname(dat, len(ast.children))

    def query_to_codes(self, output_name: str, user_query: str) -> Tuple[int, List[int]]:
        """Convert a user-written query into the program representation."""
        res_codes = [self.lookup_by_fname(output_name, 0)]
        min_complexity = 0

        ast = Context.PARSER.parse(user_query)

        def _recurse(node):
            nonlocal res_codes, min_complexity
            if isinstance(node, Tree) and node.data == "wildcard":
                wc_codes = [Context.SPECIAL_OPCODES["wildcard"]]
                max_wc_complexity = 80
                wc_terms = set()
                wc_banned = set()

                for child in node.children:
                    if isinstance(child, Tree):
                        wc_codes.append(Context.SPECIAL_OPCODES["exclude"])
                        term_code = self.translate_ast(child.children[0])
                        wc_banned.add(term_code)
                        wc_codes.append(term_code)
                    elif child.type in ["SINGLE_ESCAPED_STRING", "DOUBLE_ESCAPED_STRING"]:
                        term_name = child.value.strip("\"'")
                        if term_name not in self.registers:
                            raise ValueError(f"Input '{term_name}' in query but not in input_names.")
                        term_code = self.lookup_by_fname(term_name, 0)
                        wc_terms.add(term_code)
                        wc_codes.append(term_code)
                    else:
                        max_wc_complexity = min(int(child.value) + 50, 80)

                wc_codes.append(max_wc_complexity)
                res_codes += wc_codes

                min_wc_complexity = max(1, 2 * (len(wc_terms) - 1))
                complexity_diff = min_wc_complexity - (max_wc_complexity - 50)
                if complexity_diff > 0:
                    raise ValueError(
                        f"\n\nToo much complexity requested in wildcard subtree. Either increase the allowed complexity (currently {max_wc_complexity-50}) or remove {complexity_diff} input(s) from the wildcard."
                    )
                inconsistent = [self.registers[c - 10000] for c in wc_terms.intersection(wc_banned)]
                if inconsistent:
                    msg = "Inconsistent required inclusion and exclusion of terminal"
                    if len(inconsistent) >= 2:
                        msg += "s"
                    msg += " " + ", ".join([f"'{t}'" for t in inconsistent]) + "."
                    raise ValueError(msg)
                min_complexity += min_wc_complexity
                return

            min_complexity += 1
            res_codes.append(self.translate_ast(node))
            if isinstance(node, Tree):
                nchildren = len(node.children)
                if nchildren:
                    _recurse(node.children[0])
                if nchildren == 2:
                    _recurse(node.children[1])
                if nchildren > 2:
                    _recurse(Tree(node.data, node.children[1:]))

        _recurse(ast)
        return min_complexity, res_codes

    def lookup_by_fname(self, name: str, arity: int) -> int:
        """Recover the opcode of 'fname' with arity 'arity'."""
        assert arity <= 2

        if arity == 0:
            try:
                ix = self.registers.index(name)
            except ValueError:
                # New register
                ix = len(self.registers)
                self.registers.append(name)

            return 10000 + ix

        for opcode, fname in feyn.OPCODE_MAP.items():
            if fname == name and opcode // 1000 == arity:
                return opcode

        raise ValueError(f"Unaware of '{name}' with arity {arity} in the context.")

    def get_codes(self, arity: int, names: list):
        if arity == 0:
            # A register
            names = set(names)
            extra = sorted(names.difference(self.registers))
            self.registers += extra

            base = 10000
            return [base + ix for ix, name in enumerate(self.registers) if name in names]

        if names is None:
            names = feyn.OPCODE_MAP.values()

        # An operator
        return [
            opcode
            for opcode, function_name in feyn.OPCODE_MAP.items()
            if function_name in names and opcode // 1000 == arity
        ]

    def to_model(self, program, output_name, stypes={}):
        l = len(program)
        if l < 2:
            # TODO: Why not raise an exception?
            # Invalid program
            return None

        names = []
        fnames = []

        for ix in range(l):
            if ix == 0:
                names.append(output_name)
                stype = stypes.get(output_name, "f")
                if stype in ("b"):  # Classifier?
                    fnames.append("out:lr")
                else:
                    fnames.append("out:linear")
                continue

            code = program[ix]
            arity = program.arity_at(ix)

            if arity == 0:
                name = self.registers[code - 10000]
                names.append(name)

                stype = stypes.get(name, "f")
                if stype in ["c", "cat", "categorical"]:
                    fnames.append("in:cat")
                else:
                    fnames.append("in:linear")
            else:
                name = ""
                fname = feyn.OPCODE_MAP.get(code)
                fnames.append(fname)
                names.append("")

        return feyn.Model(program, names, fnames)
