import json
import pathlib
import string


def _make_enum_name(name: str) -> str:
    """Clean a language name to make it a valid uppercase enum name."""

    # Handle languages like F# or Objective C++
    name = name.replace("+", "p").replace("#", "sharp")
    chars = [
        char
        for char in name.upper()
        if char in string.ascii_letters + string.digits + "_"
    ]
    pre = "_" if chars[0] in string.digits else ""
    return pre + "".join(chars)


# Languages support by Carbon, data from https://github.com/carbon-app/carbon
# See revision https://github.com/carbon-app/carbon/blob/fa6a4ee4b4fee807029e7e9911507dfaa97585cd/lib/constants.js
_CARBON_LANGUAGES = [
    {
        "name": "Auto",
        "mode": "auto",
    },
    {
        "name": "Apache",
        "mode": "apache",
        "mime": "text/apache",
        "custom": True,
        "highlight": True,
    },
    {
        "name": "Bash",
        "mode": "shell",
        "mime": "application/x-sh",
        "highlight": True,
    },
    {
        "name": "Plain Text",
        "mode": "text",
    },
    {
        "name": "C",
        "mode": "clike",
        "mime": "text/x-csrc",
        "short": "c",
    },
    {
        "name": "C++",
        "mode": "clike",
        "mime": "text/x-c++src",
        "short": "c-like",
        "highlight": True,
    },
    {
        "name": "C#",
        "mode": "clike",
        "mime": "text/x-csharp",
        "short": "csharp",
        "highlight": True,
    },
    {
        "name": "Clojure",
        "mode": "clojure",
        "highlight": True,
    },
    {
        "name": "COBOL",
        "mode": "cobol",
    },
    {
        "name": "CoffeeScript",
        "mode": "coffeescript",
        "highlight": True,
    },
    {
        "name": "Crystal",
        "mode": "crystal",
        "highlight": True,
    },
    {
        "name": "CSS",
        "mode": "css",
        "highlight": True,
    },
    {
        "name": "D",
        "mode": "d",
        "highlight": True,
    },
    {
        "name": "Dart",
        "mode": "dart",
        "highlight": True,
    },
    {
        "name": "Diff",
        "mode": "diff",
        "mime": "text/x-diff",
        "highlight": True,
    },
    {
        "name": "Django",
        "mode": "django",
        "highlight": True,
    },
    {
        "name": "Docker",
        "mode": "dockerfile",
        "highlight": True,
    },
    {
        "name": "Elixir",
        "mode": "elixir",
        "custom": True,
        "highlight": True,
    },
    {
        "name": "Elm",
        "mode": "elm",
        "highlight": True,
    },
    {
        "name": "Erlang",
        "mode": "erlang",
        "highlight": True,
    },
    {
        "name": "F#",
        "mime": "text/x-fsharp",
        "mode": "mllike",
        "short": "fsharp",
        "highlight": True,
    },
    {
        "name": "Fortran",
        "mode": "fortran",
        "highlight": True,
    },
    {
        "name": "Gherkin",
        "mode": "gherkin",
        "highlight": True,
    },
    {
        "name": "GraphQL",
        "mode": "graphql",
        "custom": True,
    },
    {
        "name": "Go",
        "mode": "go",
        "mime": "text/x-go",
        "highlight": True,
    },
    {
        "name": "Groovy",
        "mode": "groovy",
        "highlight": True,
    },
    {
        "name": "Handlebars",
        "mode": "handlebars",
        "highlight": True,
    },
    {
        "name": "Haskell",
        "mode": "haskell",
        "highlight": True,
    },
    {
        "name": "HTML/XML",
        "mode": "htmlmixed",
    },
    {
        "name": "Java",
        "mode": "clike",
        "mime": "text/x-java",
        "short": "java",
        "highlight": True,
    },
    {
        "name": "JavaScript",
        "mode": "javascript",
        "short": "javascript",
        "highlight": True,
    },
    {
        "name": "JSON",
        "mode": "javascript",
        "mime": "application/json",
        "short": "json",
        "highlight": True,
    },
    {
        "name": "JSX",
        "mode": "jsx",
        "short": "jsx",
    },
    {
        "name": "Julia",
        "mode": "julia",
        "highlight": True,
    },
    {
        "name": "Kotlin",
        "mode": "clike",
        "mime": "text/x-kotlin",
        "short": "kotlin",
        "highlight": True,
    },
    {
        "name": "LaTeX",
        "mode": "stex",
        "short": "latex",
        "highlight": True,
    },
    {
        "name": "Lisp",
        "mode": "commonlisp",
        "short": "lisp",
        "highlight": True,
    },
    {
        "name": "Lua",
        "mode": "lua",
        "highlight": True,
    },
    {
        "name": "Markdown",
        "mode": "markdown",
        "highlight": True,
    },
    {
        "name": "Mathematica",
        "mode": "mathematica",
        "highlight": True,
    },
    {
        "name": "MATLAB/Octave",
        "mode": "octave",
        "mime": "text/x-octave",
        "short": "matlab",
        "highlight": True,
    },
    {
        "name": "MySQL",
        "mode": "sql",
        "mime": "text/x-mysql",
        "short": "mysql",
    },
    {
        "name": "N-Triples",
        "mode": "ntriples",
        "mime": "application/n-triples",
    },
    {
        "name": "NGINX",
        "mode": "nginx",
        "highlight": True,
    },
    {
        "name": "Nim",
        "mode": "nim",
        "custom": True,
        "highlight": True,
    },
    {
        "name": "Objective C",
        "mode": "clike",
        "mime": "text/x-objectivec",
        "short": "objectivec",
        "highlight": True,
    },
    {
        "name": "OCaml",
        "mode": "mllike",
        "short": "ocaml",
        "highlight": True,
    },
    {
        "name": "Pascal",
        "mode": "pascal",
    },
    {
        "name": "Perl",
        "mode": "perl",
        "highlight": True,
    },
    {
        "name": "PHP",
        "mode": "php",
        "mime": "text/x-php",
        "short": "php",
        "highlight": True,
    },
    {
        "name": "PowerShell",
        "mode": "powershell",
        "highlight": True,
    },
    {
        "name": "Python",
        "mode": "python",
        "highlight": True,
    },
    {
        "name": "R",
        "mode": "r",
        "highlight": True,
    },
    {
        "name": "RISC-V",
        "mode": "riscv",
        "custom": True,
    },
    {
        "name": "Ruby",
        "mode": "ruby",
        "highlight": True,
    },
    {
        "name": "Rust",
        "mode": "rust",
        "highlight": True,
    },
    {
        "name": "Sass",
        "mode": "sass",
    },
    {
        "name": "Scala",
        "mode": "clike",
        "mime": "text/x-scala",
        "short": "scala",
        "highlight": True,
    },
    {
        "name": "Smalltalk",
        "mode": "smalltalk",
        "highlight": True,
    },
    {
        "name": "Solidity",
        "mode": "solidity",
        "custom": True,
    },
    {
        "name": "SPARQL",
        "mode": "sparql",
        "mime": "application/sparql-query",
    },
    {
        "name": "SQL",
        "mode": "sql",
        "highlight": True,
    },
    {
        "name": "Stylus",
        "mode": "stylus",
        "mime": "stylus",
        "highlight": True,
    },
    {
        "name": "Swift",
        "mode": "swift",
        "highlight": True,
    },
    {
        "name": "TCL",
        "mode": "tcl",
        "highlight": True,
    },
    {
        "name": "TOML",
        "mode": "toml",
    },
    {
        "name": "Turtle",
        "mode": "turtle",
        "mime": "text/turtle",
    },
    {
        "name": "TypeScript",
        "mode": "javascript",
        "mime": "application/typescript",
        "short": "typescript",
        "highlight": True,
    },
    {
        "name": "TSX",
        "mode": "jsx",
        "mime": "text/typescript-jsx",
        "short": "tsx",
    },
    {
        "name": "Twig",
        "mode": "twig",
        "mime": "text/x-twig",
        "highlight": True,
    },
    {
        "name": "VB.NET",
        "mode": "vb",
    },
    {
        "name": "Verilog",
        "mode": "verilog",
        "highlight": True,
    },
    {
        "name": "VHDL",
        "mode": "vhdl",
        "highlight": True,
    },
    {
        "name": "Vue",
        "mode": "vue",
    },
    {
        "name": "XQuery",
        "mode": "xquery",
        "highlight": True,
    },
    {
        "name": "YAML",
        "mode": "yaml",
        "highlight": True,
    },
]


