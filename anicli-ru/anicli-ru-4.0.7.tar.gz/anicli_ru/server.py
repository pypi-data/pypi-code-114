from sys import modules as sys_modules

from anicli_ru import loader


try:
    from flask import Flask, escape, request
except ImportError:
    print("Need install flask package")
    exit(-1)

IMPORTED_MODULES = []
extractors = loader.all_extractors()
for m in ["anicli_ru.extractors." + m for m in extractors]:
    __import__(m)
    if m not in sys_modules:
        raise ImportError("Failed import {} extractor".format(m))
    IMPORTED_MODULES.append(sys_modules[m])
    print("LOAD", m)


app = Flask(__name__)


@app.route("/")
def test():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


def main(host: str, port: int, debug: bool):
    app.run(host=host, port=port, debug=debug)
