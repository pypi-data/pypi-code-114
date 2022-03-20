from cookiecutter.main import cookiecutter

DEFAULT_GIT_URL = "https://github.com/joon-solutions/cookiecutter-dbt.git"


def generate_dbt(**_kwarg):
    print(f"Enter Git URL [{DEFAULT_GIT_URL}]: ")
    git_url = input()
    if not git_url:
        git_url = DEFAULT_GIT_URL
    cookiecutter(git_url)


def run(args):
    generate_dbt(**(args.__dict__))


def config_parser(parser):
    parser.set_defaults(func=run)
