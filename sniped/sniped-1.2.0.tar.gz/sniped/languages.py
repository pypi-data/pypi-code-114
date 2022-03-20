"""Utilities related to themes supported by each service."""

import enum

from .services import Service


class Language(enum.Enum):
    AUTO = "auto"
    APACHE = "apache"
    BASH = "bash"
    PLAINTEXT = "plain-text"
    C = "c"
    CPP = "c++"
    CSHARP = "c#"
    CLOJURE = "clojure"
    COBOL = "cobol"
    COFFEESCRIPT = "coffeescript"
    CRYSTAL = "crystal"
    CSS = "css"
    D = "d"
    DART = "dart"
    DIFF = "diff"
    DJANGO = "django"
    DOCKER = "docker"
    ELIXIR = "elixir"
    ELM = "elm"
    ERLANG = "erlang"
    FSHARP = "f#"
    FORTRAN = "fortran"
    GHERKIN = "gherkin"
    GRAPHQL = "graphql"
    GO = "go"
    GROOVY = "groovy"
    HANDLEBARS = "handlebars"
    HASKELL = "haskell"
    HTML = "html"
    XML = "xml"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    JSON = "json"
    JSX = "jsx"
    JULIA = "julia"
    KOTLIN = "kotlin"
    LATEX = "latex"
    LISP = "lisp"
    LUA = "lua"
    MARKDOWN = "markdown"
    MATHEMATICA = "mathematica"
    MATLAB = "matlab"
    OCTAVE = "octave"
    MYSQL = "mysql"
    NTRIPLES = "n-triples"
    NGINX = "nginx"
    NIM = "nim"
    OBJECTIVEC = "objective-c"
    OCAML = "ocaml"
    PASCAL = "pascal"
    PERL = "perl"
    PHP = "php"
    POWERSHELL = "powershell"
    PYTHON = "python"
    R = "r"
    RISCV = "risc-v"
    RUBY = "ruby"
    RUST = "rust"
    SASS = "sass"
    SCALA = "scala"
    SMALLTALK = "smalltalk"
    SOLIDITY = "solidity"
    SPARQL = "sparql"
    SQL = "sql"
    STYLUS = "stylus"
    SWIFT = "swift"
    TCL = "tcl"
    TOML = "toml"
    TURTLE = "turtle"
    TYPESCRIPT = "typescript"
    TSX = "tsx"
    TWIG = "twig"
    VBNET = "vb.net"
    VERILOG = "verilog"
    VHDL = "vhdl"
    VUE = "vue"
    XQUERY = "xquery"
    YAML = "yaml"
    ABAP = "abap"
    ACTIONSCRIPT = "actionscript"
    APPLESCRIPT = "applescript"
    ASTRO = "astro"
    INI = "ini"
    JUPYTER = "jupyter"
    LESS = "less"
    MDX = "mdx"
    OBJECTIVECPP = "objective-c++"
    PLSQL = "pl/sql"
    PRISMA = "prisma"
    SHELL = "shell"
    SVELTE = "svelte"
    WASM = "wasm"
    ZSH = "zsh"