# List of languages that the Snappify editor knows (as of 20-03-2022).
# The API expects these exact same strings, up to casing.
_SNAPPIFY_LANGUAGES = [
    "ABAP",
    "ActionScript",
    "Apache",
    "AppleScript",
    "Astro",
    "Bash",
    "C",
    "C++",
    "C#",
    "Clojure",
    "CSS",
    "Dart",
    "Docker",
    "Elixir",
    "Elm",
    "GraphQL",
    "Go",
    "Groovy",
    "Haskell",
    "HTML",
    "INI",
    "Java",
    "JavaScript",
    "Jupyter",
    "JSX",
    "JSON",
    "Kotlin",
    "LateX",
    "Less",
    "Lisp",
    "Lua",
    "Markdown",
    "MATLAB / Octave",
    "MDX",
    "NGINX",
    "Objective C",
    "Objective C++",
    "OCAML",
    "Pascal",
    "Perl",
    "PHP",
    "Plain Text",
    "PL/SQL",
    "PowerShell",
    "Prisma",
    "Python",
    "R",
    "Ruby",
    "Rust",
    "Sass",
    "Scala",
    "Shell",
    "Smalltalk",
    "Solidity",
    "SQL",
    "Stylus",
    "Svelte",
    "Swift",
    "TOML",
    "TypeScript",
    "TSX",
    "Vue",
    "WASM",
    "XML",
    "YAML",
    "ZSH",
]


