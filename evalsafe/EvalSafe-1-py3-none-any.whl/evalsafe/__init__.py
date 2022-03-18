__author__ = "Zedikon"
__copyright__ = "Copyright Zedikon 2022"


block_tok = {
    "return": "return",
    "print": "print",
    "input": "input",
    "import": "import",
    "if": "if",
    "else": "else",
    "from": "from",
    "eval": "eval",
    "exec": "exec",
}

def evals(code):
    if block_tok["return"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["import"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["print"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["input"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["if"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["else"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["from"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["eval"] in code:
        return "Error, incorrect value entered!"
    elif block_tok["exec"] in code:
        return "Error, incorrect value entered!"
    else:
        try:
            res = eval(code)
            return res
        except Exception:
            return "Error, incorrect value entered!"