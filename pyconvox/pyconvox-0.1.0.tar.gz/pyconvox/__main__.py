import argparse
import configparser
import os
import sys
import json
import subprocess
import re


def Env(args,apps,parser):
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

def SetEnv(args,apps,parser):
    re.escape()
    if args.app:
        if args.app in apps:
            option=''
            while option not in 'Y,y,N,n'.split(','):
                option=str(input("Would you like pyconvox to promote the new release? (Y/N): ")).strip()
                if option == 'Y' or option == 'y':
                    stream = os.system(f"convox env set '{args.key}={args.value}' -a {args.app} -p -w")
                elif option == 'N' or option == 'n':
                    stream = os.system(f"convox env set '{args.key}={args.value}' -a {args.app}")
                else:
                    print("Only Y or N accepted!")
            # print(args.app)
        else:
            print("Wrong Application Name!!..\nPlease provide application name from the below")
            for index,appname in enumerate(apps):
                print(f"{index+1}. {appname}")
            print()
            parser.print_help()
    else:
        print('Please specify the application name using --app / -a <application_name>')


def Scale(args,apps,parser):
    if args.app:
        if args.app in apps:
            stream = os.popen(f"convox scale -a {args.app}")
            services = str(stream.read()).strip().split('\n')
            for line in services:
                print(f'{line}')
            # print(args.app)
        else:
            print("Wrong Application Name!!..\nPlease provide application name from the below")
            for index,appname in enumerate(apps):
                print(f"{index+1}. {appname}")
            print()
            parser.print_help()
    else:
        print('Please specify the application name using --app / -a <application_name>')

def RailsC(args,apps,parser):
    if args.app:
        if args.app in apps:
            if args.service:
                service=str(args.service)
            else:
                stream = os.popen(f"convox scale -a {args.app} | grep -v SERVICE | grep -E 'web|rake' | awk '"+"{print $1}' | head -n 1")
                service = str(stream.read()).strip()
            print(service)
            stream = os.system(f"convox run {service} 'rails c' -a {args.app}")
            # console = str(stream.read()).strip()
            print(stream)
        else:
            print("Wrong Application Name!!..\nPlease provide application name from the below")
            for index,appname in enumerate(apps):
                print(f"{index+1}. {appname}")
            print()
            parser.print_help()
    else:
        print('Please specify the application name using --app / -a <application_name>')


def main():
    parser = argparse.ArgumentParser(description='pyconvox - a wrapper for the convox application')
    subparsers = parser.add_subparsers(help='Commands')
    parser_0 = subparsers.add_parser('envset', help='set env var')
    parser_0.add_argument('--app', '-a', help='application name')
    parser_0.add_argument('--key', '-k', help='key')
    parser_0.add_argument('--value', '-v', help='value')
    parser_0.set_defaults(which='envset')

    parser_a = subparsers.add_parser('env', help='list env vars')
    parser_a.add_argument('--app', '-a', help='application name')
    parser_a.set_defaults(which='env')

    parser_b = subparsers.add_parser('railsc', help='run rails c')
    parser_b.add_argument('--app', '-a', help='application name')
    parser_b.add_argument('--service', '-s', help='Service name')
    parser_b.set_defaults(which='railsc')
    parser_b.set_defaults(service='')
    parser_c = subparsers.add_parser('scale', help='scale a service')
    parser_c.add_argument('--app', '-a', help='application name')
    parser_c.set_defaults(which='scale')

    args = parser.parse_args()
    stream = os.popen("convox apps | grep -v APP | awk '{print $1}'")
    apps = str(stream.read()).strip().split('\n')
    # print(apps)

    if hasattr(args, 'which'):
        if args.which == 'env':
            Env(args,apps,parser)
        elif args.which == 'railsc':
            RailsC(args,apps,parser)
        elif args.which == 'scale':
            Scale(args,apps,parser)
        elif args.which == 'envset':
            SetEnv(args,apps,parser)
        else:
            parser.print_help()


if __name__ == '__main__':
    main()