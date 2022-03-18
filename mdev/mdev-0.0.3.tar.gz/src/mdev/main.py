import sys
import os
import errno
import pathlib
import argparse
import subprocess
import shutil

from mdev import log

__version__ = '0.0.3'

def mkdir_p(path):  # type: (str) -> None
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

def get_env():  # type: () -> None
    home = str(pathlib.Path.home())
    env_path = os.path.abspath(os.path.join(home, '.mdev'))
    if not os.path.exists(env_path):
        log.inf(f'Directory {env_path} was not found.')
        log.inf(f'Creating {env_path} ...')
        mkdir_p(env_path)
    return env_path

def do_build(args):
    env_path = get_env()
    build_diretory = f'build/{args.application}-{args.module}'

    if args.clean:
        log.dbg(f'Removing {build_diretory} ...')
        shutil.rmtree(build_diretory, ignore_errors=True)

    command = f'cmake -B {build_diretory} -GNinja -DAPP={args.application} -DMODULE={args.module} -DFLASH={args.flash} -DMXOS_ENV={env_path}'
    log.dbg(command)
    subprocess.run(command, shell=True)

    command = f'cmake --build {build_diretory}'
    log.dbg(command)
    subprocess.run(command, shell=True)

def do_clean(args):
    log.dbg('Removing build ...')
    shutil.rmtree('build', ignore_errors=True)

def main(argv=None):

    parser = argparse.ArgumentParser(prog='mdev',
        description=f'The MXOS meta-tool v{__version__}.',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-V', '--version', action='version',
        version=f'mdev version: v{__version__}',
        help='print the program version and exit')
    parser.add_argument('-v', '--verbose', default=0, action='count',
        help='''Display verbose output. May be given
        multiple times to increase verbosity.''')

    subparsers = parser.add_subparsers(metavar='<command>', dest='command')

    parser_build = subparsers.add_parser('build', help='build a MXOS application')
    parser_build.add_argument('-m', '--module', required=True, help='module to build for')
    parser_build.add_argument('-f', '--flash', default='NONE', help='type to flash, can be APP or ALL')
    parser_build.add_argument('-c', '--clean', action='store_const', const=True, help='clean the build directory and rebuild the project')
    parser_build.add_argument('application', help='application source directory')
    parser_build.set_defaults(func=do_build)

    parser_build = subparsers.add_parser('clean', help='clean all the build directories')
    parser_build.set_defaults(func=do_clean)

    if len(sys.argv) <= 1:
        return parser.print_help()

    args = parser.parse_args()
    log.set_verbosity(args.verbose)
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()
