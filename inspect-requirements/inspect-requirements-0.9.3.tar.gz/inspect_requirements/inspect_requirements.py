import sys
import os
from pkg_resources import RequirementParseError
from pkg_resources.extern.packaging.requirements import InvalidRequirement

try:
    import requirements
except ImportError:
    print('Error: dependency "requirements_parser" is required: '
          'https://pypi.org/project/requirements-parser/')
    exit(1)


def inspect(wd):
    results = {}
    idx = 0
    for d in subdirs(wd):
        files = has_requirements_txt(os.path.join(wd, d))
        for sd in subdirs(d):
            files += has_requirements_txt(os.path.join(wd, d, sd))

        if files:
            idx += 1
            results[d] = {
                'index': idx,
                'files': files,
            }

    return results


def has_requirements_txt(path):
    path, _, files = next(os.walk(path))
    return [
        os.path.join(path, s) for s in files
        if (
            ('requirements' in s
             or path.endswith('/requirements'))
            and s.endswith('.txt')
        )]


def subdirs(d):
    return next(os.walk(d))[1]


def print_data(data, selection=None):
    selection = selection or set()
    for d, di in data.items():
        print(f'{"* " if di["index"] in selection else "  "}{di["index"]}: {d}')


def prompt_user_selection(data):
    selection = set()

    while 1:
        print('Select repositories (or "a" for all)')
        print_data(data, selection)

        s = input('\nType a number or "q" to continue >')
        method = 'remove' if s.startswith('-') else 'add'

        try:
            s = int(s)
            if s in selection:
                selection.remove(s)
            elif s in [d['index'] for d in data.values()]:
                selection.add(s)
        except Exception:
            if s == 'a':
                [selection.add(d['index']) for d in data.values()]
                continue

            if s in ['exit', 'q']:
                break
            print('Bad input')

    return {k: v for k, v in data.items() if v['index'] in selection}


def print_summary(wd, data):
    summary = {}

    for d, results in data.items():
        for req_file in results['files']:
            with open(req_file, 'r') as f:
                try:
                    for req in requirements.parse(f):
                        summary.setdefault(req.name.lower(), []).append((d, req_file, req))
                except (RequirementParseError, InvalidRequirement) as e:
                    print(f'Failed to parse requirements ({req_file}): {e}')

    summary_items = summary.items()
    summary_items = sorted(summary_items, key=lambda d: len(d[1]), reverse=True)

    print('\nSummary:\n')

    for package, details in summary_items:
        if len(details) == 1 and '--min=2' in sys.argv:
            continue
        different_versions = set(tuple(d[2].specs) for d in details)
        if len(different_versions) == 1 and '--min-different=2' in sys.argv:
            continue
        print(f'{package}, {len(different_versions)} different versions')
        for dets in details:
            print(f'** {dets[1].split(wd)[1][1:]} {dets[2].specs}')


def console_command():
    wd = os.getcwd()
    data = inspect(wd)
    data = prompt_user_selection(data)
    print_summary(wd, data)


if __name__ == '__main__':
    console_command()
