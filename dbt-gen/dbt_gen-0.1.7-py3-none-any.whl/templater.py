from jinja2 import Environment, PackageLoader, select_autoescape, Template


class Templater:
    def __init__(self):
        self.env = Environment(loader=PackageLoader("dbt_gen"), autoescape=select_autoescape())

    def load_template(self, path: str) -> Template:
        return self.env.get_template(path)


_templater = None


def get_template(path: str) -> Template:
    global _templater
    if not _templater:
        _templater = Templater()
    return _templater.load_template(path)
