#!/usr/bin/env python3

import logging
import argparse
from datetime import datetime
from googlesearch import search
from oxdork import colors, minimal, default, banner         

def main():
    parser = argparse.ArgumentParser(description=f"{colors.white}Google dorking tool — by Richard Mwewa | https://about.me/rly0nheart{colors.reset}",epilog=f"{colors.red}ox{colors.white}Dork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers.{colors.reset}")
    parser.add_argument("query", help="query",metavar="<query>")
    parser.add_argument("-c","--count",help="number of results to show (default is 10)",metavar="<number>", default=10)
    parser.add_argument("-o","--output",help="write output to specified file",metavar="<filename>")
    parser.add_argument("-m","--minimal",help="enable a minimal alternative of oxdork",action="store_true")
    parser.add_argument("-v","--verbose",help="enable verbosity",action="store_true")
    parser.add_argument("--version",version="2022.2.2.0 Released on 20th March 2022",action="version")
    args = parser.parse_args()

    start_time = datetime.now()
    logging.basicConfig(format=f"%(asctime)s {colors.white}%(message)s{colors.reset}",datefmt=f"{colors.white}%I{colors.red}:{colors.white}%M{colors.red}:{colors.white}%S%p{colors.reset}",level=logging.DEBUG)
    
    print(banner.banner)
    while True:
        try:
            if args.minimal:
                print(minimal.dork(args))
                break
            else:
            	default.dork(args,logging)
            	break
            	
        except KeyboardInterrupt:
            if args.verbose:
            	print("\n")
            	logging.info(f"{colors.white}Process interrupted with {colors.red}Ctrl{colors.white}+{colors.red}C{colors.reset}")
            	break
            break
            
        except Exception as e:
            if args.verbose:
            	logging.error(f"{colors.white}Error: {colors.red}{e}{colors.reset}")
            	
    if args.verbose:
        logging.info(f"{colors.white}Stopped in {colors.green}{datetime.now()-start_time}{colors.white} seconds.{colors.reset}")