LANGUAGES = {
    Service.CARBON: [
        Language.APACHE,
        Language.AUTO,
        Language.BASH,
        Language.C,
        Language.CLOJURE,
        Language.COBOL,
        Language.COFFEESCRIPT,
        Language.CPP,
        Language.CRYSTAL,
        Language.CSHARP,
        Language.CSS,
        Language.D,
        Language.DART,
        Language.DIFF,
        Language.DJANGO,
        Language.DOCKER,
        Language.ELIXIR,
        Language.ELM,
        Language.ERLANG,
        Language.FORTRAN,
        Language.FSHARP,
        Language.GHERKIN,
        Language.GO,
        Language.GRAPHQL,
        Language.GROOVY,
        Language.HANDLEBARS,
        Language.HASKELL,
        Language.HTML,
        Language.JAVA,
        Language.JAVASCRIPT,
        Language.JSON,
        Language.JSX,
        Language.JULIA,
        Language.KOTLIN,
        Language.LATEX,
        Language.LISP,
        Language.LUA,
        Language.MARKDOWN,
        Language.MATHEMATICA,
        Language.MATLAB,
        Language.MYSQL,
        Language.NGINX,
        Language.NIM,
        Language.NTRIPLES,
        Language.OBJECTIVEC,
        Language.OCAML,
        Language.OCTAVE,
        Language.PASCAL,
        Language.PERL,
        Language.PHP,
        Language.PLAINTEXT,
        Language.POWERSHELL,
        Language.PYTHON,
        Language.R,
        Language.RISCV,
        Language.RUBY,
        Language.RUST,
        Language.SASS,
        Language.SCALA,
        Language.SMALLTALK,
        Language.SOLIDITY,
        Language.SPARQL,
        Language.SQL,
        Language.STYLUS,
        Language.SWIFT,
        Language.TCL,
        Language.TOML,
        Language.TSX,
        Language.TURTLE,
        Language.TWIG,
        Language.TYPESCRIPT,
        Language.VBNET,
        Language.VERILOG,
        Language.VHDL,
        Language.VUE,
        Language.XML,
        Language.XQUERY,
        Language.YAML,
    ],
    Service.SNAPPIFY: [
        Language.ABAP,
        Language.ACTIONSCRIPT,
        Language.APACHE,
        Language.APPLESCRIPT,
        Language.ASTRO,
        Language.BASH,
        Language.C,
        Language.CLOJURE,
        Language.CPP,
        Language.CSHARP,
        Language.CSS,
        Language.DART,
        Language.DOCKER,
        Language.ELIXIR,
        Language.ELM,
        Language.GO,
        Language.GRAPHQL,
        Language.GROOVY,
        Language.HASKELL,
        Language.HTML,
        Language.INI,
        Language.JAVA,
        Language.JAVASCRIPT,
        Language.JSON,
        Language.JSX,
        Language.JUPYTER,
        Language.KOTLIN,
        Language.LATEX,
        Language.LESS,
        Language.LISP,
        Language.LUA,
        Language.MARKDOWN,
        Language.MATLAB,
        Language.MDX,
        Language.NGINX,
        Language.OBJECTIVEC,
        Language.OBJECTIVECPP,
        Language.OCAML,
        Language.OCTAVE,
        Language.PASCAL,
        Language.PERL,
        Language.PHP,
        Language.PLAINTEXT,
        Language.PLSQL,
        Language.POWERSHELL,
        Language.PRISMA,
        Language.PYTHON,
        Language.R,
        Language.RUBY,
        Language.RUST,
        Language.SASS,
        Language.SCALA,
        Language.SHELL,
        Language.SMALLTALK,
        Language.SOLIDITY,
        Language.SQL,
        Language.STYLUS,
        Language.SVELTE,
        Language.SWIFT,
        Language.TOML,
        Language.TSX,
        Language.TYPESCRIPT,
        Language.VUE,
        Language.WASM,
        Language.XML,
        Language.YAML,
        Language.ZSH,
    ],
}