enum_data = []  # List of all Language enum (name, value) pairs.
# Map Language enum values to strings the carbon API handles.
_LANG_TO_CARBON_VALUE = {}
# Map Language enum values to strings the Snappify API handles.
_LANG_TO_SNAPPIFY_VALUE = {}

# Parse data from all services to build lists of languages.
carbon_names = set()
for lang_dict in _CARBON_LANGUAGES:
    for lang in lang_dict["name"].split("/"):
        name = _make_enum_name(lang)
        value = lang.lower().replace(" ", "-")
        enum_data.append((name, value))
        carbon_value = lang_dict.get("mime", "") or lang_dict.get("mode", "")
        _LANG_TO_CARBON_VALUE[value] = carbon_value
        carbon_names.add(name)

snappify_names = set()
for lang in _SNAPPIFY_LANGUAGES:
    for _lang in lang.split(" / "):
        name = _make_enum_name(_lang)
        value = _lang.lower().replace(" ", "-")
        _LANG_TO_SNAPPIFY_VALUE[value] = lang.lower()
        if name in carbon_names:
            assert (name, value) in enum_data
        else:
            enum_data.append((name, value))
        snappify_names.add(name)


# Build the string that defines the Language enum.
language_enum_definition = "class Language(enum.Enum):\n" + "\n".join(
    " " * 4 + f'{name} = "{value}"' for name, value in enum_data
)

# Build the string that defines the LANGUAGES dictionary.
nl = "\n"
languages_dict_definition = f"""LANGUAGES = {{
    Service.CARBON: [
{nl.join(" " * 8 + f"Language.{name}," for name in sorted(carbon_names))}
    ],
    Service.SNAPPIFY: [
{nl.join(" " * 8 + f"Language.{name}," for name in sorted(snappify_names))}
    ],
}}
"""


languages = f'''"""Utilities related to themes supported by each service."""

import enum

from .services import Service


{language_enum_definition}


{languages_dict_definition}


_LANG_TO_CARBON_VALUE = {json.dumps(_LANG_TO_CARBON_VALUE, indent=4, sort_keys=True)}


_LANG_TO_SNAPPIFY_VALUE = {json.dumps(_LANG_TO_SNAPPIFY_VALUE, indent=4, sort_keys=True)}


def language_to_service_value(service: Service, value: str):
    if service == Service.CARBON:
        return _LANG_TO_CARBON_VALUE[value]
    else:
        assert service == Service.SNAPPIFY
        return _LANG_TO_SNAPPIFY_VALUE[value]
'''


dest = pathlib.Path(__file__).parent / "languages.py"
dest.write_text(languages + "\n")
