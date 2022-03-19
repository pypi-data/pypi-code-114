import argparse
import configparser
import os
import sys
import json


def main():
    parser = argparse.ArgumentParser(description='pyconvox')
    subparsers = parser.add_subparsers(help='Commands')
    parser_a = subparsers.add_parser('env', help='Get all environment variables of the specified application')
    parser_a.add_argument('--app', '-a', help='Application name')
    parser_a.set_defaults(which='app')

    # parser_b = subparsers.add_parser('domain', help='Query a domain')
    # parser_b.add_argument('DOMAIN', help='Domain to be requested')
    # parser_b.add_argument('--json', '-j', action='store_true', help='Show raw json')
    # parser_b.set_defaults(which='domain')

    # parser_c = subparsers.add_parser('adsense', help='Query an adsense id')
    # parser_c.add_argument('ID', help='id to be requested')
    # parser_c.add_argument('--raw', '-r', action='store_true',
    #         help='Print raw list of domains')
    # parser_c.add_argument('--json', '-j', action='store_true',
    #         help='Print raw json result')
    # parser_c.set_defaults(which='adsense')

    # parser_d = subparsers.add_parser('analytics', help='Query a Google Analytics id')
    # parser_d.add_argument('ID', help='id to be requested')
    # parser_d.add_argument('--raw', '-r', action='store_true',
    #         help='Print raw list of domains')
    # parser_d.add_argument('--json', '-j', action='store_true',
    #         help='Print raw json')
    # parser_d.set_defaults(which='analytics')

    # parser_e = subparsers.add_parser('ip', help='Query an IP Address')
    # parser_e.add_argument('IP', help='IP address to be requested')
    # parser_e.add_argument('--raw', '-r', action='store_true',
    #         help='Print raw list of domains')
    # parser_e.add_argument('--json', '-j', action='store_true',
    #         help='Print raw json')
    # parser_e.set_defaults(which='ip')

    # parser_f = subparsers.add_parser('nsdomain', help='Query an Name Server domain')
    # parser_f.add_argument('DOMAIN', help='Name Server Domain to be requested')
    # parser_f.add_argument('--raw', '-r', action='store_true',
    #         help='Print raw list of domains')
    # parser_f.set_defaults(which='nsdomain')

    # parser_g = subparsers.add_parser('nsip', help='Query a Name Server IP address')
    # parser_g.add_argument('IP', help='Name Server IP Address to be requested')
    # parser_g.add_argument('--raw', '-r', action='store_true',
    #         help='Print raw list of domains')
    # parser_g.set_defaults(which='nsip')
    args = parser.parse_args()
    stream = os.popen("convox apps | grep -v APP | awk '{print $1}'")
    apps = str(stream.read()).strip().split('\n')
    print(apps)

    if hasattr(args, 'which'):
        # print('inside 1',args.which)
        if args.which == 'app':
            # print('inside 2')
            if args.app:
                if args.app in apps:
                    stream = os.popen(f"convox env -a {args.app}")
                    envs = str(stream.read()).strip().split('\n')
                    for envvar in envs:
                        print(f'{envvar}')
                    # print(args.app)
                else:
                    print("Wrong Application name!!..\nPlease choose application name from the below")
                    for index,appname in enumerate(apps):
                        print(f"{index+1}. {appname}")
            else:
                print('Please specify the application name using --app / -a <application_name>')
        else:
            parser.print_help()

if __name__ == '__main__':
    main()