_LANG_TO_CARBON_VALUE = {
    "apache": "text/apache",
    "auto": "auto",
    "bash": "application/x-sh",
    "c": "text/x-csrc",
    "c#": "text/x-csharp",
    "c++": "text/x-c++src",
    "clojure": "clojure",
    "cobol": "cobol",
    "coffeescript": "coffeescript",
    "crystal": "crystal",
    "css": "css",
    "d": "d",
    "dart": "dart",
    "diff": "text/x-diff",
    "django": "django",
    "docker": "dockerfile",
    "elixir": "elixir",
    "elm": "elm",
    "erlang": "erlang",
    "f#": "text/x-fsharp",
    "fortran": "fortran",
    "gherkin": "gherkin",
    "go": "text/x-go",
    "graphql": "graphql",
    "groovy": "groovy",
    "handlebars": "handlebars",
    "haskell": "haskell",
    "html": "htmlmixed",
    "java": "text/x-java",
    "javascript": "javascript",
    "json": "application/json",
    "jsx": "jsx",
    "julia": "julia",
    "kotlin": "text/x-kotlin",
    "latex": "stex",
    "lisp": "commonlisp",
    "lua": "lua",
    "markdown": "markdown",
    "mathematica": "mathematica",
    "matlab": "text/x-octave",
    "mysql": "text/x-mysql",
    "n-triples": "application/n-triples",
    "nginx": "nginx",
    "nim": "nim",
    "objective-c": "text/x-objectivec",
    "ocaml": "mllike",
    "octave": "text/x-octave",
    "pascal": "pascal",
    "perl": "perl",
    "php": "text/x-php",
    "plain-text": "text",
    "powershell": "powershell",
    "python": "python",
    "r": "r",
    "risc-v": "riscv",
    "ruby": "ruby",
    "rust": "rust",
    "sass": "sass",
    "scala": "text/x-scala",
    "smalltalk": "smalltalk",
    "solidity": "solidity",
    "sparql": "application/sparql-query",
    "sql": "sql",
    "stylus": "stylus",
    "swift": "swift",
    "tcl": "tcl",
    "toml": "toml",
    "tsx": "text/typescript-jsx",
    "turtle": "text/turtle",
    "twig": "text/x-twig",
    "typescript": "application/typescript",
    "vb.net": "vb",
    "verilog": "verilog",
    "vhdl": "vhdl",
    "vue": "vue",
    "xml": "htmlmixed",
    "xquery": "xquery",
    "yaml": "yaml",
}


_LANG_TO_SNAPPIFY_VALUE = {
    "abap": "abap",
    "actionscript": "actionscript",
    "apache": "apache",
    "applescript": "applescript",
    "astro": "astro",
    "bash": "bash",
    "c": "c",
    "c#": "c#",
    "c++": "c++",
    "clojure": "clojure",
    "css": "css",
    "dart": "dart",
    "docker": "docker",
    "elixir": "elixir",
    "elm": "elm",
    "go": "go",
    "graphql": "graphql",
    "groovy": "groovy",
    "haskell": "haskell",
    "html": "html",
    "ini": "ini",
    "java": "java",
    "javascript": "javascript",
    "json": "json",
    "jsx": "jsx",
    "jupyter": "jupyter",
    "kotlin": "kotlin",
    "latex": "latex",
    "less": "less",
    "lisp": "lisp",
    "lua": "lua",
    "markdown": "markdown",
    "matlab": "matlab / octave",
    "mdx": "mdx",
    "nginx": "nginx",
    "objective-c": "objective c",
    "objective-c++": "objective c++",
    "ocaml": "ocaml",
    "octave": "matlab / octave",
    "pascal": "pascal",
    "perl": "perl",
    "php": "php",
    "pl/sql": "pl/sql",
    "plain-text": "plain text",
    "powershell": "powershell",
    "prisma": "prisma",
    "python": "python",
    "r": "r",
    "ruby": "ruby",
    "rust": "rust",
    "sass": "sass",
    "scala": "scala",
    "shell": "shell",
    "smalltalk": "smalltalk",
    "solidity": "solidity",
    "sql": "sql",
    "stylus": "stylus",
    "svelte": "svelte",
    "swift": "swift",
    "toml": "toml",
    "tsx": "tsx",
    "typescript": "typescript",
    "vue": "vue",
    "wasm": "wasm",
    "xml": "xml",
    "yaml": "yaml",
    "zsh": "zsh",
}


def language_to_service_value(service: Service, value: str):
    if service == Service.CARBON:
        return _LANG_TO_CARBON_VALUE[value]
    else:
        assert service == Service.SNAPPIFY
        return _LANG_TO_SNAPPIFY_VALUE[value]
