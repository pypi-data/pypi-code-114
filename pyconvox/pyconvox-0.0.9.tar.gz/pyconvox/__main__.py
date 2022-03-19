import argparse
import configparser
import os
import sys
import json


def App(args,apps,parser):
    if args.app:
        if args.app in apps:
            stream = os.popen(f"convox env -a {args.app}")
            envs = str(stream.read()).strip().split('\n')
            for envvar in envs:
                print(f'{envvar}')
            # print(args.app)
        else:
            print("Wrong Application Name!!..\nPlease provide application name from the below")
            for index,appname in enumerate(apps):
                print(f"{index+1}. {appname}")
            print()
            parser.print_help()
    else:
        print('Please specify the application name using --app / -a <application_name>')


def main():
    parser = argparse.ArgumentParser(description='pyconvox')
    subparsers = parser.add_subparsers(help='Commands')
    parser_a = subparsers.add_parser('env', help='Get all environment variables of the specified application')
    parser_a.add_argument('--app', '-a', help='Application name')
    parser_a.set_defaults(which='app')

    args = parser.parse_args()
    stream = os.popen("convox apps | grep -v APP | awk '{print $1}'")
    apps = str(stream.read()).strip().split('\n')
    # print(apps)

    if hasattr(args, 'which'):
        if args.which == 'app':
            App(args,apps,parser)
        else:
            parser.print_help()


if __name__ == '__main__':
    main()