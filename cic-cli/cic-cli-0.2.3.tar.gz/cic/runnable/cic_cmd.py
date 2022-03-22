# standard imports
import os
import logging
import sys
import importlib

# external imports
import chainlib.cli

# local imports
import cic.cmd.init as cmd_init
import cic.cmd.show as cmd_show
import cic.cmd.ext as cmd_ext
import cic.cmd.export as cmd_export
import cic.cmd.wizard as cmd_wizard
from cic.config import ensure_base_configs

logging.basicConfig(level=logging.WARNING)
logg = logging.getLogger()

script_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')
base_config_dir = os.path.join(data_dir, 'config')
schema_dir = os.path.join(script_dir, '..', 'schema')
user_config_dir = os.path.join(os.path.expanduser("~"), ".config", "cic", "cli", "config") 

arg_flags = chainlib.cli.argflag_std_read | chainlib.cli.Flag.SEQ
argparser = chainlib.cli.ArgumentParser(
    env=os.environ,
    arg_flags=arg_flags,
    description='CIC cli tool for generating and publishing tokens'
)

sub = argparser.add_subparsers()
sub.dest = 'command'

sub_init = sub.add_parser('init', help='initialize new cic data directory')
cmd_init.process_args(sub_init)

sub_show = sub.add_parser('show', help='display summary of current state of cic data directory')
cmd_show.process_args(sub_show)

sub_export = sub.add_parser('export', help='export cic data directory state to a specified target')
cmd_export.process_args(sub_export)

sub_ext = sub.add_parser('ext', help='extension helpers')
cmd_ext.process_args(sub_ext)

sub_wizard = sub.add_parser('wizard', help='An interactive wizard for creating and publishing contracts')
cmd_wizard.process_args(sub_wizard)

args = argparser.parse_args(sys.argv[1:])

if args.command is None:
    logg.critical('Subcommand missing')
    sys.stderr.write("\033[;91m" + 'subcommand missing' + "\033[;39m\n")
    argparser.print_help(sys.stderr)
    sys.exit(1)

modname = f'cic.cmd.{args.command}'
logg.debug(f'using module {modname}')
cmd_mod = importlib.import_module(modname)

extra_args = {
    'p': 'RPC_PROVIDER',
}
ensure_base_configs(user_config_dir)

config = chainlib.cli.Config.from_args(args, arg_flags=arg_flags, base_config_dir=base_config_dir, extra_args=extra_args)

def main():
    try:
        cmd_mod.execute(config, args)
    except Exception as e:
        logg.exception(e)
        sys.stderr.write("\033[;91m" + str(e) + "\033[;39m\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
