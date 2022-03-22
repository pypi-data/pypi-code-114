import argparse
import os

from bobthebuilder import BobBuilder, IniModifier


def build_cli():
    args = argparse.ArgumentParser(description="Сборщик проектов на defold")
    args.add_argument('-p', choices=['js-web'], dest='platform', help='Build platform.', required=True)
    args.add_argument('-a', choices=['js-web', 'js-web,wasm-web'], dest='arch', help='Build Architecture', required=True)
    args.add_argument('-d', help='Game project directory')
    args.add_argument('-o', help='Compiled artifact directory', dest='out_dir', required=True)
    args.add_argument('--variant', help="Bob build variant", choices=['debug', 'release'], default='release')
    parsed = args.parse_args()
    project_dir = parsed.d if parsed.d else os.getcwd()
    bob = BobBuilder(project_dir)
    bob.resolve_deps()
    bob.build(parsed.platform, parsed.arch)
    bob.bundle(parsed.out_dir, platform=parsed.platform, arch=parsed.arch, variant=parsed.variant)


def set_version():
    args = argparse.ArgumentParser(description='Tool for setting game version')
    args.add_argument("-f", dest='game_project_file', help='game.project file', required=True)
    args.add_argument('-v', dest='version', help='Game version, ex: 1.0.0', required=True)
    parsed = args.parse_args()
    ini = IniModifier(parsed.game_project_file)
    ini.set('project', 'version', parsed.version)
    ini.save()
